# Consumer
Consumer locator REST API. 

The REST API built with Python, Django, Django rest framework. 

Uses PostgreSQL database with Postgis extension to handle geospatial data.


## Local Set Up
App has been set with docker, and this requires a local docker installation.

To start the app

```docker compose up```

Seeding Consumer data. On the shell run the command below.

```docker exec -it app python manage.py seed seed_data/consumers.csv```

## To test
Use a client such as Postman to access the API and requests.

Locally

```http://localhost:8000/api/consumers```

Accepts query params
1. status. [collected, in_progress, active]
2. previous_jobs_count. [any number]
3. max_previous_jobs_count. [any number]
4. min_previous_jobs_count. [any number]
5. page. [any number to traverse the available pages]


Deployed version

```https://consumer-him9.onrender.com/api/consumers```



## Todo.

These are some of the other features that would be added.

1. API Docs Improve usage.
2. Caching, to improve performance and API response times.
3. Logging and monitoring.

