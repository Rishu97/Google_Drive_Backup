#from myDict import ori_dict

def get_ori_dict(dir_path):
	import ast
	try :
		ori_dict = ast.literal_eval(open(dir_path + 'myDict.py','r').read())
		return ori_dict
	except :
		f = open(dir_path + 'myDict.py','w')
		f.write("{}")
		f.close()	
		print open(dir_path + 'myDict.py','r').read()
		ori_dict = ast.literal_eval(open(dir_path + 'myDict.py','r').read())
		return ori_dict

''' The except block is used when we create a new folder to create a file named myDict.py which keeps the track of modification time of files in that folder....'''