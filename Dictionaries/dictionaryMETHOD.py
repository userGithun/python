a = {
    "name":"pninfosys",
    "college":"RJIT",
    # "college":"itm",  #duplicated Not Allowed
    "Mark" : [1,2,3,4], #list
    "education":{'ram':'MCA'},
    1:2,
}
# print(a["name12"])
# print(a.get("name12"))
# print(a.get['college123'])
# print(a['college'])
# print(a.keys())
# print(type(a.keys()))
# print(list(a.keys()))
# print(a.values())
# print(a.items())

# update Dictionary
# print(a)

updatedict ={ 
    "branch":"it",
    "phone": 9827414827,
    "salary": 4000,
    "name":"rohit" #update
}
a.update(updatedict)  #update the dictionary
print(a)





try:
    print(a["name123"])
except Exception as w:
    print(w)

print(a["college"])
