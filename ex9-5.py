thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
  "year":1984
}
print(thisdict)
print(len(thisdist))

print(thisdict["brand"])
print(thisdict["model"])
print(thisdict["year"])

thisdict["brand"]="BMW"
print(thisdict)

print(thisdict.keys())

x=thisdict.keys()

print(x)  #before the change

thisdict["color1"]="green"
print(thisdict)

#thisdict.pop("model")
#print(thisdict)

thisdict.popitem()
print(thisdict)

thisdict.popitem()
print(thisdict)


