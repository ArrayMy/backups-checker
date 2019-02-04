import configparser
import glob
import datetime

'''
Find DATE IN NAME
'''
def find_date(File):
    print(File)

def read_config():
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
      Date_pattern[num] = '%H'
    elif x == 'M':
      Date_pattern[num] = '%M'   
    elif x == 'S':
      Date_pattern[num] = '%S'
    num = num+1
  print (Date_pattern)


def last_backup(DIR,file_names,Format,file=False):
    if file==True:
        print ('DIR:',DIR)
        file_names = file_names.split(",")
        Format = Format.split(",")
        for x in file_names:
          for y in Format:
            if glob.glob(x+"*"+y): 
              File = glob.glob(x+"*"+y)
              find_date(File)
              print("Easy!")
            else:
              print("File: "+x+"(DATE)."+y+" is not exist!")
    elif file==False:
        print ('file_name_from_cfg:',DIR)
        print (file_names,Format)

if __name__ == '__main__':
    read_config()
