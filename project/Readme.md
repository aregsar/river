


//http://stackoverflow.com/questions/4239825/static-files-in-flask-robot-txt-sitemap-xml-mod-wsgi

//https://devcenter.heroku.com/articles/getting-started-with-python-o#local-workstation-setup
//web: gunicorn -b "0.0.0.0:$PORT" -w 4 manage:app --log-file=-


===========================================================

//heroku plugins:install git://github.com/heroku/heroku-pipeline.git


git clone https://github.com/heroku/riverbed.git
cd riverbed
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
pip freeze > requirements.txt
heroku login
heroku local
heroku create myapp
git push heroku master
heroku ps:scale web=1
heroku logs --tail
heroku ps
heroku open
heroku plugins:install heroku-pipelines
heroku fork --from riverbed --to riverbed-stage
heroku info -a riverbed-stage
git remote add riverbed-stage git@heroku.com:riverbed-stage.git
git push riverbed-stage master
git remote rename heroku riverbed-prod
#git remote rename riverbed-stage heroku
heroku ps:scale web=1 -a riverbed-stage
heroku pipelines:create -a riverbed
#heroku pipelines:add -a example-staging example
heroku pipeline:add riverbed
heroku pipeline
heroku pipeline:add riverbed-stage -s staging
heroku pipeline
heroku pipeline:diff
==========================================================

#promote staging to prod

heroku maintenance:on -a riverbed
heroku scale worker=0 -a riverbed
heroku run python manage.py db:migrate -a riverbed
heroku pipeline:promote -a riverbed-stage
#heroku restart -a riverbed
heroku scale worker=1 -a riverbed
heroku maintenance:off -a riverbed

===========================================================

//http://telliott.io/2015/09/07/a-first-look-at-pipelines-on-heroku.html
//https://devcenter.heroku.com/articles/pipelines



heroku releases --app riverbed
heroku releases --app riverbed-stage


heroku help pipelines

#one off dynos
heroku run python

#check the logs
heroku logs

//https://devcenter.heroku.com/articles/error-pages#customize-pages
heroku config:set \
  ERROR_PAGE_URL=//s3.amazonaws.com/<your_bucket>/your_error_page.html \
  MAINTENANCE_PAGE_URL=//s3.amazonaws.com/<your_bucket>/your_maintenance_page.html

===========================================================




River
A project template for rapid MVP development with the Python Flask Micro
Web Framework


The goal of the project is:

1- To provide a minimal project structure for rapid and productive development
so as not to get in the way of development yet be more than a single file app,
with the ability to easily expand out the a bigger project structure as the app grows.

2-Make it clear where all the code for the application resides.
An example is loction global error handling and databse connection setup and teardown.
another is app configuration where all the keys are contained in one file
for all environments and all the settings are contained in a .env file.

3-provide out of the box functionality applicable to 80 percent of web apps.



Whats in the box:

-minimal subfolder project structure
-sqlalchemy postgres database configuration
-starter flask app configuration
-single config file with environment variable
based configuration for all environemnts(never worry
about checking in production config)
-starter heroku procfile for deployment to heroku
-starter gulpfile for asset compilation including source maps
including template injection
-starter alembic migration for user account model
-token based user account with:
registration with optional email confirmation
signin
signout
forgot password reset
invalid signin configurable lockout period
user activity history
beta invites
-starter mailers for account activation and password reset
-background email delivery via RQ and heroku
-backgrount task running via RQ and heroku
-twitter bootstrap CDN setup
-jquery CDN setup
-google analytics script
-starter manage.py setup for running app server and migrations
-mailcatcher setup for test emails
-starter application logging setup(must configure log path)
-default global exception handling setup including json responses
-(statsd integration)



Starter templates, code and scripts:

-starter .gitignore
-starter heroku postgres,sendgrid,redis,RQ,Scheduer setup scripts
-starter database table access scripts via flask-sqlalchemy
-starter local postgres database creation scripts
-starter travis ci integration
-starter test case setup for user accounts with testcase and nose
-starter ajax json post handling with
jquery forms for registrationa,signin,forgot password and password
reset
-loadmore feed pagination with jquery loadmore button for
paging feeds and html partial rendered via json responses
-global antiforgery support
-starter template for sqlalchemy multiple database support
-SSL cert supports


The River Console task runner and generator.

[] == optional param
<> == required param

python and virtual environemnts setup(one time setup)
-river install python [version]

postgres setup(one time setup)
-river install postgres [version]


new river flask project setup:

-river new <myproject> [optional python version - default 2.7]
#creates project directory
#cds into it and creates a virtual env for the project
#runs river install to install dependancies

Optionally run:

-river db setup [optional postgres connection string]
#starts postgres server
#creates postgres database with name of project
#runs river db migrate to migrates to latest database migration
#setting up user accounts tables

Optionally run:

-river git setup [optional remote-repo-name]
#runs the following
git init
git add -A
git commit -m "initial commit"

Optionally run:

-river git remote [optional remote-repo-name]
git add remote <remote-repo-name>
git push -u master remote

now you are inside myproject and ready to make changes


-river run --nodebug
#runs the flask web server

-river install
#reinstalls dependancies in requirements.txt and freezes the result
back to requirements.txt

-river migration <migation file name>
#adds a new migration file

-river responder <responder name>
#adds a new responder file
#also adds bluprints to app\__init__.py and folder under templates


-river assets build
#runs gulp build tasks

-river assets watch
#watched for asset file changes and runs gulp build tasks


River db commands below use app.config['database_url']

-river db migrate [optional postgres connection string] --offline
#runs all remaining migrations

-river db upgrade [optional postgres connection string] --offline
#migrates to next revision

-river db downgrade [optional postgres connection string] --offline
#rolls back to previous migration

-river db goto <revision-hash> [optional postgres connection string] --offline
#runs migrations to get to specific version specified

-river db reset [optional postgres connection string] --offline
#downgrades to initial database state

-river db add accounts [optional postgres connection string]
#sets up dummy user accounts table

-river db truncate accounts [optional postgres connection string]
#truncates acounts table









