def individual_serial(inpt) ->dict:
    return{
        "id" : str(inpt["_id"]),
        "nameoftrend1" : inpt["nameoftrend1"],
        "nameoftrend2" : inpt["nameoftrend2"],
        "nameoftrend3" : inpt["nameoftrend3"],
        "nameoftrend4" : inpt["nameoftrend4"],
        "nameoftrend5" : inpt["nameoftrend5"],
        "dateOfCreation" : inpt["dateofcreation"],
        "timeOfCreation" :inpt["timeofcreation"],
        "ip": inpt["ip"]
          }
