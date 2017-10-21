def filter_file(new_dict,mime_type,dir_path,fid) :
	from update import update_file
	from upload import upload_file
	from get_dict import get_ori_dict
	from put_dict import put_ori_dict
	import os
	old_dict = get_ori_dict(dir_path)   ''' Getting the files which already has been uploaded...'''
	for elem in new_dict :
		mime = (str(os.path.splitext(dir_path + str(elem))[1]))[1:]
		mime = mime_type[mime]
		if elem in old_dict :										"""Check if the file has been created after/before last backup Compare modification times if the was already there"""
			if new_dict[elem] == old_dict[elem] :
				continue
			else:
				old_dict[elem] = new_dict[elem]
				update_file(elem,mime,dir_path,fid)
		else :
			old_dict[elem] = os.path.getmtime(dir_path + str(elem))
			print mime
			upload_file(elem,mime,dir_path,fid)		

	put_ori_dict(old_dict,dir_path)    ''' Update the dictionary......'''
			
