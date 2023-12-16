import os
import json


def read_stream(file_name: str) -> dict:
    """
        Read a JSON file and return its content as a dictionary.

        Args:
            file_name (str): The name of the JSON file to read.

        Returns:
            dict: The content of the JSON file as a dictionary. If the file
                     does not exist, an empty dictionary is returned.
    """
    current_dir = os.path.dirname(__file__)
    cv_data_path = os.path.join(current_dir, file_name)

    with open(cv_data_path, "r", encoding="utf-8") as file:
        try:
            cv_data = json.load(file)
        except FileNotFoundError:
            cv_data = {}

    return cv_data
