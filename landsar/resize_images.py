from PIL import Image
import os

input_folder = "images"
output_folder = "images_resized"
os.makedirs(output_folder, exist_ok=True)

target_width = 600

for file in os.listdir(input_folder):
    if file.endswith(".png"):
        path = os.path.join(input_folder, file)
        img = Image.open(path)

        w, h = img.size
        new_height = int((target_width / w) * h)

        resized = img.resize((target_width, new_height), Image.LANCZOS)
        resized.save(os.path.join(output_folder, file))

print("Done resizing.")