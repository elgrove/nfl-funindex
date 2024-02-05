venv:
	cd app; poetry install
	cd app; poetry run pip install --index-url https://pypi.org/simple/ --disable-pip-version-check --upgrade pip==21.0.1 setuptools==57.5.0;

rmvenv:
	rm -rf app/.venv
	rm -rf app/poetry.lock

# merge jsons
# 3 args, source A, source B, destination 
define merge
    content=$$( jq -s $(1) $(2) $(3) ) && printf "%s" "$$content" > $(4)
endef

package:
	cd app; poetry export --without-hashes --format requirements.txt --output requirements.txt
	cd app; poetry run chalice package --pkg-format terraform ../infra
	python utils/terraforming.py
	$(call merge,".[0] * .[1]"	,"./app/.chalice/additional_resources.tf.json","./infra/chalice.tf.json","./infra/chalice.tf.json")


plan:
	cd infra; terraform plan

apply:
	cd infra; terraform apply -auto-approve

destroy:
	cd infra; terraform apply -destroy -auto-approve

clean:
	rm -rf ./app/.chalice/deployments
	rm -rf ./app/requirements.txt
	rm -rf ./infra/chalice.tf.json
	rm -rf ./infra/deployment.zip
	rm -rf ./infra/layer-deployment.zip

deploy: package plan apply

build-clean: destroy clean package plan apply

purge: destroy clean