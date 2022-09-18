import zipfile
import time

folderpath = input('Path to file: ')
zipf = zipfile.ZipFile(folderpath)
result = 0
tried = 0
c = 0
if not zipf:
    print('The zipped file/folder is not password protected! You can successfully open it!')
else:
    start_time = time.time()
    word_list = open('wordlist.txt', 'r', errors='ignore')
    words = word_list.read().split('\n')
    for word in words:
        password = word.encode('utf-8').strip()
        c = c + 1
        print('Trying: ' + word)
        try:
            with zipfile.ZipFile(folderpath, 'r') as zf:
                zf.extractall(pwd=password)
                print('Success! The password is ' + word)
                end_time = time.time()
                result = 1
            break
        except:
            pass
if result == 0:
    print('Password not found. Tried ' + str(c) + ' passwords')
else:
    duration = end_time - start_time
    print('Zip successfully extracted. Tried ' +
          str(c) + ' passwords in ' + str(duration) + ' seconds')
