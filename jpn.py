#coding: utf-8

#never save a text document from word or else it will have utf-8 bom encoding and no regex will match.. lesson learned.
import re

places_dict = {}
places_dict = {
	"yokohama": [9,12,4],
	"ueno": [7,9,4],
	"tokyo": [7,5,4],
	"shinjuku": [6,8,4],
	"shibuya": [9,9,4],
	"roppongi": [17,9,4], #this had the error, try repasting it and going again
	"odaiba": [7,8,4],
	"nikko": [4,4,4],
	"urayasu": [6,4,4],
	"kichijoji": [5,8,4],
	"kamakura": [6,6,4],
	"hakone": [13,6,4],
	"ginza": [6,5,4],
	"fuji": [0,0,0], #update later
	"enoshima": [6,4,4],
	"asakusa": [6,5,4]
}

x = 0
y = 0
z = 0
for key,val in places_dict.items():
	x += val[0]
	y += val[1]
	z += val[2]
# print(x,y,z, x+y+z)

regex_dict = {}
regex_dict = {
	"areaname": r"(^Area.Name:.*$)",                    #15
	"areadesc": r"(^Area.Description:.*$)",             #15
	"areapic": r"(^Area.Picture.*:.*$)",                #15
	"names": r"(^[0-9]*..Name:.*$)",                    #275
	"briefdesc": r"(^Brief.Description:.*$)",           #113
	"cost": r"(^Cost:.*$)",                             #113
	"hours": r"(^Hours:.*$)",                           #215
	"piclink": r"(^Picture.link:.*$)",                  #114
	"maps": r"(^Google.Maps.Link:.*$)",                 #113
	"cats": r"(^Category:.*$)",                         #101
	"comments": r"(^Comments:.*$)",                     #162
	"maps2": r"(^Address/Google Map Link:.*$)",         #101
	"price": r"(^Price:.*$)",                           #162
	"piclink2": r"(^Picture.if.available.*:.*$)",       #101
	"amenities": r"(^.*Amenities.*:.*$)",               #60
	"tripad": r"(^.*Trip.Advisor.Link:.*$)"             #60
}

output_dict = {}
# output_dict = {
# 	"areaname":[],
# 	"areadesc": [],
# 	"areapic": [],
# 	"names": [],
# 	"briefdesc": [],
# 	"cost": [],
# 	"hours": [],
# 	"piclink": [],
# 	"maps": [],
# 	"cats": [],
# 	"comments": [],
# 	"maps2": [],
# 	"price": [],
# 	"piclink2": [],
# 	"amenities": [],
# 	"tripad":[]
# }

filename = 'jpn2.txt'
temp_list = []



for k,v in regex_dict.items():
	# print(k,v)
	with open (filename, 'rt') as textfile:
		for line in textfile:
			# print(line)
			fa = re.findall(v, line)
			if fa: 
				temp_list.append(fa)
				# print(temp_list)
		output_dict.update( {k : temp_list} )
		temp_list = []

# for keys,values in output_dict.items():
#     print(keys)
#     print(len(values))

# print(output_dict['areaname'])
x = 0
y = 0
z = 0
a = 0
b = 0
c = 0
d = 0
e = 0
# print(places_dict['yokohama'][0])
# print(output_dict['names'][30])



#do this 15 times
for x in range(len(output_dict['areaname'])):
	print(output_dict['areaname'][x])
	print(output_dict['areadesc'][x])
	print(output_dict['areapic'][x])
	# print("test" , places_dict['yokohama'][0])
	print("Things to Do:")
	#do this 9 times
	for y in range(places_dict[list(places_dict.keys())[x]][0]):
		print(output_dict['names'][z])
		print(output_dict['briefdesc'][y])
		print(output_dict['cost'][c])
		print(output_dict['hours'][b])
		print(output_dict['piclink'][c])
		print(output_dict['maps'][c])
		z = z + 1
		b = b + 1
		c = c + 1
	print("Places to Eat:")
	for y in range(places_dict[list(places_dict.keys())[x]][1]):
		print(output_dict['names'][z])
		print(output_dict['cats'][d])
		print(output_dict['comments'][a])
		print(output_dict['hours'][b])
		print(output_dict['price'][a])
		print(output_dict['maps2'][d])
		print(output_dict['piclink2'][d])
		z = z + 1
		a = a + 1
		b = b + 1
		d = d + 1
	print("Places to Stay:")
	for y in range(places_dict[list(places_dict.keys())[x]][2]):
		print(output_dict['names'][z])
		print(output_dict['comments'][a])
		print(output_dict['price'][a])
		print(output_dict['amenities'][e])
		print(output_dict['tripad'][e])
		z = z + 1
		a = a + 1
		e = e + 1





# for i in output_dict: 
#     print(i) 




# patterns = [

# with open (filename, 'rt') as textfile:
# 	for line in textfile:
# 		# all_lines.append(line.strip())
# 		for k,v in regex_dict.items():
# 			fa = re.findall(v, line)
# 		if fa:
# 			output_dict.update( {k : v.append(fa)} )

	

# print(area, len(area))

# areaname   areadesc    areapic = 15 each
# to do      to eat      to stay = 275 total
# 113        102         60

