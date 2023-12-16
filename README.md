# Alexandra Dudari CV App

This Flask application serves CV data through a JSON REST API and a CLI command.

## 1. Running the REST API

1. Make sure you have Python 3.11 and virtualenv installed.
2. Create a virtual environment: 
`python -m venv venv` or
`python -m venv /path/to/new/virtual/environment`
3. Activate the virtual environment:
    - On Linux/macOS: `source venv/bin/activate`
    - On Windows: `venv\Scripts\activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Run the Flask app: `python app.py`

The API will be available at http://127.0.0.1:5000/.

## 2. Running the CLI Command

1. Make sure you have Python 3.11 and virtualenv installed.
2. Create a virtual environment: 
`python -m venv venv` or
`python -m venv /path/to/new/virtual/environment`
3. Activate the virtual environment:
    - On Linux/macOS: `source venv/bin/activate`
    - On Windows: `venv\Scripts\activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Execute the CLI command: `flask show key`. The key can have one of the following values:
- personal
- experience
- education
- certifications

Example of usage: `flask show experience`


## 3. Running the unittest
To run unittest from the command line in Python, you can use the following command:

`python -m unittest discover`

This command will run all the tests in the current directory and its subdirectories. If you want to run a specific test file, you can use the following command:

`python -m unittest test_file.py`

If you want to run a specific test case or test method, you can use the following command:

`python -m unittest test_file.TestClass.test_method`
