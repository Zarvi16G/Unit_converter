
def type_unit_form_weight(weight, unit_from, unit_to):
    if unit_from == 'milligram':
        return weight_milligram_to(weight, unit_to)
    elif unit_from == 'gram':
        return weight_gram_to(weight, unit_to)
    elif unit_from == 'kilogram':
        return weight_kilogram_to(weight, unit_to)
    elif unit_from == 'ounce':
        return weight_ounce_to(weight, unit_to)
    elif unit_from == 'pound':
        return weight_pound_to(weight, unit_to)
    
def weight_milligram_to(weight, unit_to):
    if unit_to == 'gram':
        return weight / 1000  # 1 gram = 1000 milligrams
    elif unit_to == 'kilogram':
        return weight / 1_000_000  # 1 kilogram = 1,000,000 milligrams
    elif unit_to == 'ounce':
        return weight / 28349.5  # 1 ounce = 28,349.5 milligrams
    elif unit_to == 'pound':
        return weight / 453592  # 1 pound = 453,592 milligrams
    else:
        return weight  # mismo peso en miligramo

def weight_gram_to(weight, unit_to):
    if unit_to == 'milligram':
        return weight * 1000  # 1 gram = 1000 milligrams
    elif unit_to == 'kilogram':
        return weight / 1000  # 1 kilogram = 1000 grams
    elif unit_to == 'ounce':
        return weight / 28.3495  # 1 ounce = 28.3495 grams
    elif unit_to == 'pound':
        return weight / 453.592  # 1 pound = 453.592 grams
    else:
        return weight  # mismo peso en gramos

def weight_kilogram_to(weight, unit_to):
    if unit_to == 'milligram':
        return weight * 1_000_000  # 1 kilogram = 1,000,000 milligrams
    elif unit_to == 'gram':
        return weight * 1000  # 1 kilogram = 1000 grams
    elif unit_to == 'ounce':
        return weight * 35.274  # 1 kilogram = 35.274 ounces
    elif unit_to == 'pound':
        return weight * 2.20462  # 1 kilogram = 2.20462 pounds
    else:
        return weight  # mismo peso en kilogramos

def weight_ounce_to(weight, unit_to):
    if unit_to == 'milligram':
        return weight * 28349.5  # 1 ounce = 28,349.5 milligrams
    elif unit_to == 'gram':
        return weight * 28.3495  # 1 ounce = 28.3495 grams
    elif unit_to == 'kilogram':
        return weight / 35.274  # 1 ounce = 0.0283495 kilograms
    elif unit_to == 'pound':
        return weight / 16  # 1 pound = 16 ounces
    else:
        return weight  # mismo peso en onzas

def weight_pound_to(weight, unit_to):
    if unit_to == 'milligram':
        return weight * 453592  # 1 pound = 453,592 milligrams
    elif unit_to == 'gram':
        return weight * 453.592  # 1 pound = 453.592 grams
    elif unit_to == 'kilogram':
        return weight / 2.20462  # 1 pound = 0.453592 kilograms
    elif unit_to == 'ounce':
        return weight * 16  # 1 pound = 16 ounces
    else:
        return weight  # mismo peso en libras

