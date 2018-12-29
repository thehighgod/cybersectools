import hashlib
import re

with open('filename') as fh:
               read_data =  fh.read()
found = False
loop_counter = 0

def md5(data):
	m = hashlib.md5()
	m.update(str(data))
	h = m.hexdigest()
	return h

while not found:
	hash = md5(read_data + "\n" + str(loop_counter))
	#I originally used this to get the hash to be 0e followed by 30 digits. This was to exploit a type juggling flaw in PHP
	if (re.match("HASH or partial hash using REGEX", str(hash))):
		found = True
		print(hash)
		with open('new filename', 'a') as fh:
                	fh.write(read_data + "\n" + str(loop_counter))
		print(read_data + "\n" + str(loop_counter))
	else:
		loop_counter += 1


