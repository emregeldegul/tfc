import sys
from json import loads
from os.path import exists, expanduser, join

from .tfc import Translation




def main():
    """ Entry point for cli. """
    if not exists(join(expanduser("~"), '.tfc.config.json')):
        print('TFC Could Not Find The Configuration File.')
        exit(1)

    with open(join(expanduser("~"), '.tfc.config.json'), 'r') as configFile:
        config = loads(configFile.read())

    print('TFC listens To Your Clipboard For Translation.')
    print('='*50)

    translation = Translation(config)
    translation.start()

if __name__ == '__main__':
    main()
