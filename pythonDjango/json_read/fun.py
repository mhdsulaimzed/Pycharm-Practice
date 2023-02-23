# # json
# javascript object notation
# is a format used to communicate and exchange data
# extentsion is .json
# install json.py module
from json import load
with open("db.json","r") as f:
    data=load(f)
# print(len(data))
# print([movie.get("title")for movie in data if "Fantasy" in movie.get("genres")])
#
# print(max(data,key=lambda m:int(m.get("runtime"))))
#
# print(sorted(data,key=lambda m:int(m.get("runtime"))))
mc={}
for movie in data:
    year=movie.get("year")
    if year in mc:
        mc[year]+=1
    else:
        mc[year]=1
print(mc)
