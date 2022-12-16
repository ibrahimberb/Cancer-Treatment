import pandas as pd

from logger import get_handler
import logging

handler = get_handler()

logger = logging.getLogger(__name__)
logger.handlers[:] = []
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)
logger.propagate = False


class TrainDataHandler:
    def __init__(self, train_variants_path, train_text_path, handle_nan="eliminate") -> None:
        self.train_variants_path = train_variants_path
        self.train_text_path = train_text_path
        self.train_variants_data = self.load_train_variants(self.train_variants_path)
        self.train_text_data = self.load_train_text_data(self.train_text_path)
        self.train_data = self.load_train_data(self.train_variants_data, self.train_text_data)

        if handle_nan == "eliminate":
            # get rid of NaN entries in Text column
            self.train_data = self.train_data[self.train_data['Text'].notnull()].copy()
        
        else:
            raise NotImplementedError("Only 'eliminate' is implemented for handling NaN values.")

        logger.info(f"Train data is loaded. (Data size: {self.train_data.shape})")

    @staticmethod
    def load_train_variants(data_path):
        logger.debug("Loading the train variants data..")
        train_variants_data = pd.read_csv(data_path)
        return train_variants_data

    @staticmethod
    def load_train_text_data(data_path):
        logger.debug("Loading the train text data..")
        train_text_data = pd.read_csv(data_path, sep="\|\|", engine='python', header=None, skiprows=1, names=["ID","Text"])
        return train_text_data

    @staticmethod
    def load_train_data(train_variants_data, train_text_data):
        logger.debug("Preparing train data ..")
        train_data = pd.merge(train_variants_data, train_text_data, on='ID')
        return train_data


