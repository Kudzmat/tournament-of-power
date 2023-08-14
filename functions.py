from PIL import Image
import os


def split_spritesheet(input_path, output_path, sprite_width, sprite_height):
    # Open the spritesheet image
    spritesheet = Image.open(input_path)

    # Get the dimensions of the spritesheet
    sheet_width, sheet_height = spritesheet.size

    # Calculate the number of sprites in each row and column
    num_sprites_x = sheet_width // sprite_width
    num_sprites_y = sheet_height // sprite_height

    # Split the spritesheet into individual sprites
    for y in range(num_sprites_y):
        for x in range(num_sprites_x):
            # Calculate the coordinates of the sprite
            left = x * sprite_width
            upper = y * sprite_height
            right = left + sprite_width
            lower = upper + sprite_height

            # Crop the sprite from the spritesheet
            sprite = spritesheet.crop((left, upper, right, lower))

            # Save the sprite
            sprite.save(f"{output_path}/sprite_{x}_{y}.png")

    print("Spritesheet split into individual sprites!")


# Example usage
gohan_path = "assets/Characters/gohan/"
folder_path = "assets/Characters/gohan"
split_spritesheet(gohan_path, folder_path, 32, 32)
