import configparser
import glob
def read_config():
    ConfigParser = configparser.RawConfigParser()   
    configFilePath = r'config'
    ConfigParser.read(configFilePath)
    Format = ConfigParser.get('SETTINGS','Format')
    DIR = ConfigParser.get('SETTINGS','DIR')
    file = ConfigParser.get('SETTINGS','Predeclared_Files')
    file_names = 'NULL'
    if file == 'yes':
        file_names = ConfigParser.get('SETTINGS','File_names')
        last_backup(DIR,file_names,Format,True)
    elif file == 'no':
        last_backup(DIR,file_names,Format)   
        
def last_backup(DIR,file_names,Format,file=False):
    if file==True:
        print ('dir_from_input:',DIR)
        file_names = file_names.split(",")
        Format = Format.split(",")
        print(file_names)
        for x in file_names:
          for y in Format:
            print(x+"."+y)
        '''fnames = glob.glob(file_names[0]+"*"+Format[0])
        print(fnames[0])'''
    elif file==False:
        print ('file_name_from_cfg:',DIR)
        print (file_names,Format)

if __name__ == '__main__':
    read_config()
