import os
import os.path
import imp
import datetime
import json
import ast
from os import listdir
from os.path import isfile, join
import pickle
import time
import re
'''
import utils
imp.reload(utils)

refresh('utils')
from utils import *
'''

'''

'''
def RunDict(function, d, *arg):
    for key,value in d.items():
        function(name, url, *arg)

def isFileExists(file):
    return os.path.isfile(file)

'''
a = getFiles('tmp/20170406')
a = getFiles('tmp/20170406','.json')
'''
def getFiles(folder, ext=None):
    onlyfiles = [f for f in listdir(folder) if isfile(join(folder, f)) and (ext is None or os.path.splitext(f)[1] == ext) ]
    return onlyfiles

'''
runFolder(lambda x:print(x), './')
'''
def runFolder(function, folder, ext=None, *args, **kw):
    files = getFiles(folder,ext)
    for f in files:
        fromFile = join(folder,f)
        log(fromFile)
        LogExp(function, fromFile, *args, **kw)    

'''
g = lambda:1/0
LogExp(g)
LogExp(lambda:1/0)
LogExp((lambda x,y:x/y),4,2)
LogExp(tuple,[4,2])
'''
def LogExp(function, *args, **kw):
    try:
        a = function(*args, **kw)
    except Exception as e: 
        log(str(function))
        log(str(e)) 
        return None
    else:
        return a   
'''
s = readFile('20170406/21_15.json',byFileType=False)
'''
def readFile(file, default='', byFileType=True):
    data = default
    if not isFileExists(file):
        return data
    with open(file, 'r') as f:
        if byFileType:
            extension = os.path.splitext(file)[1]
            if extension == '.json':
                data = json.load(f)
            else:
                data=f.read()
        else:
            data=f.read()
#           data=myfile.read().replace('\n', '')
    return data

'''
d = readJson('tmp/20170407/west.json')
'''
def readJson(file, default=[]):
    return readFile(file,default)


'''
dumpJson('aaa.json',o["Results"])
'''
def dumpJson(filename, obj):
    try:
        writeFile(filename, obj, 'w')
    except Exception as e: 
        log(str(e))


'''
writeFile('r.js',s,'w')
writeFile("00.html",html.encode('utf-8'),"wb")
writeFile('s.json',str(r.json()),'w')

   with open("00.html", "wb") as f:
        f.write(html.encode('utf-8'))
'''
def writeFile(filename, obj, format):
    d = os.path.dirname(filename)
    if d != '':
        os.makedirs(d, exist_ok=True)
    with open(filename, format) as f:
        if inType(obj, [str, bytes]):
            f.write(obj)
        else:
            json.dump(obj, f)

def inType(obj, typeList):
    result = False
    for t in typeList:
        if type(obj) is t:
            result = True
    return result

def log(s, file='log/log.txt'):
    writeFile(file, '{0} - {1}\n'.format(s,getStrFromDate(format='%Y-%m-%d %H:%M:%S')), 'a')
    print(s)

def getStrFromDate(date = datetime.datetime.now(), format='%Y%m%d'):
    return date.strftime(format)

def refresh(file, func = None):
    exec('import imp')
    exec('import {0}'.format(file))
    exec('imp.reload({0})'.format(file))
'''    if func is not None:
        exec('from {0} import {1}'.format(file, func))
    #exec 'import {0}'.format(s) in globals(), locals()
    exec('import imp'.format(s), globals(), locals())
    exec('import {0}'.format(s), globals(), locals())
    exec('imp.reload({0})'.format(s), globals(), locals())
    exec('from {0} import *'.format(s), globals(), locals())
    #exec()

    #from s import *'''



def getText(element, attr = None):
    if element != None:
        try:
            if (attr == None):
                return element.text
            else:
                return element[attr]
        except Exception as e: 
            print(str(e))
            return ''
    else:
        return ''

def isNone(value, default):
    if (value is None):
        return default
    else:
        return value



