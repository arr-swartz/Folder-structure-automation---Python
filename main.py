
# libraries used in this project

import os
import csv
import pandas as pd
import datetime
import shutil


# function for creating original structure( structure of folders practical1 ,practical2 ,practical3 ... ,each folder has different file
#                                          like .ipynb ,.py ,.txt etc.)

def create_original_structure():
    # taking input from user for number of folders
    n = int(input("\nenter number of folder : "))
    # path where user want to make folders
    path = input("\nenter path where you want to make folders : ")
    print('-'*121)
    # creating folders using os.mkdir( make directory which takes path as arguemnt) function
    for i in range(n):
        try:
            os.mkdir(path+"/practical"+str(i+1))
        except FileExistsError:
            print("\nfolder practical{} already exists\n".format(i+1))
    # making files in folders
    for i in range(n):
        print('-'*121)
        # taking input from user for number of files in particular folder
        m = int(input("\nenter how many files you want in practical"+str(i+1)+" : "))
        # making files
        for j in range(m):
            g = input("enter name of file "+str(j+1) +
                      " of folder practical"+str(i+1)+" : ")
            f = open(path+"/practical"+str(i+1)+"/"+g, 'w')
            # closing the file
            f.close()
    # version_control will append that 'folder are created at this path' in our version_control file
    version_control(-1, path)


# function for creating new structure ( files with same extension in specific folder, naming convention will be like practical1.extension )
#  ( if folder has multiple files with same extension ,naming convention will be like practical1a.extension , practical1b.extension etc)

