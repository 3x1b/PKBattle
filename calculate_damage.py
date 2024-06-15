import random

def type_chart(type_atk, type_def): # WHY
    type_chart = {
        'none':      {'Rock': 1, 'Ghost': 1, 'Normal': 1, 'Fighting': 1, 'Flying': 1, 'Poison': 1, 'Ground': 1, 'Bug': 1, 'Fire': 1, 'Water': 1, 'Grass': 1, 'Electric': 1, 'Psychic': 1, 'Ice': 1, 'Dragon': 1, 'none': 1},
        'Normal':    {'Rock': 0.5, 'Ghost': 0, 'Normal': 1, 'Fighting': 1, 'Flying': 1, 'Poison': 1, 'Ground': 1, 'Bug': 1, 'Fire': 1, 'Water': 1, 'Grass': 1, 'Electric': 1, 'Psychic': 1, 'Ice': 1, 'Dragon': 1, 'none': 1},
        'Fighting':  {'Rock': 2, 'Ghost': 0, 'Normal': 2, 'Fighting': 1, 'Flying': 0.5, 'Poison': 0.5, 'Ground': 1, 'Bug': 0.5, 'Fire': 1, 'Water': 1, 'Grass': 1, 'Electric': 1, 'Psychic': 0.5, 'Ice': 2, 'Dragon': 1, 'none': 1},
        'Flying':    {'Rock': 0.5, 'Ghost': 1, 'Normal': 1, 'Fighting': 2, 'Flying': 1, 'Poison': 1, 'Ground': 1, 'Bug': 2, 'Fire': 1, 'Water': 1, 'Grass': 2, 'Electric': 0.5, 'Psychic': 1, 'Ice': 1, 'Dragon': 1, 'none': 1},
        'Poison':    {'Rock': 0.5, 'Ghost': 0.5, 'Normal': 1, 'Fighting': 1, 'Flying': 1, 'Poison': 0.5, 'Ground': 0.5, 'Bug': 2, 'Fire': 1, 'Water': 1, 'Grass': 2, 'Electric': 1, 'Psychic': 1, 'Ice': 1, 'Dragon': 1, 'none': 1},
        'Ground':    {'Rock': 2, 'Ghost': 1, 'Normal': 1, 'Fighting': 1, 'Flying': 0, 'Poison': 2, 'Ground': 1, 'Bug': 0.5, 'Fire': 2, 'Water': 1, 'Grass': 0.5, 'Electric': 2, 'Psychic': 1, 'Ice': 1, 'Dragon': 1, 'none': 1},
        'Rock':      {'Rock': 1, 'Ghost': 1, 'Normal': 1, 'Fighting': 0.5, 'Flying': 2, 'Poison': 1, 'Ground': 0.5, 'Bug': 2, 'Fire': 2, 'Water': 1, 'Grass': 1, 'Electric': 1, 'Psychic': 1, 'Ice': 2, 'Dragon': 1, 'none': 1},
        'Bug':       {'Rock': 1, 'Ghost': 0.5, 'Normal': 1, 'Fighting': 0.5, 'Flying': 0.5, 'Poison': 0.5, 'Ground': 1, 'Bug': 1, 'Fire': 0.5, 'Water': 1, 'Grass': 2, 'Electric': 1, 'Psychic': 2, 'Ice': 1, 'Dragon': 1, 'none': 1},
        'Ghost':     {'Rock': 1, 'Ghost': 2, 'Normal': 0, 'Fighting': 1, 'Flying': 1, 'Poison': 1, 'Ground': 1, 'Bug': 1, 'Fire': 1, 'Water': 1, 'Grass': 1, 'Electric': 1, 'Psychic': 0, 'Ice': 1, 'Dragon': 1, 'none': 1},
        'Fire':      {'Rock': 0.5, 'Ghost': 1, 'Normal': 1, 'Fighting': 1, 'Flying': 1, 'Poison': 1, 'Ground': 1, 'Bug': 2, 'Fire': 0.5, 'Water': 0.5, 'Grass': 2, 'Electric': 1, 'Psychic': 1, 'Ice': 2, 'Dragon': 0.5, 'none': 1},
        'Water':     {'Rock': 2, 'Ghost': 1, 'Normal': 1, 'Fighting': 1, 'Flying': 1, 'Poison': 1, 'Ground': 2, 'Bug': 1, 'Fire': 2, 'Water': 0.5, 'Grass': 0.5, 'Electric': 1, 'Psychic': 1, 'Ice': 1, 'Dragon': 0.5, 'none': 1},
        'Grass':     {'Rock': 2, 'Ghost': 1, 'Normal': 1, 'Fighting': 1, 'Flying': 0.5, 'Poison': 0.5, 'Ground': 2, 'Bug': 0.5, 'Fire': 0.5, 'Water': 2, 'Grass': 0.5, 'Electric': 1, 'Psychic': 1, 'Ice': 1, 'Dragon': 0.5, 'none': 1},
        'Electric':  {'Rock': 1, 'Ghost': 1, 'Normal': 1, 'Fighting': 1, 'Flying': 2, 'Poison': 1, 'Ground': 0, 'Bug': 1, 'Fire': 1, 'Water': 2, 'Grass': 0.5, 'Electric': 0.5, 'Psychic': 1, 'Ice': 1, 'Dragon': 0.5, 'none': 1},
        'Psychic':   {'Rock': 1, 'Ghost': 1, 'Normal': 1, 'Fighting': 2, 'Flying': 1, 'Poison': 2, 'Ground': 1, 'Bug': 1, 'Fire': 1, 'Water': 1, 'Grass': 1, 'Electric': 1, 'Psychic': 0.5, 'Ice': 1, 'Dragon': 1, 'none': 1},
        'Ice':       {'Rock': 1, 'Ghost': 1, 'Normal': 1, 'Fighting': 1, 'Flying': 2, 'Poison': 1, 'Ground': 2, 'Bug': 1, 'Fire': 1, 'Water': 0.5, 'Grass': 2, 'Electric': 1, 'Psychic': 1, 'Ice': 0.5, 'Dragon': 2, 'none': 1},
        'Dragon':    {'Rock': 1, 'Ghost': 1, 'Normal': 1, 'Fighting': 1, 'Flying': 1, 'Poison': 1, 'Ground': 1, 'Bug': 1, 'Fire': 1, 'Water': 1, 'Grass': 1, 'Electric': 1, 'Psychic': 1, 'Ice': 1, 'Dragon': 2, 'none': 1},
    }

    return type_chart.get(type_atk, {}).get(type_def, 1)

def calc_damage(pkmn_types, move_type, power, atk, defe):
    # Calculate crit:
    crit = 1
    if random.randint(1, 16) == 8:
        crit = 2

    attacking_types = pkmn_types[0]
    defending_types = pkmn_types[1]

    damage = (((2 * 50 * crit) / 5) + 2) * power * (atk/defe) / 50

    if move_type in attacking_types: damage *= 1.5 # account for S.T.A.B.

    damage *= type_chart(move_type, defending_types[0])
    damage *= type_chart(move_type, defending_types[1])

    rand = random.randint(217, 255) / 255
    if damage == 1:
        rand = 1

    damage *= rand

    return round(damage)

print(calc_damage([["Fire", "none"],["Water", "Grass"]], "Fire", 120, 159, 144))