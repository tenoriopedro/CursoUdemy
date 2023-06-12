# Pillow: redimensionando imagens com Python
# Essa biblioteca é o Photoshop do Python

from PIL import Image
from pathlib import Path

ROOT_FOLDER = Path(__file__).parent
IMAGE_PATH = ROOT_FOLDER / 'Imagem_esposa.jpg'
NEW_IMAGE = ROOT_FOLDER / 'New.jpg'

pil_image = Image.open(IMAGE_PATH)

width, height = pil_image.size
# exif = pil_image.info['exif']

new_width = 500
new_height = round(height * new_width / width)



new_image = pil_image.resize(size=(new_width, new_height))
new_image.save(
    NEW_IMAGE,
    optimize=True,
    quality=70
)