.PHONY: setup test deploy-google
PWD=$(shell pwd)
G_CREDENTIALS=$(PWD)/{{cookiecutter.google_credential_filename}}.json
VERSION=$(shell cat $(PWD)/{{cookiecutter.algorithm_name}}/version)

check-preffix-var:
ifndef DEPLOY_PREFFIX
	$(error you must pass a DEPLOY_PREFFIX)
endif

setup:
	@pip install -r {{cookiecutter.algorithm_name}}/requirements.txt
	@pip install -r requirements-dev.txt

lint:
	@pylint {{cookiecutter.algorithm_name}}/

clean:
	@rm -rf {{cookiecutter.algorithm_name}}/dist
	@rm -rf {{cookiecutter.algorithm_name}}/{{cookiecutter.algorithm_name}}.egg-info

build: clean
	@cd {{cookiecutter.algorithm_name}} && python setup.py sdist

deploy:
	@echo "Version: $(VERSION)"
	@read -p "Enter New Version:" number; \
	echo "$$number" > $(PWD)/{{cookiecutter.algorithm_name}}/version; \
	git add $(PWD)/{{cookiecutter.algorithm_name}}/version; \
	git commit -m "Bump $$number"; \
	git tag $$number ; \
	git push origin $$number
	@$(MAKE) deploy-google

deploy-google:
	@$(MAKE) build
	@GOOGLE_APPLICATION_CREDENTIALS=$(G_CREDENTIALS) python scripts/deploy_google.py $(DEPLOY_PREFFIX)

run-google:
	@GOOGLE_APPLICATION_CREDENTIALS=$(G_CREDENTIALS) python scripts/submit_google.py $(DEPLOY_PREFFIX)

submit-google-local: check-preffix-var
	@echo "BUILDING..."
	@$(MAKE) build
	@echo "BUILD DONE!"
	@echo "UPLOADING..."
	@$(MAKE) deploy-google
	@echo "UPLOAD DONE!"
	@echo "RUNNING..."
	@$(MAKE) run-google
	@echo "DONE!"







