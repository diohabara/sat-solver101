install:
	pyenv install && poetry install

run:
	poetry run python src/main.py --input=data/01.in

lint:
	poetry run pysen run lint

test:
	poetry run pytest
