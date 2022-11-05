def run_request(request_object):
    """
    Function for execute the request to the endpoint
    """
    conn_attemps = 1 #Variable to control connection attemps

    while True:
        #Connection attemp, if this fail, retry again two more times
        try:
            response = request_object.operation()
            #If the code is 200 or 202, request made correctly
            if (response.status_code == 200) or (response.status_code == 202):
                print("------------Success------------")
                return (response.json(),response.status_code)
            else:
                print("------------Failed Request------------")
                return (None,response.status_code)

        except Exception as e:
           
            if conn_attemps == 3:
                print("------------Failed Connection-------------")
                return (e,0)
            else: 
                print("------------Failed Connection. Retry------------")
                conn_attemps = conn_attemps+1