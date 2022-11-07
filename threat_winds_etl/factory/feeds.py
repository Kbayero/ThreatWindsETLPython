from abc import ABC, abstractmethod
import urllib.request, sys

from pythreatwinds_sdk import *
from ..src import extract_data
from ..transform_data import transform_data


class Object_feed(ABC):

    def download(self):
        try:
            print("Download file in the link:", self.url_feed)
            print("...")
            urllib.request.urlretrieve(self.url_feed,self.filename)
        except Exception as e:
            print(e)
            sys.exit()

    @abstractmethod
    def extract(self):
        pass

    @abstractmethod
    def transform(self):
        pass

    def load(self):
        return sent_entities(self.list_entities)    

class Feodo(Object_feed):

    def __init__(self, url_feed, filename, filename_cleaned):
        self.url_feed = url_feed
        self.filename = "./threat_winds_etl/data/" + filename
        self.filename_cleaned = "./threat_winds_etl/data/" + filename_cleaned
    
    def extract(self):
        self.data = extract_data.clean_feodo(self.filename, self.filename_cleaned)

    def transform(self):
        self.list_entities = transform_data.convert_to_json_feodo(self.data)