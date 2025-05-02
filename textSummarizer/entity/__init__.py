from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=False)
class DataIngestionConfig:
    def __init__(self, root_dir: Path, source_URL: str, local_data_file: Path, unzip_dir: Path):
        try:
            self.root_dir = root_dir
            self.source_URL = source_URL
            self.local_data_file = local_data_file
            self.unzip_dir = unzip_dir
        except Exception as e:
            raise ValueError(f"Error initializing DataIngestionConfig: {e}")
        

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    ALL_REQUIRED_FILES: list


