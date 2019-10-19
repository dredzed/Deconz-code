import requests

r = requests.get("http://192.168.1.45:40850/api/1C17E08298/sensors")
# print(r.json())

deconzdict = r.json()
# print("\n\n" "This is the dictionary: ", deconzdict, "\n")
for x in deconzdict:
    if "battery" in deconzdict[x]["config"]:
        #        print(deconzdict[x])
        print("Sensor: ", deconzdict[x]["name"])
        print("Battery: ", deconzdict[x]["config"]["battery"], "\n")
# print("Sensor: ", deconzdict["name"])
# print("Battery: ", deconzdict["config"]["battery"], "\n\n")
## create a dictionary with name : bettry level and save in a database?
## Then plot a graph qith data.
## Transfer code to nuc via ssh and run once a day
## convert into a function that return dictionary of name : battery
## poll is sensor is reachable or not
