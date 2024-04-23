start:
	python manage.py runserver
migrate:
	python3 manage.py makemigrations  &&  python3 manage.py migrate
create-super:
	python manage.py createse
bootstrap:
	python3 manage.py makemigrations  &&  python3 manage.py migrate && python3 manage.py createsuperuser