from PIL import Image
file_path = input("Enter the image path:")
img = Image.open(file_path)

if file_path.split('.')[1] == 'png':
    img = img.convert('RGB')

amount = int(input("Enter the compress factor:"))
height, width = img.size
new_size = int(width // amount), int(height // amount)
compressed = img.resize(new_size,Image.ANTIALIAS)
compressed.save("compressed.jpg", optimize=True, quality=95)
