
CMD_MAKEMIGRATIONS := python manage.py makemigrations
CMD_MIGRATE := python manage.py migrate
CMD_START_API := python manage.py runserver

makemigrations:
	$(CMD_MAKEMIGRATIONS)

migrate:
	$(CMD_MIGRATE)

start-api:
	$(CMD_MAKEMIGRATIONS)
	$(CMD_MIGRATE)
	$(CMD_START_API)