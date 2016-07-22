import json

class event:
    start = 0
    end = 0


def addinf( name ,start, end , map ):
   e = event()
   e.start =start
   e.end = end
   print(name)
   print(start)
   print(end)
   if name not in map:
        map[name]=[]
   map[name].append(e)

with open('/Users/Ching/Desktop/trans.json','r', encoding='latin1') as f:
    data = json.load(f)

map = {}

for index in data["resource"]["events"]:
    name = index.get('character','NA')
    if name=='NA':
        continue
    addinf(name,index["when"][0],index["when"][1],map)

for index in map:
    print(index)
    for event in map[index]:
    	print(event.start)
