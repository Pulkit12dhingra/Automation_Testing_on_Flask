# Flask Website Skeleton with Comprehensive Testing

This repository provides a useful skeleton for developing and testing Flask-based websites. It includes a basic Flask application and a comprehensive suite of tests to ensure the functionality and performance of the application.

## Getting Started

### Prerequisites

- Python 3.x
- Flask
- Selenium
- Locust
- Bandit

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/flask-website-skeleton.git
    cd flask-website-skeleton
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

### Running the Application

To run the Flask application, execute:
```sh
python app.py
```

### Running the Tests

To run all the tests, execute:
```sh
python test.py
```

Individual tests are located in the `testing` folder and can be run separately if needed.

### Types of Testing

We are running the following types of tests for this website:

- **Unit Testing**: Ensures that individual components of the application work as expected. These tests are typically written for individual functions or methods.
- **Functional Testing**: Validates the software against the functional requirements/specifications. It ensures that the application behaves as expected.
- **Load Testing**: Assesses the application's performance under a specific expected load. This helps identify performance bottlenecks.
- **Browser Testing**: Uses Selenium to automate browser actions and verify that the web application works correctly in different browsers.
- **API Testing**: Ensures that the API endpoints of the application are functioning correctly and returning the expected responses.
- **Security Testing**: Identifies potential vulnerabilities in the application using tools like Bandit to ensure the application is secure from common threats.