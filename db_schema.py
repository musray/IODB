# -*- coding: utf-8 -*-

import fileinput
import os

txt_file = "11.1.txt"

def getFile():
    file_lst = []
    cwd = os.getcwd()
    lst = [i for i in os.listdir(cwd) if i.endswith('.txt')]
    for i in lst:
        file_lst.append(os.path.join(cwd, i))

    return file_lst, cwd
    
def reader(txt_file):
    f = fileinput.input(txt_file)
    return [i for i in f]

def modi(txt_file, cert):
    content = []
    content_new = []
    content = reader(txt_file)
    #print "len(content) = %r" % len(content)
    for row in content:
        row_lst = row.split(',')
        if len(row_lst) > 2:
            #print row_lst
            row_lst[2] = cert 
            row_str = ','.join(row_lst)
            content_new.append(row_str)
        else:
            content_new.append(row)
    new_file(content_new, txt_file)

def new_file(content, original_file):
    cwd = os.getcwd()
    new_file_name = original_file[:-4] + "_new.txt"
    new_file = os.path.join(cwd, new_file_name)
    f = open(new_file, 'w')
    for i in content:
        f.writelines(i)
    f.close()
    print "%s is done!" % original_file

def main():
    file_list, cwd_path = getFile()
    cert = '"' + raw_input('Give me your Voucher No.-->') + '"'
    for f in file_list:
        modi(f, cert) 
    raw_input("all files are OK! press ENTER to quit...")
    
if __name__ == "__main__": main()

