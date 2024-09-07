import base64
import json

save_path = "C:/Program Files (x86)/Steam/steamapps/common/Ale and Tale Tavern/Ale and Tale Tavern_Data/saves/happy.sav"
backup_path = f"{save_path}_backup.sav"
with open(backup_path, 'w') as file:
    file.write(open(save_path, 'r').read())

## Decode
with open(save_path, 'r') as file:
    encoded_data = file.read()

decoded_data = base64.b64decode(encoded_data)
save_json = json.loads(decoded_data)
decoded_str = json.dumps(save_json, indent=4, ensure_ascii=False)

with open("happy.json", "w", encoding="utf-8") as f:
    f.write(decoded_str)

# Money
# save_json["money"] = 999999
# save_json["reputation"] = 99999
# save_json["cleanliness"] = 99999
# save_json["activeWebs"] = []
# save_json["junk"] = []

## Modify inventory
print("==========Inventory==========")
for i, player in enumerate(save_json["containers"]):
    print(f"=====Player {i+1}=====")
    for j, item in enumerate(player["items"]):    
        if item["dataId"] == 5: # bucket
            save_json["containers"][i]["items"][j]["charge"] = 99999

        if item["dataId"] == 303: # watering can
            save_json["containers"][i]["items"][j]["charge"] = 99999

        # durability
        if item["durability"] != 0:
            save_json["containers"][i]["items"][j]["durability"] = 99999

        print(item)

## Devices
print("==========Devices==========")
for i, device in enumerate(save_json["devices"]):
    if device["itemDataId"] == 1108: # auto dishwasher
        save_json["devices"][i]["supplySources"][0]["value"] = 99999 # water

    # reliability
    if device["reliability"] != 0:
        save_json["devices"][i]["reliability"] = 99999

    # print(save_json["devices"][i])

## Paddock
print("==========Paddock==========")
save_json["paddock"]["barleyFeeder"] = 99999
save_json["paddock"]["waterFeeder"] = 99999

## Save
if input("Save? (y/n): ") == "y":
    modified_json = json.dumps(save_json)
    encoded_data = base64.b64encode(modified_json.encode('utf-8')).decode('utf-8')

    with open(save_path, 'w') as file:
        file.write(encoded_data)

    print("Data saved successfully!")
