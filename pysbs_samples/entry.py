import os
import pysbs
import user_settings
import custom_logger
import config_bakes


def batch_bake(
        substance_automation_toolkit_path,
        bake_output_path,
        low_poly_meshes_directory_path,
        high_poly_meshes_directory_path,
        input_format,
        output_format,
        low_poly_nameflag,
        high_poly_nameflag,
        bake_types_list):
    """
    :param substance_automation_toolkit_path: (string)
    :param bake_output_path: (string)
    :param low_poly_meshes_directory_path: (string)
    :param high_poly_meshes_directory_path: (string)
    :param input_format: (string)
    :param output_format: (string)
    :param low_poly_nameflag: (string)
    :param high_poly_nameflag: (string)
    :param bake_types_list: (list)
    """
    if not os.path.exists(bake_output_path):
        os.mkdir(bake_output_path)

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
                bake_bentnormal(
                    low_poly_input_path=low_poly_input_path,
                    high_poly_input_path=high_poly_input_path,
                    output_size=bent_normal_bake_configs.output_size,
                    output_format=current_user_settings.output_format,
                    output_path=current_user_settings.output_path,
                    baker_name="",
                    udim=""
                )

    cl.log("Batch baking successfully completed.")


def bake_bentnormal(low_poly_input_path,
                    high_poly_input_path,
                    output_size,
                    output_format,
                    output_path,
                    baker_name,
                    udim):
    """
    :param low_poly_input_path: (string) Path to the low mesh.
    :param high_poly_input_path: (string) Path to the high poly mesh.
    :param output_size: (int) Output size as a power of two
    :param output_format: (str) Output format of the baked map (example: png)
    :param output_path: (str) Output folder path
    :param baker_name: (str) Name of the baker
    :param udim: (str) The udim to process
    """
    cl.log("--- --- Baking: Bent Normal started.")
    output_name = '%s_%s' % (baker_name, udim)
    pysbs.batchtools.sbsbaker_curvature(low_poly_input_path,
                                        output_size=[output_size, output_size],
                                        output_format=output_format,
                                        output_path=output_path,
                                        udim=udim,
                                        output_name=output_name).wait()
    cl.log("--- --- Baking: Bent Normal successfully completed.")


# Instantiate the user settings
current_user_settings = user_settings.UserSetting()

# Instantiate the custom logger
cl = custom_logger.CustomLogger()

# SAMPLE: Trigger a bake for BENT_NORMAL
batch_bake(
    substance_automation_toolkit_path=current_user_settings.substance_automation_toolkit_path,
    bake_output_path=current_user_settings.output_path,
    low_poly_meshes_directory_path=current_user_settings.low_polys_path,
    high_poly_meshes_directory_path=current_user_settings.high_polys_path,
    output_format=current_user_settings.output_format,
    input_format=current_user_settings.input_format,
    low_poly_nameflag=current_user_settings.lowpoly_nameflag,
    high_poly_nameflag=current_user_settings.highpoly_nameflag,
    # For the "bake_types_list", many more bake types can be added to the list for multi-baking below
    bake_types_list=[config_bakes.BENT_NORMAL])
