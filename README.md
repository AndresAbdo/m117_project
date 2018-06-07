# How to run StudyBuddy

To see a fully deployed version, visit http://andresabdo.pythonanywhere.com

To run the code from scratch on local host:
1. Install Django as described in https://docs.djangoproject.com/en/2.0/topics/install/
2. Install django-filter as described in
https://pypi.org/project/django-filter/
3. Download the repository at https://github.com/AndresAbdo/m117_project and extract the "StudyBuddyProj" directory to a location of your choice.
4. Using the command line, navigate to the directory in the StudyBuddyProj containing the "manage.py" file.
5. Enter "py -3 manage.py makemigrations" in Windows or "python manage.py makemigrations" in Linux.
6. Enter "py -3 manage.py migrate" in Windows or "python manage.py migrate" in Linux.
7. Enter "py -3 manage.py runserver" in Windows or "python mange.py runserver" to start running the webapplication!
8. The website shall now be accesible through http://127.0.0.1:8000/
