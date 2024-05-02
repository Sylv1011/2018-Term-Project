import bs4 as bs
import urllib.request
import requests
from tkinter import *
import os
import string
from PIL import Image
from PIL import ImageTk
import planClothes

##sources
#https://www.cs.cmu.edu/~112/notes/notes-oopy-animation.html
#All images of clothes comes from these three websites:
#http://us.topshop.com/?geoip=home
#https://www.farfetch.com/shopping/women/items.aspx
#https://www.net-a-porter.com/us/en/d/Shop/Clothing/All?cm_sp=topnav-_-clothing-_-topbar&pn=1&npp=60&image_view=product&dScroll=0

#Images of backgrounds are:
#https://uigradients.com/#Opa



##Stores all image information here

#backgrounds
background1 = Image.open("bg2.gif")
bg2 = Image.open("images.jpg")
background2 = bg2.resize((1600, 1400), Image.ANTIALIAS)
bg3 = Image.open("bg4.jpg")
background3 = bg3.resize((1600, 1400), Image.ANTIALIAS)
# cl1 = Image.open("icons/drought.png")
# clip1 = cl1.resize((180, 220), Image.ANTIALIAS)

##stores all clothing files
top = "Top.csv"
dress = "dress.csv"
bottom = "bottom.csv"
outwear = "outwear.csv"

##Scrap Weather 
# Web scrap the weather information for the next five days from website and 
# display out.

myurl = urllib.request.urlopen("https://weather.com/weather/5day/l/15289:4:US").read()
#https://weather.com/weather/5day/l/USPA1290:1:US

#https://weather.com/weather/5day/l/15289:4:US
    
soup = bs.BeautifulSoup(myurl, "html.parser")

table = soup.table

table_rows = soup.find_all("tr",class_="clickable closed")

weatherList = ["Weather", "High", "Low", \
"Precipitation","Wind"]

#Function that does basic web scraping and returns a list of date, temperature,
#weather wind and precipitation etc. 
def datesWeather(table_rows):
    dates = []
    for tr in table_rows:
        td = tr.find_all("td")
        row=[i.text for i in td]
        dates += [row[1:]]
    #for better result of display, need to divide into two cases
    for info in dates: 
        info.pop()
        temp = info[2][-3:]
        info.insert(3, temp)
        info[2] = info[2][:-3]
    for info in dates:
        if info[0][-2] not in string.digits:
            info[0]+=" "
    print(dates)
    return dates

######Overall
#Overall calling of the project
######

def init(data):
##data for first UI
    data.mode = "weatherinfo"
    data.image1 = ImageTk.PhotoImage(background1)
    data.margin = data.width/50
    data.gap = data.width/100
    data.weather = datesWeather(table_rows)
    #big rectangle size
    data.recSize = (data.width-2*data.margin)//3
    #big rectangle height
    data.recHei = (0.58)*data.height
    #rectagle coordinate at the margin
    data.reks = Display(data.margin, data.margin)
    #small rectangle size and height
    data.recSmall=(data.width-2*data.margin-data.recSize-2*data.gap)/2
    data.recHmall=(data.recHei-data.gap)/2
    data.text=Texts(data.margin,data.margin)
    data.button1 = Click(data.margin+data.recSize, \
    data.margin+data.recHei+(data.height-data.margin-data.recHei)/4, "coral1")
    data.button2 = Click(data.margin+data.recSize, \
    2*data.margin+data.recHei+(data.height-data.margin-data.recHei)/2, "coral1")
    data.b1text = Texts(data.width/2,data.margin+data.recHei+(data.height-data.margin-data.recHei)/2.7)
    data.text2 =Texts(data.width/2,data.margin)
    # data.clip1 = ImageTk.PhotoImage(clip1)
    
