# Permissions Analyzer

# Permissions Analyzer

## Overview
Permissions Analyzer is a Python-based tool designed to extract and display the permissions requested by an Android APK file. Using the powerful [Androguard](https://github.com/androguard/androguard) library, this tool categorizes permissions into dangerous and other permissions, providing a structured and detailed output for analysis. Permissions can be displayed directly on the terminal or saved to a file for future reference.

## Features
- Analyze any APK file to extract permissions.
- Categorize permissions into **Dangerous Permissions** and **Other Permissions**.
- View detailed APK metadata such as app name, package name, and version.
- Output permissions to the terminal or save them to a text file.
- Automatically generate a well-formatted output file.
- User-friendly command-line interface.

## Requirements
- Python 3.x
- [Androguard](https://github.com/androguard/androguard) library

## Installation
1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/permissions-analyzer.git
    cd permissions-analyzer
    ```

2. Create and activate a virtual environment (recommended):
    ```bash
    python3 -m venv analyzer-env
    source analyzer-env/bin/activate
    ```

3. Install dependencies:
    ```bash
    pip install androguard
    ```

## Usage
1. Run the script:
    ```bash
    python permissions_analyzer.py
    ```

2. Follow the prompts:
    - Enter the path to the APK file.
    - Choose whether to display the results on the screen or save them to a file.

### Example Output (Terminal)

========= Permissions Analysis ========= File: example.apk App Name: Example App Package Name: com.example.app Version: 1.0.0 Analysis Date: 2025-01-21 14:45:00

Summary:

    Total permissions: 25
    Dangerous permissions: 8
    Other permissions: 17

Dangerous Permissions:

    android.permission.CAMERA
    android.permission.ACCESS_FINE_LOCATION
    android.permission.READ_CONTACTS

Other Permissions:

    android.permission.INTERNET
    android.permission.BLUETOOTH
    android.permission.VIBRATE
