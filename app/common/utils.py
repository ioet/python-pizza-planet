
def check_required_keys(keys: tuple, element: dict):
    return all(element.get(key) for key in keys)

def response_to_dict(response, key):
    data_dict = {}
    for item in response.json:
        data_dict[item[key]] = item
    return data_dict