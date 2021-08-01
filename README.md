[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/mmanchev23/commerce/blob/master/LICENSE)

# **Commerce** - Project #2 from Harvard's CS50w-2020

### **Technologies**
<ul>
    <li>
        Programming Languages - Python, HTML5, CSS3
        <br/>
        <img alt="Python" src="https://img.shields.io/badge/python-%2314354C.svg?style=for-the-badge&logo=python&logoColor=white"/>
        <img alt="HTML5" src="https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white"/>
        <img alt="CSS3" src="https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white"/>
    </li>
    <li>
        Frameworks - Django
        <br/>
        <img alt="Django" src="https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white"/>
    </li>
    <li>
        Database - SQLite 3
        <br/>
        <img alt="SQLite" src ="https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white"/>
    </li>
    <li>
        Version Controll Systems - Git and Github
        <br/>
        <img alt="Git" src="https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white"/>
        <img alt="GitHub" src="https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white"/>
    </li>
    <li>
        IDEs - Visual Studio Code
        <br/>
        <img alt="Visual Studio Code" src="https://img.shields.io/badge/VisualStudioCode-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white"/>
    </li>
</ul>

## **How to start the project locally?**
1. Install [Python](https://www.python.org/downloads/)
2. Open the folder with the project inside and install the required packages in the virtual environment:
   - `pip install -r requirements.txt`
3. Configure the database:
   1. `python manage.py makemigrations`
   2. `python manage.py migrate`
   3. `python manage.py runserver`

## **Files & Directories**
- `auctions` - all the files for the main app
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
  - `__init__.py` - the main file
  - `asgi.py` - the file for the deployment
  - `settings.py` - the settings file
  - `urls.py` - the routing file
  - `wsgi.py` - the file for the deployment
- `manage.py` - the startpoint file
- `requirements.txt` - the file container for all the necessery packages
