import json

# Defining the user customizable data
USER_SETTINGS_FILE = "user_settings.json"

# Loading the user customizable data
with open(USER_SETTINGS_FILE) as user_settings:
    user_settings_dictionary = json.load(user_settings)


class UserSetting(object):
    # Establishing the project constants based on the user configured files
    def __init__(self):
        self.substance_automation_toolkit_path = user_settings_dictionary["substance_automation_toolkit_path"]
        self.output_path = user_settings_dictionary["output_path"]
        self.low_polys_path = user_settings_dictionary["lows_path"]
        self.high_polys_path = user_settings_dictionary["highs_path"]
        self.input_format = user_settings_dictionary["input_format"]
        self.output_format = user_settings_dictionary["output_format"]
        self.lowpoly_nameflag = user_settings_dictionary["low_poly_nameflag"]
        self.highpoly_nameflag = user_settings_dictionary["high_poly_nameflag"]
