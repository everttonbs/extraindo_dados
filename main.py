
from PIL import Image, ExifTags

def info_file(image):
    info_image= dict()
    file = Image.open(image)
    exif_data = file._getexif() # type -> dict

    for key, value in exif_data.items():
        if key in ExifTags.TAGS:            
            info_image[ExifTags.TAGS[key]] = value
            print(ExifTags.TAGS[key], value)

def main():
    info_file('test_img.JPG')


if __name__ == '__main__':
    main()
    