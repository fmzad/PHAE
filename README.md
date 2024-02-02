# Private/Public Homepage And Encyclopedia
- A platform for creating private/public Forests. A Forest is a page structure resembling a forest of trees.
- Pages are shown in Homepage Mode or Encyclopedia Mode.
	- Encyclopedia Mode uses Github Markdown
	- Homepage Mode uses Github Markdown, HTML, CSS, and Javascript.
- Pages are tracked, having history. You cannot change the title of the page. You can, however, move content of a page to another page, essentially changing the title. You cannot delete a page once created.
- Page URL are /username/forestname/pageurl
	- pageurl is based on title(title if no slash, simple uuid if slash): heize -> album1 => title/heize/album1 | heize/ -> album1 => uuid/heize//album1 | heize -> /album1 => uuid/heize//album1
- Dependencies
	- Language: Python 3.7
	- Framework: Django 3.0

# Structure
- This repo is a directory/folder which in turn is a django project made with `django-admin startproject`.
- `app` is the main app.

# Setup
Easy. Make a python environment and install dependencies + run django commands.
1. Set up a python 3.7 virtual environment
2. python setup.py install
3. python manage.py makemigrations
4. python manage.py migrate
5. python manage.py runserver
Optional
1. python manage.py createsuperuser

# Contribution
Contact me at `kicomah@gmail.com`
