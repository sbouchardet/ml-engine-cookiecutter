import os

gs_bucket="{{cookiecutter.gs_bucket}}"
gs_project = "{{cookiecutter.gs_project}}"
gs_region = "{{cookiecutter.gs_region}}"

with open("{{cookiecutter.algorithm_name}}/version") as v:
    version = v.read().strip()

artefact_name = "{{cookiecutter.algorithm_name}}-{}.tar.gz".format(version)
local_artefact = os.path.join("{{cookiecutter.algorithm_name}}", "dist", artefact_name)

def storage_artefact_path(deploy_prefix=None):
    version_folder = version if deploy_prefix is None else "{}_{}".format(deploy_prefix, version)
    return os.path.join(
        "artefacts",
        "algorithms",
        "{{cookiecutter.algorithm_name}}",
        version_folder)
