from config import Config

from threat_winds_etl.factory.builders import *
from pythreatwinds_sdk import *

if __name__ == "__main__":

    url = Config.FEED_URL

    if url == "https://feodotracker.abuse.ch/downloads/ipblocklist.csv":
        file_name = "ipblocklist.csv"
        file_name_cleaned = "ipblocklist_cleaned.csv"

        creator = FeodoCreatorConcret()
        new_object_feed = creator.build_object_feed(url, file_name, file_name_cleaned)

        new_object_feed.download()
        new_object_feed.extract()
        new_object_feed.transform()
        
        response, code = new_object_feed.load()

        print("Code: ",code)
        print("Text: ",response)