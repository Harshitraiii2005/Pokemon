import random
import streamlit as st

def start_battle_1v1(user_pokemon_name, opponent_pokemon_details):
    # Example battle logic (you can enhance this)
    result = f"{user_pokemon_name} battles {opponent_pokemon_details['name']}!"
    winner = random.choice([user_pokemon_name, opponent_pokemon_details['name']])

    # Assuming you're fetching the user's Pokémon image from an API or predefined location
    user_pokemon_details = {
        'name': user_pokemon_name,
        'image': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png'  # Example image URL
    }

    opponent_pokemon_details = {
        'name': opponent_pokemon_details['name'],
        'image': opponent_pokemon_details['sprites']['front_default']
    }

    return result, winner, user_pokemon_details, opponent_pokemon_details

def battle_page_1v1():
    user_pokemon_name = 'bulbasaur'  # Example user Pokémon
    opponent_pokemon_details = {
        'name': 'charmander',
        'sprites': {'front_default': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/4.png'}
    }

    result, winner, user_pokemon_details, opponent_pokemon_details = start_battle_1v1(user_pokemon_name, opponent_pokemon_details)

    st.write(result)
    st.write(f"The winner is: {winner}")  # Display winner

    # Display Pokémon details in cards below the battle result
    st.markdown("""
        <div style="border: 1px solid #ddd; padding: 10px; border-radius: 10px; text-align: center; margin-bottom: 20px;">
            <h3>Your Pokémon: {}</h3>
            <img src="{}" width="200"/>
        </div>
    """.format(user_pokemon_details['name'], user_pokemon_details['image']), unsafe_allow_html=True)

    st.markdown("""
        <div style="border: 1px solid #ddd; padding: 10px; border-radius: 10px; text-align: center;">
            <h3>Opponent's Pokémon: {}</h3>
            <img src="{}" width="200"/>
        </div>
    """.format(opponent_pokemon_details['name'], opponent_pokemon_details['image']), unsafe_allow_html=True)

# To display the battle page, call battle_page_1v1()
battle_page_1v1()
