from dotenv import load_dotenv

from pythreatwinds_sdk.factory.builders import *
from pythreatwinds_sdk.connection.connection import *
from pythreatwinds_sdk.controller.controller import *

#Function for sent new entities to API of ThreatWinds
def sent_entities(new_entities):
    """
    This function makes a POST request to the endpoint
    https://api.sandbox.threatwinds.com/api/v1/entities for 
    submit new entities to the ThreatWinds API
    Note that it returns two values: on request
    successful, returns the successful response and response code(202).
    In case of a bad request, it returns the value None and the error code.
    In case there are problems with the connection, return the error body as
    the first value and 0 as the second value
    """

    #Load .env in environment variables
    load_dotenv()

    #Building new instance of request object
    resourc = "entities"
    creator = PostCreatorConcret()
    new_request = creator.build_request(resourc, new_entities)
    return (run_request(new_request))

#Function for sent new associations to API of ThreatWinds
def sent_associations(new_associations):
    """
    This function makes a POST request to the endpoint
    https://api.sandbox.threatwinds.com/api/v1/associations for 
    submit new associations to the ThreatWinds API
    Note that it returns two values: on request
    successful, returns the successful response and response code(202).
    In case of a bad request, it returns the value None and the error code.
    In case there are problems with the connection, return the error body as
    the first value and 0 as the second value
    """
    #Load .env in environment variables
    load_dotenv()

    resourc = "entities/associations"
    creator = PostCreatorConcret()
    new_request = creator.build_request(resourc,new_associations)
    return (run_request(new_request))

#Function for request entity definitions to the API of ThreatWinds
def get_def_entities():
    """
    This function makes a GET request to the endpoint
    https://api.sandbox.threatwinds.com/api/v1/entities/definitions for request the entity definitions.
    Note that it returns two values: on request
    successful, returns a list of entity definitions and response code(200).
    In case of a bad request, it returns the value None and the error code.
    In case there are problems with the connection, return the error body as 
    the first value and 0 as the second value
    """
    #Load .env in environment variables
    load_dotenv()
    
    resourc = "entities/definitions"
    creator = GetCreatorConcret()
    new_request = creator.build_request(resourc)
    return (run_request(new_request))

#Function for search entities with a phrase
def get_entities_search(value, limit = 50, offset = 0):
    """
    This function makes a GET request to the endpoint
    https://api.sandbox.threatwinds.com/api/v1/entities/search for search entities with a phrase
    Note that it returns two values: on request
    successful, returns a list of entities found and response code(200).
    In case of a bad request, it returns the value None and the error code.
    In case there are problems with the connection, return the error body as
    the first value and 0 as the second value
    """
    #Load .env in environment variables
    load_dotenv()
    
    params = {"value": value, "limit":limit, "offset": offset}
    resourc = "entities/search"

    creator = GetCreatorConcret()
    new_request = creator.build_request(resourc,params)
    return (run_request(new_request))

#Function for search entities with a type
def get_entities_type(value, limit = 50, offset = 0, reputation = "bad", accuracy = 0, lsa ="now-24h"):
    """
    This function makes a GET request to the endpoint
    https://api.sandbox.threatwinds.com/api/v1/entities/type for search entities with a type.
    Note that it returns two values: on request
    successful, it returns a list of entities found and a response code(200).
    In case of a bad request, it returns the value None and the error code.
    In case there are problems with the connection, return the error body as
    the first value and 0 as the second value
    """
    #Load .env in environment variables
    load_dotenv()
    
    params = {"value": value, "limit":limit, "offset": offset, "reputation": reputation, "accuracy": accuracy, "lsa": lsa}
    resourc = "entities/type"

    creator = GetCreatorConcret()
    new_request = creator.build_request(resourc, params)
    return (run_request(new_request))

