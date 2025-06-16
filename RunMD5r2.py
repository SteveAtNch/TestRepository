#   output is a https://www.programiz.com/python-programming/set
#   Example: python RunMd5.py "c:/temp/"

import os
import sys
import hashlib
import datetime as datetime
import msvcrt

def left(s, amount):
    return s[:amount]

def right(s, amount):
    return s[-amount:]

def mid(s, offset, amount):
    return s[offset:offset+amount]

def isMultipleof10(n): 
    while ( n > 0 ): 
        n = n - 10
    if ( n == 0 ): 
        return 1
    return 0

if len(sys.argv) == 1:
    root_dir = 'C:\\Temp\\'    #   VCcode running
else:
    root_dir = sys.argv[1]      #   for command line input

# make sure the last charactor is '/'
if right(root_dir, 1) != "/" and right(root_dir, 1) != "\\":
    root_dir = root_dir + "/"

print("\r\nThe root folder will be: " + root_dir)
file_set = set()
print(str(datetime.datetime.now()) + ': ', end='')
startTime = datetime.datetime.now()
results=[]

try:
        OutputCSVfile = open('C:\\temp\\OutputCSVfile.csv', 'w')
        OutputCSVfile.write('Index, Timestamp, OutputHash, filesize, filename\n')
except IOError:
        print("access error to OutputCSVfile.csv!"  )

index=0
for root, dirs, files in os.walk(root_dir):
        for file_name in files:
                rel_dir = os.path.relpath(root, root_dir)
                rel_file = os.path.join(rel_dir, file_name)
                file_set.add(rel_file)

for filenames in file_set:
        if left(filenames, 1) == '.' :
                amount = len(filenames)-2
                NewFileName = right(filenames, amount)
                filenames = root_dir + NewFileName
                filenames = filenames.replace('\\\\', '\\')
        else:
                filenames = root_dir + filenames

        if isMultipleof10(index):
                print('.',end='')
        try:
                with open(filenames,"rb") as f:
                        if msvcrt.kbhit():
                                if ord(msvcrt.getch()) == 27:
                                        print('Escape Key Pressed!')
                                        break
                        if right(filenames, 4) == '.exe':
                                break
                        if right(filenames, 4) == '.com':
                                break
                        if right(filenames, 4) == '.dll':
                                break
                        index = index + 1
                        statinfo = os.stat(filenames)
                        bytes = f.read() # read entire file as bytes
                        readable_hash = hashlib.sha256(bytes).hexdigest()
                        OutputCSVfile.write(str(index) + '\t' + str(datetime.datetime.now()) + '\t' + readable_hash + '\t' + str(statinfo.st_size) + '\t' + filenames + '\n')
                        results.append([readable_hash,filenames])
        except:
                print('\nError: \t' + str(sys.exc_info()[0]) + ': \t' + filenames)
        # except IOError:
        #         print('\nIOError: \t' + str(sys.exc_info()[0]) + ': \t' + filenames)
        # except MemoryError:
        #         print('\nMemory Error: \t' + sys.exc_info()[0] + ': \t' + str(statinfo.st_size) + ': \t' + filenames)
        # except FileNotFoundError:
        #         print('\nFile not found: \t' + sys.exc_info()[0] + ': \t' + str(statinfo.st_size) + ': \t' + filenames)
        # finally:
        #         print('Closing the "OutputCSVfile"')
        #         OutputCSVfile.close()

OutputCSVfile.close()

print()
distinctResults=[]
OutputResults=[]

for x in results:
        if x[0] not in distinctResults:
                distinctResults.append(x[0])
        else:
                OutputResults.append(x[0])

Final = []
for x in OutputResults:
        for y in results:
                # print(x, y[0])
                if x == y[0]:
                        Final.append(y[1])
                
print('len(results):', len(results))
print('len(distinctResults):', len(distinctResults))

print("Output results shows " + str(len(results)-len(distinctResults)))
print('\nClosing the "OutputCSVfile" with ' + str(index) + ' records.')
print('Execution Time was: ' + str(1*(datetime.datetime.now()-startTime)) + '\r\n')


print('\r\n---------------------------------------------------------------------------------------------------------\r\nDone.\r\n')
