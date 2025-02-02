import random
import streamlit as st

def start_battle_2v2(user_pokemon1_name, user_pokemon2_name, opponent_pokemon1_details, opponent_pokemon2_details):
    result = f"{user_pokemon1_name} and {user_pokemon2_name} battle against {opponent_pokemon1_details['name']} and {opponent_pokemon2_details['name']}!"
    
    # Randomly pick a winner from the four Pokémon
    winner = random.choice([user_pokemon1_name, user_pokemon2_name, opponent_pokemon1_details['name'], opponent_pokemon2_details['name']])

    # User's Pokémon details
    user_pokemon1_details = {'name': user_pokemon1_name, 'image': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png'}  # Example image URL
    user_pokemon2_details = {'name': user_pokemon2_name, 'image': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/2.png'}  # Example image URL

    # Opponent's Pokémon details
    opponent_pokemon1_details = {'name': opponent_pokemon1_details['name'], 'image': opponent_pokemon1_details['sprites']['front_default']}
    opponent_pokemon2_details = {'name': opponent_pokemon2_details['name'], 'image': opponent_pokemon2_details['sprites']['front_default']}

    return result, winner, user_pokemon1_details, user_pokemon2_details, opponent_pokemon1_details, opponent_pokemon2_details

def battle_page_2v2():
    user_pokemon1_name = 'bulbasaur'  # Example user Pokémon 1
    user_pokemon2_name = 'ivysaur'   # Example user Pokémon 2

    opponent_pokemon1_details = {
        'name': 'charmander',
        'sprites': {'front_default': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/4.png'}
    }

    opponent_pokemon2_details = {
        'name': 'charmeleon',
        'sprites': {'front_default': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/5.png'}
    }

    result, winner, user_pokemon1_details, user_pokemon2_details, opponent_pokemon1_details, opponent_pokemon2_details = start_battle_2v2(user_pokemon1_name, user_pokemon2_name, opponent_pokemon1_details, opponent_pokemon2_details)

    # Displaying the result and winner
    st.write(result)
    st.write(f"The winner is: {winner}")  # Display winner

    # Displaying Your Pokémon details in cards
    st.markdown("""
        <div style="border: 1px solid #ddd; padding: 10px; border-radius: 10px; text-align: center; margin-bottom: 20px;">
            <h3>Your Pokémon 1: {}</h3>
            <img src="{}" width="200"/>
        </div>
    """.format(user_pokemon1_details['name'], user_pokemon1_details['image']), unsafe_allow_html=True)

    st.markdown("""
        <div style="border: 1px solid #ddd; padding: 10px; border-radius: 10px; text-align: center; margin-bottom: 20px;">
            <h3>Your Pokémon 2: {}</h3>
            <img src="{}" width="200"/>
        </div>
    """.format(user_pokemon2_details['name'], user_pokemon2_details['image']), unsafe_allow_html=True)

    # Displaying Opponent's Pokémon details in cards
    st.markdown("""
        <div style="border: 1px solid #ddd; padding: 10px; border-radius: 10px; text-align: center; margin-bottom: 20px;">
            <h3>Opponent's Pokémon 1: {}</h3>
            <img src="{}" width="200"/>
        </div>
    """.format(opponent_pokemon1_details['name'], opponent_pokemon1_details['image']), unsafe_allow_html=True)

    st.markdown("""
        <div style="border: 1px solid #ddd; padding: 10px; border-radius: 10px; text-align: center; margin-bottom: 20px;">
            <h3>Opponent's Pokémon 2: {}</h3>
            <img src="{}" width="200"/>
        </div>
    """.format(opponent_pokemon2_details['name'], opponent_pokemon2_details['image']), unsafe_allow_html=True)

# To display the battle page, call battle_page_2v2()
battle_page_2v2()
