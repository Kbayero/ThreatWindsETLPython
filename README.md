# ThreatWindsPythonETL

_ThreatWindsPythonETL is an ETL process that allows extracting, transforming and loading different data of detected threats_

## Getting started
_You must create in the root of your project an .env file that will contain the API key, the API secret of the ThreatWinds API and the feed from which the data will be extracted. You must define them with the names TW_API_KEY ,TW_API_SECRET and FEED_URL. This project works together with **ThreatWindsPythonSDK**, to load the data after being transformed_

### Requirements

pandas
python-dotenv
requests
ThreatWindsPythonSDK

### Allowed feed list

The FEED_URL could be one of the following URLs:

https://feodotracker.abuse.ch/downloads/ipblocklist.csv