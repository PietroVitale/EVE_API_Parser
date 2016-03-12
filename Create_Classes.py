import urllib.request
import re
from xml.dom import minidom
import os
from NewClass import NewClass

##########################
#Define user API
char_keyID = '5555555';
char_vCode = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX';

corp_keyID = '5555555'
corp_vCode = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

#Define output file name
file = 'API_Classes.py'
##########################

#Import API endpoints
ep_url = 'https://api.eveonline.com/api/CallList.xml.aspx'
ep_bytes = urllib.request.urlopen(ep_url).read()
ep_string = ep_bytes.decode('utf-8')

Nep = ep_string.count('\n')+1  				#number of endpoint lines
ep_lines = ep_string.split('\n', Nep)		#endpoint lines

#Overwrite file
if os.path.isfile(file):
	os.remove(file)


for ep in range(0, Nep-1):
	temp = ep_lines[ep]
	ep_indent_char = temp.find('<')
	ep_line = temp[temp.find('<'):len(ep_lines[ep])]
	
	ep_NS = ep_line.count(' ')
	ep_words = ep_line.split(' ',ep_NS)
	
	if ep_words[0] == '<row' and ep_words[1].find('accessMask') > -1:
		ep_type_str = ep_words[2]																	#char or corp
		ep_name_str = ep_words[3]																	#endpoint name
		#Parse endpoint name
		ep_name = re.sub('"','',ep_name_str[ep_name_str.find('name="')+6:len(ep_name_str)])
		
		#Parse endpoint type
		ep_type_str = re.sub('"','',ep_type_str[ep_type_str.find('type="')+6:len(ep_type_str)])
		if ep_type_str == 'Character':
			ep_type = 'char'
			keyID = char_keyID
			vCode = char_vCode
		elif ep_type_str == 'Corporation':
			ep_type = 'corp'
			keyID = corp_keyID
			vCode = corp_vCode
		else:
			print('Invalid endpoint type - ')
			print(ep_type_str)
		
		#Fix deprecated API endpoints
		if ep_name == 'Locations':
			ep_name = 'AssetList'
		if ep_name == 'AccountStatus':
			ep_type = 'account'
		if ep_name == 'CharacterInfo':
			ep_name = 'AccountBalance'
		
		
		#Import API
		parts = ['https://api.eveonline.com/',ep_type,'/',ep_name,'.xml.aspx?keyID=',keyID,'&vCode=',vCode]
		url_string = ''.join(parts)
		#print(ep)
		try:
			xml_bytes = urllib.request.urlopen(url_string).read()
		except:
			print('Error with API call: ')
			print(ep_name)
			continue
		body = xml_bytes.decode('utf-8')
		LN = body.count('\n')+1 #total lines

		lines = body.split('\n', LN)
		
		#Start writing endpoint class
		
		f = open(file,'a')
		f.write('class ')
		f.write(ep_type)
		f.write('_')
		f.write(ep_name)
		f.write(':\n')
		f.write('\tdef __init__(self):\n\n')
		f.close()
		
		IL = 0						#initialize indentation level
		pIL = 0						#initialize previous indentation level
		
		class_count = 0
		class_IL = []
		class_names = []
		
		for i in range(1, LN-1):
			temp = lines[i]
			indent_char = lines[i].find('<')						#character "<" indentation
			line = temp[lines[i].find('<'):len(lines[i])]
			
			NS = line.count(' ')
			words = line.split(' ',NS)
			
			if words[0] == '<rowset':
				IL = int(round(indent_char/4))
				
				for j in range(0, class_count):
					if class_IL[j] > IL:
						class_IL[j] = -1									#Remove from uniqueness consideration
				
				#Get rowset name, check for uniqueness at this indentation
				name_str = words[1]
				name = name_str[name_str.find('name="')+6:len(name_str)]
				name = re.sub('"','',name)
				
				if class_count > 0:
					class_flag = 0											#Initialize flag
					for j in range(0,class_count):
						if name == class_names[j] and IL == class_IL[j]:
							class_flag = 1									#Class already exists
					if class_flag == 0:									#New class
						#newClass(name,parameters)
						NewClass(file, name, IL, words[2],words[3])
						class_names.append(name)
						class_IL.append(IL)
						class_count = class_count+1
				else:
					#New class
					NewClass(file, name, IL, words[2],words[3])
					class_names.append(name)
					class_IL.append(IL)
					class_count = class_count+1
			
		if ep == 18:	
			pass
			#break	#test with only one class
		
