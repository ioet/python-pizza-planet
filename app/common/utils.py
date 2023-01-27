def check_required_keys(keys: tuple, element: dict):
    return all(element.get(key) for key in keys)
