
'''This function is called when an already existing file needs to be updated... '''


def update_file(name,mime,dir_path,fid) :
	from pydrive.auth import GoogleAuth
	from pydrive.drive import GoogleDrive
	
	gauth = GoogleAuth()
	drive = GoogleDrive(gauth)
	gauth.LocalWebserverAuth()
	#name = 'nsdf.txt'
	query = "title= " + "\'"+name+"\'"
	print query

	file_list = drive.ListFile({'q': query + "and trashed = False" }).GetList()
	if len(file_list) == 1:
		f = file_list[0]
	print len(file_list)
	f.Delete()
	f = drive.CreateFile({'title':str(name) ,'mimeType':str(mime),"parents": [{"kind": "drivefileLink","id":str(fid)}]})
	f.SetContentFile(dir_path+str(name))
	f.Upload()
