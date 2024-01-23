# Consumer
Consumer locator API. This is a REST API built with Django, Django rest framework. Uses PostgreSQL database with Postgis extension to handle geospatial data.


## Local Set Up
App has been set with docker, and this requires a local docker installation.

To start the app

```docker compose up```

Seeding Consumer data. On the shell run the command below.

```docker exec -it app python manage.py seed seed_data/consumers.csv```




## Todo.

These are some of the other features that would be added.

1. API Docs Improve usage.
2. Caching, to improve performance and API response times.
3. Logging and monitoring.

