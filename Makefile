install:
	poetry install
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	python3 -m pip install --user dist/*.whl
lint:
	poetry run flake8 gendiff
	poetry run flake8 tests
test:
	poetry run pytest -vv
test-cov:
	poetry run pytest --cov=gendiff
test-coverage:
	poetry run pytest --cov-report xml --cov=gendiff
