[running server](http://tastytut.nicerobot.c9.io/api/entry/?format=json)

# Steps:

	python --version
Python 2.7.2

	python -c "import django,tastypie; print(django.get_version());print(tastypie.__version__)"
1.5.1
(0, 9, 14)

	django-admin.py startproject tut
	cd tut
	python manage.py startapp myapp
	python manage.py runserver # works
	# configure myapp/models.py per tutorial
	# configure myapp/api.py per tutorial
	# configure tut/urls.py per tutorial
	python manage.py syncdb # produces tut.sqlite
	python manage.py runserver

# Result:

	"error_message": "maximum recursion depth exceeded"
