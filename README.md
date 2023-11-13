# Score Calculator App
This Flask-based web application enables users to input a difficulty score and 
execution deductions to automatically calculate a final score. It's designed to
simplify performance evaluations in a gymnastics competitions.

## Get started
To get started with the Flask scoring application, the user should follow these steps

### Set up the environment:
Ensure Python and pip are installed on the system. Create a virtual environment in the project directory:

``
    python -m venv venv
``

Activate the virtual environment:
On Windows:


``
    venv\Scripts\activate
``

On Unix or MacOS:

``
    source venv/bin/activate
``

### Install Flask:
With the virtual environment activated, install Flask using pip:

``
    pip install flask
``
### Start the application:
The main Python file is main.py. Run it with the following command:
``
    python app.py
``
### Access the application:
Open a web browser and navigate to http://127.0.0.1:5000/ to use the application.

The file app.py contains all the routes and logic for the web application and serves as the entry point to the Flask application.

### Other cases
In other cases the user might first have to install some project dependencies
first has to run something like this (a sample requirements.txt file is also
included in the project template):

``
    pip install -r requirements.txt
``

## Understanding the sources
The software leverages Flask's simplicity for web service creation, focusing on 
ease of use and clear data flow. The idea was to provide a user-friendly interface 
for score calculation without extensive setup. The core concept involves input
validation and automated calculation to ensure reliability, which might not be 
apparent from the code alone.
