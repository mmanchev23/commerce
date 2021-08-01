[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/mmanchev23/commerce/blob/master/LICENSE)

# **Commerce** - Harvard's CS50 2020

## eBay-like e-commerce auction site. This is the third project for CS50's Web Programming with Python and JavaScript.

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

### **How to start the project locally?**
1. Install [Python](https://www.python.org/downloads/)
2. Open the folder with the project inside and install the required packages in the virtual environment:
   - `pip install -r requirements.txt`
3. Configure the database:
   1. `python manage.py makemigrations`
   2. `python manage.py migrate`
   3. `python manage.py runserver`

### **Files & Directories**
- `auctions` - app folder
  - `images` - images folder
  - `migrations` - migrations folder
  - `static/auctions` - files folder
  - `templates/auctions` - template folder
  - `__init__.py` - constructor/package file
  - `admin.py` - admin file
  - `apps.py` - app configuration file
  - `models.py` - models file
  - `urls.py` - routing file
  - `views.py` - views file
- `commerce` - project file
  - `__init__.py` - constructor/package file
  - `asgi.py` - deployment file
  - `settings.py` - settings file
  - `urls.py` - routing file
  - `wsgi.py` - deployment file
- `manage.py` - the startpoint file
- `requirements.txt` - required packages
