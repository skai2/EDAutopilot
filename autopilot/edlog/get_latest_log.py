# Get latest log file
def get_latest_log(path_logs=None):
    """Returns the full path of the latest (most recent) elite log file (journal) from specified path"""
    if not path_logs:
        path_logs = environ['USERPROFILE'] + "\Saved Games\Frontier Developments\Elite Dangerous"
    list_of_logs = [join(path_logs, f) for f in listdir(path_logs) if
                    isfile(join(path_logs, f)) and f.startswith('Journal.')]
    if not list_of_logs:
        return None
    latest_log = max(list_of_logs, key=getmtime)
    return latest_log