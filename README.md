# Steps:

	python --version
Python 2.7.2

	python -c "import django,tastypie; print(django.get_version());print(tastypie.__version__)"
1.5.1
(0, 9, 14)

	django-admin.py startproject tut
	cd tut
	python manage.py startapp myapp
	python manage.py runserver 8990 # works
	# configure myapp/models.py per tutorial
	# configure myapp/api.py per tutorial
	# configure tut/urls.py per tutorial
