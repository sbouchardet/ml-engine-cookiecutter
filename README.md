# ml-engine-cookiecutter

This cookiecutter will help you to build a algorithm to run on [Google ML Engine](https://cloud.google.com/ml-engine). 

## Setup
Install cookiecutter

```bash
pip install cookiecutter
```

## How to use
To generate your ML Engine package

```bash
cookiecutter https://github.com/sbouchardet/ml-engine-cookiecutter.git
```

## Parameters
- `project_name`: name of project that will contain the algorithm
- `project_description`: brief description of the project
- `project_author_name`: author's name
- `project_author_email`: author's email
- `algorithm_name`: name of the algorithm that you will deploy to Google's ML Engine
- `ml_engine`: Choosen engine to implementes the algorithm. Today Google's ML Engine suport only [Ternsorflow](https://www.tensorflow.org/), [Keras](https://keras.io/), [PyTorch](https://pytorch.org/), [Scikit Learn](https://scikit-learn.org/stable/) and [XGboost](https://xgboost.readthedocs.io/en/latest/).
- `gs_region`: The region where the job will run on Google's ML Engine. The suported regions can be found on the [link](https://cloud.google.com/ml-engine/docs/tensorflow/regions) 
- `gs_bucket`: The bucket from Google Storage where the input and output data for the job is.
- `google_credential_filename`: name of the file of google application credential inside the project. 