def create_new_structure():
    print('-'*121)
    # taking path from where he/she has put folders
    path = input("enter path for your folders of practicals : ")
    valid = []  # list for containing valid extensions
    # making a panda dataframe for our csv file which will contain our original file and its path ,and new file and path of new file
    df = pd.DataFrame(
        columns=['original file', 'path of original file', 'new file', 'path to new file'])

    # checking for folder access and extracting folders with name like practical1 ,practical2,... etc
    try:
        subfolder = []  # this list will contain files and folders which has read access
        try:
            # os.walk will iterate over every subfolders and files in that subfolders
            for root, sub, file1 in os.walk(path.strip()):
                for i in sub:
                    # os.access will check if file/folder has read access or not, it will take path
                    if(os.access(path+'/'+i, os.R_OK)):
                        # as arguement and os.R_OK for read access,os.W_OK for write and os.X_OK for execute
                        subfolder.append(i)
                break
        except:
            print('inner searching ...........')
            print('error occured! Try again by changing location of folders')

        p = []  # this list will contain folders with name like practical1 ,practical2 ,....etc
        for filename in subfolder:
            # this will check that it is a file or a folder ,it will take path of folder as arguement
            if os.path.isdir(path+'/'+filename):
                # now we will check if folder name contains 'practical' or not
                if (filename[:-1] == 'practical' and filename[-1].isdigit()) or (filename[:-2] == 'practical' and filename[-2:].isdigit()):
                    p.append(filename)

        IO_flag = 0  # flag for checking IO Images folder has been created or not
        # iterating over every file in that folders and making speacific folders for them and renaming the file
        for filename in p:
            files = []  # this list will contain extension of file
            # os.listdir will iterate over every file in that folder ,it takes path as arguement
            for filename2 in os.listdir(path+'/'+filename):
                # extracting file extension from filename ,it takes filename as arguement
                file_name, file_extension = os.path.splitext(filename2)
                files.append(file_extension)
                if file_extension not in valid:  # checking for if extension is in valid ,if not we will make directory for that and append it in valid
                    valid.append(file_extension)
                    if file_extension == '.ipynb':  # for .ipynb files ,we will make 'Jupyter Notebooks' folder
                        os.mkdir(path+'/Jupyter Notebooks')
                    elif file_extension == '.txt':  # for .txt file ,we will make 'Text Files' folder
                        os.mkdir(path+'/Text Files')
                    # for images we will make IO Images folder first ,then we will make specific folder
                    elif file_extension == '.jpeg' or file_extension == '.jpg':
                        if IO_flag == 0:  # checking if IO Images folder has been created or not
                            os.mkdir(path+'/IO Images')
                            IO_flag = 1
                        # for .jpeg ,we will make IO Images/JPEG folder
                        os.mkdir(path+'/IO Images/JPEG')
                    elif file_extension == '.png':
                        if IO_flag == 0:
                            os.mkdir(path+'/IO Images')
                            IO_flag = 1
                        # for .png ,we will make IO Images/PNG folder
                        os.mkdir(path+'/IO Images/PNG')
                    elif file_extension == '.gif':
                        if IO_flag == 0:
                            os.mkdir(path+'/IO Images')
                            IO_flag = 1
                        # for .gif ,we will make IO Images/GIF folder
                        os.mkdir(path+'/IO Images/GIF')
                    elif file_extension == '.html':
                        # for html files ,we will make 'html files' folder
                        os.mkdir(path+'/html files')
                    elif file_extension == '.css':
                        # for css files ,we will make 'css styling files' folder
                        os.mkdir(path+'/css styling files')
                    elif file_extension == '.js':
                        # for javascript files ,we will make 'javascript files' folder
                        os.mkdir(path+'/javascript files')
                    elif file_extension == '.py':
                        # for .py files ,we will make 'Python files' folder
                        os.mkdir(path+'/Python files')
                    else:
                        # for any other file type ,we will make folders according to file extension
                        os.mkdir(path+'/'+file_extension)

            # dictionary that will contan number of files with same extension like 4 .py files, 3 .ipynb files etc.
            dict1 = {}
            for name in set(files):
                dict1[name] = 0  # setting initial value to 0
            # iterating over every file in folders
            for filename1 in os.listdir(path+'/'+filename):
                file_name, file_extension = os.path.splitext(
                    filename1)  # taking file extension
                if file_extension in valid:  # checking if file_extension is valid or not, if not we will do nothing
                    old_path = path+'/'+filename+'/' + \
                        filename1  # old (current) path of file
                    if file_extension == '.ipynb':  # if file extension is .ipynb
                        if(files.count('.ipynb') == 1):  # if folder contain only one .ipynb file
                            # shutil.move will move the file from source to destination
                            shutil.move(path+'/'+filename+'/'+filename1,
                                        path+'/Jupyter Notebooks/'+filename+'.ipynb')
                            new_path = path+'/Jupyter Notebooks/'+filename+'.ipynb'  # new path of file
                            new_name = filename+'.ipynb'  # new_name of file
                        else:  # if folder contain multiple .ipynb file
                            shutil.move(path+'/'+filename+'/'+filename1, path+'/Jupyter Notebooks/' +
                                        filename+str(chr(ord('a')+dict1[file_extension]))+'.ipynb')
                            new_path = path+'/Jupyter Notebooks/'+filename + \
                                str(chr(
                                    ord('a')+dict1[file_extension]))+'.ipynb'  # path of new file
                            # new name of file (if dict1['.ipynb'] = 1 that means there is already one file so append b behind the name of file)
                            new_name = filename + \
                                str(chr(
                                    ord('a')+dict1[file_extension]))+'.ipynb'
                            # increamenting count in dictionary
                            dict1[file_extension] += 1
                    elif file_extension == '.txt':  # if file extension is .txt
                        if(files.count('.txt') == 1):  # if folder contain only one .txt file
                            shutil.move(path+'/'+filename+'/'+filename1,
                                        path+'/Text Files/'+filename+'.txt')
                            new_path = path+'/Text Files/'+filename+'.txt'
                            new_name = filename+'.txt'
                        else:  # if folder contain multiple .txt file
                            shutil.move(path+'/'+filename+'/'+filename1, path+'/Text Files/' +
                                        filename+str(chr(ord('a')+dict1[file_extension]))+'.txt')
                            new_path = path+'/Text Files/'+filename + \
                                str(chr(ord('a')+dict1[file_extension]))+'.txt'
                            new_name = filename + \
                                str(chr(ord('a')+dict1[file_extension]))+'.txt'
                            dict1[file_extension] += 1
                    # if file extension iss .png, .jpeg, .jpg, .gif
                    elif file_extension == '.jpeg' or file_extension == '.jpg' or file_extension == '.png' or file_extension == '.gif':
                        if file_extension == '.jpeg' or file_extension == '.jpg':  # if file extension is .jpeg or ,jpg
                            # if folder contain only one file
                            if(files.count('.jpeg')+files.count('.jpg') == 1):
                                shutil.move(
                                    path+'/'+filename+'/'+filename1, path+'/IO Images/JPEG/'+filename+file_extension)
                                new_path = path+'/IO Images/JPEG/'+filename+file_extension
                                new_name = filename+file_extension
                            else:  # if folder contain multiple files of .jpeg or .jpg extension
                                shutil.move(path+'/'+filename+'/'+filename1, path+'/IO Images/JPEG/'+filename+str(
                                    chr(ord('a')+dict1[file_extension]))+file_extension)
                                new_path = path+'/IO Images/JPEG/'+filename + \
                                    str(chr(
                                        ord('a')+dict1[file_extension]))+file_extension
                                new_name = filename + \
                                    str(chr(
                                        ord('a')+dict1[file_extension]))+file_extension
                                dict1[file_extension] += 1
                        elif file_extension == '.png':  # if extension is .png
                            if(files.count('.png') == 1):  # for only one file
                                shutil.move(path+'/'+filename+'/'+filename1,
                                            path+'/IO Images/PNG/'+filename+'.png')
                                new_path = path+'/IO Images/PNG/'+filename+'.png'
                                new_name = filename+'.png'
                            else:  # for multiple file
                                shutil.move(path+'/'+filename+'/'+filename1, path+'/IO Images/PNG/'+filename+str(
                                    chr(ord('a')+dict1[file_extension]))+'.png')
                                new_path = path+'/IO Images/PNG/'+filename + \
                                    str(chr(
                                        ord('a')+dict1[file_extension]))+'.png'
                                new_name = filename + \
                                    str(chr(
                                        ord('a')+dict1[file_extension]))+'.png'
                                dict1[file_extension] += 1
                        else:  # if extension is .gif
                            if(files.count('.gif') == 1):  # for only one file
                                shutil.move(path+'/'+filename+'/'+filename1,
                                            path+'/IO Images/GIF/'+filename+'.gif')
                                new_path = path+'/IO Images/GIF/'+filename+'.gif'
                                new_name = filename+'.gif'
                            else:  # for multiple files
                                shutil.move(path+'/'+filename+'/'+filename1, path+'/IO Images/GIF/'+filename+str(
                                    chr(ord('a')+dict1[file_extension]))+'.gif')
                                new_path = path+'/IO Images/GIF/'+filename + \
                                    str(chr(
                                        ord('a')+dict1[file_extension]))+'.gif'
                                new_name = filename + \
                                    str(chr(
                                        ord('a')+dict1[file_extension]))+'.gif'
                                dict1[file_extension] += 1
                    elif file_extension == '.html':  # if extension is .html
                        if(files.count('.html') == 1):  # for only one file
                            shutil.move(path+'/'+filename+'/'+filename1,
                                        path+'/html files/'+filename+'.html')
                            new_path = path+'/html files/'+filename+'.html'
                            new_name = filename+'.html'
                        else:  # for multiple files
                            shutil.move(path+'/'+filename+'/'+filename1, path+'/html files/' +
                                        filename+str(chr(ord('a')+dict1[file_extension]))+'.html')
                            new_path = path+'/html files/'+filename + \
                                str(chr(
                                    ord('a')+dict1[file_extension]))+'.html'
                            new_name = filename + \
                                str(chr(
                                    ord('a')+dict1[file_extension]))+'.html'
                            dict1[file_extension] += 1
                    elif file_extension == '.css':  # if extension is css
                        if(files.count('.css') == 1):  # for only one file
                            shutil.move(path+'/'+filename+'/'+filename1,
                                        path+'/css styling files/'+filename+'.css')
                            new_path = path+'/css styling files/'+filename+'.css'
                            new_name = filename+'.css'
                        else:  # for multiple files
                            shutil.move(path+'/'+filename+'/'+filename1, path+'/css styling files/' +
                                        filename+str(chr(ord('a')+dict1[file_extension]))+'.css')
                            new_path = path+'/css styling files/'+filename + \
                                str(chr(ord('a')+dict1[file_extension]))+'.css'
                            new_name = filename + \
                                str(chr(ord('a')+dict1[file_extension]))+'.css'
                            dict1[file_extension] += 1
                    elif file_extension == '.js':  # if extension is .js
                        if(files.count('.js') == 1):  # for only one file
                            shutil.move(path+'/'+filename+'/'+filename1,
                                        path+'/javascript files/'+filename+'.js')
                            new_path = path+'/javascript files/'+filename+'.js'
                            new_name = filename+'.js'
                        else:  # for multiple files
                            shutil.move(path+'/'+filename+'/'+filename1, path+'/javascript files/' +
                                        filename+str(chr(ord('a')+dict1[file_extension]))+'.js')
                            new_path = path+'/javascript files/'+filename + \
                                str(chr(ord('a')+dict1[file_extension]))+'.js'
                            new_name = filename + \
                                str(chr(ord('a')+dict1[file_extension]))+'.js'
                            dict1[file_extension] += 1
                    elif file_extension == '.py':  # if extension is .py
                        if(files.count('.py') == 1):  # for only one file
                            shutil.move(path+'/'+filename+'/'+filename1,
                                        path+'/Python files/'+filename+'.py')
                            new_path = path+'/Python files/'+filename+'.py'
                            new_name = filename+'.py'
                        else:  # for multiple files
                            shutil.move(path+'/'+filename+'/'+filename1, path+'/Python files/' +
                                        filename+str(chr(ord('a')+dict1[file_extension]))+'.py')
                            new_path = path+'/Python files/'+filename + \
                                str(chr(ord('a')+dict1[file_extension]))+'.py'
                            new_name = filename + \
                                str(chr(ord('a')+dict1[file_extension]))+'.py'
                            dict1[file_extension] += 1
                    else:  # for any other file type
                        if(files.count(file_extension) == 1):  # for only one file
                            shutil.move(path+'/'+filename+'/'+filename1, path +
                                        '/'+file_extension+'/'+filename+file_extension)
                            new_path = path+'/'+file_extension+'/'+filename+file_extension
                            new_name = filename+file_extension
                        else:  # for multiple files
                            shutil.move(path+'/'+filename+'/'+filename1, path+'/'+file_extension +
                                        '/'+filename+str(chr(ord('a')+dict1[file_extension]))+file_extension)
                            new_path = path+'/'+file_extension+'/'+filename + \
                                str(chr(
                                    ord('a')+dict1[file_extension]))+file_extension
                            new_name = filename + \
                                str(chr(
                                    ord('a')+dict1[file_extension]))+file_extension
                            dict1[file_extension] += 1
                    # appending information of original name , path and new name , path to dataframe
                    df = df.append({'original file': filename1, 'path of original file': old_path,
                                    'new file': new_name, 'path to new file': new_path}, ignore_index=True)
            del dict1  # deleting dictionary of folder
            try:
                # removing folder (shutil.rmtree will remove the folder and remaining files in it)
                shutil.rmtree(path+'/'+filename)
            except OSError as e:
                print("Error: %s - %s." % (e.filename, e.strerror))
        # if version_control_and_csv folder doesn't exsist
        if(not(os.path.exists('./version_control_and_csv'))):
            os.mkdir('./version_control_and_csv')  # create folder
        # converting dataframe to csv file( change.csv )
        df.to_csv('./version_control_and_csv/change.csv',
                  encoding='utf-8', index=False)
        # calling version_control function for appending details to version_control.csv file
        version_control(0, './version_control_and_csv/change.csv')
    except OSError as e:
        print(' outer Searching ..........')
        print("Error: %s - %s." % (e.filename, e.strerror))


