import os
import urllib.request as request
import zipfile
from cnnClassifier import logger
from cnnClassifier.utils.common import get_size
import gdown
from cnnClassifier.entity.config_entity import DataIngestionConfig
from pathlib import Path

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            gdown.download(self.config.source_URL, str(self.config.local_data_file), quiet=False)
            logger.info(f"{self.config.local_data_file} downloaded!")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")

    def extract_zip_file(self):
        # Check if the file is a valid zip file before extracting
        if zipfile.is_zipfile(self.config.local_data_file):
            unzip_path = self.config.unzip_dir
            os.makedirs(unzip_path, exist_ok=True)
            with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
                zip_ref.extractall(unzip_path)
            logger.info(f"Extracted data to {unzip_path}")
        else:
            logger.error(f"Downloaded file is not a valid zip file: {self.config.local_data_file}")
            raise Exception("File is not a valid zip file")