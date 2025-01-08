CREATE TABLE PUBLIC.movies (
	id serial PRIMARY KEY
	,title VARCHAR(100)
	,date_input TIMESTAMP DEFAULT now()
	,ean BIGINT NOT NULL UNIQUE
	);

# dbsuser IS your user FOR the postgressql-DB