import alchemy.grimoire as grimoire

if __name__ == "__main__":
    print("== Kaboom 0 ==")
    print("Using grimoire module directly")
    res = grimoire.light_spell_record("Fantasy", "Dark and fire")
    print(f"Testing record light spell: {res}")
