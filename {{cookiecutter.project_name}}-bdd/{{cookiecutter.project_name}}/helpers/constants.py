"""When you write your constants to help you."""

from os import getcwd
from os.path import join

exe_path = r'C:\\hello.exe'

PATH = getcwd()
LOG_FILE_DIR = join(PATH, "log")
LOGGER_CONFIG = join(PATH, "{{cookiecutter.project_name}}", "data", "logging.json")