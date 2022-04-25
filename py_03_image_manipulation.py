from PIL import Image, ImageFilter

# ========== Resize Image Start ========== #
img = Image.open('images/img_in/git_01.jpeg')
resize = img.resize((200, 300))
resize.save('images/img_out/resize_output.jpeg')
# ========== Resize Image End ========== #
# ========== Blur Image Start ========== #
img = Image.open('images/img_in/git_00.jpg')
blur = img.filter(ImageFilter.BLUR)
blur.save('images/img_out/blur_output.jpg')
# ========== Blur Image End ========== #
# ========== Sharp Image Start ========== #
img = Image.open('images/img_in/git_01.jpeg')
sharp = img.filter(ImageFilter.SHARPEN)
sharp.save('images/img_out/sharp_output.jpeg')
# ========== Sharp Image End ========== #
# ========== Crop Image Start ========== #
img = Image.open('images/img_in/python_00.jpg')
crop = img.crop((550, 550, 850, 850))
crop.save('images/img_out/crop_output.jpg')
# ========== Crop Image End ========== #
# ========== Rotate Image Start ========== #
img = Image.open('images/img_in/python_01.png')
rotate = img.rotate(90)
rotate.save('images/img_out/rotate_output.png')
# ========== Rotate Image End ========== #
# ========== Flip Image Start ========== #
img = Image.open('images/img_in/python_01.png')
flip = img.transpose(Image.FLIP_LEFT_RIGHT)
flip.save('images/img_out/flip_output.png')
# ========== Flip Image End ========== #
# ========== Transpose Image Start ========== #
img = Image.open('images/img_in/git_01.jpeg')
transpose = img.transpose(Image.TRANSPOSE)
transpose.save('images/img_out/transpose_output.jpeg')
# ========== Transpose Image End ========== #
# ========== Convert Image to GreyScale Start ========== #
img = Image.open('images/img_in/git_00.jpg')
convert = img.convert('L')
convert.save('images/img_out/convert_output.jpg')
# ========== Convert Image to GreyScale End ========== #
