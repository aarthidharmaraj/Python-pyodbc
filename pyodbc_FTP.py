import pysftp
#with  dummy server that doesn't exist
hostname='localhost'
username='root'
password='Aspire@123'
# port='127.0.0.1:49675'
# cnopts = pysftp.CnOpts()##connecting options
with pysftp.Connection(host=hostname,username=username,password=password) as sftp:
    print("Connected to server !..")
##Switch to a remote directory
    sftp.cwd(".\pyodbc and pycobc\sftp")
    list_dir=sftp.listdir_attr()
    for directory in list_dir:
        print(directory.filename,directory)
    
    
## For Uploading a file

    # Defining a file that we want to upload from the local directorty  
    # or absolute path.
    local_File_Path = './ftp_pyodbc.txt'  
    # remote path where the file will be uploaded  
    remote_File_Path = '/pyodbc and pycobc/sftp/ftp_pyodbc.txt'  
    # put method to upload a file  
    sftp.put(local_File_Path, remote_File_Path)  
    
    # copy files from images, to remote static/images directory, preserving modification time
    sftp.put_d('images', 'static/images', preserve_mtime=True)
    
    # recursively copy files and directories from local static, to remote static,
    sftp.put_r('static', 'static', preserve_mtime=True)
    
##For downloading the file
    ##path of the file to be downloaded
    remote_File_Pathdown = '/pyodbc and pycobc/sftp/ftp_pyodbc.txt'  
    ## directory to save the file.  
    local_File_Pathdown = './ftp_pyodbcdown.txt'  
    # Using the get method to download a file  
    sftp.get(remote_File_Path, local_File_Path)  
    
    ##copy all files under public to a local path, preserving modification time
    ## get_d(remotedir, localdir, preserve_mtime=False/True)
    sftp.get_d('public', 'local', preserve_mtime=True)
    
     ##copy all files AND directories recursively under public to a local path
    sftp.get_r('public', 'local', preserve_mtime=True)
    
    
##for deleting the file.
    # Absolute path of the file 
    remote_File_Path = '/pyodbc and pycobc/sftp/ftp_pyodbc.txt'  
    sftp.remove(remote_File_Path)  

    ##mode is an integer representation of the octal mode to use.
    ##Converts to octal mode
    sftp.chmod('readme.txt', 644) ##mode
    
    ##converts an octal mode result back to an integer representation
    attr = sftp.stat('readme.txt')
    print(attr.st_mode)#==>33188
    pysftp.st_mode_to_int(attr.st_mode)#==>644

    
## Working with directory
    with sftp.cd('static'):     # now in ./static
        sftp.chdir('here')    ##chdir or cwd  # now in ./static/here
        sftp.chdir('there')     # now in ./static/here/there
        
        ## Returns the current working directory.
        print(sftp.pwd)
    
        ##create all directories in a path
        sftp.makedirs('dir/show/path') 
        
        sftp.mkdir('show', mode=644)  # user r/w, group and other read-only

        ##Checking for a directory
        sftp.isdir('dir') #returns true or false
        
        sftp.isfile('pub')##Checking for a file
        
        sftp.readlink('readme.sym')#return either an absolute or a relative path. 
        
        #Returns true if an remote entitiy exists whether it is a file or directory
        sftp.exists('readme.txt')   # a file
        sftp.exists('pub')          # a dir
        
        ##Truncate the file and returns its file size
        sftp.truncate('readme.txt', 4096)

        print(list(pysftp.path_advance))#generator to iterate over a file path

        print(list(pysftp.path_retreat)) #generator to iterate over a file path in reverse

         #copy a directory structure to a new path 
        pysftp.reparent('backup', '/home/test/dir')
        
        ##For downloading the matching file in a list of files
        import fnmatch
        for filename in sftp.listdir('/remote/path'):
            if fnmatch.fnmatch(filename, "*.txt"):
                sftp.get("/remote/path/" + filename, "/local/path/" + filename)
        
        ##Using re.search method
        filelist = sftp.listdir()
        import re
        for filename in filelist:
            filedate = re.search(".*\.txt$", filename)
            if filedate:
                print ("FOUND FILE " , filename)
        
        ## filtered Based on dates
        import sys
        import datetime


        dn = datetime.now().strftime("%Y%m%d%H");
        myFileList = sftp.listdir("files/")
        for filename in myFileList:
            if (filename.rfind("ArrivalList_" + dn) != -1):
                sftp.get("files/" + filename, "/tmp/" + filename)
# connection closed automatically at the end of the with statement  or use sftp.close()
