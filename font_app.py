 
from tkinter import*
import math 

root = Tk()
blank_space = "  "
root.title (50 * blank_space + "VS Code Calculation")
root.resizable(width = FALSE , hight = FALSE)
root.geometry("520-721*890+21")
 
coverFrame = Frame(root , bd=20 , pady=2 , relief= RIDGE)
coverFrame.grid()

coverMainFrame = Frame(coverFrame , bd=20 , pady=2 , bg='blue' , relief=RIDGE)
coverMainFrame.grid()

MainFrame= Frame(coverMainFrame , bd=20 , pady=2 , relief=RIDGE)
MainFrame.grid()
