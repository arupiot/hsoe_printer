#/usr/bin/env python3
#!/usr/bin/env python3

from os import listdir, system, environ
from os.path import join, splitext
from time import sleep
import signal
from pyfiglet import Figlet

IMAGES_PATH='/opt/images'
IMAGES_EXT = '.png'
PRINTING_INTERVAL = '10'
PRINTER_NAME = 'tmt'

try:
  if environ['IMAGES_PATH'] != '':
    IMAGES_PATH = environ['IMAGES_PATH']
  else:
    IMAGES_PATH = '/opt/images'

  if environ['IMAGES_EXT'] != '':
    IMAGES_EXT = environ['IMAGES_EXT']
  else:
    IMAGES_EXT = '.png'

  if environ['PRINTING_INTERVAL'] != '':
    PRINTING_INTERVAL = environ['PRINTING_INTERVAL']
  else:
    PRINTING_INTERVAL = '10'

  if environ['PRINTER_NAME'] != '':
    PRINTER_NAME = environ['PRINTER_NAME']
  else:
    PRINTER_NAME = 'tmt'
except:
  pass

def main():
    files = listdir(IMAGES_PATH)
    files.sort()

    figl = Figlet(font='standard')
    print(figl.renderText('High Street Printer'))
    
    while True:
        for f in files:
            ext = splitext(f)[1]
            if ext.lower() == IMAGES_EXT:
                filename = join(IMAGES_PATH,f)
                print("Printing image:", filename)
                system("lp -d %s %s" % (PRINTER_NAME,filename))
                sleep(int(PRINTING_INTERVAL))

if __name__ == '__main__':
    main()


