#River

A process for iterating on a

production grade

always deployable

minimum viable web app

from day one



#Why?

Launching an new app or pushing new code to production should not be a scary experience

Once in production you should be able to iterate on app features quickly and confidently

Once in production you should be able to measure, monitor and respond effectively

You should be able to pivot your app without having to worry about recreating your environment

one or two developers should be able to confidently manage a deployed web app
from low to high scale


#How?

Deploy to a REAL production environment from day one, before writing any code

Use a light weight framework that allows for rapid iteration
and deployment of small incremental application features

Put in place a managed production environment to handle REAL production app
requirements common to most web apps including:

-SSL security

-background email delivery

-logging

-failure monitoring

-alerting

-simple database backups and restores

-out of the box membership system with admin

-analytics

-terms of service and privacy boilerplate

-two factor authentication

-subdomain support

-email and contact forms

-social media sharing


Use a generic domain name applicable to any type of product.

#What is river?

An opinionated, task focused, web framework skeleton.

A philosophy of development

A production platform specification

A set of task oriented prescriptions

A set of templates, plugins and extensions

A set of command line utilities and generators


#Prescriptive yet flexible

River is an open source project - you can fork it

you can substitute your own parts

you can follow your own development methodology



#Components of river

Web framework skelleton based on Flask, SqlAlchemy and specific Flask extensions

Task runners for database migrations and database backups\restores

Heroku production environment configuration:

-1 web role to run the web app- ($7\mo)

-1 worker role for background emails($7\mo)

-SSL add on for SSL secure access ($20\mo)

-postgres add on for app database ($50\mo)

-redis for background email deliver (free tier)

-sendgrid for email sending service (free tier)

-new relic - for monitoring and alerting (free tier)

-loggly for logging (free tier)


AWS S3 service for storing database backups

Twillio for two factor auth

Travis ci for continious testing

Github for source control

DNSimple for domain name registration and SSL certifcates


Step by step instructions for:

-purchacing and configuring a generic domain and subdomains

-adding SSL certificate

-Setting up email accounts with google apps


Starter email templates for user registration

Starter templates for privacy and terms of service

Starter templates for site maintenance and error pages

Asset compilation scripts

Generator commands


#Philosophy

Deploy directly to production from day one

Prefer function over style

Eschew development best practices in favor of rapid iteration on
user facing features

Use a generic domain that can be re-purposed when you pivot

Pick a production platform that reduces maintanace tasks and manages background infrastructure
for you

Use best practices for deployment efficiency and reliability

-Environment variable based configuration

-Feature flags

-Enforce development and production application parity

-make database backups and restores routine processes

-Use a CDN for compiled assets

-Automate all things possible or make it a single command process


Embrace antipatterns in favor of agility:

-Just enough structure to know where to put things

-But not so much to have to jump around to different files constantly

-Fat controller, skinny model

-Single layer application - all logic in controller action

-Only test controller actions

-No caching

-Only use server side rendered Html

-Minimal Ajax and Pjax style interactivity

-No API

-No client side MVC

-Use basic bootstrap styling



Optimized for change:

-less jumping around between different files to understand code and dependancies

-All feature logic is in one place in controller actions, so less places to change code

-Changing code in one place in controller actions does not impact any other code

-less passing around variables - helps most with dynamically typed languages

-Downsides: some code duplication and copy\paste. This is somewhat mitigated by using
extensions, helpers and expressive and readable languages like Python.


#Developer empowerment

Have a system in place to allow you to work on a REAL side project with minimal
effort

Build a web app, one fully deployable feature at a time, at your own
pace, while building a REAL production app in the process

Optimized for change:

Make small changes easily while confidently pushing them to production

Enable the feedback loop:

Be confident in knowing the status and activities of your production web app
and be able to measure the impact of feature changes

Change your ideas and start over without having to start from scratch

Move fast, break things and fix them fast


#Step by step implementation(TBD):

Get generic domain from DNS simple

Setup heroku app

Setup heroku background worker

Add heroku database

Add heroku ssl

Install Ssl cert

Add heroku email provider

Add heroku logging

Add heroku app monitoring

Setup alerting and email notifications

Create github repo

Generate app - includes asset compilation scripts etc

Push app to github and heroku

Setup google analytics

Setup performance monitoring

Setup mail catcher for development

Setup database backup to s3

Run a test script to create and seed a single table in database

Test loading prod and dev database from s3 backup

Add privacy and terms pages

Add twitter and Facebook accounts for site

Setup ssl and www subdomain redirects







