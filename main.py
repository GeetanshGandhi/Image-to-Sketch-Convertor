"""
Project: Image to Sketch conversion
Author: Geetansh Gandhi
Enrollment number: 0801CS221058
"""
import PIL.Image
import PIL.ImageTk
import cv2
from tkinter import Entry, Label, Button
from tkinter import Canvas
from tkinter import Tk, Toplevel
from tkinter import font
from datetime import datetime

class SketchMaker:
    location = str()
    name = str()
    sketchScale = 256.0
    #constructor to initialise location and name of image
    def __init__(self, location, name):
        self.location = location
        self.name = name
    #function to convert an image to sketch
    def convertToSketch(self):
        complete_location = self.location+"\\"+self.name
        initial_img = cv2.imread(complete_location)
        grayscale = cv2.cvtColor(initial_img, cv2.COLOR_BGR2GRAY)
        inversion1 = 255-grayscale
        gaussBlur = cv2.GaussianBlur(inversion1, (21,21), 0)
        inversion2 = 255-gaussBlur
        sketched_image = cv2.divide(grayscale, inversion2, scale = self.sketchScale)
        resized_instance = cv2.resize(sketched_image, (800,550))
        self.displayImage(resized_instance)
    #function to view original image
    def viewOriginal(self):
        complete_location = self.location+"\\"+self.name
        original_instance = cv2.imread(complete_location)
        resized_instance = cv2.resize(original_instance,(800,550))
        self.displayImage(resized_instance)
    #function to display image(both kinds)
    def displayImage(self, imageInstance):
        cv2.imshow("Output Image", imageInstance)
        cv2.waitKey(0)

