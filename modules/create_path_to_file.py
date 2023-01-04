'''
    файл create_path_to_file потрібен 
    для побудови абсолютного шляху до будь якого файлу на комп'ютері
'''
import os
def path_to_file(name_file):
    abs_path = __file__
    abs_path1 = abs_path.split("/")
    del abs_path1[-1]
    del abs_path1[-1]
    abs_path2 = "/".join(abs_path1)
    path_file = os.path.join(abs_path2, name_file)
    return path_file


