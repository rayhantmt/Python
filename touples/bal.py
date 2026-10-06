# Name: Md Abu Rayhan Mia
# Roll: 15
# Problem: 15 (Mini Project)

import json
db_file = "project_db.json"
try:
    with open(db_file, "r") as f: data = json.load(f)
except FileNotFoundError:
    data = {}

def menu():
    while True:
        print("\n1.Add 2.View 3.Search 4.Update 5.Delete 6.Stats 7.Save 8.Exit")
        ch = input("Select: ")
        if ch == '1':
            sid = input("ID: ")
            m = [float(input(f"Sub {i} Marks: ")) for i in range(1, 6)]
            data[sid] = {"Name": input("Name: "), "Marks": m, "Avg": sum(m)/5}
            print("Added.")
        elif ch == '2':
            for k, v in data.items(): print(f"ID:{k} | {v['Name']} | Avg:{v['Avg']}")
        elif ch == '3':
            q = input("Search ID: ")
            print(data.get(q, "Not Found"))
        elif ch == '4':
            sid = input("Update ID: ")
            if sid in data: data[sid]["Name"] = input("New Name: ")
        elif ch == '5':
            data.pop(input("Delete ID: "), None)
            print("Deleted.")
        elif ch == '6':
            avgs = [x['Avg'] for x in data.values()]
            if avgs: print(f"Total Students: {len(data)}, Class Avg: {sum(avgs)/len(avgs):.2f}")
        elif ch == '7':
            with open(db_file, "w") as f: json.dump(data, f)
            print("Saved.")
        elif ch == '8': break
menu()