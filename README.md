# Weel Automated Test Suite

This repository contains a Selenium-based test suite designed to automate the testing of a web application's sign-up and login functionalities. The tests are written in Python and use Pytest as the testing framework.

## Dependencies

Before running the test suite, ensure you have the following installed on your machine:

- Python 3.x
- pip (Python package installer)
- Google Chrome browser
- ChromeDriver (compatible with your version of Chrome)

## Running the Tests

1. Clone the repository:
   ```bash
   git clone https://github.com/Riya1993/Weel.git
   # You can also take code from master branch
   cd test.py
2. Install dependency:
   ```bash
   pip install -r requirements.txt
3. If you don't have a requirements.txt, install the necessary packages directly:
   ```bash
   pip install selenium pytest
4. Set Up ChromeDriver:
Ensure ChromeDriver is in your system’s PATH, or specify the path in the script (already configured in the test script).
5. Execute the test case using pytest:
   ```bash
   pytest test.py
6. Test results will be displayed in pytest output.





