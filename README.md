# Restaurant Service
Contains code for the Restaurant Service hosted on GAE

This service uses the restaurant cloud sql database (see restaurant_db and restaurant_etl repositories for more detail)

This service provides a root endpoint that accepts **grade** and **cuisine** parameters in order to perform search.

	The grade search is hierarchical (i.e. the search will match the specified or above grade)
	The cuisine search is exact match

e.g. http://localhost:8000/?grade=B&cuisine=Thai

Please note that grade is upper case and cuisine has been conformed to be title case (as per the example above)

At present this is a non-paged API as result sets are anticipated to be small and no client-side requirements have been specified.

# Running Locally

Create a virtualenv and activate (python3)

Install requirements via pip

Setup environment properties as per the details provided in app.yaml. Note an easy option is to modify your local hosts file to 
resolve the Cloud SQL public ip address (34.76.18.46) as 'tree.sql'

Run 	gunicorn -b :8000 src.restaurant_service:app

# GAE deployment

	gcloud app deploy
	
This can take several minutes. An active version has been left running here: https://starry-core-243617.appspot.com

The default config currently uses a **'sql.tree'** private DNS entry, various GAE-->Cloud SQL connectivity methods exist but as noted above this is the simplest to use, particularly when switching from/to local execution.
