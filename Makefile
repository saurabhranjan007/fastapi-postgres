run-db:
	docker run --name pgsql-utt -d -p 2022:5432 -e POSTGRES_PASSWORD=postgres postgres
	