# function for retrieval of original structure from new structure, it has bit variable as arguement
# if bit is 1 that means vesion_control data has been lost and user is performing operation on his own risk
# if 0 that means normal execution
def retrive_original_structure(bit):
    print('-'*121)
    # checking if version_control.csv file exsists or not and bit is 0 or not
    if(os.path.exists('./version_control_and_csv/version_control.csv') or bit == 1):
        # reading csv file as pandas dataframe
        line1 = pd.read_csv('./version_control_and_csv/version_control.csv')
        if(line1.iloc[-1]['event'] == 'new structure retrieved from original structure' or line1.iloc[-1]['event'] == 'created new structure from original structure'):
            # checking the last record of version_control.csv ,if last record was for retrieval or creation of new structure then execute following code
            # checking if change.csv file exsists or not
            if(os.path.exists('./version_control_and_csv/change.csv')):
                # reading file as pandas dataframe
                df = pd.read_csv('./version_control_and_csv/change.csv')
                folder = []  # this list will contain new path of the folders which we will use for remoing the file
                for index, row in df.iterrows():  # iterating over every row of dataframe
                    # checking if new file exsists or not
                    if(os.path.exists(row['path to new file'])):
                        # spilting path of new file for extracting path of folders to be removed
                        f = row['path to new file'].split('/')
                        # checking for removal of IO Images folder
                        t = f[-1].split('.')
                        # if file is a image
                        if t[-1] == 'png' or t[-1] == 'jpeg' or t[-1] == 'jpg' or t[-1] == 'gif':
                            # append path of IO Images folder
                            folder.append('/'.join(f[:-2]))
                        # appending path of folders
                        folder.append('/'.join(f[:-1]))
                        # spilting path of original file for extracting path of original folders to be created
                        path = row['path of original file'].split('/')
                        path = '/'.join(path[:-1])
                        if(os.path.exists(path)):  # if new folder already exsists
                            # shutil.move function will move the file from new location to original location
                            shutil.move(row['path to new file'],
                                        row['path of original file'])
                        else:
                            # if original folder doesn't exsist ,then we will create it
                            os.mkdir(path)
                            # move the file to original location
                            shutil.move(row['path to new file'],
                                        row['path of original file'])
                    else:  # if new file doesn't exsists, then we will drop record of that file, because we don't have access to it now
                        df = df.drop(index)
                # creating set of folders with unique elements
                folder = set(folder)
                for i in folder:
                    try:
                        # shutil.retree will remove the folder and all the remaining files of that folder
                        shutil.rmtree(i)
                    except OSError as e:  # printing exception error
                        print("Error: %s - %s." % (e.filename, e.strerror))
                # removing change.csv file
                os.remove('./version_control_and_csv/change.csv')
                # creating change.csv file from pandas dataframe object
                df.to_csv('./version_control_and_csv/change.csv',
                          encoding='utf-8', index=False)
                # calling version_control function for appending details to version_control.csv file
                version_control(1, './version_control_and_csv/change.csv')
            else:  # if change.csv file doesn't exsist , then we will print the message as no further execution can be performed
                print('Oops! records lost\n')
        else:  # if last record of version_control.csv is not for retrieval or creation of new structure, that means original structure already exsists
            print('original structure already exsists')
    else:  # if version_control.csv doesn't exsists
        print('\n version control file not found')
        print('Do you really want to retrieve original structure , it can give unexpected result')
        print('  1.Yes\n  2.No')  # asking for user's permission
        n = int(input('enter your choice : '))
        if(n == 1):  # if yes, then call the retrive_original_structure with arguement 1
            retrive_original_structure(1)
        else:  # otherwise return
            return