##  #datas for plan for tmr page  
    #clothing lists
    data.topRecom=topList(top,data) #helps another page that shows all selected clothes(image)
    data.topSaved=[]
    print(data.topRecom)
    data.bottomRecom=bottomList(bottom,data)
    print(data.bottomRecom)
    data.bottomSaved=[]
    data.dressRecom=dressList(dress,data)
    print(data.dressRecom)
    data.dressSaved=[]
    data.outwearRecom=outwearList(outwear,data)
    data.outwearSaved=[]
    data.outwearChanged=[]
    
    data.dresses = Recs(data.width/2-data.width/15-data.recSize, data.margin+data.width/13)
    data.outwearC = Recs(data.width/2+data.width/15, data.margin+data.width/13)
    data.text4 = Texts(data.width/2, data.height/9)
    data.image2 = ImageTk.PhotoImage(background2)
    data.topRec = Recs(data.margin+data.gap, data.margin+data.width/13)
    data.bottomRec = Recs(data.gap+2*data.margin+(12/13)*data.recSize, data.margin+data.width/13)
    data.outwearRec = Recs(data.gap+3*data.margin+2*(12/13)*data.recSize, data.margin+data.width/13)
    #two buttons on bottom
    data.plandbutton1 = Buttons(data.gap,data.height-data.gap-data.width/13,\
    "light yellow")
    data.plandbutton2 = Buttons(data.width-data.gap-data.width/6,data.height-data.gap-data.width/13,\
    "light yellow")
    
    #image in the topbox
    data.imagetop=ImageTk.PhotoImage(Top(data.topRecom[0]).top1)
    data.imagebottom=ImageTk.PhotoImage(Bottom(data.bottomRecom[0]).bottom1)
    data.imageoutwear=ImageTk.PhotoImage(Outwear(data.outwearRecom[0]).out1)
    data.imagedress=ImageTk.PhotoImage(Dress(data.dressRecom[0]).dress1)
    data.changeText1 = Decision(data.margin+data.recSize/2,data.margin+data.width/2)
    data.saveText1 = Decision(data.margin+data.recSize/2, data.margin+data.width/8)
    data.changebutton1 = Buttons(data.margin+data.recSize/2,data.margin+data.width/2,"papaya whip")
    data.savebutton1 = Buttons(data.margin+data.recSize/2, data.margin+data.width/8, "papaya whip")
    data.changeText2 = Decision(2*data.margin+data.gap+1.4*data.recSize,data.margin+data.width/2)
    data.saveText2 = Decision(2*data.margin+data.gap+1.4*data.recSize, data.margin+data.width/8)
    data.changebutton2 = Buttons(2*data.margin+data.gap+1.4*data.recSize,data.margin+data.width/2,"papaya whip")
    data.savebutton2 = Buttons(2*data.margin+data.gap+1.4*data.recSize, data.margin+data.width/8, "papaya whip")
    data.changeText3 = Decision(2*data.margin+data.gap+2.37*data.recSize,data.margin+data.width/2)
    data.saveText3 = Decision(2*data.margin+data.gap+2.37*data.recSize, data.margin+data.width/8)
    data.changebutton3 = Buttons(2*data.margin+data.gap+2.37*data.recSize,data.margin+data.width/2,"papaya whip")
    data.savebutton3 = Buttons(2*data.margin+data.gap+2.37*data.recSize, data.margin+data.width/8, "papaya whip")
    data.dress = True
    
    #dress mode buttons
    data.changeText4 = Decision(data.margin+data.gap+0.72*data.recSize,data.margin+data.width/2)
    data.saveText4 = Decision(data.margin+data.gap+0.72*data.recSize, data.margin+data.width/8)
    data.changebutton4 = Buttons(data.margin+data.gap+0.72*data.recSize,data.margin+data.width/2,"papaya whip")
    data.savebutton4 = Buttons(data.margin+data.gap+0.72*data.recSize, data.margin+data.width/8, "papaya whip")
    data.changeText5 = Decision(data.margin+data.gap+2.14*data.recSize,data.margin+data.width/2)
    data.saveText5 = Decision(data.margin+data.gap+2.14*data.recSize, data.margin+data.width/8)
    data.changebutton5 = Buttons(data.margin+data.gap+2.14*data.recSize,data.margin+data.width/2,"papaya whip")
    data.savebutton5 = Buttons(data.margin+data.gap+2.14*data.recSize, data.margin+data.width/8, "papaya whip")

    
## datas for clothes saved page
    data.image3 = ImageTk.PhotoImage(background3)
    data.remove1=Decision(data.margin+data.recSize/2, 4.5*data.margin+data.width/5+data.recHei/2)
    data.remove2=Decision(2*data.margin+data.gap+1.4*data.recSize,4*data.margin+data.width/5+data.recHei/3)
    data.remove3=Decision(2*data.margin+data.gap+2.4*data.recSize, 4.5*data.margin+data.width/5+data.recHei/2)
    data.remove4=Decision(data.margin+0.85*data.recSize, 4.5*data.margin+data.width/5+data.recHei/2)
    data.remove5=Decision(2*data.margin+data.gap+2*data.recSize, 4.5*data.margin+data.width/5+data.recHei/2)
    if len(data.topSaved) != 0:
        data.savedtop=ImageTk.PhotoImage(Top(data.topSaved[0]).top1)
    if len(data.bottomSaved) != 0:
        data.savedbottom=ImageTk.PhotoImage(Bottom(data.bottomSaved[0]).bottom1)
    if len(data.outwearSaved) != 0:
        data.savedoutwear=ImageTk.PhotoImage(Outwear(data.outwearSaved[0]).out1)
    if len(data.dressSaved) != 0:
        data.saveddress=ImageTk.PhotoImage(Dress(data.dressSaved[0]).dress1)

