import logging
import os
from pathlib import Path
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
list_of_files=[
    ".github/work_flow/.gitkeep" ,
    "src2/__init__.py", # pachage 
    "src2/components/__init__.py", #pachage
    "src2/components/data_engetion.py",
    "src2/components/data_transformation.py",
    "src2/components/model_training.py",
    "src2/components/model_evaluation.py",
    "src2/pipline/__init__.py", # pachage
    "src2/pipline/training.py",
    "src2/pipline/evaluation.py",
    "src2/utils/__init__.py", # pachage
    "src2/utils/utlis.py",
    "src2/logging/logging.py",
    "src2/exception/exception.py",
    "test/unit_test/__init__.py", # pachage
    "test/integration_test/__init__.py" # pachage
    , "init_situp.bat",
    "requariments.txt",
    "requirments_devolper.txt",
    "set_up.py",
    "set_up.cfg",
    "py_project.toml",
    "tox.ini",
    "experiments/experiments.ipynb"

]

for file in list_of_files:
    file_path=Path(file)
    file_dir,file_name=os.path.split(file_path)
    #print(file_dir)
    #print(file_name)

    #make_directories
    if file_dir!="":
        os.makedirs(file_dir,exist_ok=True)
        logging.info(f"creating directory: {file_dir} ,creating_files :{file_name}")
    
    #create files
    if (not os.path.exists(file_path) or  os.path.getsize(file_path)==0):
        with open(file_path,"w") as f :
            pass


