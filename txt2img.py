from PIL import Image, ImageDraw, ImageFont
import textwrap
from string import ascii_letters
import sys
import os
import tamil 

current_dir = os.getcwd()
font_path = os.path.join(current_dir, "Fonts")
img_path = os.path.join(current_dir, "Images")

language = sys.argv[1]

image = Image.open(os.path.join(img_path, 'background.jpg'))
draw = ImageDraw.Draw(im=image)


with open("textvalue.txt") as tv:
	text = tv.read()
if language == 'ta':
	fnt = ImageFont.truetype(os.path.join(font_path, 'Bamini.ttf'), 30)
	avg_char_width = sum(fnt.getsize(char)[0] for char in ascii_letters) / len(ascii_letters)
	max_char_count = int( (image.size[0] * .95) / avg_char_width )
	text = textwrap.fill(text=text, width=max_char_count)
	text = tamil.txt2unicode.unicode2bamini(text)
else:
	fnt = ImageFont.truetype(os.path.join(font_path, 'arial.ttf'), 30)
	avg_char_width = sum(fnt.getsize(char)[0] for char in ascii_letters) / len(ascii_letters)
	max_char_count = int( (image.size[0] * .95) / avg_char_width )
	text = textwrap.fill(text=text, width=max_char_count)


draw.text((image.size[0]/2,image.size[1]/2), text, font=fnt, fill='#000000', anchor='mm')

image.save(os.path.join(img_path, 'pil_text.png'))
