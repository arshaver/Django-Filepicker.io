#Django-Filepicker.io

A trivial image upload application demonstrating how to use [Django](https://www.djangoproject.com/ "Django") and [Filepicker.io](https://www.filepicker.io/ "Filepicker.io") together.

###NOTE - this project has been superseded by the official [django-filepicker](https://github.com/Filepicker/django-filepicker) app.

###Setup

---
Everything should work locally after a few steps:

1. Install the requirements (`pip install -r requirements.txt`)
2. Fill in your `FILEPICKER_API_KEY` and a `SECRET_KEY` in settings.py
3. Run `./manage.py syncdb` to create the database
4. Run `./manage.py runserver` to start the server
5. Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/ "http://127.0.0.1:8000/") to see it in action

###TODO

---
* Set up a demo on Heroku
* Restructure as a reusable app
