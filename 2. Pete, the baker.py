def cakes(recipe, available):
    """ Function that checks whether Peter can do the recipe 
    based on a list of ingredients and current availability """
    result = []
    for key, values in recipe.items():
        if key in available:
            capacity = available[key] // values
            if capacity > 0:
                result.append(capacity)
                continue
            else:
                return 0
        else:
            return 0

    return min(result)