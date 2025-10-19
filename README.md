# Universal-Calculator
The Universal Unit Converter is a Flask web app for converting units across Mass, Length, Volume, Time, and Temperature. It features a dynamic interface where units change based on category. The backend handles metric and temperature-specific math, all styled with a modern, glassy CSS design.

## Universal Unit Converter Setup Guide

This guide will walk you through setting up and running the Universal Unit Converter web application on your local machine.

### Prerequisites

Before you start, you'll need the following installed:

  * **Python 3** (The application was developed using Python and the Flask framework.)
  * **pip** (Python's package installer, usually included with Python 3.)

### 1\. Project Structure

When you download the project (e.g., by extracting `Universal Calculator.zip`), ensure your folder structure looks like this:

```
Universal Calculator/
├── python1.py           # The Flask application logic (main file)
├── static/
│   ├── 1.jpg            # Background image
│   └── styles.css       # Custom CSS styling
└── templates/
    └── index.html       # The main HTML page
```

**Note:** The main Python file is named `python1.py` and the main folder is `Universal Calculator`.

### 2\. Install Dependencies

You need to install the **Flask** package to run the application.

1.  **Open your terminal or command prompt.**
2.  **Navigate to the project directory:**
    ```bash
    cd "Universal Calculator"
    ```
3.  **Install Flask:**
    ```bash
    pip install Flask
    ```

### 3\. Run the Application

Once Flask is installed, you can start the web server.

1.  **Ensure you are still in the `Universal Calculator` directory.**
2.  **Run the Python file:**
    ```bash
    python python1.py
    ```
    *You should see output indicating that the Flask server is running.*

### 4\. Access the Converter

1.  **Open your web browser** (Chrome, Firefox, Edge, etc.).
2.  **Go to the following address:**
    ```
    http://127.0.0.1:5000/
    ```

You should now see the Universal Unit Converter interface. The server will continue running in your terminal until you stop it (usually by pressing **Ctrl + C**).
