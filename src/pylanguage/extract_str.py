def extract(file_path: str):
	f = open(file_path, 'r')
	d = f.read()
	f.close()
	f = open("../translations/base.json", 'w')
	dat = get_string(d)
	f.write(dat)
	f.close()

def get_string(data: str):
	regex_expression = ""
	d = re.compile.findall(regex_expression, data)
	return d
