# battle_1v1.py

import streamlit as st

# Function to create a battle outcome based on stats
def start_battle_1v1(pokemon1_stats, pokemon2_stats):
    # Basic 1v1 battle logic based on attack stat
    p1_attack = pokemon1_stats['attack']
    p2_attack = pokemon2_stats['attack']
    if p1_attack > p2_attack:
        return "Pokemon 1 wins!", True
    elif p1_attack < p2_attack:
        return "Pokemon 2 wins!", False
    else:
        return "It's a draw!", None

# Function to handle evolution logic (after a win)
def evolve(pokemon_name, pokemon_stats):
    # Example logic: if attack stat > 100, evolve the Pokémon
    if pokemon_stats['attack'] > 100:
        evolved_name = f"{pokemon_name} (Evolved)"
        evolved_stats = {key: value * 1.2 for key, value in pokemon_stats.items()}  # Boost stats by 20%
        return evolved_name, evolved_stats
    return pokemon_name, pokemon_stats
