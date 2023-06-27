import os
import shutil

SP_FORMAT_FOLDER = "sp_format/"
FIVEM_FORMAT_FOLDER = "fivem_format/"

for os_fivem_file in os.scandir(FIVEM_FORMAT_FOLDER):
    CURRENT_FILE_PATH = SP_FORMAT_FOLDER + os_fivem_file.name.replace('^', '/')
    ONLY_CURRENT_FILE_PATH_PARENT_FOLDERS = '/'.join(CURRENT_FILE_PATH.split('/')[:-1])

    if not os.path.exists(ONLY_CURRENT_FILE_PATH_PARENT_FOLDERS):
        os.makedirs(ONLY_CURRENT_FILE_PATH_PARENT_FOLDERS)

    shutil.copyfile(os_fivem_file.path, CURRENT_FILE_PATH)