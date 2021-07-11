# PythonProjects

# FileDownload
Script to download file from GoogleDrive

Description:- The Script used the request library and retreive the REST API response to validate the input link. It also used the OS module to interact with the local file storage where the file is saved.

###Important
Prerequisites:
1. Login into the Google Drive account
2. Select the File -> Right Click on it -> Click on Shareable Link
3. Copy the Link
4. The program will prompt for a link while running. Enter the copied link in the requested URL
5. The second prompt in the program will ask for the Filename to be downloaded.Enter the file name along with format

### Usage:

####EXE file that was being built via ```pyinstaller```

- to run the program via command prompt.select the current directory and run the exe. The exe was generated with all dependencies.
- It will prompt for FileLink and File Name with format type and the file will be download in local CWD.

####UnitTest.py covers the unit test cases written to validate the script
 - The Unit test case will prompt for below input while running the unittest.py
 1. URL:- Link for the file
 2. path:- Local path where the file will be stored
 3. filename:- Filename with format
 
 
 
 ####Testing Scenarios which are covered
 
  1. To Validate the http response of input link is returning 200(ok)
  2. To Validate the Http response of input link is not returning 401(Unautorised)
  3. To Validate the Http response of input link is not returning 500(Internal Server Error)
  4. To Validate the File is successfully downloaded in local file path
  5. To Validate if the Input Link is correct
  
  
  ####Testing Scenarios which are not covered
 
 1. Negative Scenarios  are not covered in unittest 
 2. To validate the content of downloaded File. The content will be of binary type
 3. Downloading folder from google Drive
 4. Downloading Audio/Video format are not supported
 

If you're on Linux or MacOS, install the SoX ([Sound eXchange](http://sox.sourceforge.net/ "Sound eXchange")) before running the Python script. To install, run:

Ubuntu:
```
sudo apt install sox
```
MacOS:
```
brew install sox
```

Finally, run the script file as shown below:
```
python src\FileDownload.py
```

```

### Python 3.7.3 Installation in Windows
- Check if Python is already installed by opening command prompt and running ```python --version```.
- If the above command returns ```Python <some-version-number>``` you're probably good - provided version number is above 3.6
- If Python's not installed, command would say something like: ```'python' is not recognized as an internal or external command, operable program or batch file.```
- If so, download the installer from: https://www.python.org/ftp/python/3.7.3/python-3.7.3-amd64.exe
- Run that. In the first screen of installer, there will be an option at the bottom to "Add Python 3.7 to Path". Make sure to select it.
- Open command prompt and run ```python --version```. If everything went well it should say ```Python 3.7.3```
- You're all set! 

