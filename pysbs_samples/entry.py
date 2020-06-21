import os
import pysbs
import user_settings
import custom_logger
import config_bakes


def batch_bake(
        bake_output_path,
        low_poly_meshes_directory_path,
        high_poly_meshes_directory_path,
        input_format,
        low_poly_nameflag,
        high_poly_nameflag,
        bake_types_list):
    """
    :param bake_output_path: (string) The path to the desired export directory.
    :param low_poly_meshes_directory_path: (string) The path to the existing low poly assets.
    :param high_poly_meshes_directory_path: (string) The path to the existing high poly assets.
    :param input_format: (string) The model format of the input (for example "fbx")
    :param low_poly_nameflag: (string) The naming differentiator that identifies an asset as the low poly ("_low")
    :param high_poly_nameflag: (string) The naming differentiator that identifies an asset as the high poly ("_high")
    :param bake_types_list: (list) A list of the bake types (as defined in the config_bakes.py) you want to batch
    """
    if not os.path.exists(bake_output_path):
        os.mkdir(bake_output_path)

    extension_len = len(input_format) + 1

    # Assemble a list of the found lowpoly assets
    found_files_in_lowpoly_directory = []
    for (directory_path, directory_names, filenames) in os.walk(low_poly_meshes_directory_path):
        found_files_in_lowpoly_directory.extend(filenames)
        break
    found_lowpoly_assets = []
    for found_file in found_files_in_lowpoly_directory:
        if str(found_file).lower().endswith(input_format):
            found_lowpoly_assets.append(str(found_file))

    # Determine matching high poly names and build a dictionary of matchings
    low_to_high_match_dictionary = {}
    for lowpoly_asset in found_lowpoly_assets:
        expected_highpoly_asset_name = lowpoly_asset.replace(low_poly_nameflag, high_poly_nameflag)
        expected_highpoly_path = os.path.join(high_poly_meshes_directory_path, expected_highpoly_asset_name)
        if os.path.exists(expected_highpoly_path):
            low_to_high_match_dictionary[lowpoly_asset] = expected_highpoly_asset_name
        else:
            low_to_high_match_dictionary[lowpoly_asset] = lowpoly_asset

    # For each match, run the bake request
    for low_poly_name, high_poly_name in low_to_high_match_dictionary.items():
        low_poly_input_path = os.path.join(low_poly_meshes_directory_path, low_poly_name)
        high_poly_input_path = os.path.join(high_poly_meshes_directory_path, high_poly_name)
        cl.log("For the following pairing: ")
        cl.log("--- low poly mesh: " + low_poly_input_path)
        cl.log("--- high poly mesh: " + high_poly_input_path)

        # For each type of provided bake, run a bake if it matches the rules
        for bake_type in bake_types_list:
            if bake_type == config_bakes.BENT_NORMAL:
                # Instantiate the Bent Normal Bake Config
                bent_normal_bake_configs = config_bakes.BentNormals()
                bent_normal_bake_file_name = \
                    low_poly_name[:-extension_len].replace(low_poly_nameflag, "") + \
                    bent_normal_bake_configs.output_name_flag
                bake_bentnormal(
                    low_poly_input_path=low_poly_input_path,
                    high_poly_input_path=high_poly_input_path,
                    output_size=bent_normal_bake_configs.output_size,
                    output_format=current_user_settings.output_format,
                    output_path=current_user_settings.output_path,
                    output_name=bent_normal_bake_file_name,
                    antialiasing=str(bent_normal_bake_configs.antialiasing),
                    ignore_backface=str(bent_normal_bake_configs.ignore_backface),
                    self_occlusion=str(bent_normal_bake_configs.self_occlusion),
                    use_lowdef_as_highdef=str(bent_normal_bake_configs.use_lowdef_as_highdef),
                    uv_set=str(bent_normal_bake_configs.uv_set))

    cl.log("Batch baking successfully completed.")


def bake_bentnormal(low_poly_input_path,
                    high_poly_input_path,
                    output_size,
                    output_format,
                    output_path,
                    output_name,
                    antialiasing="0",
                    ignore_backface="true",
                    self_occlusion="0",
                    use_lowdef_as_highdef="false",
                    uv_set="0"
                    ):
    """
    :param low_poly_input_path: (string) Path to the low mesh.
    :param high_poly_input_path: (string) Path to the high poly mesh.
    :param output_size: (int) Output size as a power of two (i.e. 12 represents 2^12 = 4096, 11 represents 2^11 = 2048).
    :param output_format: (str) Output format of the baked map (i.e. "png", "tga").
    :param output_path: (str) Output folder path.
    :param output_name: (str) Name of the baked image file.
    :param antialiasing: (str) The integer antialiasing value, passed as a string.
    :param ignore_backface: (str) The boolean to respect or ignore back faces, passed as a string.
    :param self_occlusion: (str) The integer self occlusion amount, passed as a string.
    :param use_lowdef_as_highdef: (str) The boolean to use the low poly as high poly, passed as a string.
    :param uv_set: (str) The integer UV set number, passed as a string.
    """
    cl.log("--- --- Baking: Bent Normal for '{0}' has started.".format(output_name))
    pysbs.batchtools.sbsbaker_bent_normal_from_mesh(inputs=low_poly_input_path,
                                                    highdef_mesh=high_poly_input_path,
                                                    output_size=[output_size, output_size],
                                                    output_format=output_format,
                                                    output_path=output_path,
                                                    output_name=output_name,
                                                    antialiasing=antialiasing,
                                                    ignore_backface=ignore_backface,
                                                    self_occlusion=self_occlusion,
                                                    use_lowdef_as_highdef=use_lowdef_as_highdef,
                                                    uv_set=uv_set
                                                    ).wait()
    cl.log("--- --- Baking: Bent Normal for '{0}' has successfully completed.".format(output_name))


# Instantiate the user settings
current_user_settings = user_settings.UserSetting()

# Instantiate the custom logger
cl = custom_logger.CustomLogger()

# SAMPLE: Trigger a bake for BENT_NORMAL
batch_bake(
    bake_output_path=current_user_settings.output_path,
    low_poly_meshes_directory_path=current_user_settings.low_polys_path,
    high_poly_meshes_directory_path=current_user_settings.high_polys_path,
    input_format=current_user_settings.input_format,
    low_poly_nameflag=current_user_settings.lowpoly_nameflag,
    high_poly_nameflag=current_user_settings.highpoly_nameflag,
    # For the "bake_types_list", many more bake types can be added to the list for multi-baking below
    bake_types_list=[config_bakes.BENT_NORMAL])
