import urllib.request, sys, re, os
import pandas as pd

#Function that download the file:
def download(url,file_name):
    try:
        print("Download file in the link:", url)
        print("...")
        urllib.request.urlretrieve(url,file_name)
    except Exception as e:
        print(e)
        sys.exit()

#Function that delete file
def del_file(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)

#Function that clean the downloaded file
def clean (file_name, file_name_cleaned):
    try:
        print("Cleaning the downloaded file...")
        with open(file_name) as File:
            csv_cleaned= open(file_name_cleaned,"w")
            for line in File:
                if line[0]!="#":
                    sentence= re.sub('","',',',line,flags=re.IGNORECASE)
                    sentence = re.sub('"','',sentence,flags=re.IGNORECASE)
                    csv_cleaned.write(sentence)
            csv_cleaned.close()
    except Exception as e:
        print(e)
        sys.exit()
    #Create a dataframe with the data from the file
    data = pd.read_csv(file_name_cleaned)
    data=data.drop(["first_seen_utc","dst_port","last_online"],axis=1)#removing unnecessary columns
     
     #Deleting all IPs that are in offline status
    data = data.drop(data[data['c2_status']=="offline"].index)
    data=data.drop(["c2_status"],axis=1)#removing unnecessary columns
    del_file(file_name_cleaned)
    return data