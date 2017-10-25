# Google_Drive_Backup

Overview:
This progam automatically update a particular folder in drive so that you always have a cloud storage of your important files using pyDrive module

Steps to run the program

1. Enter the location of the folder which you want to be backed up in dir_path variable in drive.py file.
2. Run the test.py file 

Basic Explaination

1. From Google API's download and authenticate google drive API. Refer the link (https://developers.google.com/drive/v3/web/quickstart/python)

2.I then created a dictionary to store containing the name and modification time of the files in the folder to be backed up and an empty dictionary which gets updated as soon as a new file is uploaded.

3. The modification time of files from both the dictionaries is compared and if the modification time does not match or if there is a new key(a new file) then the update or upload function is called respectively.
