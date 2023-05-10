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
run-help-gendiff:
	poetry run python -m gendiff.scripts.gendiff -h
run-gendiff:
	poetry run python -m gendiff.scripts.gendiff file_1 file_2

