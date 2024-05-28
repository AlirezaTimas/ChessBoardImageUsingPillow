from PIL import Image, ImageDraw

size = (256, 256) #size image


img = Image.new("RGB", size, "white") #image ba background sefid
draw = ImageDraw.Draw(img)

square_size = 32 #size har khoone safhe (pixel)
width, height = img.size

#code rasm chessboard :
for i in range(0, width, square_size * 2):
    for j in range(0, height, square_size * 2):
        draw.rectangle([i, j, i + square_size, j + square_size], fill='black')
        draw.rectangle([i + square_size, j + square_size, i +(square_size*2), j + (square_size*2)], fill='black')

img.save("chess_board.png")
img = Image.open("chess_board.png")
img.show()

