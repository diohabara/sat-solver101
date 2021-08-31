install:
	pyenv install && poetry install

run:
	poetry run python src/main.py

lint:
	poetry run pysen run lint

test:
	poetry run pytest
