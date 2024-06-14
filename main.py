from team_genner import make_team
import sys
from pathlib import Path

script_path = Path(__file__).resolve()
main_path = script_path.parent

assets_path = main_path / "assets"

if not assets_path.exists(): raise Exception("assets folder not found!")

team = make_team()

ascii_art_path = assets_path / "sprite_ascii"

if not assets_path.exists(): raise Exception("assets folder not found!")

print("\n" * 100)

for pokemon in team:
    try:
        sprite_path = ascii_art_path / f"{pokemon.lower()}.txt"
        print(sprite_path.read_text())
    except FileNotFoundError:
        raise Exception(f"Ascii data for {pokemon} not found!")
    input()