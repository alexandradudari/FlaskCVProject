import manage
from flask import Flask, render_template

from core import read_stream

app = Flask(__name__, static_url_path='/static')
app.config.from_object("config")
app.cli.add_command(manage.show)


def render_template_with_cv_data(template_name: str, file_name: str, data_key: str) -> str:
    """
        Render a Flask template with data from a JSON file.

        Args:
            template_name (str): The name of the Flask template.
            file_name (str): The name of the JSON file containing data.
            data_key (str): The key to extract data from the JSON file.

        Returns:
            str: The rendered HTML content of the template.
    """
    cv_data = read_stream(file_name=file_name)
    return render_template(template_name, **{data_key: cv_data.get(data_key, {})})


@app.route("/", methods=["GET"])
def get_cv():
    return render_template("home.html")


@app.route("/personal", methods=["GET"])
def get_personal_info() -> str:
    return render_template_with_cv_data(
        template_name="personal.html",
        file_name="cv_data.json",
        data_key="personal"
    )


@app.route("/education", methods=["GET"])
def get_education() -> str:
    return render_template_with_cv_data(
        template_name="education.html",
        file_name="cv_data.json",
        data_key="education"
    )


@app.route("/experience", methods=["GET"])
def get_experience() -> str:
    return render_template_with_cv_data(
        template_name="experience.html",
        file_name="cv_data.json",
        data_key="experience"
    )


@app.route("/certifications", methods=["GET"])
def get_certifications() -> str:
    return render_template_with_cv_data(
        template_name="certifications.html",
        file_name="cv_data.json",
        data_key="certifications"
    )


if __name__ == "__main__":
    app.run()
