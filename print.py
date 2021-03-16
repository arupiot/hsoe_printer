#/usr/bin/env python3

from os import system, environ, putenv, getenv, environ, listdir
from os.path import exists, join
import random
from time import sleep
from PIL import Image, ImageDraw, ImageFont
from signal import alarm, signal, SIGALRM, SIGKILL
import pygame
from pygame.locals import *

TXT_FILE = "/opt/text/text.txt"
PRINTER_NAME = "tmt" 
INTERVAL_SECONDS = 5
MAX_CHARACTERS = 20

sleep(0.75)
pygame.display.init()
pygame.font.init()
sleep(0.75)
display_info = pygame.display.Info()
SCREEN_WIDTH = display_info.current_w
SCREEN_HEIGHT = display_info.current_h
DIM = (SCREEN_WIDTH, SCREEN_HEIGHT)
FONT_SIZE = int(SCREEN_HEIGHT/8)

print(DIM)

putenv('SDL_VIDEODRIVER', 'fbcon')
putenv('SDL_FBDEV', '/dev/fb0')
putenv('SDL_MOUSEDRV', 'TSLIB')
putenv('SDL_MOUSEDEV', '/dev/input/event0')

WHITE      = (255, 255, 255)
BLACK      = (  0,   0,   0)
BLUE       = (  0,   0, 255)
GREEN      = (  0, 255,   0)
RED        = (255,   0,   0)
ORANGE     = (255, 165,   0)
GREY       = (128, 128, 128)
YELLOW     = (255, 255,   0)
PINK       = (255, 192, 203)
LBLUE      = (191, 238, 244)

lcd = None

class Alarm(Exception):
    pass

def alarm_handler(signum, frame):
    raise Alarm

    signal(SIGALRM, alarm_handler)
    alarm(3)
    try:
        print("alarm")
        pygame.init()
        DISPLAYSURFACE = pygame.display.set_mode((DISPLAYWIDTH, DISPLAYHEIGHT)) 
        alarm(0)
    except Alarm:
        raise KeyboardInterrupt

    pygame.display.set_caption('Drawing')


def split_into_lines(sentence):
    words = sentence.split()
    lines = [""]
    l = 0
    for word in words:
        if len(lines[l]) <= MAX_CHARACTERS:
            lines[l] += word + " "
        else:
            l += 1
            lines.append(word + " ")
    return(lines)


def main():
   global FONT_SIZE
   global lcd
   signal(SIGALRM, alarm_handler)
   alarm(3)
   try:
      lcd = pygame.display.set_mode(DIM)
      alarm(0)
   except Alarm:
      raise KeyboardInterrupt
   pygame.mouse.set_visible(False)
   lcd.fill((0,0,0))

   # get fonts
   font_files = listdir("fonts")
   fonts = []
   for font_name in font_files:
       print(font_name)
       fonts.append(ImageFont.truetype(join("fonts", font_name), FONT_SIZE))


   if exists(TXT_FILE):
       f = open(TXT_FILE)
       lines = f.readlines()
       n = len(lines)
       while True:
           i = int(random.random()*n)
           f = int(random.random()*len(fonts))
           print(lines[i])
           sentence_lines = split_into_lines(lines[i])
           print(sentence_lines)
           # create an image
           out = Image.new("RGB", (SCREEN_WIDTH , SCREEN_HEIGHT), (255, 255, 255))
           # get a font
           #fnt = ImageFont.truetype("fonts/Lobster_1.3.otf", FONT_SIZE)
           # get a drawing context
           d = ImageDraw.Draw(out)
           # draw multiline text
           j = 0
           step = FONT_SIZE
           for sentence_line in sentence_lines:
                d.text((10,step+step*j), sentence_line, font=fonts[f], fill=(0, 0, 0))
                j += 1
           out.show()
           image_name = "tmp.jpg"
           out.save(image_name)
           #print(dir(out))
           #strFormat = 'RGBA'
           #raw_str = out.tostring("raw", strFormat)
           #surface = pygame.image.fromstring(raw_str, out.size, strFormat)
           system("lp -d %s tmp.jpg" % PRINTER_NAME)
           image = pygame.image.load(image_name)
           resized_image = pygame.transform.scale(image, (SCREEN_WIDTH, SCREEN_HEIGHT))
           pygame.display.flip()
           pygame.display.update()
           lcd.blit(resized_image, (0, 0))
           #draw_screen()
           sleep(INTERVAL_SECONDS)


if __name__ == "__main__":
    main()


