from threat_winds_etl.manager import manager as mng
from pythreatwinds_sdk import *

if __name__ == "__main__":
    
    data = mng.extract_data()
    list_entities = mng.transform_data(data)
    response, code = sent_entities(list_entities)
    
    print("Code: ",code)
    print("Text: ",response)