###Overall control of this entire Program
#let user swiches mode and see different UIs
###    
def mousePressed(event, data):
    if data.mode == "weatherinfo": weatherMousePressed(event, data)
    if data.mode == "pland": plandMousePressed(event, data)
    if data.mode == "clothTmr": clothTmrMousePressed(event, data)
    
    
def keyPressed(event, data):
    if data.mode=="weatherinfo": weatherKeyPressed(event, data)
    if data.mode=="pland":plandKeyPressed(event,data)
    if data.mode=="clothTmr":clothTmrKeyPressed(event,data)

def timerFired(data):
    if data.mode=="weatherinfo": weatherTimerFired(data)
    if data.mode=="pland": plandTimerFired(data)
    if data.mode=="clothTmr":clothTmrTimerFired(data)
    
def redrawAll(canvas,data):
    if data.mode=="weatherinfo":weatherRedrawAll(canvas, data)
    if data.mode=="pland": plandRedrawAll(canvas, data)
    if data.mode=="clothTmr": clothTmrRedrawAll(canvas, data)
    
    
    
###first page
#weather info mode
###    

##Defines elements of the main window (Animation using tkinter)

#setting a start page with different features

#a class that create different instances that gets displayed on this page
class Display(object):
    
    #set coordinates for windows of displaying weather
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    #draws five rectangles that displays weather
    def draw(self, data, canvas):
        canvas.create_rectangle(self.x,self.y,self.x+data.recSize,self.y+data.recHei,\
        fill="mint cream")
        x1=self.x+data.recSize+data.gap
        y1=self.y
        x2=x1+data.recSmall
        y2=y1+data.recHmall
        canvas.create_rectangle(x1,y1,x2,y2,fill="mint cream")
        canvas.create_rectangle(x2+data.gap,y1,x2+data.gap+data.recSmall,\
        y2,fill="mint cream")
        canvas.create_rectangle(x1,y2+data.gap,x2,y2+data.gap+data.recHmall,\
        fill="mint cream")
        canvas.create_rectangle(x2+data.gap,y2+data.gap,x2+data.gap+data.recSmall,\
        y2+data.gap+data.recHmall,fill="mint cream")
    
    #draw background
    def backDraw(self, data, canvas):
        pass

#draws the buttons to switch another interface 
class Click(Display):
    
    def __init__(self, x, y, color):
        super().__init__(x,y)
        self.color = color
        
    def draw(self, data, canvas):
        length = (1/3)*data.width
        height = (data.height-data.margin-data.recHei)/4
        canvas.create_rectangle(self.x, self.y,self.x+length,\
        self.y+height, fill=self.color)
    
                
#puts the weather information into the correponsing box
class Texts(Display):
    
    def draw1(self, data, canvas):
        temp1=data.weather[0][0]
        if "\n" in temp1:
            temps=temp1.replace("\n", " ")
        else:
            temps = temp1[:-6]+" "+temp1[-6:]
        canvas.create_text(self.x+data.recSize/2, self.y+data.recHei/10,\
        text="%s"% temps, font="Chaparral 25")
        for i in range (5):
            if len(data.weather[0][i+1])<=13:
                canvas.create_text(self.x+data.recSize/2, self.y+data.recHei/4+i*data.recHei/8, \
                text = "%s: %s" % (weatherList[i], data.weather[0][i+1]), \
                font="Courier 19")
            else: #in case the string is too long
                canvas.create_text(self.x+data.recSize/2, self.y+data.recHei/4+i*data.recHei/8, \
                text = "%s: %s" % (weatherList[i], (data.weather[0][i+1].split(" "))[0]), \
                font="Courier 19")
                
    def draw2(self, data, canvas):
        height = (data.height-data.margin-data.recHei)/4
        canvas.create_text(self.x, self.y, text="Plan for Tomorrow", \
        font="Delevane 20 italic")
        canvas.create_text(self.x, self.y+\
        (data.height-data.margin-data.recHei)/3.2, \
        text="See your style today",font="Delevane 20 italic")
    
    #diaplays the next four dates
    def draw3(self, data, canvas):
        height = (data.height-data.margin-data.recHei)/4
        for i in range (4):
            temp1=data.weather[i+1][0]
            if "\n" in temp1:
                temps=temp1.replace("\n", " ")
            else:
                temps = temp1[:3]+" "+temp1[3:]
            if i < 2:
                canvas.create_text(self.x+i*data.recSize, self.y+data.recHei/14,\
                text="%s"% temps, font="Amazone 20 italic")
            else:
                canvas.create_text(self.x+(i-2)*data.recSize, self.y+data.recHei/4+2*height,\
                text="%s"% temps, font="Amazone 20 italic")
    
    #displays weather for the next four days
    def draw4(self, data, canvas):
        for i in range (3):
            canvas.create_text(self.x, self.y+i*2*data.margin,\
            text = "%s: %s" % (weatherList[i], data.weather[1][i+1]), font="Courier 17")
            canvas.create_text(self.x+data.recSize, self.y+i*2*data.margin,\
            text = "%s: %s" % (weatherList[i], data.weather[2][i+1]), font="Courier 17")
            canvas.create_text(self.x, self.y+data.recHmall+data.gap+i*2*data.margin,\
            text = "%s: %s" % (weatherList[i], data.weather[3][i+1]), font="Courier 17")
            canvas.create_text(self.x+data.recSize, self.y+data.recHmall+data.gap+i*2*data.margin,\
            text = "%s: %s" % (weatherList[i], data.weather[4][i+1]), font="Courier 17")       
    
