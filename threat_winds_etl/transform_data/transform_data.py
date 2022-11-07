from ..entities import entities

def convert_to_json_feodo(data):
    print("Creating entities...")
    list_objects = []
    
    for index in range(len(data)):
        object = entities.feodo()
        object["value"] = str(data.iloc[index]["malware"])
        object["associations"][0]["entity"]["value"] = str(data.iloc[index]["dst_ip"])
        list_objects.append(object)
    return list_objects