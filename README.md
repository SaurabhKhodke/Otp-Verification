# Employee Login and OTP Verification System

This project is a simple Employee Login and OTP (One Time Password) verification system built using Flask, MySQL, and Flask-Mail.

## Overview

This project aims to provide a secure and user-friendly login system for employees. It utilizes Flask, a Python web framework, to handle HTTP requests, MySQL database for storing employee information, and Flask-Mail for sending OTPs via email for verification.

## Features

- Employee login with OTP verification.
- Admin panel for adding new employees.
- Secure OTP generation using Python's random module.
- Integration with Gmail SMTP for sending emails.


Once the database is created, import the employees.sql file located in the project directory to create the required table.

Configuration
Open the app.py file and update the following configurations:

MySQL connection details (MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB)
Gmail SMTP server details (MAIL_SERVER, MAIL_PORT, MAIL_USERNAME, MAIL_PASSWORD, MAIL_DEFAULT_SENDER)

## Usage
### Employee Login
Visit the login page (/login) of the application.
Enter your employee ID, name, and email.
Click on the "Login" button.
An OTP (One Time Password) will be sent to your email.
Enter the received OTP for verification.
### Admin Panel
Access the admin panel (/admin) to add new employees.
Enter the employee details and submit the form.
The new employee will be added to the database.

## Screenshots

```bash
pip install Flask Flask-Mail Flask-MySQLdb
