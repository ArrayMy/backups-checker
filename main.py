import configparser
def read_config():
    ConfigParser = configparser.RawConfigParser()   
    configFilePath = r'config'
    ConfigParser.read(configFilePath)
    DIR = ConfigParser.get('SETTINGS','DIR')
    file = ConfigParser.get('SETTINGS','Predeclared_Files')
    file_names = 'NULL'
    if file == 'yes':
        file_names = ConfigParser.get('SETTINGS','File_names')
        last_backup(DIR,file_names,True)
    elif file == 'no':
        last_backup(DIR,file_names)   
        
def last_backup(DIR,file_names,file=False):
    if file==True:
        print ('dir_from_input:',DIR)
        print (file_names)
    elif file==False:
        print ('file_name_from_cfg:',DIR)
        print (file_names)

if __name__ == '__main__':
    read_config()
