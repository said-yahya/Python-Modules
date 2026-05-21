from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed = dark_spell_allowed_ingredients()
    ingredients_lower = ingredients.lower()
    is_valid = any(item in ingredients_lower for item in allowed)

    status: str = "INVALID"
    if is_valid:
        status = "VALID"
    return f"{ingredients} {status}"
