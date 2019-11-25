import configparser

config = configparser.ConfigParser();
config.read('config.ini');
print(config['config']['test']);

# config.ini内部
'''
[config]
test = yes
'''
