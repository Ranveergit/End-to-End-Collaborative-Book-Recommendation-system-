
import os

ROOT_DIR = os.getcwd()
# Main config file path
CONFIG_FOLDER_NAME = "config"
CONFIG_FILE_NAME = "config.yaml"
CONFIG_FILE_PATH = os.path.join(ROOT_DIR,CONFIG_FOLDER_NAME,CONFIG_FILE_NAME)



#The constants/ folder is typically used to store fixed values that are reused across your pipeline. These might include:

#File paths (e.g., where raw data or models are stored)

#Hyperparameters (e.g., learning rate, batch size)

#Column names

#API keys or configuration flags

# Directory names (like raw data, artifacts, models)



# -------------------------------------------------------------------------------------------------------------------------------------------------# The __init__.py file is a special Python file that indicates to Python that the directory should be treated as a package. This allows you to import modules from this directory in a structured way.

# _init__.py turns a folder into a Python package, allowing you to import files/modules from it like this:

# python
# Copy
# Edit
# from constants.config import DATA_PATH
# Without __init__.py, Python might not recognize the folder as a module, especially in older versions (<3.3), or in more structured setups like when deploying or packaging the pipeline.

# here we as directory of the config file is constant across the pipiline that's why we are keeping it in the constant folder
# The __init__.py file can be empty, or it can contain initialization code for the package. In this case, we are using it to define constants that will be used throughout the pipeline.