##Draws the main window

def weatherKeyPressed(event,data):
    pass

#creates the effect of instant click and changes back color
def weatherTimerFired(data):
    if data.button1.color == "firebrick":
        data.button1.color = "coral1"
    elif data.button2.color == "firebrick":
        data.button2.color = "coral1"
    
#clicking event only happens on two rectangles
def weatherMousePressed(event, data):
    length = (1/3)*data.width
    height = (data.height-data.margin-data.recHei)/4
    ypos = data.margin+data.recHei+(data.height-data.margin-data.recHei)/4
    if data.button1.x<= event.x <= event.x+length and \
    (data.button1.y<=event.y<=data.button1.y+height):
        data.button1.color = "firebrick"
        data.mode = "pland"
    elif data.button2.x<= event.x <= event.x+length and \
    data.button2.y<=event.y<=data.button2.y+height:
        data.button2.color = "firebrick"
        #call on to another interface

def weatherRedrawAll(canvas, data):
    canvas.create_image(0,0, image=data.image1)
    data.reks.draw(data,canvas)
    data.button1.draw(data,canvas)
    data.button2.draw(data,canvas)
    data.b1text.draw2(data,canvas)
    data.text.draw1(data,canvas)
    data.text2.draw3(data,canvas)
    data.text4.draw4(data,canvas)
    #canvas.create_image(data.width/6,data.height/6, image=data.clip1)
    

###Second page
#plan display mode
###    

##Calls the machine learning functions
#Modifies the csv file so that we can get first step of recommendation
def modTop(filename, data):
    dataset=planClothes.test_num(6,planClothes.numCSV(filename))
    #Split clothes based on the feature and weather
    if int(data.weather[1][3][:-1])>=68:
        for tops in dataset[0]:
            planClothes.writeFile1(filename,tops[0],8,"Recommend")
        for tops in dataset[1]:
            planClothes.writeFile1(filename,tops[0],8,"No")
    else:
        for tops in dataset[0]:
            planClothes.writeFile1(filename,tops[0],8,"No")
        for tops in dataset[1]:
            planClothes.writeFile1(filename,tops[0],8,"Recommend")

#get a list of top that is recommended in the first step so that we can store
#in init
def topList(filename,data):
    modTop(filename, data)
    #make prediction from ML algorithm
    tl = planClothes.load_csv(filename)
    result=[]
    for tops in tl:
        if tops[-1] == "Recommend":
            result.append(tops[0])
    return result

#manually divides bottoms to be short and long so that 
#different temperature yields different result
def modBottom(filename,data):
    dataset=planClothes.test_num(1,planClothes.numCSV(filename))
    if int(data.weather[1][3][:-1])>68:
        for tops in dataset[0]:
            planClothes.writeFile2(filename,tops[0],7,"Recommend")
        for tops in dataset[1]:
            planClothes.writeFile2(filename,tops[0],7,"No")
    else:
        for tops in dataset[0]:
            planClothes.writeFile2(filename,tops[0],7,"No")
        for tops in dataset[1]:
            planClothes.writeFile2(filename,tops[0],7,"Recommend")

#ADDS all available bottoms into a list for rec            
def bottomList(filename,data):
    modBottom(filename,data)
    bl = planClothes.load_csv(filename)
    result=[]
    for bottoms in bl:
        if bottoms[-1] == "Recommend":
            result.append(bottoms[0])
    return result

#samething for outwear
def modOutwear(filename,data):
    dataset=planClothes.test_num(1,planClothes.numCSV(filename))
    if int(data.weather[1][2][:-1])>50 and int(data.weather[1][3][:-1])>43:
        for outs in dataset[0]:
            planClothes.writeFile3(filename,outs[0],6,"Recommend")
        for outs in dataset[1]:
            planClothes.writeFile3(filename,outs[0],6,"No")
    else:
        for outs in dataset[0]:
            planClothes.writeFile3(filename,outs[0],6,"No")
        for outs in dataset[1]:
            planClothes.writeFile3(filename,outs[0],6,"Recommend")
            
