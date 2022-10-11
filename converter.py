import PIL.Image
import math
import os.path

# --------------initial variables and setup---------------

x = 0

print("Enter a valid path:")
path = input(str())

try:
    img = PIL.Image.open(path)
except:
    print("invalid path")

print("Enter file name")
file_name = input(str())


if (not file_name):
    file_name = 'img'


# -----------image manipulation--------------


ascii = ('$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|'
         '()1{}[]?-_+~<>i!lI;:,"^`\'.            ')
width, height = img.size
aspect_ratio = height/width
new_w = 100
new_h = int(new_w*aspect_ratio*0.5)
img = img.resize((new_w, new_h))
img = img.convert("L")
pixels = img.getdata()

ascii_img = ''

for pixel in pixels:
    ascii_img += str(ascii[math.floor(pixel/256*len(ascii))])

txt_img = ''
for i in range(0, len(ascii_img), new_w):
    txt_img += str(ascii_img[i:i+new_w])
    txt_img += '\n'

# ----------text file creation---------------

if (os.path.exists(f'{file_name}.txt')):
    x = 1
    while (os.path.exists(f'{file_name}({x}).txt')):
        x += 1

if x == 0:
    with open(f'{file_name}.txt', 'w') as f:
        f.write(txt_img)
else:
    with open(f'{file_name}({x}).txt', 'w') as f:
        f.write(txt_img)
input("press any key to exit")
