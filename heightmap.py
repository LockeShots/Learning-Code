from PIL import Image

IMAGE_FILENAME = './heightmap.jpg'

SEA_LEVEL_BASE = 24
SCALE_FACTOR = 12
CROP_UNITED_KINGDOM = (3850, 700, 4150, 950)

data = (
    # name, height, color
    ('level8', 220, (0, 255, 0)),
    ('level7', 190, (0, 220, 0)),
    ('level6', 150, (0, 190, 0)),
    ('level5', 100, (0, 175, 0)),
    ('level4', 40, (0, 150, 0)),
    ('level3', 35, (0, 130, 0)),
    ('level2', 30, (0, 100, 0)),
    ('level1', SEA_LEVEL_BASE, (0, 75, 0)),
    ('sea', 0, (0, 0, 255)),
)

def dataparser():
    heightdata = open('heightdata.txt')


def colorizer(land_height):
    for name, height, color in data:
        if land_height >= height:
            return color

image_src = Image.open(IMAGE_FILENAME)
image_src = image_src.crop(CROP_UNITED_KINGDOM)
image_des = Image.new('RGB', (image_src.width, image_src.height), 0x000000)

# TODO - sea_level to meters function
for y in range(image_src.height):
    for x in range(image_src.width):
        land_height = image_src.getpixel((x, y))  # Greyscale image so we get 0->255 back from getpixel
        image_des.putpixel((x, y), colorizer(land_height))

image_des.show()