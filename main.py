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
        fnames = glob.glob("/*.txt")
        print ('dir_from_input:',DIR)
        print (file_names,Format)
    elif file==False:
        print ('file_name_from_cfg:',DIR)
        print (file_names,Format)

if __name__ == '__main__':
    read_config()
