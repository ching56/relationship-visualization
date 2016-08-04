import json

class event:
		start = 0
		end = 0

class character:
	events =[]
	relation={}
	def __init__(self):
		events = []
		relation={}

def addinf( name ,start, end , map ):
	e = event()
	e.start =start
	e.end = end
	if name not in map:
				map[name]=character()
				map[name].events = []
	map[name].events.append(e)

def maxEvent( chara ):
	max = 0
	for event in chara.events:
			time = event.end - event.start
			if time > max :
				max = time
	return max

def getRelationValue(chara1, chara2):
	relation = 0
	overlapStart = 0
	overlapEnd = 0
	for event1 in chara1.events:
		for event2 in chara2.events:
			if event1.end <= event2.start:
				break
			if event1.start >= event2.end:
				continue
			if event1.start > event2.start:
				overlapStart = event1.start
			else:
				overlapStart = event2.start
			if event1.end < event2.end:
				overlapEnd = event1.end
			else:
				overlapEnd = event2.end
			relation = relation - overlapStart + overlapEnd
	if relation == 0:
		return relation
	elif relation < 1000:
		return 0.1
	elif relation >= 1000 and relation < 2000:
		return 1
	elif relation >= 2000 and relation <3000:
		return 5
	elif relation >= 3000 and relation <4000:
		return 10
	else:
		return 15




with open('/Users/Ching/Desktop/trans.json','r', encoding='latin1') as f:
		data = json.load(f)

map = {}

for index in data["resource"]["events"]:
		name = index.get('character','NA')
		if name=='NA':
				continue
		addinf(name,index["when"][0],index["when"][1],map)

#delete the role which only appear once or twice
for index in list(map):
	if maxEvent(map[index]) and len(map[index].events) < 3:
		del map[index]

# for index in map:
# 		print(index)
# 		print(len(map[index].events))
# 		print(maxEvent(map[index]))
# 		for event in map[index].events:
# 		    print(event.start)



nodes =[]
i = 1
for index in map:
	d ={"id":index,"group":i}
	i = i+1
	nodes.append(d)

links = []
for index1 in map:
	for index2 in map:
		if index1 == index2:
			continue
		r = getRelationValue(map[index1],map[index2])
		if r == 0:
			continue
		d = {"source": index1, "target": index2, "value":r}
		ifExist = 0
		for i in links:
			if i["target"] == index1 and i["source"] == index2:
				ifExist = 1
		if ifExist == 0:
			links.append(d)
		print(getRelationValue(map[index1],map[index2]))


trans = {}
trans["nodes"] = nodes
trans["links"] =links

with open('transData.json', 'w') as fp:
    json.dump(trans, fp)
