f = open('File IO/pn.txt')

t = f.read()
if 'raj' in t:
    print("raj is present")
else:
    print("raj is not present")
f.close()        