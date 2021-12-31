import cv2
import numpy as np
import pandas as pd
from PIL import Image #Python Imaging Library


index=["color","color_name","hex","R","G","B"]
csv = pd.read_csv('colors.csv', names=index, header=None)

def getColorName(R,G,B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R- int(csv.loc[i,"R"])) + abs(G- int(csv.loc[i,"G"]))+ abs(B- int(csv.loc[i,"B"]))
        if(d<=minimum):
            minimum = d
            cname = csv.loc[i,"color_name"]
    return cname

def PIX(event, x, y, flags, param):
	if event == cv2.EVENT_LBUTTONDBLCLK:
		r, g, b = rgbimg.getpixel((x,y))
		text =getColorName(r,g,b)+ '\n' +str(r)+","+str(g)+","+str(b)
		bg = np.zeros((200, 400, 3), np.uint8)
		bg[:,0:400] = (b,g,r)
		font = cv2.FONT_ITALIC
		y0, dy = 100, 50
		for i, txt in enumerate(text.split('\n')):
			y = y0+i*dy
			cv2.putText(bg, txt, (10,y), font, 1, (255,255,255), 2, cv2.LINE_AA)
	
		cv2.imshow('rgb',bg)

cap = cv2.VideoCapture(0)
while(True):
    ret, frame = cap.read()   #read
    flipped = cv2.flip(frame, 1) #flip
    cv2.imshow('vid', flipped) #show

    if cv2.waitKey(1) & 0xFF == ord('c'): #press 'c' to capture the
        cv2.imwrite('1.png',flipped)
        imge = Image.open('1.png')
        rgbimg = imge.convert('RGB')
        cv2.imshow('pic',flipped)            
        cv2.setMouseCallback('pic', PIX) #function that captures the current pixel and displays on a window

    elif cv2.waitKey(1) & 0xFF == ord(' '): #hit space to quit
        break
        
cap.release()
cv2.destroyAllWindows()
