from abc import ABC, abstractmethod
from .feeds import *

class Creator(ABC):
    
    def build_object_feed(self, url_feed, filename, filename_cleaned):
        req = self.factory_method(url_feed, filename, filename_cleaned)

        return req

    @abstractmethod
    def factory_method(self):
        pass

class FeodoCreatorConcret(Creator):

    def factory_method(self, url_feed, filename, filename_cleaned)->Object_feed:
        return Feodo(url_feed, filename, filename_cleaned)