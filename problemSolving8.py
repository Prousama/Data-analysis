# Convert the following dictionary into JSON format
import json
studentData = {"name":"Osama","age":24,"marks":"99"}
print(type(studentData))
data = json.dumps(studentData)
print(type(data))
print(data)

# Access the value of "age" from the dictionary
studentData = '{"name":"Osama","age":24,"marks":"99"}'
data = json.loads(studentData)
print(data["age"])

# Pretty print the dictionary data
studentData = {"name":"Osama","age":24,"marks":"99"}
data = json.dumps(studentData,indent=4,separators=(",","="))
print(data)

# Sort the follwoing JSON keys and write them into a file
studentData = {"name":"Osama","age":24,"marks":"99"}
f = open("demo.json","w")
data = json.dumps(studentData,indent=4,sort_keys=True)
f.write(data)

# Access the nested key "marks" from the following nested data
studentData ="""{"student":
                    {"grade":
                        {"name":"owais","marks":87}
                    }
                }"""
data = json.loads(studentData)
print(data["student"]["grade"]["marks"])
