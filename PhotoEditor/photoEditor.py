from PIL import Image, ImageEnhance, ImageFilter
import os

path = './imgs'
pathOut = 'editedImgs'

# Ensure that the output folder exists
os.makedirs(pathOut, exist_ok=True)

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    # Apply various effects
    edit = img.filter(ImageFilter.SHARPEN).rotate(-180)
    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)

    # Color inversion effect
    edit = ImageEnhance.Color(edit).enhance(1)

    # Additional effects
    edit = edit.transpose(Image.FLIP_LEFT_RIGHT)  # Flip horizontally
    edit = edit.transpose(Image.FLIP_TOP_BOTTOM)  # Flip vertically

    # Save the edited image
    clean_name = os.path.splitext(filename)[0]
    edited_filename = f'{pathOut}/{clean_name}_edited.jpg'
    edit.save(edited_filename)
