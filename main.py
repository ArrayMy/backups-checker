import configparser
import glob
import datetime

'''
Find DATE IN NAME
'''
full_date = False
def find_date(File,full_date=False):
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
    print("Last backup ("+File[0].split("-")[0]+"."+File[0].split(".")[1]+"): "+Year+"-"+Month+"-"+Day+" "+Hour+":"+Minutes+":"+Seconds)

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
    if file==True:
        print ('DIR:',DIR)
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
        print ('file_name_from_cfg:',DIR)
        print (file_names,Format)

if __name__ == '__main__':
    read_config()
