def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients

    allowed = light_spell_allowed_ingredients()
    ingredients_lower = ingredients.lower()
    is_valid = any(item in ingredients_lower for item in allowed)

    status: str = "INVALID"
    if is_valid:
        status = "VALID"
    return f"{ingredients} {status}"
