from PIL import Image

def bilde():

  datne = '15.11.2021/suns.jpg'

  with Image.open(datne)as im:
    print(datne, im.format,f'{im.size}x{im.mode}')
    im.show()
    izmers = (100,100)
    im.thumbnail(izmers)
    im.save('15.11.2021/maza_bilde.jpg',im.format)
    im.show()

bilde()

#nolasa attēlu
im = Image.open("15.11.2021/suns.jpg")


#pagriež attēlu

angle = 90

out = im.rotate(angle)
out.save('rotate-output.png')