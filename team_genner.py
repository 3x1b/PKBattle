from random import choice

bkp_main_pkmn = ['Venusaur', 'Charizard', 'Blastoise', 'Nidoqueen', 'Nidoking', 'Clefable', 'Ninetales', 'Dugtrio', 'Primeape', 'Arcanine', 'Poliwrath', 'Alakazam', 'Machamp', 'Tentacruel', 'Golem', 'Rapidash', 'Slowbro', 'Haunter', 'Gengar', 'Onix', 'Hypno', 'Electrode', 'Rhydon', 'Chansey', 'Kangaskhan', 'Scyther', 'Jynx', 'Electabuzz', 'Magmar', 'Pinsir', 'Tauros', 'Gyarados', 'Lapras', 'Ditto', 'Vaporeon', 'Jolteon', 'Flareon', 'Aerodactyl', 'Snorlax', 'Dragonite']
main_pkmn = ['Venusaur', 'Charizard', 'Blastoise', 'Nidoqueen', 'Nidoking', 'Clefable', 'Ninetales', 'Dugtrio', 'Primeape', 'Arcanine', 'Poliwrath', 'Alakazam', 'Machamp', 'Tentacruel', 'Golem', 'Rapidash', 'Slowbro', 'Haunter', 'Gengar', 'Onix', 'Hypno', 'Electrode', 'Rhydon', 'Chansey', 'Kangaskhan', 'Scyther', 'Jynx', 'Electabuzz', 'Magmar', 'Pinsir', 'Tauros', 'Gyarados', 'Lapras', 'Ditto', 'Vaporeon', 'Jolteon', 'Flareon', 'Aerodactyl', 'Snorlax', 'Dragonite']
leg_pkmn = ['Articuno', 'Zapdos', 'Moltres', 'Articuno', 'Zapdos', 'Moltres', 'Mewtwo', 'Mew']

def make_team(pkmn=5, legs=1):
    if pkmn + legs <= 6:
        to_return = []
        for i in range(pkmn):
            pk = choice(main_pkmn)
            to_return.append(pk)
            main_pkmn.remove(pk)
        for i in range(legs):
            to_return.append(choice(leg_pkmn))
        return to_return
    else:
        raise Exception("Error: Too many pokemon! Please only use maximum 6!")