from abc import ABC, abstractmethod

from .requ import *

class Creator(ABC):
    
    def build_request(self, resourc, request = None):
        # Call the factory method to create a Product object.
        req = self.factory_method(resourc, request)

        return req

    @abstractmethod
    def factory_method(self):
        pass

class PostCreatorConcret(Creator):

    def factory_method(self,resource, body)->Request:
        return PostRequest(resource, body)

class GetCreatorConcret(Creator):
    def factory_method(self, resource, params)->Request:
        return GetRequest(resource,params)