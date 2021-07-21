# **E-Buy** - [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

## **How to start the project locally?**
<ol>
    <li>
        You should install Python in order to run the app.
        <br/>
        <code>
            <u>https://www.python.org/downloads/</u>
        </code>
    </li>
    <li>
        Open the project in console, IDE or text editor.
    </li>
    <li>
        Install virtual environment (if you haven't already!!!) in the backend folder. My virtual environment of choice is "Pipenv", but feel free to use other as well.
        <br/>
        <code>
            pip install pipenv
        </code>
    </li>
    <li>
        Open the virtual environment.
        <br/>
        <code>
            pipenv shell
        </code>
    </li>
    <li>
        Install the required packages:
        <br/>
        <code>
            pipenv install -r requirements.py
        </code>
    </li>
    <li>
        Run the following commands:
        <br/>
        <code>
            1. python manage.py makemigrations
        </code>
        <br/>
        <code>
            2. python manage.py migrate
        </code>
        <br/>
        <code>
            3. python manage.py runserver
        </code>
    </li>
    <li>
        Open the following link:
        <br/>
        <code>
            <u>http://127.0.0.1:8000/</u>
        </code>
    </li>
</ol>

## **Files & Directories**
- `auctions` - all the files for the main app
  - `__pycache__` - error log files
  - `images` - the images for the project
  - `migrations` - the migrations used in the database
  - `static/auctions` - all the static files for the project
  - `templates/auctions` - all the template files for the project
  - `__init__.py` - the main file
  - `admin.py` - the file for the registrations in the admin panel
  - `apps.py` - the file for the app configuration
  - `models.py` - the file containing the models
  - `urls.py` - the routing file
  - `views.py` - the file containing the views
- `commerce` - all the files for the main project
  - `__pycache__` - error log files
  - `__init__.py` - the main file
  - `asgi.py` - the file for the deployment
  - `settings.py` - the settings file
  - `urls.py` - the routing file
  - `wsgi.py` - the file for the deployment
- `Pipfile` - the virtual environment
- `Pipfile.lock` - the lock for the virtual environment
- `db.sqlite3` - the database
- `manage.py` - the startpoint file
- `requirements.txt` - the file container for all the necessery packages

## **Technologies**
<ul>
    <li>
        Programming Languages - Python, Javascript, HTML5, CSS3
        <br/>
        <img alt="Python" src="https://img.shields.io/badge/python-%2314354C.svg?style=for-the-badge&logo=python&logoColor=white"/>
        <img alt="JavaScript" src="https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E"/>
        <img alt="HTML5" src="https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white"/>
        <img alt="CSS3" src="https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white"/>
    </li>
    <li>
        Framework - Django
        <br/>
        <img alt="Django" src="https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white"/>
    </li>
    <li>
        Database - SQLite 3
        <br/>
        <img alt="SQLite" src ="https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white"/>
    </li>
    <li>
        Deployment - Heroku
        <br/>
        <img alt="Heroku" src="https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white"/>
    </li>
    <li>
        Version Controll Systems - Git and Github
        <br/>
        <img alt="Git" src="https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white"/>
        <img alt="GitHub" src="https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white"/>
    </li>
    <li>
        IDE - Visual Studio Code
        <br/>
        <img alt="Visual Studio Code" src="https://img.shields.io/badge/VisualStudioCode-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white"/>
    </li>
</ul>