class Interface:
    algorithm = ["The image is first converted to grayscale format.",
                "The image is masked so that original properties are restored.",
                "The image contrast is increased by the gaussian blur function.",
                "The image is unmasked to retain original properties.",
                "The image is resized to 800x550 px format."]
    #function to view algorithm
    def viewAlgorithm(self):
        #defining tkinter window
        algoWindow = Toplevel()
        algoWindow.configure(bg = "black")
        algoWindow.geometry("700x300")
        algoWindow.title("Conversion Algorithm")
        algoWindow.resizable(False,False)
        width = 700
        height = 300
        cAlign = width//2
        # defining canvas over window
        canvas = Canvas(algoWindow, width=700, height=300, highlightthickness=0)
        canvas.pack(fill="both", expand=True)
        # adding background to canvas
        imageLocation = "background_img.jpg"
        img_input = PIL.Image.open(imageLocation)
        resized_instance = img_input.resize((width, height), PIL.Image.ANTIALIAS)
        tkinter_friendly = PIL.ImageTk.PhotoImage(resized_instance)
        # adding background to canvas
        canvas.create_image(0, 0, image=tkinter_friendly, anchor="nw")

        #font profile
        mainHeadFont = font.Font(family = "algerian", size = 20)
        bodyFont = font.Font(family = "arial", size = 14)
        closebuttonFont = font.Font(family = "Consolas", size = 13)
        #color profile
        mainHeadColor = "thistle"
        bodyColor = "white"
        closebuttonBG = "navy"
        closebuttonFG = "mediumpurple1"

        #label: main heading
        headText = "Algorithm of Sketching"
        canvas.create_text(cAlign, 20, text = headText, font = mainHeadFont, fill = mainHeadColor)
        #looping algorithm step list elements to labels
        y_coordinate = 70
        counter = 1
        for string in self.algorithm:
            counterstr = str(counter)
            bodyText = counterstr+") "+string
            canvas.create_text(20, y_coordinate, text = bodyText, font = bodyFont,
                               fill = bodyColor,anchor = "nw")
            y_coordinate += 30
            counter+=1

        #close button
        closebutton = Button(algoWindow, text = "Close", bg = closebuttonBG, fg = closebuttonFG,
                             font = closebuttonFont, command = algoWindow.destroy)
        canvas.create_window(cAlign, 260, window = closebutton, anchor = "center")
        algoWindow.mainloop()

    #main user interface window
    def MainUIWindow(self):
        ##defining tkinter window
        window = Tk()
        window.configure(bg = "black")
        window.geometry("700x500")
        window.title("Image to sketch convertor")
        window.resizable(False, False)
        width = 700
        height = 500
        centerAlign = width // 2
        # functions to call function of SketchMaker class
        def originalImageOnClick(self):
            inputLocation = locationEntry.get()
            inputName = nameEntry.get()
            Viewer = SketchMaker(inputLocation, inputName)
            try:
                error.config(text = "")
                Viewer.viewOriginal()
            except:
                errorMsg = "Invalid file name or location!"
                error.config(text = errorMsg)
        def sketchedImageOnClick(self):
            inputLocation = locationEntry.get()
            inputName = nameEntry.get()
            Viewer = SketchMaker(inputLocation, inputName)
            Viewer.convertToSketch()

        #defining canvas over window
        canvas = Canvas(window, width = 700, height = 500, highlightthickness = 0)
        canvas.pack(fill = "both", expand = True)
        #adding background to canvas
        imageLocation = "background_img.jpg"
        img_input = PIL.Image.open(imageLocation)
        resized_instance = img_input.resize((width,height),PIL.Image.ANTIALIAS)
        tkinter_friendly = PIL.ImageTk.PhotoImage(resized_instance)
        #adding background to canvas
        canvas.create_image(0, 0, image = tkinter_friendly, anchor = "nw")

        #font profile
        mainHeadFont = font.Font(family = "Algerian", size = 20)
        subHeadFont = font.Font(family = "Arial", size = 12, slant = "italic")
        dateMsgFont = font.Font(family = "arial", size = 15)
        dateFont = font.Font(family = "Consolas", size = 15, slant = "italic")
        mainMsgFont = font.Font(family = "comic sans ms")
        entryFont = font.Font(family = "Lucida console", size = 13, weight="bold")
        closebuttonFont = font.Font(family = "Consolas", size = 12)
        algobuttonFont = font.Font(family = "arial", size = 12, slant = "italic")
        imageViewFont = font.Font(family = "arial", size = 15)
        errorFont = font.Font(family="myanmar text", size=12, weight="bold")
        #color profile
        mainHeadColor = "thistle"
        dateColor = "plum1"
        mainMsgColor = "papaya whip"
        entryBackground = "lemon chiffon"
        entryForeground = "midnight blue"
        closebuttonBG = "Mediumpurple4"
        closebuttonFG = "white"
        algobuttonBG = "Mediumpurple4"
        algobuttonFG = "white"
        imgViewBG = "white"
        imgViewFG = "slateblue4"
        errorBG = "Red"
        errorFG = "white"
        #adding labels: 1)main heading
        mainHeadText = "Make a Sketch out of Image!"
        canvas.create_text(centerAlign, 30, text = mainHeadText, anchor = "center", font = mainHeadFont, fill = mainHeadColor)
        #1.1) subheading
        subHeadText = "For landscape images only"
        canvas.create_text(centerAlign, 60, text = subHeadText, anchor = "center", font = subHeadFont, fill = mainHeadColor)
        #2)date tag
        currDateTime = datetime.now()
        currDateTimeFormatted = currDateTime.strftime("%d-%m-%Y %H:%M:%S")
        currDate = currDateTimeFormatted[0:10]
        dateMsg = "Date: "
        canvas.create_text(30, 100, text=dateMsg, anchor = "center", font = dateMsgFont,fill = dateColor)
        canvas.create_text(120, 100, text=currDate, anchor = "center", font = dateFont, fill = dateColor)
        #3)time tag
        currTimeRev = currDateTimeFormatted[-1:-9:-1]
        currTime = currTimeRev[::-1]
        timeMsg = "Time: "
        canvas.create_text(550, 100, text=timeMsg, anchor = "center", font = dateMsgFont, fill = dateColor)
        canvas.create_text(640, 100, text=currTime, anchor = "center", font = dateFont, fill = dateColor)
        #4)input location message
        locInpMsg = "Enter the complete location of the image:"
        canvas.create_text(centerAlign, 170, text = locInpMsg, anchor = "center", font = mainMsgFont, fill = mainMsgColor)
        #5)input image name msg
        inInpMsg = "Enter the name of the image with extension:"
        canvas.create_text(centerAlign, 280, text = inInpMsg, anchor = "center", font = mainMsgFont, fill = mainMsgColor)
        #6) error message
        errorText = str("")
        error = Label(window, text = errorText, bg = errorBG, fg = errorFG, font = errorFont)
        error.place(x=centerAlign - 100, y=230)

        # Entry for location
        locationEntry = Entry(window, width = 60,font = entryFont,
                              justify = "center", bg = entryBackground, fg= entryForeground)
        canvas.create_window(centerAlign, 210, window = locationEntry, anchor = "center")
        #Entry for name
        nameEntry = Entry(window, width = 30, font = entryFont,
                          justify = "center", fg = entryForeground, bg = entryBackground)
        canvas.create_window(centerAlign, 320, window = nameEntry, anchor = "center")

        #buttons: 1) close the window
        closeText = "Close the program"
        closeButton = Button(window, text = closeText, command = window.destroy,font = closebuttonFont,
                             bg = closebuttonBG, fg = closebuttonFG)
        canvas.create_window(200, 460, window = closeButton, anchor = "center")
        #2)view algorithm
        algoText = "View Basic Algorithm"
        algoButton = Button(window, text = algoText, command = self.viewAlgorithm, font = algobuttonFont,
                            bg = algobuttonBG, fg = algobuttonFG)
        canvas.create_window(500, 460, window = algoButton, anchor = "center")

        #3) view original image button
        originMsg = "View Original Image"
        viewOrigin = Button(window, text = originMsg, font = imageViewFont, bg = imgViewBG,
                            fg = imgViewFG, command = lambda: originalImageOnClick(self))
        canvas.create_window(200, 400, window = viewOrigin, anchor = "center")
        #4) view sketched image button
        sketchedMsg = "View Sketch"
        viewSketch = Button(window, text = sketchedMsg, font = imageViewFont, bg = imgViewBG,
                            fg = imgViewFG, command = lambda: sketchedImageOnClick(self))
        canvas.create_window(500,400, window = viewSketch, anchor = "center")
        window.mainloop()

if __name__ == "__main__":
    callObject = Interface()
    callObject.MainUIWindow()