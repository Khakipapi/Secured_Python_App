# Flask Web Application

## Introduction
This repository contains a Flask web application that includes user authentication, database interaction, and form handling.

## Table of Contents
- [Introduction](#introduction)
- [Usage](#usage)
- [Features](#features)
- [Dependencies](#dependencies)
- [Configuration](#configuration)
- [Examples](#examples)
- [Troubleshooting](#troubleshooting)
- [Contributors](#contributors)
- [License](#license)

## Usage
To start the Flask application, run the `app.py` script:

```bash
flask run
```

## Features
- **User Authentication:** Includes user login and registration.
- **Database Interaction:** Uses SQLite for storing user data.
- **Form Handling:** Uses WTForms for form validation and handling.

## Dependencies
- Flask
- Flask SQLAlchemy
- Flask Login
- Flask WTForms
- Flask Bcrypt

You can install the dependencies using the following command:

```bash
pip install flask flask_sqlalchemy flask_login flask_wtf flask_bcrypt
```

## Configuration
Configuration settings such as the database URI and secret key are set in the `app.py` file. Ensure these configurations are correct for your environment.

## Examples
### Running the Flask Application
```bash
flask run
```

Example interaction:

```
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

## Troubleshooting
- Ensure Python and the required packages are installed correctly.
- Verify the database is set up correctly and migrations are applied.
- Ensure the Flask server is running and accessible.

## Contributors
- Jose Reyes - Initial work

## License
This project is licensed under the MIT License. See the LICENSE file for details.