def outwearList(filename,data):
    modOutwear(filename,data)
    ol = planClothes.load_csv(filename)
    result=[]
    for outs in ol:
        if outs[-1] == "Recommend":
            result.append(outs[0])
    return result

def modDress(filename,data):
    dataset=planClothes.test_num(1,planClothes.numCSV(filename))
    if int(data.weather[1][3][:-1])>74:
        for tops in dataset[0]:
            planClothes.writeFile2(filename,tops[0],6,"Recommend")
        for tops in dataset[1]:
            planClothes.writeFile2(filename,tops[0],6,"No")
    else:
        for tops in dataset[0]:
            planClothes.writeFile2(filename,tops[0],6,"No")
        for tops in dataset[1]:
            planClothes.writeFile2(filename,tops[0],6,"Recommend")
            
def dressList(filename,data):
    modDress(filename,data)
    dl = planClothes.load_csv(filename)
    result=[]
    for dress in dl:
        if dress[-1] == "Recommend":
            result.append(dress[0])
    return result
##Display interface
#clothing suggestions on the interface by uploading different images

class Recs(object):
    
    #draws boxes to diaplay recommendation based on temperature
    def __init__(self, x,y):
        self.x=x
        self.y=y
        
    def draw(self, canvas, data):
        canvas.create_rectangle(self.x, self.y,self.x+(12/13)*data.recSize,self.y+data.recHei, fill="lavender blush")
        
class Buttons(object):
    
    def __init__(self,x,y,color):
        self.x=x
        self.y=y
        self.color=color
    
    def draw(self,canvas,data):
        canvas.create_rectangle(self.x,self.y,self.x+data.width/8,\
        self.y+data.width/13, fill=self.color)
    
    #save and change button
    def create(self,canvas,data):
        canvas.create_rectangle(self.x-data.recSize/6,self.y-data.recHei/22,self.x+data.recSize/6,\
        self.y+data.recHei/22, fill=self.color)
    
    #plan button right bottom
    def plan(self,canvas,data):
        canvas.create_rectangle(self.x,self.y,self.x+data.width/6,\
        self.y+data.width/13, fill=self.color)

#Create classes to process images so that user can change image on the screen
class Top(object):
    
    def __init__(self, name):
        self.name=name
        self.path = "Clothing/Tops/"+self.name+".jpg"
        self.tp1 = Image.open(self.path)
        self.top1 = self.tp1.resize((180,220), Image.ANTIALIAS)
    
class Bottom(object):
    
    def __init__(self, name):
        self.name=name
        self.path = "Clothing/Bottoms/"+self.name+".jpg"
        self.bt1 = Image.open(self.path)
        self.bottom1 = self.bt1.resize((180,220), Image.ANTIALIAS)
        
class Outwear(object):
    
    def __init__(self, name):
        self.name=name
        self.path = "Clothing/Outwear/"+self.name+".jpg"
        self.o1 = Image.open(self.path)
        self.out1 = self.o1.resize((180,220), Image.ANTIALIAS)
    
class Dress(object):
    
    def __init__(self, name):
        self.name=name
        self.path = "Clothing/Dresses/"+self.name+".jpg"
        self.dr1 = Image.open(self.path)
        self.dress1 = self.dr1.resize((180,220), Image.ANTIALIAS)
    
class Decision(object):
    #texts for option save or change
    def __init__(self, x, y):
        self.x=x
        self.y=y
        
    def change(self, canvas, data):
        canvas.create_text(self.x,self.y, text="change",font="Courier 20 italic")
        
    def save(self, canvas, data):
        canvas.create_text(self.x,self.y, text="save",font="Courier 20 italic")
        
    def remove(self, canvas, data):
        canvas.create_text(self.x,self.y, text="remove",font="Courier 24 italic")

        
##Second page draws        
    
    
def plandKeyPressed(event,data):
    pass
    
