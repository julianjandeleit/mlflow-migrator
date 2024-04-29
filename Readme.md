# Requirements

 - python 3.11 (probably 3.8 upwards)
 - pip:
  ```
  mlflow-export-import
  tabulate 
  ```

# Usage

`python migrate_mlflow.py`
 
 Enter experiment names, intermediate directory and  source and target mlflow tracking data.
 Then the script will first download and then upload the data from source to target server with the provided credentials.
 Attention: Creation dates will be changed and executing multiple times leads to repeated run entries.
