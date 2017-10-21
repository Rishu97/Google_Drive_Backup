def backup(dir_path,fid) :
    import os 
    from Filter import filter_file
    from folder import create_folder , delete_folder    
    lst = os.listdir(dir_path)
    dic = {}
    """ Apparently the os creates an executable file everytime a file is modified so we filter out those file. All the executable files have 		a '~' after the name""" 	
    for x in lst :
        name = str(x)
        if(name[len(name)-1] == '~') :
            continue
        dic[name] = os.path.getmtime(dir_path + str(name))
    print ("I'm in drive")

    dic1 = {}
    #print dic	
    mime_type = {"xls":'application/vnd.ms-excel',
        "xlsx":'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        "xml" :'text/xml',
        "ods":'application/vnd.oasis.opendocument.spreadsheet',
        "csv":'text/plain',
        "tmpl":'text/plain',
        "pdf": 'application/pdf',
        "php":'application/x-httpd-php',
        "jpg":'image/jpeg',
        "png":'image/png',
        "gif":'image/gif',
        "bmp":'image/bmp',
        "txt":'text/plain',
        "doc":'application/msword',
        "js":'text/js',
        "swf":'application/x-shockwave-flash',
        "mp3":'audio/mpeg',
        "zip":'application/zip',
        "rar":'application/rar',
        "tar":'application/tar',
        "arj":'application/arj',
        "cab":'application/cab',
        "html":'text/html',
        "htm":'text/html',
        "":'application/vnd.google-apps.folder'}
    for element in dic : 
    		   
        file_ext = str(os.path.splitext(dir_path + str(element))[1])
    
        if file_ext[1:] in mime_type :
            if(file_ext != '') :
                dic1[element] = dic[element]
    	    """ If the file ext is " " , it means it is a folder so we create a folder in drive and the recurvisely call the backup 			function in drive.py every time passing the id of the folder created"""	
            else :
                if('myDict.py' in os.listdir(dir_path + element + '/'))  :
                    delete_folder(element)
                fid1 = create_folder(element,mime_type[""],fid)
                f = open(dir_path + element +'/'+ 'myDict.py','w')
                f.write("{}")
                f.close()
                backup((dir_path + element + '/'),fid1)

    filter_file(dic1,mime_type,dir_path,fid)
				
        
    
