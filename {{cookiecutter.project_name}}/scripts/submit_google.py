from gcloud_utils.ml_engine import MlEngine
import sys
import config_google as c

deploy_prefix = None if len(sys.argv)==1 else sys.argv[1]

package_path = c.storage_artefact(deploy_prefix)

ml = MlEngine(
    c.gs_project,
    c.gs_bucket,
    c.gs_region,
    package_path=package_path)

job = ml.start_training_job(
    "teste",
    c.artefact_name,
    "trainer.main",
     python_version="3.5",
     runtime_version="1.13"
    ).execute()

job_id = job['jobId']

state = ml.wait_job_to_finish(job_id, sleep_time=5)


if not state == "SUCCEEDED":
    raise Exception("Job {} finished with state {}".format(job_id, state))