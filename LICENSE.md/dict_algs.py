Ivan ={
    "name": "ivan",
    "age": 34,
    "children": [{
        "name": "vasja",
        "age": 12,
    },{
        "name": "petja",
        "age": 10,
    }],
}

Darja ={
    "name": "darja",
    "age": 41,
    "children": [{
        "name": "kirill",
        "age": 21,
    },{
        "name": "pavel",
        "age": 15,
    }],
}

emps = [Ivan, Darja]

for k in emps:
    for j in k["children"]:
        if (j["age"])>18:
            print(k["name"])
            pass
