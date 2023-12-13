# Project Setup Guide

This guide will help you set up and run the project on your local machine.

## Prerequisites

Before you begin, make sure you have the following software installed:

- [Python 3.x](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)

## Setup

1. Clone the project repository to your local machine:

   ```bash
   git clone git@github.com:LuizFrra/poc-genai-chunk-strategy.git
   ```

2. Create a Python virtual environment (venv) to isolate the project's dependencies

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment

    3.1 Windows
    ```bash 
    venv\\Scripts\\activate
    ```
    3.2 MacOS or Linux
    ```bash 
    source venv/bin/activate
    ```
4. Install the spaCy model xx_sent_ud_sm:
    ```bash 
    python -m spacy download xx_sent_ud_sm
    ```

## Usage

1. You can choose which chunk strategy you would like to test modifying the main.py file, there are some optios commented.

2. Go to folder src and execute the following comand
    ```bash 
    python main.py
    ```


