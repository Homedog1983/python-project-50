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
run-gendiff-h:
	poetry run python -m gendiff.scripts.gendiff -h
run-gendiff-1:
	poetry run python -m gendiff.scripts.gendiff tests/fixtures/file1.json tests/fixtures/file2.json
run-gendiff-2:
	poetry run python -m gendiff.scripts.gendiff tests/fixtures/file2.yaml tests/fixtures/file1.yml
run-gendiff-nested-stylish:
	poetry run python -m gendiff.scripts.gendiff tests/fixtures/file1_nested.json tests/fixtures/file2_nested.yaml
run-gendiff-plain:
	poetry run python -m gendiff.scripts.gendiff -f plain tests/fixtures/file1.json tests/fixtures/file2.yaml
run-gendiff-nested-plain:
	poetry run python -m gendiff.scripts.gendiff -f plain tests/fixtures/file1_nested.json tests/fixtures/file2_nested.yaml
run-gendiff-flat-json:
	poetry run python -m gendiff.scripts.gendiff -f json tests/fixtures/file1.json tests/fixtures/file2.yaml
run-gendiff-nested-json:
	poetry run python -m gendiff.scripts.gendiff -f json tests/fixtures/file1_nested.json tests/fixtures/file2_nested.yaml