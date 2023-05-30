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
run-gendiff-flat:
	poetry run python -m gendiff.scripts.gendiff tests/fixtures/file1.json tests/fixtures/file2.json
run-gendiff-nested:
	poetry run python -m gendiff.scripts.gendiff tests/fixtures/file1_n.json tests/fixtures/file2_n.json
