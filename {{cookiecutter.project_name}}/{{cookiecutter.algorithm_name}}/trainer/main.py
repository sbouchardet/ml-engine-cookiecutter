import argparse
from {{cookiecutter.algorithm_name}}_trainer import Trainer

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Run algorithm {{cookiecutter.algorithm_name}}')
    parser.add_argument('--job-dir', help="job directory")
    parser.add_argument('--input-data', help="Path of input dataset")

    parsed_args = parser.parse_args()
    Trainer().run(parsed_args.job_dir, parsed_args.input_data)