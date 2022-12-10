"""Object Processor"""
import glob
import os
import shutil
import zipfile

source_path = '../source/*'
destination_path = '../destination/'
postfix = [1, 2, 3]

while (True):
    source_object = glob.glob(source_path)
    #print(source_object)  # ['../source\\some.txt']

    for index2, folderfiles in enumerate(source_object):
        object_path = source_object[index2]

        if folderfiles.endswith('.txt'):

            shutil.copy(object_path, '.')

            object_name = (object_path.split('\\')[-1]).split('.')
            prefix = object_name[0] #some
            postfix2 = object_name[1] #txt
            #print(type(object_name))
            #print((object_name)) #['some', 'txt']
            files = []
            for item in postfix:
                filename = prefix+'_'+str(item)+'.'+postfix2
                files.append(filename)
                #print(filename)
                shutil.copy(object_path, f'{filename}')

                with open(f"{object_path}") as f:
                    with open(f"{filename}", "w") as f1:
                        for index, line in enumerate(f):

                            if index>(postfix[item-1])*10:
                                break
                            f1.write(line)
            #print(files)
            with zipfile.ZipFile('files.zip', 'w', zipfile.ZIP_DEFLATED) as my_zip:
                for item in files:

                    my_zip.write(item)

                shutil.copy('files.zip', f'{destination_path}')

            zip_file_name = folderfiles.split('\\')[-1]
            #print(zip_file_name)
            os.system("cd ..\\destination & tar -xf files.zip")
            # os.system('tar -xf ' + "files.zip")

            os.remove(object_path)
            os.remove((object_path.split('\\')[-1]))

        elif folderfiles.endswith('.py'):

            py_file_name = folderfiles.split('\\')[-1]
            #print(py_file_name)
            os.system('python ' + f"..\\source\\{py_file_name}")

            os.remove(object_path)



        index2 +=1
