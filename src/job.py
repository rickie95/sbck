from pathlib import Path
import shutil
import os


class Job:
    """  A Job performs a copy from a `source` folder to a `destination` folder.
        Two parameters are expected:
        - `source_path` is the base path of the files/directories to be copied
        - `destination_path` is the base path of where the content of `source_path` will be copied. Note: `destination_path` must exists.
    """

    def __init__(self, source_path, destination_path):
        self.__src = source_path
        self.__dest = destination_path
        self.__filelist = []

    def create_filelist(self):
        for (root, dirs, files) in os.walk(self.__src):
            relative_path = os.path.relpath(root, self.__src)
        
            for file in files:
                if relative_path == ".":
                    self.__filelist.append(file)
                else:
                    self.__filelist.append(os.path.join(relative_path, file))
        return self.__filelist

    def copy_files(self):
        assert len(self.__filelist) != 0
        assert self.__src != None
        assert self.__dest != None

        for file in self.__filelist:
            dest_path = Path.joinpath(self.__dest, file)
            Path(dest_path.parent).mkdir(parents=True, exist_ok=True)
            shutil.copy2(str(Path.joinpath(self.__src, file)), str(dest_path))
