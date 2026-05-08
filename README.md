# Online Store API Automation Framework

This project demonstrates an API automation framework built using Python, pytest, and requests library. It is designed to validate REST API endpoints of an online store application.

## Features

* Automated API testing using pytest framework
* Supports HTTP methods: GET, POST, PUT, DELETE
* JSON response validation using assertions
* Data-driven testing using pytest
* Centralized configuration and reusable fixtures
* Logging of request and response details
* Allure reporting for test execution results

## Tech Stack

* Python
* pytest
* requests
* Allure Reports

## How to Run

1. Install dependencies:
   pip install -r requirements.txt

2. Run tests:
   pytest testcases/ --alluredir=reports/allure-results

3. Generate report:
   allure generate reports/allure-results -o reports/allure-report --clean

4. Open report:
   allure open reports/allure-report

or from command prompt->run.bat

## Learning Outcome

* Gained hands-on experience in API automation using pytest
* Learned to design reusable and scalable test frameworks
* Understood request-response handling
