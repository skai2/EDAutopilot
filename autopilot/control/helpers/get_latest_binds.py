def get_latest_binds(path_bindings=None):
    if not path_bindings:
        path_bindings = environ['LOCALAPPDATA'] + "\Frontier Developments\Elite Dangerous\Options\Bindings"
    list_of_bindings = [join(path_bindings, f) for f in listdir(path_bindings) if isfile(join(path_bindings, f))]
    if not list_of_bindings:
        return None
    latest_bindings = max(list_of_bindings, key=getmtime)
    return latest_bindings