from config import Config
from ..src import feodo as feodo_ext
from ..transform_data import feodo as feodo_tr

url = Config.FEED_URL

def extract_data():
    file_path = "./threat_winds_etl/data/"
    if url == "https://feodotracker.abuse.ch/downloads/ipblocklist.csv":
        file_name = file_path + "ipblocklist.csv"
        file_name_cleaned = file_path + "ipblocklist_cleaned.csv"
        feodo_ext.download(url, file_name)
        data = feodo_ext.clean(file_name,file_name_cleaned)
        return data

def transform_data(data):
    if url == "https://feodotracker.abuse.ch/downloads/ipblocklist.csv":
        return feodo_tr.convert_to_json(data)
