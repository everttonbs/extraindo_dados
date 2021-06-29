
from PIL import Image, ExifTags
import argparse

def info_file(image):

    info_image= dict()
    file = Image.open(image)
    exif_data = file._getexif() # type -> dict

    for key, value in exif_data.items():
        if key in ExifTags.TAGS:            
            info_image[ExifTags.TAGS[key]] = value
            print(ExifTags.TAGS[key], value)

def main():   
    my_parser = argparse.ArgumentParser(description='Extraindo informações de imagem')

    my_parser.add_argument('-i', action = 'store', dest = 'image',
                           default = 'test_img.JPG', required = False,
                           help = 'Será extraído as informações da imagem.')

    arguments = my_parser.parse_args()
   
    info_file(arguments.image)

if __name__ == '__main__':
    main()    

