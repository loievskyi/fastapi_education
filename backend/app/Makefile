PHONY: mm m

mm:  # make migrations
	alembic revision --autogenerate -m ${message}

m:  # migrate
	alembic upgrade head
