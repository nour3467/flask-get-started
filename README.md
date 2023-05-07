# Get Started with Flask 🌐

## Description

This README provides a guide on how to get started with Flask, a Python microframework for writing web applications. Flask is minimal, clean, and simple to use. It comes with a minimal set of features, which allows developers to avoid bloatware and focus on building the specific features they require for their projects [Source 4](https://www.wisdomgeek.com/development/web-development/flask/getting-started-with-flask-a-python-microframework/).

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [References](#references)

## Installation 💻

Before you begin, make sure you have Python 3 and pip installed on your system. To install Flask, follow the steps below:

1. Create a virtual environment for your project:

   ```bash
   python3 -m venv venv
   ```

2. Activate the virtual environment:

   ```bash
   source venv/bin/activate
   ```

3. Install Flask using pip:

   ```bash
   pip install Flask
   ```

   [Source 1](https://flask.palletsprojects.com/en/2.2.x/quickstart/)

## Usage 🚀

To create a simple Flask application, follow the steps below:

1. Create a new file called `app.py` in your project directory.

2. Add the following code to `app.py`:

   ```python
   from flask import Flask

   app = Flask(__name__)

   @app.route("/")
   def hello():
       return "Hello, World! 👋"

   if __name__ == "__main__":
       app.run()
   ```

3. Run the Flask application:

   ```bash
   python app.py
   ```

   This will start a local development server on `http://localhost:5000/`. You can visit this URL in your browser to see the "Hello, World!" message displayed.

   [Source 4](https://www.wisdomgeek.com/development/web-development/flask/getting-started-with-flask-a-python-microframework/)

## Features 🌟

Flask is a microframework, which means it provides a minimal set of features out of the box. This allows developers to avoid unnecessary bloatware and focus on building the specific features they require for their projects. Some of the key features of Flask include:

- URL routing 🛣️
- Template rendering 🎨
- Error handling ⚠️
- Static file serving 📂
- Support for extensions 🔌

  [Source 4](https://www.wisdomgeek.com/development/web-development/flask/getting-started-with-flask-a-python-microframework/)

## References 📚

- [Flask Quickstart](https://flask.palletsprojects.com/en/2.2.x/quickstart/)
- [Getting started with Flask: a Python microframework](https://www.wisdomgeek.com/development/web-development/flask/getting-started-with-flask-a-python-microframework/)
