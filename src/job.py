from pathlib import Path
import shutil
import os


class Job:
    """  A Job performs a copy from a `source` folder to a `destination` folder.
        Two parameters are expected:
        - `source_path` is the base path of the files/directories to be copied
        - `destination_path` is the base path of where the content of `source_path` will be copied. Note: `destination_path` must exists.
    """

    __dest__ = ""
    __src__ = ""

    def __init__(self, source_path, destination_path):
        self.__src__ = source_path
        self.__dest__ = destination_path

    def create_filelist(self):
        filelist = []
        for (root, dirs, files) in os.walk(self.__src__):
            relative_path = os.path.relpath(root, self.__src__)
        
            for file in files:
                if relative_path == ".":
                    filelist.append(file)
                else:
                    filelist.append(os.path.join(relative_path, file))
        return filelist

    def copy_files(self, filelist):
        for file in filelist:
            dest_path = Path.joinpath(self.__dest__, file)
            Path(dest_path.parent).mkdir(parents=True, exist_ok=True)
            shutil.copy2(str(Path.joinpath(self.__src__, file)), str(dest_path))
