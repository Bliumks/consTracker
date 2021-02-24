
import json
import csv
import os



# with open(os.path.expanduser('backend\data.csv'), "r") as f:
#     reader = csv.reader(f)
#     next(reader)
#     data= {"people":[]}
#     for row in reader:
#         data["people"].append(
#             {"fname": "", "lname": row[4], "email": row[8],
#              "semail": "", "phone": row[5], "mphone": row[6], 
#              "address": row[0], "city": row[1],
#              "province": row[2],"postal": row[3],"supportlvl":"", "volunteer":"" })

# with open(os.path.expanduser('backend\peopl.json'), "w") as f:
#     json.dump(data, f, indent=4)

def convert(file):
    reader = csv.reader(file)
    next(reader)
    data= {"people":[]}
    for row in reader:
        data["people"].append(
            {"fname": "", "lname": row[4], "email": row[8],
             "semail": "", "phone": row[5], "mphone": row[6], 
             "address": row[0], "city": row[1],
             "province": row[2],"postal": row[3],"supportlvl":"", "volunteer":"" })

    with open(os.path.expanduser('backend\new.json'), "w") as f:
        json.dump(data, f, indent=4)
