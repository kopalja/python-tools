import os
import shutil
import typing


def get_files(dir_name: str, sort: bool = False) -> typing.List[str]:
    """
    Get names of files on directory.
    :param dir: Path to diretory to list files
    :param sort: Return files in sorted order.

    :return: List of names in directory
    """
    files = [f for f in os.listdir(dir_name) if os.path.isfile(os.path.join(dir_name, f))]
    return sorted(files) if sort else files


def mkdir(dir_name: str, force: False) -> str:
    """
    Create dir
    :param dir_name: Name of directory to create
    :param force: Remove existing direcotry
    :return: Path to created directory
    """
    if os.path.exists(dir_name) and force:
        shutil.rmtree(dir_name)
    os.makedirs(dir_name)
    return dir_name
