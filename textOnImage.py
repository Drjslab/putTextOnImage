from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


def text_wrap(text, font, max_width):
    lines = []
    # If the width of the text is smaller than image width
    # we don't need to split it, just add it to the lines array
    # and return
    if font.getsize(text)[0] <= max_width:
        lines.append(text) 
    else:
        # split the line by spaces to get words
        words = text.split(' ')  
        i = 0
        # append every word to a line while its width is shorter than image width
        while i < len(words):
            line = ''         
            while i < len(words) and font.getsize(line + words[i])[0] <= max_width:                
                line = line + words[i] + " "
                i += 1
            if not line:
                line = words[i]
                i += 1
            # when the line gets longer than the max width do not append the word, 
            # add the line to the lines array
            lines.append(line)    
    return lines

img = Image.open("sample.jpg")
draw = ImageDraw.Draw(img)
W, H = img.size
msg = "The Beaune Altarpiece is a large polyptych altarpiece by the Early Netherlandish artist Rogier van der Weyden. It was commissioned in 1443 for the Hospices de Beaune by Nicolas Rolin, Chancellor of the Duchy of Burgundy, and his wife Guigone de Salins, who was buried in front of the altarpiece. The polyptych consists of fifteen paintings spread across nine panels, of which six are painted on both sides. The inner panels contain scenes from the Last Judgement, with a central image that shows Christ seated in judgement, and the Archangel Michael holding scales as he weighs souls."
font = ImageFont.truetype("ArimaKoshi-Light.otf", 50)
# w1, h1 = draw.textsize(msg, font=font)
lines = text_wrap(msg, font, W)
w, h  = font.getsize('hg')
y = 10
for line in lines:
    # draw the line on the image
    # draw.text((x, y), line, fill=color, font=font)
    w1, h1 = draw.textsize(line, font=font)
    draw.text(((W-w1)/2,y),line,(255,255,255), font=font)
    # update the y position so that we can use it for next line
    y = y + h
# save the image
img.save('sample-out.jpg')