#Function for search entities with a ID
def get_entity_id(value, limit = 50, offset = 0):
    """
    This function makes a GET request to the endpoint
    https://api.sandbox.threatwinds.com/api/v1/entity/id for search entities with a ID.
    Note that it returns two values: on request
    successful, it returns a list of entities found and a response code(200).
    In case of a bad request, it returns the value None and the error code.
    In case there are problems with the connection, return the error body as
    the first value and 0 as the second value
    """
    #Load .env in environment variables
    load_dotenv()
    
    params = {"value": value, "limit":limit, "offset": offset}
    resourc = "entity/id"

    creator = GetCreatorConcret()
    new_request = creator.build_request(resourc, params)
    return (run_request(new_request))

#Function for search entities with a value
def get_entity_value(value, limit = 50, offset = 0):
    """
    This function makes a GET request to the endpoint
    https://api.sandbox.threatwinds.com/api/v1/entity/value for search entities with a value.
    Note that it returns two values: on request
    successful, it returns a list of entities found and a response code(200).
    In case of a bad request, it returns the value None and the error code.
    In case there are problems with the connection, return the error body as
    the first value and 0 as the second value
    """
    #Load .env in environment variables
    load_dotenv()
    
    params = {"value": value, "limit":limit, "offset": offset}
    resourc = "entity/value"

    creator = GetCreatorConcret()
    new_request = creator.build_request(resourc, params)
    return (run_request(new_request))

#Function for add or update geolocation segments
def sent_geoip_location(new_location):
    """
    This function makes a POST request to the endpoint
    https://api.sandbox.threatwinds.com/api/v1/geoip/location to 
    add or update geolocation segments. Note that it returns two values: on request
    successful, returns the successful response and response code(202).
    In case of a bad request, it returns the value None and the error code.
    In case there are problems with the connection, return the error body as
    the first value and 0 as the second value
    """

    #Load .env in environment variables
    load_dotenv()

    #Building new instance of request object
    resourc = "geoip/location"
    creator = PostCreatorConcret()
    new_request = creator.build_request(resourc, new_location)
    return (run_request(new_request))

#Function for search a location with IP address
def get_geoip_location(ip):
    """
    This function makes a GET request to the endpoint
    https://api.sandbox.threatwinds.com/api/v1/geoip/location for search a location with IP address.
    Note that it returns two values: on request
    successful, it returns a ip found and a response code(200).
    In case of a bad request, it returns the value None and the error code.
    In case there are problems with the connection, return the error body as
    the first value and 0 as the second value
    """
    #Load .env in environment variables
    load_dotenv()
    
    resourc = "geoip/location/" + ip

    creator = GetCreatorConcret()
    new_request = creator.build_request(resourc)
    return (run_request(new_request))

#Function for add or update segments organization
def sent_geoip_organization(new_organization):
    """
    This function makes a POST request to the endpoint
    https://api.sandbox.threatwinds.com/api/v1/geoip/organization to 
    add or update segments organization. Note that it returns two values: on request
    successful, returns the successful response and response code(202).
    In case of a bad request, it returns the value None and the error code.
    In case there are problems with the connection, return the error body as
    the first value and 0 as the second value
    """

    #Load .env in environment variables
    load_dotenv()

    #Building new instance of request object
    resourc = "geoip/organization"
    creator = PostCreatorConcret()
    new_request = creator.build_request(resourc, new_organization)
    return (run_request(new_request))

#Function for search a organization with IP address
def get_geoip_organization(ip):
    """
    This function makes a GET request to the endpoint
    https://api.sandbox.threatwinds.com/api/v1/geoip/organization 
    for search a organization with IP address.
    Note that it returns two values: on request
    successful, it returns a ip found and a response code(200).
    In case of a bad request, it returns the value None and the error code.
    In case there are problems with the connection, return the error body as
    the first value and 0 as the second value
    """
    #Load .env in environment variables
    load_dotenv()
    
    resourc = "geoip/organization/" + ip

    creator = GetCreatorConcret()
    new_request = creator.build_request(resourc)
    return (run_request(new_request))