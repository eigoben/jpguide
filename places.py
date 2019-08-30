import unicodedata
import re

places_dict = {}
places_dict = {
	"yokohama": [9,12,4],
	"ueno": [7,9,4],
	"tokyo": [7,5,4],
	"shinjuku": [6,8,4],
	"shibuya": [9,8,4],
	"roppongi": [17,9,4], #this had the error, try repasting it and going again
	"odaiba": [7,8,4],
	"nikko": [4,4,4],
	"urayasu": [6,4,4],
	"kichijoji": [5,8,4],
	"kamakura": [6,6,4],
	"hakone": [13,6,4],
	"ginza": [6,5,4],
	# "fuji": [0,0,0], #update later
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
print(x,y,z, x+y+z)


abc = ["asf oi p:    sasfoa. sdfp adsf "]
# print(abc.find(":"))
# colon = abc.find(":")
# print(abc[:].replace(" ", "_"))
# print(abc[:colon+1] + r'"' + abc[colon+1:] + r'"')



abc = abc[0]
abc = abc.strip()
abc = unicodedata.normalize("NFKD", abc)
colon = abc.find(":")
defg = abc[:colon].replace(" ", r"_")
hij = abc[colon+1:].replace("","")
hij = hij.strip()
abc = defg + r': "' + hij + r'"'
print(abc)


regex_dict = {
	"areaname": r"(^Area.Name:.*$)",                    #15
	"areadesc": r"(^Area.Description:.*$)",             #15
	"areapic": r"(^Area.Picture.*:.*$)",                #15
	"names": r"^(?:[0-9]*..)(Name:.*$)",                    #275
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

replace_list = [
[r'(^Area.Name:.*$)', r'(^Area.Name:)', r'Area_Name:'],
[r'(^Area.Description:.*$)', r'(^Area.Description:)', r'Area_Description:'],
[r'(^Area.Picture.*:.*$)', r'(^Area.Picture)', r'Area_Picture:'],
[r'^(?:[0-9]*..)(Name:.*$)', r'^(?:[0-9]*..)(Name:)', r'Name:'],
[r'(^Brief.Description:.*$)', r'(^Brief.Description:)', r'Comments:'],
[r'(^Cost:.*$)', r'(^Cost:)', r'Price:'],
[r'(^Hours:.*$)', r'(^Hours:)', r'Hours:'],
[r'(^Picture.link:.*$)', r'(^Picture.link:)', r'Picture:'],
[r'(^Google.Maps.Link:.*$)', r'(^Google.Maps.Link:)', r'Map:'],
[r'(^Category:.*$)', r'(^Category:)', r'Category:'],
[r'(^Comments:.*$)', r'(^Comments:)', r'Comments:'],
[r'(^Address/Google Map Link:.*$)', r'(^Address/Google Map Link:)', r'Map:'],
[r'(^Price:.*$)', r'(^Price:.*$)', r'Price:'],
[r'(^Picture.if.available.*:.*$)', r'(^Picture.if.available.*:)', r'Picture:'],
[r'(^.*Amenities.*:.*$)', r'(^.*Amenities.*:)', r'Amenities:'],
[r'(^.*Trip.Advisor.Link:.*$)', r'(^.*Trip.Advisor.Link:)', r'Trip_Advisor:']
]

print("RRR", replace_list[0][1])
test_text = 'test1.txt'
with open(test_text, 'rt') as file: 
	for line in file:
		out = re.sub(replace_list[0][1], replace_list[0][2], line)
		# print(out)

test_string = r"Address/Google Map Link: https://fanultimate.com"
result = re.sub(regex_dict['price'],  r'Maps.*$',    test_string)
print("result: " , result)

for k,v in regex_dict.items():
	print (v)


print(replace_list[0][1])