def plandMousePressed(event, data):
    if data.gap<=event.x<=data.gap+data.width/8 and \
    data.height-data.gap-data.width/13<=event.y<=data.height-data.gap:
        data.plandbutton1.color="SeaGreen1"
        data.mode = "weatherinfo"
    if data.width-data.gap-data.width/6<=event.x<=data.width-data.gap and\
    data.height-data.gap-data.width/13<=event.y<=data.height-data.gap:
        data.mode = "clothTmr"
    
    if int(data.weather[1][2][:-1])>=68 and data.dress==True:
        if data.margin+data.gap+0.72*data.recSize-data.recSize/6<=event.x<=data.margin+data.gap+0.72*data.recSize+data.recSize/6 and \
        data.margin+data.width/2-data.recHei/22<=event.y<=data.margin+data.width/2+data.recHei/22:
            data.dressRecom.append(data.dressRecom.pop(0))
            planClothes.writeFile2(dress,data.dressRecom[0],5,"change")
        if data.margin+data.gap+0.72*data.recSize-data.recSize/6<=event.x<=data.margin+data.gap+0.72*data.recSize+data.recSize/6 and \
        data.margin+data.width/8-data.recHei/22<=event.y<=data.margin+data.width/8+data.recHei/22:
            if data.dressSaved==[]:
                data.dressSaved.append(data.dressRecom[0])
                planClothes.writeFile2(dress,data.dressRecom[0],5,"save")
        if data.margin+data.gap+2.14*data.recSize-data.recSize/6<=event.x<=data.margin+data.gap+2.14*data.recSize+data.recSize/6 and \
        data.margin+data.width/2-data.recHei/22<=event.y<=data.margin+data.width/2+data.recHei/22:
            data.outwearRecom.append(data.outwearRecom.pop(0))
            planClothes.writeFile3(outwear,data.outwearRecom[0],5,"change")
        if data.margin+data.gap+2.14*data.recSize-data.recSize/6<=event.x<=data.margin+data.gap+2.14*data.recSize+data.recSize/6 and \
        data.margin+data.width/8-data.recHei/22<=event.y<=data.margin+data.width/8+data.recHei/22:
            if data.outwearSaved==[]:
                data.outwearSaved.append(data.outwearRecom[0])
                planClothes.writeFile3(outwear,data.outwearRecom[0],5,"save")
        
        if data.width/2-data.recSize/2<=event.x<=data.width/2+data.recSize/2 and\
         data.height-7*data.margin-data.recSize/8<=event.y<=data.height-7*data.margin+data.recSize/8:
             data.dress = False
    
    else:    
        #change for top clothes
        if data.margin+data.recSize/2-data.recSize/6<=event.x<=data.margin+data.recSize/2+data.recSize/6 and\
        data.margin+data.width/2-data.recHei/22<=event.y<=data.margin+data.width/2+data.recHei/22:
            data.topRecom.append(data.topRecom.pop(0))
            #edit the file about the decision
            planClothes.writeFile1(top,data.topRecom[0],7,"change")
        if data.margin+data.recSize/2-data.recSize/6<=event.x<=data.margin+data.recSize/2+data.recSize/6 and\
        data.margin+data.width/8-data.recHei/22<=event.y<=data.margin+data.width/8+data.recHei/22:
            if data.topSaved==[]:
                data.topSaved.append(data.topRecom[0])
                planClothes.writeFile1(top,data.topRecom[0],7,"save")
                
        #change for bottom clothes
        if 2*data.margin+data.gap+1.4*data.recSize-data.recSize/6<=event.x<=2*data.margin+data.gap+1.4*data.recSize+data.recSize/6 and\
        data.margin+data.width/2-data.recHei/22<=event.y<=data.margin+data.width/2+data.recHei/22:
            data.bottomRecom.append(data.bottomRecom.pop(0))
            planClothes.writeFile2(bottom,data.bottomRecom[0],6,"change")
        if 2*data.margin+data.gap+1.4*data.recSize-data.recSize/6<=event.x<=2*data.margin+data.gap+1.4*data.recSize+data.recSize/6 and\
        data.margin+data.width/8-data.recHei/22<=event.y<=data.margin+data.width/8+data.recHei/22:
            if data.bottomSaved==[]:
                data.bottomSaved.append(data.bottomRecom[0])
                planClothes.writeFile2(bottom,data.bottomRecom[0],6,"save")

    #change for outwear clothes
        if 2*data.margin+data.gap+2.37*data.recSize-data.recSize/6<=event.x<=2*data.margin+data.gap+2.37*data.recSize+data.recSize/6 and\
        data.margin+data.width/2-data.recHei/22<=event.y<=data.margin+data.width/2+data.recHei/22:
            data.outwearRecom.append(data.outwearRecom.pop(0))
            planClothes.writeFile3(outwear,data.outwearRecom[0],5,"change")
            planClothes.writeFile3(outwear,data.outwearRecom[0],6,"No")
            # if data.outwearRecom != []:
            #     data.outwearChanged.append(data.outwearRecom.pop(0))
            #     print(data.outwearRecom)
        if 2*data.margin+data.gap+2.37*data.recSize-data.recSize/6<=event.x<=2*data.margin+data.gap+2.37*data.recSize+data.recSize/6 and\
        data.margin+data.width/8-data.recHei/22<=event.y<=data.margin+data.width/8+data.recHei/22:
            if data.outwearSaved==[]:
                data.outwearSaved.append(data.outwearRecom[0])
                planClothes.writeFile3(outwear,data.outwearRecom[0],5,"save")
    

