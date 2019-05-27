from gcloud_utils.ml_engine import MlEngine
from gcloud_utils.storage import Storage
import sys
import os

BUCKET = "{{cookiecutter.gs_bucket}}"
PROJECT = "{{cookiecutter.gs_project}}"
REGION = "{{cookiecutter.gs_region}}"

alg = "{{cookiecutter.algorithm_name}}"

deploy_prefix = None if len(sys.argv)==1 else sys.argv[1]

with open("{{cookiecutter.algorithm_name}}/version".format(alg)) as v:
    version = v.read()

version_folder = version if deploy_prefix is None else "{}_{}".format(deploy_prefix, version)
package_path=os.path.join("artefacts","algorithms",version_folder)
artefact_name = "{{cookiecutter.algorithm_name}}-{}.tar.gz".format(version)

ml = MlEngine(PROJECT,BUCKET,REGION, package_path=package_path)

job = ml.start_training_job(
    "teste",
    artefact_name,
    "trainer.main",
     python_version="3.5",
     runtime_version="1.13"
    ).execute()

job_id = job['jobId']

state = ml.wait_job_to_finish(job_id, sleep_time=5)


if not state == "SUCCEEDED":
    raise Exception("Job {} finished with state {}".format(job_id, state))