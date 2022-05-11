import os
import shutil

current_dir = os.path.dirname(os.path.realpath(__file__))

for filename in os.listdir(current_dir):
    ## organize images
    if filename.endswith((".png" , ".jpg" , ".jpeg" , ".gif", '.tiff', '.psd', '.svg')):
        if not os.path.exists('Images'):
            os.mkdir('Images')
        shutil.copy(filename, 'Images')
        os.remove(filename)
        print('Images done')

    ## organize videos
    if filename.endswith((".mp4" , ".mkv" , ".mpg" , ".mov", '.wmv', '.MOV')):
        if not os.path.exists('Videos'):
            os.mkdir('Videos')
        shutil.copy(filename, 'Videos')
        os.remove(filename)
        print('Videos done')

    ## organize zip files
    if filename.endswith((".zip" , ".rar" , ".egg" , ".jar", '.gz')):
        if not os.path.exists('Zips'):
            os.mkdir('Zips')
        shutil.copy(filename, 'Zips')
        os.remove(filename)
        print('Zips done')

    ## organize Docs
    if filename.endswith((".pdf" , ".docs" , '.dotx', '.docx' , ".doc" , ".word", '.pptx', '.csv', '.xlsx', '.xls', '.xlsm', '.xlsb')):
        if not os.path.exists('Docs'):
            os.mkdir('Docs')
        shutil.copy(filename, 'Docs')
        os.remove(filename)
        print('Docs done')

    ## organize programs
    if filename.endswith((".exe" , ".exec", '.msi')):
        if not os.path.exists('Programms'):
            os.mkdir('Programms')
        shutil.copy(filename, 'Programms')
        os.remove(filename)
        print('Programms done')

    ## organize mp3
    if filename.endswith((".mp3" , ".waptt" , ".wem" , ".wav")):
        if not os.path.exists('Music'):
            os.mkdir('Music')
        shutil.copy(filename, 'Music')
        os.remove(filename)
        print('Music done')

    ## organize codes
    if filename.endswith((".html" , ".css" , ".js" , ".php" , ".sql", 'json', '.xml')):
        if not os.path.exists('Codes'):
            os.mkdir('Codes')
        shutil.copy(filename, 'Codes')
        os.remove(filename)
        print('Codes done')

print('All files is organized')