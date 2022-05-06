The compose file runs successfully, but communication between containers doesn't work yet.

Run Flask container:

``docker build --network host -t flask-app .``

``docker run -d -p 80:5000 flask-app``

Run Postgres container:

``docker run --name postgres -d -p 5432:5432 --network-alias postgres -e POSTGRES_PASSWORD=secret -e POSTGRES_DB=restsdb postgres:14``

(optional) Access psql CLI:

``docker exec -it postgres psql -U postgres``

Run test.py to load data into Postgres:

``.venv/bin/python test.py``