
''' creates a new folder in the existing backup folder in the google drive'''


def create_folder(name,mime,fid) :
	from pydrive.auth import GoogleAuth
	from pydrive.drive import GoogleDrive
	
	gauth = GoogleAuth()
	drive = GoogleDrive(gauth)
	gauth.LocalWebserverAuth()
	f = drive.CreateFile({'title':str(name) ,'mimeType':str(mime),"parents": [{"kind": "drive#fileLink","id":str(fid)}]})
	f.Upload()

	return f['id']
'''This is called when a specific file inside a folder has been updated in the system and needs to be updated in the google drive '''
def delete_folder(name) :
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
