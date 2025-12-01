# Professional Streamlit Calculator

This is a simple yet professional-looking calculator built with Python and Streamlit. It provides a clean, web-based interface for basic arithmetic operations.

## Features

- Addition
- Subtraction
- Multiplication
- Division (with error handling for division by zero)
- Intuitive web interface using Streamlit

## Installation

To run this application locally, follow these steps:

1.  **Clone the repository (if you haven't already):**
    ```bash
    git clone https://github.com/javeri-a/claude_calculator.git
    cd claude_calculator/my_application
    ```

2.  **Install dependencies:**
    Make sure you have Python installed. Then, install Streamlit and other necessary packages using `pip`:
    ```bash
    pip install -r requirements.txt
    ```

## How to Run Locally

After installation, you can run the Streamlit application from your terminal:

```bash
streamlit run calculator.py
```

This command will open the calculator in your default web browser.

## Deployment to Streamlit Cloud

This application is designed to be easily deployable on [Streamlit Cloud](https://share.streamlit.io/). Follow these steps:

1.  **Ensure your code is pushed to a GitHub repository.** (This has already been done to `https://github.com/javeri-a/claude_calculator.git`)
2.  Go to [share.streamlit.io](https://share.streamlit.io/) and sign in with your GitHub account.
3.  Click on "New app".
4.  Select your repository (`javeri-a/claude_calculator`) and set the "Main file path" to `calculator.py`.
5.  Click "Deploy!".

Streamlit Cloud will handle the rest, building and deploying your application, and providing you with a public URL:https://javeri-a-claude-calculator-calculator-mpv973.streamlit.app/

