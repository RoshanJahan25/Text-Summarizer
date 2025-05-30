import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml:Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml(str): Path like input
    
    Raises:
        ValueError: if yaml file is empty
        e: empty File
    Returns:
        Configuration: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content =yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    for Path in path_to_directories:
        os.makedirs(Path, exist_ok=True)
        if verbose:
            logger.info(f"Created Directory at: {Path}")

"""Create list of directories
        Args:
            path_to_directories(list): list of path directories
            ignore_log (bool, optional): ignore if multiple dirs is to be created, Defaults to false.
"""

@ensure_annotations
def get_size(path: Path) -> str:
    
    size_in_kb = round(Path(path).stat().st_size / 1024)
    return f"~ {size_in_kb} KB" 

""" get size in KB
Args:
    path (Path): path of the file

Returns:
    str: size in KB
"""

