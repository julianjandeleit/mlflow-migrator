import subprocess
import getpass
import os

def export_experiments(source_tracking_uri, source_username, source_password, experiments, output_dir):
    command = [
        "export-experiments",
        "--experiments",
        experiments,
        "--output-dir",
        output_dir
    ]
    env = os.environ.copy()
    env["MLFLOW_TRACKING_URI"] = source_tracking_uri
    env["MLFLOW_TRACKING_USERNAME"] = source_username
    env["MLFLOW_TRACKING_PASSWORD"] = source_password

    subprocess.run(command, env=env, check=True)

def import_experiments(input_dir, dest_tracking_uri, dest_username, dest_password):
    command = [
        "import-experiments",
        "--input-dir",
        input_dir
    ]
    env = os.environ.copy()
    env["MLFLOW_TRACKING_URI"] = dest_tracking_uri
    env["MLFLOW_TRACKING_USERNAME"] = dest_username
    env["MLFLOW_TRACKING_PASSWORD"] = dest_password

    subprocess.run(command, env=env, check=True)

def main():

    experiments = input("Experiments to export (comma-separated or 'all'): ")
    output_dir = input("Output directory: ")

    print("Export MLflow experiments:")
    source_tracking_uri = input("Source Tracking URI: ")
    source_username = input("Source Username: ")
    source_password = getpass.getpass("Source Password: ")
    
    print("\nImport MLflow experiments:")
    input_dir = output_dir
    dest_tracking_uri = input("Destination Tracking URI: ")
    dest_username = input("Destination Username: ")
    dest_password = getpass.getpass("Destination Password: ")

    export_experiments(source_tracking_uri, source_username, source_password, experiments, output_dir)

    import_experiments(input_dir, dest_tracking_uri, dest_username, dest_password)

if __name__ == "__main__":
    main()
