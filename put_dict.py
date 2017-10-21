''' updates the dictionary with the new files that have been backed up along with their modification time... '''

def put_ori_dict(ori_dict,dir_path):
	f = open((dir_path + 'myDict.py'),'w')
	f.write(str(ori_dict))
	f.close()
