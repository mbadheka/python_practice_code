# file finder in python

import os,shutil

dict_extensation = {
'doct_extensation' : ('.docx','.doc','.docm'),
'software_extensation' : ('.exe'),
'image_extensation' : ('.jpg','.jpeg','.png'),
'powerpoint_extensation' : ('.ppt','.pptx','.pptm'),
'PDF_extensation' : ('.pdf'),
}

folderpath = input("please enter the path of file:  ")

def file_extractor(folder_path,file_extensation):
    files = []
    for file in os.listdir(folder_path):
        for extension in file_extensation:
            if file.endswith(extension):
                files.append(file)
    return files

for extenstion_type, extenstion_tuple in dict_extensation.items():
    # print(extenstion_tuple)
    folder_name = extenstion_type.split('_')[0]+'_folder'
    new_path =  os.path.join(folderpath,folder_name)
    os.mkdir(new_path)
    for I in file_extractor(folderpath,extenstion_tuple):
        I_path = os.path.join(folderpath,I)
        I_new_path =os.path.join(new_path,I)
        shutil.move(I_path,I_new_path)
