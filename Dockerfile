FROM python:2.7

ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt && \
	python manage.py syncdb --noinput && \
	echo "from django.contrib.auth.models import User; User.objects.create_superuser('root', 'test@localhost.com', 'root123')" | python manage.py shell
RUN chmod +x /app/run.sh
ENTRYPOINT ["/app/run.sh"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]