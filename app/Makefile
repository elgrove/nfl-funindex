format:
	-poetry run docformatter -r --in-place --black chalicelib app.py || [ $$? -eq 3 ] # accept error code 3 as success
	poetry run black chalicelib app.py
	poetry run isort chalicelib app.py

lint: format
	poetry run flake8 chalicelib app.py tests
	poetry run pylint chalicelib app.py

test:
	@bash -c 'poetry run pytest ; \
    EXIT_CODE=$$? ; \
    if [ -z "$$EXIT_CODE" ]; then exit 1 ; \
    elif [ $$EXIT_CODE -eq 5 ]; then exit 0 ; \
    else exit $$EXIT_CODE ; \
    fi'