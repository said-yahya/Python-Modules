if __name__ == "__main__":
    print("== Kaboom 1 ==")
    try:
        from alchemy.grimoire.dark_spellbook import dark_spell_record
        dark_spell_record("Doom", "bats and frogs")
    except ImportError as e:
        print(f"Test import now THIS WILL RAISE AN UNCAUGHT EXCEPTION\n{e}")
