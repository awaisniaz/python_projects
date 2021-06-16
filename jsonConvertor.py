import json

# Serialization is encode the json data
student = {
    "name":"Peter",
    "Roll_no":"0399323923",
    "Grad":"A",
    "Age":20,
    "Subject":["Computer Science","Discrete Mathmatics","Data Structure"]

}
with open("data.json","w") as file:
    json.dump(student,file)

b = json.dumps(student)
print(b)
print(json.loads(b))