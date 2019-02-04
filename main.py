import configparser
import glob
import datetime
import sys
import time
from datetime import date
import os.path, time

full_date = False
def progress(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
    print('\n')
    sys.stdout.flush() 

def find_date(File,full_date=False):
    progress(99,100,'Finding last backup')
    time.sleep(1)
    if(full_date == False or full_date == True):
      File_format = File[0].split(".")[0]
      Year = File_format.split("-")[1]
      Month = File_format.split("-")[2]
      Day = File_format.split("-")[3]
    else:
      print("Check Date in Config!")
    if(full_date == True):
      File_format2 = File[0].split(".")[0]
      File_format2 = File_format2.split("-")[4]
      Hour = File_format2.split(":")[0]
      Minutes = File_format2.split(":")[1]
      Seconds = File_format2.split(":")[2]
    if(full_date == True):
      print("Last backup in name ("+File[0].split("-")[0]+"."+File[0].split(".")[1]+"): "+Year+"-"+Month+"-"+Day+" "+Hour+":"+Minutes+":"+Seconds)
      print("Last modified: %s" % time.ctime(os.path.getmtime(File[0])))
      print("Created: %s" % time.ctime(os.path.getctime(File[0])))
    elif(full_date == False):
      print("Last backup in name("+File[0].split("-")[0]+"."+File[0].split(".")[1]+"): "+Year+"-"+Month+"-"+Day)
      print("Last modified: %s" % time.ctime(os.path.getmtime(File[0])))
      print("Created: %s" % time.ctime(os.path.getctime(File[0])))


def read_config():
    progress(25,100,'Reading config')
    time.sleep(1)
    ConfigParser = configparser.RawConfigParser()   
    configFilePath = r'config'
    ConfigParser.read(configFilePath)
    Format = ConfigParser.get('SETTINGS','Format')
    Date = ConfigParser.get('SETTINGS','Date')
    DIR = ConfigParser.get('SETTINGS','DIR')
    file = ConfigParser.get('SETTINGS','Predeclared_Files')
    set_date(Date)
    file_names = 'NULL'
    if file == 'yes':
        file_names = ConfigParser.get('SETTINGS','File_names')
        last_backup(DIR,file_names,Format,True)
    elif file == 'no':
        last_backup(DIR,file_names,Format)

'''set_date need detected Y = Year, m = Mounth, d = Day, S = sec, M = minutes, H = Hours'''
def set_date(Date):
  progress(50,100,'Parsing date')
  time.sleep(1)
  global full_date
  Date_pattern = ["NULL","NULL","NULL","NULL","NULL","NULL"]
  num = 0
  Date = Date.split("-")
  for x in Date:
    if x == 'Y':
      Date_pattern[num] = '%Y'
    elif x == 'm':
      Date_pattern[num] = '%m'
    elif x == 'd':
      Date_pattern[num] = '%d'  
    elif x == 'H':
      full_date = True
      Date_pattern[num] = '%H'
    elif x == 'M':
      full_date = True
      Date_pattern[num] = '%M'   
    elif x == 'S':
      full_date = True
      Date_pattern[num] = '%S'
    num = num+1


def last_backup(DIR,file_names,Format,file=False):
    progress(75,100,'Checking file names')
    time.sleep(1)
    if file==True:
        file_names = file_names.split(",")
        Format = Format.split(",")
        for x in file_names:
          for y in Format:
            if glob.glob(x+"*"+y): 
              ''' Add DIR in GLOB'''
              File = glob.glob(x+"*"+y)
              find_date(File,full_date)
            else:
              print("File: "+x+"(DATE)."+y+" is not exist!")
    elif file==False:
        Format = Format.split(",")
        for y in Format:
          if glob.glob("*"+"."+y):   
            File = glob.glob("*"+"."+y)
            find_date(File,full_date)

if __name__ == '__main__':
    read_config()
