'''input for data information'''
'''info[] = [nunber of town, number od bases, covered distance]'''
info = []
info = input().split()
for i in range(3):
	info[i] = int(info[i])

'''input for location data for each town'''
numLoc = info[0]
loc = []
for i in range(numLoc):
	loc.append(input().split())
	for j in range(3):
		loc[i][j] = int(loc[i][j])
# print(loc)

dis = 0					# calculation for distance between each 2 towns
covered = 0				# total covered people in each assumed base location
coveredLoc = []			# covered location corresponding to each town
cal_coveredLoc = []		# list for covered location corresponding to each town	
unchecked = []			# list for unchecked lown
cal_people = []			# list for covered people corresponding to each town	

basePeople = 0			# covered people count for chosen base locations
baseLoc = []			# list for chosen base locations

'''arrange code for each town'''
for i in range(numLoc):
	unchecked.append(i)
# print(unchecked)

'''check the covered people in each town'''
for t in range(info[1]):
	
'''calculation for covered people in each assumed base location'''
	for i in range(numLoc):
		unchecked.remove(i)
		# print(unchecked)
	
		covered = loc[i][2]
		coveredLoc.append(i)
		# print(covered)
		for j in unchecked:
			dis = (loc[i][0] - loc[j][0]) ** 2 + (loc[i][1] - loc[j][1]) ** 2
			# print(i + 1 ,j + 1, dis)
			if dis <= info[2] ** 2:
				coveredLoc.append(j)
				covered += loc[j][2]
		cal_people.append(covered)
		unchecked.append(i)
		cal_coveredLoc.append(coveredLoc)
		# print(coveredLoc)
		coveredLoc = []
	
	# print(cal_people)
	# print(cal_coveredLoc)
	if max(cal_people) == 0:
		break
		
'''check the largest covered people count in each assumed base location'''		
	for i in range(numLoc):	
		if cal_people[i] == max(cal_people):			
			for j in cal_coveredLoc[i]:
				loc[j][2] = 0
			
			baseLoc.append(i + 1)
			basePeople += max(cal_people)
			cal_people = []
			break
			
	cal_coveredLoc = []
	# print(loc)
	# print(baseLoc, basePeople)

for i in range(len(baseLoc)):
	print(baseLoc[i], end = ' ')

print(basePeople)