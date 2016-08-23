import sys

def deleteContent(pfile):
    pfile.seek(0)
    pfile.truncate()

def swapFilesContent(name_file1, name_file2):
    f = open(name_file1, 'r+')
    d = open(name_file2, 'r+')
    buffer_f = f.read()
    buffer_d = d.read()
    print buffer_f
    print buffer_d
    deleteContent(f)
    deleteContent(d)
    f.write(buffer_d)
    d.write(buffer_f)
    f.close()
    d.close()

swapFilesContent('yyy.txt', 'zzz.txt')

def read_file_content(name_file):
    file = open(name_file, 'r')
    line = file.readline()
    is_first_line_mode = True
    line = line[:-1]
    while (line != ""):
        if is_first_line_mode:
            pass
            is_first_line_mode = False
        else:
            if line != "":
                # result = line.split(";")
                print line
        line = file.readline()[:-1]

read_file_content ('salary.csv')
