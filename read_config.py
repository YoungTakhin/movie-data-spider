from configparser import ConfigParser
import os

def config(section, option_key, file_name='config.ini'):
    cur_path = os.path.dirname(os.path.realpath(__file__))
    config_path = os.path.join(cur_path, file_name)
    cp = ConfigParser()
    cp.read(config_path)
    value = cp.get(section, option_key)
    print(value)
    return value


if __name__ == '__main__':
    config('TMDB', 'api_key')