# function for retrieval of new structure from original structure, it has bit variable as arguement
# if bit is 1 that means vesion_control data has been lost and user is performing operation on his own risk
# if 0 that means normal execution


def retrive_new_structure(bit):
    print('-'*121)
    IO_flag = 0  # flag for checking IO Images folder has been created or not
    # checking if version_control.csv file exsists or not and bit is 0 or not
    if(os.path.exists('./version_control_and_csv/version_control.csv') or bit == 1):
        # reading csv file as pandas dataframe
        line1 = pd.read_csv('./version_control_and_csv/version_control.csv')
        # checking the last record of version_control.csv
        if(line1.iloc[-1]['event'] == 'original structure retrieved from new structure'):
            # if last record was for retrieval of original structure then execute following code
            # checking if change.csv file exsists or not
            if(os.path.exists('./version_control_and_csv/change.csv')):
                # reading file as pandas dataframe
                df = pd.read_csv('./version_control_and_csv/change.csv')
                folder = []  # this list will contain original path of the folders which we will use for remoing the file
                for index, row in df.iterrows():  # iterating over every row of dataframe
                    # checking if original file exsists or not
                    if(os.path.exists(row['path of original file'])):
                        # spilting path of original file for extracting path of folders to be removed
                        f = row['path of original file'].split('/')
                        # appending path of folders
                        folder.append('/'.join(f[:-1]))
                        # spilting path of new file for extracting path of new folders to be created
                        path = row['path to new file'].split('/')
                        # checking for creation of IO Images folder
                        t = path[-1].split('.')
                        # if file is a image and folder has not created
                        if (t[-1] == 'png' or t[-1] == 'jpeg' or t[-1] == 'jpg' or t[-1] == 'gif') and IO_flag == 0:
                            # create IO Images folder
                            os.mkdir('/'.join(path[:-2]))
                            IO_flag = 1
                        path = '/'.join(path[:-1])
                        if(os.path.exists(path)):  # if new folder already exsists
                            # shutil.move function will move the file from original location to new location
                            shutil.move(
                                row['path of original file'], row['path to new file'])
                        else:
                            # if new folder doesn't exsist ,then we will create it
                            os.mkdir(path)
                            # move the file to new location
                            shutil.move(
                                row['path of original file'], row['path to new file'])
                    else:  # if original file doesn't exsists, then we will drop record of that file, because we don't have access to it now
                        df = df.drop(index)
                # creating set of folders with unique elements
                folder = set(folder)
                for i in folder:
                    try:
                        # shutil.retree will remove the folder and all the remaining files of that folder
                        shutil.rmtree(i)
                    except OSError as e:  # printing exception error
                        print("Error: %s - %s." % (e.filename, e.strerror))
                # removing change.csv file
                os.remove('./version_control_and_csv/change.csv')
                # creating change.csv file from pandas dataframe object
                df.to_csv('./version_control_and_csv/change.csv',
                          encoding='utf-8', index=False)
                # calling version_control function for appending details to version_control.csv file
                version_control(2, './version_control_and_csv/change.csv')
            else:  # if change.csv file doesn't exsist , then we will print the message as no further execution can be performed
                print('Oops! records lost\n')
        else:  # if last record of version_control.csv is not for retrieval of original structure, that means new structure already exsists
            print('new structure already exsists or new structure is not created yet')
    else:  # if version_control.csv doesn't exsists
        print('\n version control file not found')
        print(
            'Do you really want to retrieve new structure , it can give unexpected result')
        print('  1.Yes\n  2.No')  # asking for user's permission
        n = int(input('enter your choice : '))
        if(n == 1):  # if yes, then call the retrive_new_structure with arguement 1
            retrive_new_structure(1)
        else:  # otherwise return
            return


