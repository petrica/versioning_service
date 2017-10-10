FROM python:2.7

ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt && \
	python manage.py syncdb --noinput && \
	echo "from django.contrib.auth.models import User; User.objects.create_superuser('myadmin', 'myemail@example.com', 'hunter2')" | python manage.py shell
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]