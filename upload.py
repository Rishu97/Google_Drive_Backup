
'''this function is called when a new file needs to be uploaded '''

def upload_file(name , mime ,dir_path,fid) :
	from pydrive.auth import GoogleAuth
	from pydrive.drive import GoogleDrive
	
	gauth = GoogleAuth()
	drive = GoogleDrive(gauth)
	gauth.LocalWebserverAuth()
	
	print name, ':',mime

	f = drive.CreateFile({'title':str(name) ,'mimeType':str(mime),"parents": [{"kind": "drive#fileLink","id":str(fid)}]})
	f.SetContentFile(dir_path+str(name))

	f.Upload()