def plandTimerFired(data):
    if data.plandbutton1.color=="SeaGreen1":
        data.plandbutton1.color = "light yellow"
    
def plandRedrawAll(canvas, data):
    data.imagetop=ImageTk.PhotoImage(Top(data.topRecom[0]).top1)
    data.imagebottom=ImageTk.PhotoImage(Bottom(data.bottomRecom[0]).bottom1)
    data.imageoutwear=ImageTk.PhotoImage(Outwear(data.outwearRecom[0]).out1)
    data.imagedress=ImageTk.PhotoImage(Dress(data.dressRecom[0]).dress1)
    canvas.create_image(0,0,image=data.image2)
    #divide into cases of the recommendations
    if int(data.weather[1][2][:-1])>=68 and data.dress==True: 
        data.dresses.draw(canvas,data)
        data.outwearC.draw(canvas,data)
        canvas.create_image(data.margin+data.gap+0.72*data.recSize,data.margin+data.width/13+data.recHei/2, image=data.imagedress)
        canvas.create_image(data.margin+data.gap+2.14*data.recSize,data.margin+data.width/13+data.recHei/2, image=data.imageoutwear)
        data.changebutton4.create(canvas,data)
        data.savebutton4.create(canvas,data)
        data.changeText4.change(canvas,data)
        data.saveText4.save(canvas,data)
        data.changebutton5.create(canvas,data)
        data.savebutton5.create(canvas,data)
        data.changeText5.change(canvas,data)
        data.saveText5.save(canvas,data)
        canvas.create_rectangle(data.width/2-data.recSize/2, data.height-7*data.margin-data.recSize/8,\
        data.width/2+data.recSize/2, data.height-7*data.margin+data.recSize/8,fill = "MistyRose2")
        canvas.create_text(data.width/2,data.height-7*data.margin,text="No Dresses! Tops!", font= "Helvatica 22 italic")
    else:
        data.topRec.draw(canvas, data)
        data.bottomRec.draw(canvas, data)
        data.outwearRec.draw(canvas, data)
        #images of top, bottom and outwear
        canvas.create_image(data.margin+data.recSize/2, data.margin+data.width/13+data.recHei/2,image=data.imagetop)
        canvas.create_image(2*data.margin+data.gap+1.4*data.recSize, data.margin+data.width/13+data.recHei/2,image=data.imagebottom)
        canvas.create_image(2*data.margin+data.gap+2.37*data.recSize,data.margin+data.width/13+data.recHei/2, image=data.imageoutwear)
        data.changebutton1.create(canvas,data)
        data.savebutton1.create(canvas,data)
        data.changeText1.change(canvas,data)
        data.saveText1.save(canvas,data)
        data.changebutton2.create(canvas,data)
        data.savebutton2.create(canvas,data)
        data.changeText2.change(canvas,data)
        data.saveText2.save(canvas,data)
        data.changebutton3.create(canvas,data)
        data.savebutton3.create(canvas,data)
        data.changeText3.change(canvas,data)
        data.saveText3.save(canvas,data)
        
    #button for back to first page
    data.plandbutton1.draw(canvas,data)
    data.plandbutton2.plan(canvas,data)
    #fills in the text for the button
    canvas.create_text(data.gap+data.width/16,data.height-data.gap-data.width/26,\
    text="Back",font="Hevetica 18 bold")
    canvas.create_text(data.width-data.gap-data.width/12,data.height-data.gap-data.width/26,\
    text="Your plan",font="Hevetica 18 bold")
    canvas.create_text(data.width/2, (data.margin+data.width/13)/2, \
    text="Tomorrow: %s ~ %s" %(data.weather[1][3],data.weather[1][2]), font="Comic 20 bold")

###Page for clothes have already planned

    
def clothTmrKeyPressed(event,data):
    pass
    
