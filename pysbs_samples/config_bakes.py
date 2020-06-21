import json

# Define the bake types
BENT_NORMAL = "bentnormal"
NORMAL = "normal"

# Defining the user customizable data
USER_SETTINGS_FILE = "user_settings.json"
CONFIG_FILES_RELATIONSHIP_DICTIONARY = {
    BENT_NORMAL: "config_bentnormal.json",
    NORMAL: "config_normal.json"
    # Add additional config files as needed
}

# Loading all the defined user configs and assembling a list of configs
configs_dict = {}
for config_key, config_value in CONFIG_FILES_RELATIONSHIP_DICTIONARY.items():
    with open(config_value) as current_config:
        current_config_dictionary = json.load(current_config)
        configs_dict[config_key] = current_config_dictionary


class BentNormals(object):
    # Bent Normals user settings; more settings can be added, as supported by the API
    def __init__(self):
        _bent_normals_config_data = BentNormals.get_bent_normals_config_data()
        # Properties
        self.output_name_flag = _bent_normals_config_data["output_name_flag"]
        self.output_size = _bent_normals_config_data["output_size"]
        self.antialiasing = _bent_normals_config_data["antialiasing"]
        self.ignore_backface = _bent_normals_config_data["ignore_backface"]
        self.self_occlusion = _bent_normals_config_data["self_occlusion"]
        self.use_lowdef_as_highdef = _bent_normals_config_data["use_lowdef_as_highdef"]
        self.uv_set = _bent_normals_config_data["uv_set"]

    @staticmethod
    def get_bent_normals_config_data():
        return configs_dict[BENT_NORMAL]
