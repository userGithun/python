a = {
    "name": "pninfosys rohit",
    "college": "rjit",
    2 : [1,2,3,4,1,1,(2,4,5)], #list
    4 : ("ram","mohit"), #key : value
    "education": {'ram':'MCA'},
    "city": "gwalior",
    "city": "gwalior1234"
}
# print(a)
# print(a[2])
# print(a[0])
# print(a[2][6])
# print(type (a[4]))
# print(a["education"]['ram'])
# print(a[2][6][1])
# print(a["education"]["ram"][1])
# print(type (a["education"])) #key
# print(a[2][2])
# print(type(['college']))
# print(a['education']['ram'])

# change Dictionary Items

# print(type(a[4]))
# print(a)

# a[4]=(40,50,60,47,89)
# a["name"]="raj"
# a["team"]=["ram","raj"]
# print(type(a[4]))
# print(a)

sample_dict ={
'a':1,
'b':2
}
sample_dict.update({
    'b':5,
    'c':10
})

# print(sample_dict['apple'])
print(sample_dict.get('raj'))
# print("hello")
# print(sample_dict.get('b'),sample_dict.get('c'))