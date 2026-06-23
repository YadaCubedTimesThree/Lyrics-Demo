#yadayadayada_
#slow and easy, thats the way i like it

# imports
from tkinter import *
from pygame import *

mixer.init()
mixer.music.load("paano_ka_ba.mp3")
mixer.music.play(loops=0)

# functions

def typeText(lyric, i, label):
    
    if i <= len(lyric):
        label.config(text=lyric[:i])
        firstLyric.after(33, lambda: typeText(lyric, i + 1, label))
        
def deleteWindow(window, x, y):
    
    if x >= 100 and y >= 100:
        x -= 10
        y -= 10
        window.geometry(f'{x}x{y}')
        
        window.after(1, lambda: deleteWindow(window, x, y))
        
    else:
        window.withdraw()
        
def moveLyric4(xPos):
    
    yPos = 100
      
    # Set up the third lyric window or whatever
    fourthLyric.geometry(f'500x500+{xPos}+{yPos}')
    fourthLyric.title('Paano Ka Ba? - Hev Abi')
    fourthLyric.config(bg='black')
    fourthLyric.lift()
    
  
    
    if xPos < 800:
        
        fourthLyric.geometry(f'500x500+{xPos}+{yPos}')
        xPos += 4
        
        fourthLyric.after(5, lambda: moveLyric4(xPos))
    
    else:
        
        # delete self
        fourthLyric.after(300, lambda: deleteWindow(fourthLyric, 500, 500))

        
def moveLyric3(xPos):
    
    yPos = 100
      
    # Set up the third lyric window or whatever
    thirdLyric.geometry(f'500x500+{xPos}+{yPos}')
    thirdLyric.title('Paano Ka Ba? - Hev Abi')
    thirdLyric.config(bg='black')
    thirdLyric.lift()
    
  
    
    if xPos > 100:
        
        thirdLyric.geometry(f'500x500+{xPos}+{yPos}')
        xPos += -4
        
        thirdLyric.after(5, lambda: moveLyric3(xPos))
    
    else:
        
        # delete self
        thirdLyric.after(100, lambda: deleteWindow(thirdLyric, 500, 500))
        
        thirdLyric.after(600, lambda: moveLyric4(-200))
        
        
def moveLyric2(yPos):
    xPos = 120
        
    # Set up the second lyric window or whatever
    secondLyric.geometry(f'500x500+{xPos}+{yPos}')
    secondLyric.title('Paano Ka Ba? - Hev Abi')
    secondLyric.config(bg='black')
    secondLyric.lift()
    

    
    if yPos > 75:
        
        secondLyric.geometry(f'500x500+{xPos}+{yPos}')
        yPos += -4
        
        secondLyric.after(5, lambda: moveLyric2(yPos))
    
    else:
        
        # delete self
        secondLyric.after(500, lambda: deleteWindow(secondLyric, 500, 500))
        
        secondLyric.after(1000, lambda: moveLyric3(1400))
        
    

def moveLyric1(yPos):
    
    xPos = 600

    if yPos < 200:
        
        firstLyric.geometry(f'500x500+{xPos}+{yPos}')
        yPos += 2
        
        firstLyric.after(5, lambda: moveLyric1(yPos))
    
    else:
        
        # delete self
        firstLyric.after(100, lambda: deleteWindow(firstLyric, 500, 500))
        
        firstLyric.after(350, lambda: moveLyric2(900))
        
# Set up the first lyric
firstLyric = Tk()
firstLyric.geometry(f'500x500+600+-50')
firstLyric.overrideredirect(True)
firstLyric.config(bg='black')


# Set up the second lyric
secondLyric = Toplevel()
secondLyric.geometry('500x500+200+1000')
secondLyric.overrideredirect(True)
secondLyric.config(bg='black')

# Set up the third lyric
thirdLyric = Toplevel()
thirdLyric.geometry('500x500+200+1000')
thirdLyric.overrideredirect(True)
thirdLyric.config(bg='black')

# Set up the fourth lyric
fourthLyric = Toplevel()
fourthLyric.geometry('500x500+200+1000')
fourthLyric.overrideredirect(True)
fourthLyric.config(bg='black')
    
# lyrics

lyric1 = Label(firstLyric, text="""""",
fg='white',
bg='black',
font=('Helvetica', 40, "bold"),
justify=LEFT, 
anchor="w"
)

lyric1.place(x=75, y=150)

lyric2 = Label(secondLyric, text="""""",
fg='white',
bg='black',
font=('Helvetica', 40, "bold"),
justify=LEFT, 
anchor="w"  
)
lyric2.place(x=75, y=125)

lyric3 = Label(thirdLyric, text="""""",
fg='white',
bg='black',
font=('Helvetica', 40, "bold"),
justify=LEFT, 
anchor="w"  
)
lyric3.place(x=25, y=125)

lyric4 = Label(fourthLyric, text="""""",
fg='white',
bg='black',
font=('Helvetica', 40, "bold"),
justify=LEFT, 
anchor="w"  
)
lyric4.place(x=25, y=125)

# run the func!!
moveLyric1(-50)

firstLyric.after(0, lambda: typeText("ANO, GANITO\nNALANG BA", 0, lyric1))
firstLyric.after(1700, lambda: typeText("LAGING\nNAKAKALITO\nANG AMBA", 0, lyric2))
firstLyric.after(3600, lambda: typeText("'DI MALAMAN\nANG GUSTO MO\nNA PALABASIN", 0, lyric3))
firstLyric.after(5800, lambda: typeText("LAGI NALANG\nNAIIWAN NA\nNAGTATAKA", 0, lyric4))

firstLyric.mainloop()