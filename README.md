django-versioning-service
=========================

[![wercker status](https://app.wercker.com/status/202bf54a2298603b81477fc5ddf49c2d/m "wercker status")](https://app.wercker.com/project/bykey/202bf54a2298603b81477fc5ddf49c2d)

A simple app written in python for getting a build nr. This website was made
for [wercker](https://wercker.com) a continuous deployment/delivery platform.
The purpose of this application is to show how you can easily extend the
platform.


Feel free to fork this site and/or deploy your own version of this app
([buildnr.herokuapp.com](http://buildnr.herokuapp.com) is deployed to a free
[heroku](http://heroku.com) instance .

_NOTE: this is not an official wercker product._

## How to use ##

You can easily register on the site: [buildnr.herokuapp.com](http://buildnr.herokuapp.com/) and create
an app.

With a single REST call you can get the build number for an app/branch/commit
hash combination. New branches by default start counting at 0.


## How to run your own? ##

### On Heroku ###

1. Fork this github repository.
2. Clone the repository.
3. Create a new app on heroku and add the following addons:
    * Heroku Postgres Dev :: Ivory (free)
    * Postmark 10,000 Messages (free)
4. You could now either add the application to wercker and add a heroku deploy
target or start pushing manually.
5. After deploying you need to run `heroku run ./manage.py syncdb` to create
the database structure and an admin login.
6. Login to the '/admin/' and update the site information to match the herokuapp
 domain.

Please update the DEFAULT_FROM_EMAIL email address in
`versioning_service/settings.py` file.

### Running it: Locally ###

1. Create a new virtual environment and activate it.
2. Run `pip install -r requirements.txt`
3. Initialize the database by running './manage.py syncdb'
4. Start the django devserver by running: `./manage.py runserver 0.0.0.0:8000`
5. Go to [http://localhost:8000/admin/](http://localhost:8000/admin/) and
update the site from `example.com` to `localhost:8000`

You may want to set some environment variables to enable emailing (used in the
registration/password reset flow). The environment variables are:

* `EMAIL_HOST` or `POSTMARK_SMTP_SERVER`
* `EMAIL_USER` or `POSTMARK_API_KEY`
* `EMAIL_PASSWORD` or `POSTMARK_API_KEY`
* `EMAIL_PORT`
* `EMAIL_TLS`

And finally: please update DEFAULT_FROM_EMAIL the email address in
`versioning_service/settings.py` file.

Happy coding!