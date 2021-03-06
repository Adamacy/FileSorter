import os, shutil, sys
from win10toast import ToastNotifier

toaster = ToastNotifier()

path_to_files = 'F:/Captures' #Enter the path here to folder
n = 0
try: 
    for subdir, dir, files in os.walk(path_to_files):
        for element in files:
            separator = ' ' #Select separator of name. for exmample: _ ; Space can be used
            try:
                folders = element.split(separator)[0] 
            except IndexError:
                toaster.show_toast('Too high number', 'You choose too high number is square bracket')
                sys.exit()
            if not os.path.exists(f'{path_to_files}/{folders}'):
                os.mkdir(f'{path_to_files}/{folders}')
        for file in files:
            if file == 'desktop.ini':
                continue
            shutil.move(path_to_files + '/' + file, path_to_files +'/' + file.split(' ')[0] + '/' + file) #moving file
            n += 1
except FileNotFoundError:
    toaster.show_toast('Files have been sorted', f'{n} files sorted', duration=4)