# function for handling version control file ,it will take flag variable and path of csv file as arguement
def version_control(flag, path_to_csv):
    if(os.path.isfile("./version_control_and_csv/version_control.csv")):  # checking if file exsists or not
        # if file exsists then we will print messages 'changes added'
        print("\nchnages added to "+os.path.abspath('version_control.csv'))
    else:  # if file doesn't exsists ,following code will be executed
        # now we will check if 'version_control_and_csv' folder exsists or not,if not we will make it
        if(not(os.path.exists('./version_control_and_csv'))):
            os.mkdir('./version_control_and_csv')
        # creating version_control.csv file
        f = open("./version_control_and_csv/version_control.csv", 'w')
        # csv writer object for writing data to csv file ,it will take file object as arguement
        writer = csv.writer(f)
        # writerow function wil add row in csv file
        writer.writerow(['event', 'date', 'path for csv file'])
        print("\nnew version control file created at " +
              os.path.abspath('version_control.csv'))  # printing message to user
        f.close()
    # opening file for appending details
    with open("./version_control_and_csv/version_control.csv", 'a', newline='') as f1:
        csv_writer = csv.writer(f1)
        if(flag == -1):  # if flag is -1 ,add details of folder creation
            csv_writer.writerow(
                ['folders created at '+path_to_csv, datetime.datetime.today(), 'No csv file'])
        elif(flag == 0):  # if flag is 0 ,add details of new structure creation
            csv_writer.writerow(
                ['created new structure from original structure', datetime.datetime.today(), path_to_csv])
        elif(flag == 2):  # if flag is 2 ,add details of retrieval of new structure from original structure
            csv_writer.writerow(
                ['new structure retrieved from original structure', datetime.datetime.today(), path_to_csv])
        else:  # otherwise ,add details of retrieval of original structure from new structure
            csv_writer.writerow(
                ['original structure retrieved from new structure', datetime.datetime.today(), path_to_csv])


