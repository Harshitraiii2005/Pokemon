import streamlit as st
import random
import requests
from battle_1v1 import start_battle_1v1
from battle_2v2 import start_battle_2v2
import os

# Global state for caught Pokémon
if 'caught_pokemon' not in st.session_state:
    st.session_state.caught_pokemon = []

# Function to fetch Pokémon details
def get_pokemon_details(pokemon_number):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_number}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Function to catch the Pokémon
def catch_pokemon(pokemon_number):
    pokemon_details = get_pokemon_details(pokemon_number)
    if pokemon_details:
        st.session_state.caught_pokemon.append({
            'name': pokemon_details['name'],
            'id': pokemon_details['id'],
            'image': pokemon_details['sprites']['front_default'],
            'stats': pokemon_details['stats'],
        })
        st.success(f"You caught {pokemon_details['name']}!")
    else:
        st.error("Pokémon not found! Please try again.")

# Set background function for the app
# Function to set the background image
import os
import streamlit as st

def set_background():
    import os
import streamlit as st

def set_background():
    img_path = r'c:\Users\admin\Downloads\726b01f279c9513b0421fb4b2ed91c10.jpg'  # Make sure this path is correct

    # Check if the image exists
    if os.path.exists(img_path):
        st.markdown(
            f"""
            <style>
            body {{
                background-image: url('file://{os.path.abspath(img_path)}');
                background-size: cover;
                background-position: center;
                background-attachment: fixed;
            }}
            </style>
            """, unsafe_allow_html=True
        )
    else:
        st.error(f"Background image not found. Please check the file path: {img_path}")



# Function to display Pokémon as a card
def show_pokemon_card(pokemon):
    with st.expander(f"{pokemon['name'].capitalize()}"):   
        st.image(pokemon['image'], width=200)
        st.write(f"**Name**: {pokemon['name']}")
        st.write(f"**ID**: {pokemon['id']}")
        for stat in pokemon['stats']:
            st.write(f"{stat['stat']['name'].capitalize()}: {stat['base_stat']}")

# Function to create the Pokéball catch button
def display_pokeball_to_catch():
    if st.button("Catch Pokémon"):
        pokemon_number = random.randint(1, 898)  # Random Pokémon number
        catch_pokemon(pokemon_number)

# Home page UI
def home_page():
    set_background()
    st.title("Pokémon Adventure")
    
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ("Home", "1v1 Battle", "2v2 Battle"))
    
    if page == "Home":
        st.header("Catch Pokémon!")
        
        # Input to enter Pokémon number
        pokemon_number = st.number_input("Enter Pokémon number (1-898)", min_value=1, max_value=898, step=1)
        
        if pokemon_number:
            pokemon_details = get_pokemon_details(pokemon_number)
            if pokemon_details:
                st.image(pokemon_details['sprites']['front_default'], width=200)
                st.write(f"**Name**: {pokemon_details['name']}")
                st.write(f"**ID**: {pokemon_details['id']}")
                
                # Show Pokémon stats
                stats = pokemon_details['stats']
                for stat in stats:
                    st.write(f"{stat['stat']['name'].capitalize()}: {stat['base_stat']}")

                # Catch Pokémon button
                if st.button("Catch this Pokémon"):
                    catch_pokemon(pokemon_number)

        # Show caught Pokémon as cards
        if st.session_state.caught_pokemon:
            st.subheader("Your Pokédex")
            for poke in st.session_state.caught_pokemon:
                show_pokemon_card(poke)

        # Start a new game button
        if st.button("Start New Game"):
            st.session_state.caught_pokemon = []
            st.success("Game reset! Catch new Pokémon.")

    elif page == "1v1 Battle":
        battle_page_1v1()

    elif page == "2v2 Battle":
        battle_page_2v2()

# 1v1 Battle page
def battle_page_1v1():
    st.title("1v1 Battle")
    
    # Select your Pokémon for battle
    if len(st.session_state.caught_pokemon) < 1:
        st.warning("You need at least one Pokémon to battle. Go back and catch some!")
        return

    st.subheader("Select your Pokémon")
    user_pokemon = st.selectbox("Choose your Pokémon", [poke['name'] for poke in st.session_state.caught_pokemon])

    # Randomly select an opponent Pokémon
    opponent_pokemon = random.randint(1, 898)
    while any(pokemon['id'] == opponent_pokemon for pokemon in st.session_state.caught_pokemon):
        opponent_pokemon = random.randint(1, 898)

    opponent_details = get_pokemon_details(opponent_pokemon)
    if opponent_details:
        st.subheader("Opponent Pokémon")
        st.image(opponent_details['sprites']['front_default'], width=100)
        st.write(f"**Name**: {opponent_details['name']}")

    if st.button("Start Battle"):
        result, winner, user_pokemon_details, opponent_pokemon_details = start_battle_1v1(user_pokemon, opponent_details)
        st.write(result)
        st.image(user_pokemon_details['image'], width=100)
        st.write(f"**Your Pokémon**: {user_pokemon_details['name']}")
        st.image(opponent_pokemon_details['image'], width=100)
        st.write(f"**Opponent's Pokémon**: {opponent_pokemon_details['name']}")

# 2v2 Battle page
def battle_page_2v2():
    st.title("2v2 Battle")
    
    # Select your two Pokémon for battle
    if len(st.session_state.caught_pokemon) < 2:
        st.warning("You need at least two Pokémon to battle. Go back and catch some!")
        return

    st.subheader("Select your Pokémon for 2v2 battle")
    user_pokemon1 = st.selectbox("Choose your first Pokémon", [poke['name'] for poke in st.session_state.caught_pokemon])
    user_pokemon2 = st.selectbox("Choose your second Pokémon", [poke['name'] for poke in st.session_state.caught_pokemon if poke['name'] != user_pokemon1])

    # Randomly select two opponent Pokémon
    opponent_pokemon1 = random.randint(1, 898)
    opponent_pokemon2 = random.randint(1, 898)

    opponent_details1 = get_pokemon_details(opponent_pokemon1)
    opponent_details2 = get_pokemon_details(opponent_pokemon2)

    if opponent_details1 and opponent_details2:
        st.subheader("Opponent Pokémon")
        st.image(opponent_details1['sprites']['front_default'], width=100)
        st.write(f"**Name**: {opponent_details1['name']}")
        st.image(opponent_details2['sprites']['front_default'], width=100)
        st.write(f"**Name**: {opponent_details2['name']}")

    if st.button("Start Battle"):
        result, winner, user_pokemon1_details, user_pokemon2_details, opponent_pokemon1_details, opponent_pokemon2_details = start_battle_2v2(
            user_pokemon1, user_pokemon2, opponent_details1, opponent_details2)
        st.write(result)
        st.image(user_pokemon1_details['image'], width=100)
        st.write(f"**Your Pokémon 1**: {user_pokemon1_details['name']}")
        st.image(user_pokemon2_details['image'], width=100)
        st.write(f"**Your Pokémon 2**: {user_pokemon2_details['name']}")
        st.image(opponent_pokemon1_details['image'], width=100)
        st.write(f"**Opponent's Pokémon 1**: {opponent_pokemon1_details['name']}")
        st.image(opponent_pokemon2_details['image'], width=100)
        st.write(f"**Opponent's Pokémon 2**: {opponent_pokemon2_details['name']}")

# Run the app
if __name__ == "__main__":
    home_page()
