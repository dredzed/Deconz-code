import requests

r = requests.get("http://192.168.1.45:40850/api/1C17E08298/lights")
# r = requests.get("http://192.168.1.45:40850/api/1C17E08298/sensors/13")
print(r.json())

# deconzdict = r.json()
# print("\n\n" "This is the dictionary: ", deconzdict, "\n")
# print("Sensor: ", deconzdict["name"])
# print("Battery: ", deconzdict["config"]["battery"], "\n\n")
