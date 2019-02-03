import configparser
import glob
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
'''
set_date need detected Y = Year, m = Mounth, d = Day, S = sec, M = minutes, H = Hours
'''
def set_date(Date):
  if Date == 'Y-m-d':
    Date_pattern = '%{YEAR:year}-%{MONTHNUM:month}-%{MONTHDAY:day}'
     
    
    
def last_backup(DIR,file_names,Format,file=False):
    if file==True:
        print ('DIR:',DIR)
        file_names = file_names.split(",")
        Format = Format.split(",")
        for x in file_names:
          for y in Format:
            if glob.glob(x+"*"+y): 
              print("Easy!")
            else:
              print("File: "+x+"."+y+" is not exist!")
    elif file==False:
        print ('file_name_from_cfg:',DIR)
        print (file_names,Format)

if __name__ == '__main__':
    read_config()
