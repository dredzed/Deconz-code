import requests
import traceback
def get_deconz_info(domain="sensors"):
    try:
        request_string = "http://192.168.1.45:40850/api/1C17E08298/" + domain
        r = requests.get(request_string)
        if r.status_code != 200:
            print("\nThere was a problem downloading from Deconz, error code: ", r.status_code)
    except:
        print("\nThere was a problem downloading from Deconz, error code: ")
    return r.json()

def deconz_groups():
    lights_dict = get_deconz_info("lights")
    print("All groups and their members:\n")
    for key in groups_dict:
        print(groups_dict[key]["name"], ":")
        light_numbers = groups_dict[key]["lights"]

        for light in light_numbers:
            light_name = lights_dict[light]["name"]
            print(light_name, end =", ")
            print("\n")

def deconz_sensors():
    print("\nWhat information do you need? \n 1: List of sensors \n 2: Battery state of sensors \n 3: Whether sensors are reachable \n 4: Information about one sensor \n")
    choice = input("Enter 1, 2, 3 or 4: ")
    if choice == "1":
        deconz_list()
    elif choice == "2":
        deconz_battery()
    elif choice == "3":
        deconz_reachable()
    elif choice == "4":
        deconz_single_info("sensors")

def deconz_lights():
    choice = input("What would you like to query: \n 1: List of lights \n 2: Whether lights are reachable \n 3: Information about 1 light \n")
    if choice == "1":
        deconz_list()
    elif choice == "2":
        deconz_reachable()
    elif choice == "3":
        deconz_single_info("lights")

def deconz_battery():
    if domain == "sensors":
        for x in deconz_dict:
            if "battery" in deconz_dict[x]["config"]:
                print("Sensor: ", deconz_dict[x]["name"])
                print("Battery: ", deconz_dict[x]["config"]["battery"], "\n")


def deconz_list():
    print("\n\n")
    for key in sorted(deconz_dict, key = int):
        print(key, deconz_dict[key]["name"], " ", deconz_dict[key]["type"])

    print("\nThere are ", len(deconz_dict), domain, "connected. \n")


def deconz_reachable():
    unavailable_device = 0
    if domain == "sensors":
        for x in deconz_dict:
            if "reachable" in deconz_dict[x]["config"]:
                if str(deconz_dict[x]["config"]["reachable"]) == "False":
                    unavailable_device += 1
                    print("\n", domain, deconz_dict[x]["name"], "is unavailable. ")

    elif domain == "lights":
        for x in deconz_dict:
            if "reachable" in deconz_dict[x]["state"]:
                if str(deconz_dict[x]["state"]["reachable"]) == "False":
                    unavailable_device += 1
                    print("\n", domain, deconz_dict[x]["name"], "is unavailable. \n")

    print("\n", unavailable_device, domain, "are unavailable \n")


def deconz_single_info(domain):
    deconz_list()
    while True:
        item = input("Which would you like information on? (Enter a number or 'q' to quit): ")
        if item == "q":
            break
        try:

            print("\n")
            print(domain[:-1], item, "......", deconz_dict[item]["name"], "..........\n")
            for x in deconz_dict[item]:
                print( x, ":", deconz_dict[item][x])
            print("\n\n")
        except KeyError:
            print(("'" + item + "'"), "is not a valid choice")    
            
while True:
    print("\n\nAvailable domains: \n 1: groups \n 2: lights \n 3: sensors")
    choice = input("Which Deconz domain? (Enter 1, 2, 3 or 'q' to quit):  ")

    if choice == "1":
        domain = "groups"
        groups_dict = get_deconz_info(domain)
        deconz_groups()


    elif choice == "2": 
        domain = "lights"
        deconz_dict = get_deconz_info(domain)
        deconz_lights()


    elif choice == "3":
        domain = "sensors"
        deconz_dict = get_deconz_info(domain)
        deconz_sensors()

    elif choice == "q": 
        exit()
