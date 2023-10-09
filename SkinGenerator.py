import re
from PIL import ImageColor, Image

colorDictJacket = {
    "#5782a3": "#000000", # base
    "#6993ac": "#000000", # lighter
    "#4f6f93": "#000000", # mid
    "#3d577b": "#000000"  # dark
}

# Function to convert hex color to ANSI escape code
def hex_to_ansi(hex_color):
    r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (1, 3, 5))
    return f"\033[38;2;{r};{g};{b}m█\033[0m"

def adjust_hex_color(hex_color, factor):
    # Remove the '#' symbol if it's present
    hex_color = hex_color.lstrip('#')

    # Convert the hex color to an RGB tuple
    rgb_color = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

    # Adjust the RGB components to make the color lighter or darker
    adjusted_rgb = tuple(max(0, min(255, int(channel + (255 - channel) * factor))) for channel in rgb_color)

    # Convert the adjusted RGB color back to a hex color code
    adjusted_hex_color = "#{:02X}{:02X}{:02X}".format(*adjusted_rgb)

    return adjusted_hex_color

def is_valid_hex_color(hex_color):
    # Regular expression pattern for a valid hex color code
    pattern = re.compile(r'^#(?:[0-9a-fA-F]{3}){1,2}$')

    # Check if the input matches the pattern
    if pattern.match(hex_color):
        return True
    else:
        return False

# color_input = input("Enter a hex color: ")

# while not is_valid_hex_color(color_input):
#     print("You entered an invalid hex color code. Please try again.")
#     color_input = input("Enter a hex color: ")

# base_skin_path = Image.open("baseSkin.png")
# generated_skin_path = "generatedSkin_"+".png"
# copied_image = base_skin_path.copy()
# copied_image.save(generated_skin_path)
# base_skin_path.close()
# copied_image.close()

def generate_jacket_colors(base_color, contrast):
    colorDictJacket["#5782a3"] = base_color
    colorDictJacket["#6993ac"] = adjust_hex_color(base_color, 0.2*(contrast*2)) # lighter
    colorDictJacket["#4f6f93"] = adjust_hex_color(base_color, -0.2*(contrast*2)) # mid
    colorDictJacket["#3d577b"] = adjust_hex_color(base_color, -.28*(contrast*2)) # dark

#generate_jacket_colors(color_input)

print(hex_to_ansi(colorDictJacket["#5782a3"]))
print(hex_to_ansi(colorDictJacket["#6993ac"]))
print(hex_to_ansi(colorDictJacket["#4f6f93"]))
print(hex_to_ansi(colorDictJacket["#3d577b"]))

def replace_color(input_image_path, output_image_path, target_color, replacement_color):
    # Convert the input hex color codes to RGB
    target_color = ImageColor.getrgb(target_color)
    
    # Convert the replacement color to RGBA (with alpha set to 255)
    replacement_color = ImageColor.getrgb(replacement_color) + (255,)

    # Open the image
    image = Image.open(input_image_path)
    width, height = image.size

    # Convert the image to RGBA mode if it's not already
    image = image.convert("RGBA")

    # Create a new image with the same size and RGBA mode
    new_image = Image.new("RGBA", (width, height))

    for x in range(width):
        for y in range(height):
            # Get the color of the current pixel
            current_color = image.getpixel((x, y))

            # Check if the current pixel's color matches the target color
            if current_color[:-1] == target_color:
                # Replace the pixel with the replacement color
                new_image.putpixel((x, y), replacement_color)
            else:
                # Keep the original pixel color
                new_image.putpixel((x, y), current_color)

    # Save the modified image
    new_image.save(output_image_path)

# for key, value in colorDictJacket.items():
#     replace_color(generated_skin_path, generated_skin_path, key, value)

def generate_skin(color, contrast):

    base_skin_path = Image.open("baseSkin.png")
    generated_skin_path = "static\generatedSkin_.png"
    copied_image = base_skin_path.copy()
    copied_image.save(generated_skin_path)
    base_skin_path.close()
    copied_image.close()

    generate_jacket_colors(color, contrast)
    for key, value in colorDictJacket.items():
        replace_color(generated_skin_path, generated_skin_path, key, value)
    print("Skin generated successfully!")