# function for printing csv files
def print_specific_csv():
    print('1. history of file structure\n2. information about all the files\n What do you want?', end=' ')
    n = int(input())  # taking user choice
    if(n == 1):
        # checking if version_control.csv file exsists or not
        if(os.path.exists('./version_control_and_csv/version_control.csv')):
            # reading csv file into pandas dataframe
            df = pd.read_csv('./version_control_and_csv/version_control.csv')
            print('\n')
            print(df)  # printing dataframe
            print('\n')
        else:  # if file not found then we will print message
            print('\n Oops! records lost\n')
    elif n == 2:
        # checking if change.csv file exsists or not
        if(os.path.exists('./version_control_and_csv/change.csv')):
            # reading csv file into pandas dataframe
            df = pd.read_csv('./version_control_and_csv/change.csv')
            print('\n')
            print(df)  # printing dataframe
            print('\n')
        else:  # if file not found then we will print message
            print('\n Oops! records lost\n')
    else:  # if user doesn't enter 1 or 2 then we will print message wrong option
        print('\n Oops! you entered wrong option\n')


# this is over main code which will interact with the user
# now we will make some welcome template with some details
print("="*57+"WELCOME"+"="*57)
print("|"+" "*119+"|")
print("|"+" "*119+"|")
print("|"+" "*119+"|")
print("="*121)
print("| ==> Question 1 :-  Making structure for students practicals"+" "*59+"|")
print("|"+" "*119+"|")
print("| ==> Question 2 :- Create separate folder for every filetype. Traverse all the folder and rename files like"+" "*12+"|")
print("|                   practical1a.py,  practical2.py and insert into newly created folders according to filetype"+" "*10+"|")
print("|"+" "*119+"|")
print("|==> Question 3 :-  Retain original structure and newly created strucutre and maintain a record in csv files"+" "*12+"|")
print("|"+" "*119+"|")
print("="*121)

