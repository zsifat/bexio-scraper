import json

filename='favn.json'
try:
	with open(filename) as f:
		fav_num=json.load(f)
except FileNotFoundError:
	fav_num = input("Input your favourite Number: ")
	fav_num = int(fav_num)
	with open(filename,'w') as f:
		json.dump(fav_num,f)

else:
	print(f'Your favourite number is: {fav_num}')

