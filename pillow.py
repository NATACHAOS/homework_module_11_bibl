from PIL import Image


# изменить размер фото
def resize_image(image_path):
    image = Image.open(image_path)
    image = image.resize((800, 600))
    image.save(image_path)


for i in range(1, 3):
    image_path = f'foto\\img {i}.png'
    resize_image(image_path)


# изменить цвет фото
def change_color(image_path):
    image = Image.open(image_path)
    image = image.convert('L')
    image.save(image_path)


for i in range(1, 3):
    image_path = f'foto\\img {i}.png'
    change_color(image_path)

# изменить цвет фото
def rotate_image(image_path):
    image = Image.open(image_path)
    image = image.rotate(90)
    image.save(image_path)


for i in range(1, 2):
    image_path = f'foto\\img {i}.png'
    rotate_image(image_path)


