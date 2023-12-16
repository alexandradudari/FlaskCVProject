import click
from flask.cli import cli, with_appcontext
from tabulate import tabulate

from core import read_stream


@cli.command("show")
@click.argument("data")
@with_appcontext
def show(data: str) -> None:
    """
        Retrieve and display specific data from the CV dataset.

        Args:
            data (str): The key indicating the data to display.

        Returns:
            None: This function prints the data table to the console.

        Raises:
            FileNotFoundError: If 'cv_data.json' is not found.
    """

    headers, data_table = [], []
    cv_data = read_stream(file_name="cv_data.json")

    data_list = cv_data.get(data, [])
    if isinstance(data_list, list) and len(data_list) > 0:
        headers = [key.capitalize() for key in data_list[0].keys()]
        data_table = [list(entry.values()) for entry in data_list]

    if headers and data_table:
        print(tabulate(data_table, headers=headers))
    else:
        print(f"No data available for '{data}'", end=".")
