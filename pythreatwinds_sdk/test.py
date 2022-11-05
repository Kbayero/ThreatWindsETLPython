from .functions import *

def sent_entities_test():
    """
    This function tests the operation of the function sent_entities
    """
    print("######################################################################")
    print("################ Test of the function sent_entities ############### ")
    print("######################################################################")

    print("\n")

    entity =[
  {
        "type": "malware",
        "value": "Dridex",
        "reputation": -3,
        "attributes": [],
        "associations": [
            {
                "name": "",
                "comment":"",
                "entity":{
                    "type": "ip",
                    "value": "51.178.161.32",
                    "reputation": -3,
                    "attributes":[],
                    "associations":[]
                }
            }
        ]
    }
]

    print("··············NEW ENTITY················")
    print(entity)

    response, code = sent_entities(entity)

    print("Showing response:",response)
    print("Showing return code:",code)

def sent_associations_test():
    """
    This function tests the operation of the function sent_associations
    """
    print("######################################################################")
    print("################ Test of the function sent_associations ############### ")
    print("######################################################################")

    print("\n")

    associations ={"associations": ["b97f454d-afad-421b-b157-38cda7d0b612", "3b387967-6242-4b8c-a25c-98c6270d1aa0"],"comment": "Any important comment about the association"}

    print("··············NEW ASSOCIATIONS················")
    print(associations)

    response, code = sent_associations(associations)

    print("Showing response:",response)
    print("Showing return code:",code)

def get_def_entities_test():
    """
    This function tests the operation of the function get_def_entities
    """
    print("######################################################################")
    print("################ Test of the function get_def_entities ############### ")
    print("######################################################################")

    print("\n")

    response, code = get_def_entities()

    print("Showing response:",response)
    print("Showing return code:",code)

def get_entities_search_test():
    """
    This function tests the operation of the function get_entities_search
    """
    print("######################################################################")
    print("################ Test of the function get_entities_search ############### ")
    print("######################################################################")

    print("\n")
    value = "malware"
    print("Value: ",value)
    print("limit: 50")
    print("offset: 0")

    response, code = get_entities_search(value= value)

    print("Showing response:",response)
    print("Showing return code:",code)

def get_entities_type_test():
    """
    This function tests the operation of the function get_entities_type
    """
    print("######################################################################")
    print("################ Test of the function get_entities_type ############### ")
    print("######################################################################")


    print("\n")
    value = "malware"
    print("Value: ",value)
    print("format: list")
    print("limit: 50")
    print("offset: 0")
    print("reputation: bad")
    print("accuracy: 0")
    print("lsa: now-24h")


    response, code = get_entities_type(value= value)

    print("Showing response:",response)
    print("Showing return code:",code) 

def get_entity_id_test():
    """
    This function tests the operation of the function get_entity_id
    """
    print("######################################################################")
    print("################ Test of the function get_entity_id ############### ")
    print("######################################################################")

    print("\n")
    value = "22721539-0471-440b-829e-069a9cdcc6ae"
    print("Value: ",value)
    print("limit: 50")
    print("offset: 0")

    response, code = get_entity_id(value= value)

    print("Showing response:",response)
    print("Showing return code:",code)

def get_entity_value_test():
    """
    This function tests the operation of the function get_entity_value
    """
    print("######################################################################")
    print("################ Test of the function get_entity_value ############### ")
    print("######################################################################")

    print("\n")
    value = "Dridex"
    print("Value: ",value)
    print("limit: 50")
    print("offset: 0")

    response, code = get_entity_value(value= value)

    print("Showing response:",response)
    print("Showing return code:",code)

def sent_geoip_location_test():
    """
    This function tests the operation of the function sent_geoip_location
    """
    print("######################################################################")
    print("################ Test of the function sent_geoip_location ############### ")
    print("######################################################################")

    print("\n")

    location ={
  "accuracyRadius": 100,
  "city": "Canberra",
  "country": "Australia",
  "countryCode": "AU",
  "latitude": 453.334,
  "longitude": -453.334,
  "segment": "1.1.1.0/24"
}

    print("··············NEW LOCATION················")
    print(location)

    response, code = sent_geoip_location(location)

    print("Showing response:",response)
    print("Showing return code:",code)

def get_geoip_location_test():
    """
    This function tests the operation of the function get_geoip_location
    """
    print("######################################################################")
    print("################ Test of the function get_geoip_location ############### ")
    print("######################################################################")

    print("\n")
    ip = "1.1.1.0"
    print("IP: ",ip)

    response, code = get_geoip_location(ip)

    print("Showing response:",response)
    print("Showing return code:",code)

def sent_geoip_organization_test():
    """
    This function tests the operation of the function sent_geoip_organization
    """
    print("######################################################################")
    print("################ Test of the function sent_geoip_organization ############### ")
    print("######################################################################")

    print("\n")

    organization ={
  "asn": 353453,
  "aso": "CloudFlare INC",
  "segment": "1.1.1.0/24"
}

    print("··············NEW ORGANIZATION················")
    print(organization)

    response, code = sent_geoip_organization(organization)

    print("Showing response:",response)
    print("Showing return code:",code)

def get_geoip_organization_test():
    """
    This function tests the operation of the function get_geoip_organization
    """
    print("######################################################################")
    print("################ Test of the function get_geoip_organization ############### ")
    print("######################################################################")

    print("\n")
    ip = "1.1.1.0"
    print("IP: ",ip)

    response, code = get_geoip_organization(ip)

    print("Showing response:",response)
    print("Showing return code:",code)