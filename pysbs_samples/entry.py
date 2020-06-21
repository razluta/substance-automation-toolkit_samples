import json
import pysbs

# Defining the user customizable data
USER_SETTINGS_FILE = "user_settings.json"
CONFIG_FILES = [
    "config_bentnormal.json"
    # Add additional config files as needed
]

# Loading the user customizable data
with open(USER_SETTINGS_FILE) as user_settings:
    user_settings_dictionary = json.load(user_settings)

# Loading all the defined user configs and assembling a list of configs
configs_list = []
for config in CONFIG_FILES:
    with open(config) as current_config:
        current_config_dictionary = json.load(current_config)
        configs_list.append(current_config_dictionary)

print user_settings_dictionary
