install:
	pyenv install && poetry install

run:
	poetry run python src/main.py

lint:
	poetry run pysen run lint

format:
	poetry run pysen run format

test:
	poetry run pytest
