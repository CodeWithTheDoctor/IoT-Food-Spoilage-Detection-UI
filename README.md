# CITS5506 IoT Project - Food Spoilage Detection System

## Contents

- [CITS5506 IoT Project - Food Spoilage Detection System](#cits5506-iot-project---food-spoilage-detection-system)
  - [Contents](#contents)
  - [Tech Stack](#tech-stack)
  - [Running Development Environment](#running-development-environment)
  - [Deployment to production](#deployment-to-production)

## Tech Stack

**Flask**: A lightweight python framework to build fullstack applications.

## Running Development Environment

When you need to do development work, these are the steps you need to take in or to run the environment first:

1. Clone this repository
   - And make sure you have set up authentication to your github account locally if you plan to push changes to this repository.

2. Create + Activate the virtual environment
     - Virtual environments are for containing the python dependencies locally within a project folder rather than installing it globally to your machine.
     - Inside the project folder, run the following commands:
       - macOS/Linux:
         - a. `python3 -m venv .venv` (skip to b. if you've done this before)
         - b. `. .venv/bin/activate`
       - Windows:
         - a. `py -3 -m venv .venv` (skip to b. if you've done this before)
         - b. `.venv\Scripts\activate`

3. Install project dependencies (flask, etc.) (Skip this step if you've done this before)
     - `pip install -r requirements.txt`

4. Running the flask application:
     - `flask run --host=0.0.0.0` (if you're running it on your own computer, just run `flask run`)
     - This runs the code from `app.py` file in the root directory. The output might look like:

       ```plaintext
       * Debug mode: off
       WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
       * Running on http://127.0.0.1:5000
       * Running on http://192.168.1.106:5000
       ```

        - Open the link in your browser to see the application running. 
          - The first link is for your local machine, and the second link is for your network. You can access the application from any device connected to the same network.

## Deployment to production

- We may or not not need to deploy this application in production mode.
- In case we do, refer to [this](https://flask.palletsprojects.com/en/3.0.x/deploying/) resource.
