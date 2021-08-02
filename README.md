[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/mmanchev23/commerce/blob/master/LICENSE)
[![Open in Visual Studio Code](https://open.vscode.dev/badges/open-in-vscode.svg)](https://open.vscode.dev/mmanchev23/commerce)

# **Commerce** - Harvard's CS50 2020

## eBay-like e-commerce auction site. This is the third project for CS50's Web Programming with Python and JavaScript.

### **Technologies**
<ul>
    <li>
        Programming Language - Python
        <br/>
        <img alt="Python" src="https://img.shields.io/badge/python-%2314354C.svg?style=for-the-badge&logo=python&logoColor=white"/>
    </li>
    <li>
        Markup Languages - HTML5, CSS3
        <br/>
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
- `commerce` - project file
- `.gitignore` - git ignore file
- `manage.py` - the startpoint file
- `Pipfile` - Python Virtual Environment
- `Pipfile.lock` - Python Virtual Environment Lock
- `requirements.txt` - required packages
