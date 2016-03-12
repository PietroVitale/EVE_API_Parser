import re

def NewClass(file, name, IL, key_str, column_str):
	key = key_str[key_str.find('key="')+5:len(key_str)]
	key = re.sub('"','',key)
	
	column_str = column_str[column_str.find('columns="')+9:len(column_str)]
	column_str = re.sub('">\r','',column_str)
	NC = column_str.count(',')
	columns = column_str.split(',',NC)
	columns[NC] = re.sub('"','',columns[NC])
	
	f = open(file,'a')
	
	for l in range (0, IL):
		f.write('\t\t')
	f.write('self.')
	f.write(name)
	f.write(' = []\n')
	f.write('\n')
	
	for l in range (0, IL):
		f.write('\t\t')
	f.write('class ')
	f.write(name)
	f.write(':\n')
	
	for l in range (0, IL):
		f.write('\t\t')
	f.write('\tdef __init__(self, key, params):\n')
	for l in range (0, IL):
		f.write('\t\t')
	f.write('\t#params = [')
	
	for i in range (1, NC-1):
		f.write(columns[i])
		if i != NC-2:
			f.write(',')
	f.write(']\n')
	
	for l in range (0, IL):
		f.write('\t\t')
	
	f.write('\t\tself.key = key\n')
	
	
	for l in range (0, IL):
		f.write('\t\t')
		
	for i in range (1, NC+1):
		f.write('\t\tself.')
		f.write(columns[i])
		f.write(' = param[')
		f.write(str(i))
		f.write(']\n')
		for l in range (0, IL):
			f.write('\t\t')
	
	f.write('\n')
	
	f.close()
	return