import os

gs_bucket="{{cookiecutter.gs_bucket}}"
gs_project = "{{cookiecutter.gs_project}}"
gs_region = "{{cookiecutter.gs_region}}"

artefact_name = "{{cookiecutter.algorithm_name}}-{}.tar.gz".format(version)
local_artefact = os.path.join("{{cookiecutter.algorithm_name}}","dist",artefact_name)

with open("{{cookiecutter.algorithm_name}}/version") as v:
    version = v.read().strip()

def storage_artefact(deploy_preffix=None):
    version_folder = version if deploy_prefix is None else "{}_{}".format(deploy_prefix, version)
    return os.path.join(
        "artefacts",
        "algorithms",
        "{{cookiecutter.algorithm_name}}",
        version_folder,
        artefact_name)




