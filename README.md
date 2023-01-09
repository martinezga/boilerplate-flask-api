# boilerplate-flask-api

![](https://img.shields.io/badge/python-v3.9.7-blue)

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)

![](https://img.shields.io/badge/flake8-v6.0.0-purple)
![](https://img.shields.io/badge/black-v22.12.0-black)
![](https://img.shields.io/badge/isort-v5.11.4-blue)
![](https://img.shields.io/badge/pytest-v7.2.0-green)
![](https://img.shields.io/badge/pytest--cov-v4.0.0-red)


## Development environment:

- Install dependencies

      pipenv install --dev

- Check code before commit:

      pipenv run black .
      pipenv run flake8 .
      pipenv run isort .
      pipenv run pytest -vv
      pipenv run pytest --cov --cov-fail-under=75
      pipenv run pre-commit run --all-files


References:

https://google.github.io/styleguide/pyguide.html
