.PHONY: setup test deploy-google
PWD=$(shell pwd)
G_CREDENTIALS=$(PWD)/{{cookiecutter.google_credential_filename}}

setup-dev: setup
	@pip install -r requirements-dev.txt

setup:
	@pip install -r {{cookiecutter.algorithm_name}}/requirements.txt

lint:
	@pylint {{cookiecutter.algorithm_name}}/

run-local:
	@cd {{cookiecutter.algorithm_name}} && python -m trainer.main

build:
	@cd {{cookiecutter.algorithm_name}} && python setup.py sdist

deploy-google: build
	@GOOGLE_APPLICATION_CREDENTIALS=$(G_CREDENTIALS) python scripts/deploy_google.py $(DEPLOY_PREFFIX)





