import pprint

op = open('data.txt', encoding='utf-8', mode='r').readlines()

# print(op)

bank_name = []
codes = []
city = False
for i in op:
	if i != ' \n':
		if city == False:
			bank_name.append(i.strip())
			city=True
		else:
			codes.append(i.strip().replace('-', ''))
			city=False
	else:
		continue

output = {}
sjs = zip(bank_name, codes)
for i, j in sjs:
	output[j] = i


pprint.pprint(output)