def clothTmrMousePressed(event,data):
    if data.gap<=event.x<=data.gap+data.width/8 and \
    data.height-data.gap-data.width/13<=event.y<=data.height-data.gap:
        data.mode = "pland"
    
        
    if int(data.weather[1][2][:-1])>=68 and data.dress==True:
        if data.margin+0.85*data.recSize-data.recSize/6<=event.x<=data.margin+0.85*data.recSize+data.recSize/6 and\
        4.5*data.margin+data.width/5+data.recHei/2-data.recHei/22<=event.y<=4.5*data.margin+data.width/5+data.recHei/2+data.recHei/22:
            data.dressSaved.pop()
        if 2*data.margin+data.gap+2*data.recSize-data.recSize/6<=event.x<=2*data.margin+data.gap+2*data.recSize+data.recSize/6 and \
        4.5*data.margin+data.width/5+data.recHei/2-data.recHei/22<=event.y<=4.5*data.margin+data.width/5+data.recHei/2+data.recHei/22:
            data.outwearSaved.pop()
            
    else:
        if data.margin+data.recSize/2-data.recSize/6<=event.x<=data.margin+data.recSize/2+data.recSize/6 and \
        4.5*data.margin+data.width/5+data.recHei/2-data.recHei/22<=event.y<=4.5*data.margin+data.width/5+data.recHei/2+data.recHei/22:
            data.topSaved.pop()
        if 2*data.margin+data.gap+1.4*data.recSize-data.recSize/6<=event.x<=2*data.margin+data.gap+1.4*data.recSize+data.recSize/6 and \
        4*data.margin+data.width/5+data.recHei/3-data.recHei/22<=event.y<=4*data.margin+data.width/5+data.recHei/3+data.recHei/22:
            data.bottomSaved.pop()
        if 2*data.margin+data.gap+2.4*data.recSize-data.recSize/6<=event.x<=2*data.margin+data.gap+2.4*data.recSize+data.recSize/6 and \
        4.5*data.margin+data.width/5+data.recHei/2-data.recHei/22<=event.y<=4.5*data.margin+data.width/5+data.recHei/2+data.recHei/22:
            data.outwearSaved.pop()
            
def clothTmrTimerFired(data):
    pass
    
def clothTmrRedrawAll(canvas,data):
    canvas.create_image(0,0, image=data.image3)
    data.plandbutton1.draw(canvas,data)
    canvas.create_text(data.gap+data.width/16,data.height-data.gap-data.width/26,\
    text="Back",font="Hevetica 18 bold")
    canvas.create_text(data.width/2,data.gap+3*data.margin, text="Your Style For Tomorrow: ", font="Courier 28 bold")

            
    if int(data.weather[1][2][:-1])>=68 and data.dress==True:
        if len(data.dressSaved) != 0:
            data.saveddress=ImageTk.PhotoImage(Dress(data.dressSaved[0]).dress1)
            canvas.create_image(data.margin+0.85*data.recSize, data.margin+data.width/10+data.recHei/2,image=data.saveddress)
            data.remove4.remove(canvas,data)
        if len(data.outwearSaved) != 0:
            data.savedoutwear=ImageTk.PhotoImage(Outwear(data.outwearSaved[0]).out1)
            canvas.create_image(2*data.margin+data.gap+2*data.recSize, data.margin+data.width/10+data.recHei/2,image=data.savedoutwear)
            data.remove5.remove(canvas,data)
        
        if len(data.outwearSaved)==0 and len(data.dressSaved)==0:
            canvas.create_text(data.width/2,data.height/2, text="You have nothing planned for tomorrow yet:(", font = "Courier 30")
            
    #if anything's saved, they all get displayed onto the page
    else:
        if len(data.topSaved) != 0:
            data.savedtop=ImageTk.PhotoImage(Top(data.topSaved[0]).top1)
            canvas.create_image(data.margin+data.recSize/2, data.margin+data.width/10+data.recHei/2,image=data.savedtop)
            data.remove1.remove(canvas,data)

        if len(data.bottomSaved) != 0:
            data.savedbottom=ImageTk.PhotoImage(Bottom(data.bottomSaved[0]).bottom1)
            canvas.create_image(2*data.margin+data.gap+1.4*data.recSize, data.margin+data.width/13+data.recHei/3,image=data.savedbottom)
            data.remove2.remove(canvas,data)

        if len(data.outwearSaved) != 0:
            data.savedoutwear=ImageTk.PhotoImage(Outwear(data.outwearSaved[0]).out1)
            canvas.create_image(2*data.margin+data.gap+2.4*data.recSize, data.margin+data.width/10+data.recHei/2,image=data.savedoutwear)
            data.remove3.remove(canvas,data)
            
        if len(data.outwearSaved)==0 and len(data.bottomSaved)==0 and len(data.topSaved)==0:
            canvas.create_text(data.width/2,data.height/2, text="You have nothing planned for tomorrow yet:(", font = "Courier 30")
        
    
####################################
# Code from 15-112 website but change the GUI a bit with window location and name
####################################
#following functions all from course website
def run(width=800, height=650):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    root = Tk()
    
    #GUI name of the window
    root.title("PittWear")
    
    w = 800 #width for tk root
    h = 650 #width for tk height
    
    #get screen width and height
    ws = root.winfo_screenwidth()#width
    hs = root.winfo_screenheight()#height
    
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run()