# running an infinite loop (it will run until user say to exit)
while True:
    print("-"*121)
    # providing diffrent options to user
    print(' 1. create original file structure\n 2. create new file structure\n 3. retrive new structure from original structure')
    print(' 4. retrive original structure from new structure\n 5. display information\n 6. exit')
    print(' What do you want ? ', end=' ')
    n = int(input())
    print("-"*121)
    if(n == 1):
        print("="*121)
        create_original_structure()  # calling function for creating an original structure
        print("="*121)
    elif n == 2:
        print("="*121)
        create_new_structure()  # calling function for creating new folder structure
        print("="*121)
    elif n == 3:
        print("="*121)
        # calling function for retriving value new structure using details of change.csv files
        retrive_new_structure(0)
        print("="*121)
    elif n == 4:
        print("="*121)
        # calling function for retriving value original structure using details of change.csv files
        retrive_original_structure(0)
        print("="*121)
    elif n == 5:
        print("="*121)
        # calling function for printing change.csv or version_control.csv file
        print_specific_csv()
        print("="*121)
    elif n == 6:
        print("="*121)
        print(' GOOD BYE !')  # printing exit message to user
        print("="*121)
        break
    else:
        print("="*121)
        # if user doesn't enter digits between 1-6 ,we will print invalid choicea
        print('Invalid choice')
        print("="*121)
