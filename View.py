from logging import root
from Controller import Controller
from Player import Player
import Errors

import sys

import tkinter as tk
import pyglet
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

class View:

    controller = Controller()

    def __init__(self):
        pyglet.font.add_file('./assets/JockeyOne-Regular.ttf')
        self.mainColorOrange = "#FA8B1E"

        self.root = tk.Tk()
        self.root.title("game")
        self.root.geometry("810x530")
        self.root.resizable(False, False)
        self.root.iconbitmap("./assets/burger.ico")

        self.container = tk.Frame(self.root)
        self.container.pack()

        self.bg_image = ImageTk.PhotoImage(Image.open("./assets/BG.png"))
        self.logo_image = ImageTk.PhotoImage(Image.open("./assets/logo.png"))
        self.burger_image = ImageTk.PhotoImage(Image.open("./assets/burger.png"))
        self.player = self.controller.player

        self.loginScreen()
        self.root.mainloop()

        
    def goToSignUpScreen(self):
            self.currentCanvas.destroy()
            self.signUpScreen()

    def goToGameScreen(self):
            self.currentCanvas.destroy()
            self.gameScreen()

    def login(self):
        res = self.controller.login(self.username_entry.get(), self.password_entry.get())
        if res == 0:
            self.goToGameScreen()
        else:
                messagebox.showerror("Warning", Errors.getError(res))

    def goToLogInScreen(self):
        self.currentCanvas.destroy()
        self.loginScreen()

    def goToGameScreen(self):
        self.currentCanvas.destroy()
        self.gameScreen()

    def signup(self):
        res = self.controller.signup(self.username_entry.get(), self.password_entry.get(), self.confirmPassword_entry.get())
        if res == 0:
            self.goToGameScreen()
        else:
            messagebox.showerror("Warning", Errors.getError(res))

    def menu(self):
        self.currentCanvas.destroy()
        self.gameMenu()

    def updateScore(self):
        self.scoreLabel.config(text=str(int(self.player.borglars)))
        self.controller.playerFactory()
        self.currentCanvas.after(2, self.updateScore)

    def updateUpgrades(self):
        self.upgrade1_Label.config(text="Cost: " + str(self.player.up1Cost) + " Have: " + str(self.player.up1))
        self.upgrade2_Label.config(text="Cost: " + str(self.player.up2Cost) + " Have: " + str(self.player.up2))
        self.upgrade3_Label.config(text="Cost: " + str(self.player.up3Cost) + " Have: " + str(self.player.up3))

    def playerClick(self):
        self.controller.playerClick()
        
    def buyUpgrade1(self):
        self.player.upgrade1()
        self.updateUpgrades()

    def buyUpgrade2(self):
        self.player.upgrade2()
        self.updateUpgrades()

    def buyUpgrade3(self):
        self.player.upgrade3()
        self.updateUpgrades()
        
    def save(self):
        self.controller.saveGame()

    def saveExit(self):
        self.controller.saveGame()
        sys.exit()
    
    def loginScreen(self):  
        self.currentCanvas = tk.Canvas(self.root, width=810, height=530)
        self.currentCanvas.pack()
        self.currentCanvas.create_image(0, 0, anchor=tk.NW, image=self.bg_image)

        self.currentCanvas.create_image(0, 35, image=self.logo_image, anchor=tk.NW)

        style = ttk.Style()
        
        style.configure('TEntry', relief='flat')

        square_coords = (200, 200, 600, 400)

        self.currentCanvas.create_rectangle(square_coords, fill=self.mainColorOrange)

        username_label = tk.Label(
            self.root,
            text="User:",
            font=('Jockey One', 24),
            fg="white", 
            background=self.mainColorOrange
        )

        self.currentCanvas.create_window(230, 260, anchor=tk.W, window=username_label)

        self.username_entry = ttk.Entry(
            self.root, 
            style='TEntry', 
            width="25", 
            font=('Jockey One', 16), 
            foreground=self.mainColorOrange
        )

        self.currentCanvas.create_window(440, 265, window=self.username_entry)

        password_label = tk.Label(
            self.root,
            text="Code:",
            font=('Jockey One', 24),
            fg="white", 
            background=self.mainColorOrange
        )

        self.currentCanvas.create_window(230, 325, anchor=tk.W, window=password_label)

        self.password_entry = ttk.Entry(
            self.root, 
            style='TEntry', 
            width="25", 
            font=('Jockey One', 16), 
            foreground=self.mainColorOrange
        )
        
        self.currentCanvas.create_window(440, 330, window=self.password_entry)

        login_button = tk.Button(
        self.root,
        text="Log In",
        font=('Jockey One', 16),
        bg=self.mainColorOrange,
        fg="white",
        relief="flat",
        width="15",
        command=self.login
        )

        self.currentCanvas.create_window(775, 500, anchor=tk.SE, window=login_button)

        notAUserLabel_label = tk.Label(
            self.root,
            text="Not a user?",
            font=('Jockey One', 14),
            fg="white", 
            background=self.mainColorOrange
        )

        self.currentCanvas.create_window(30, 475, anchor=tk.W, window=notAUserLabel_label)

        goToSignup_button = tk.Button(
        self.root,
        text="Sign Up",
        font=('Jockey One', 10),
        bg=self.mainColorOrange,
        fg="white",
        relief="flat",
        width="10",
        height="1",
        command=self.goToSignUpScreen
        )

        self.currentCanvas.create_window(183, 491, anchor=tk.SE, window=goToSignup_button)

    def signUpScreen(self):
        self.currentCanvas = tk.Canvas(self.root, width=810, height=530)
        self.currentCanvas.pack()
        self.currentCanvas.create_image(0, 0, anchor=tk.NW, image=self.bg_image)

        self.currentCanvas.create_image(0, 35, image=self.logo_image, anchor=tk.NW)

        style = ttk.Style()
        
        style.configure('TEntry', relief='flat')

        square_coords = (200, 200, 600, 400)

        self.currentCanvas.create_rectangle(square_coords, fill=self.mainColorOrange)

        username_label = tk.Label(
            self.root,
            text="User:",
            font=('Jockey One', 24),
            fg="white", 
            background=self.mainColorOrange
        )

        self.currentCanvas.create_window(230, 240, anchor=tk.W, window=username_label)

        self.username_entry = ttk.Entry(
            self.root, 
            style='TEntry', 
            width="25", 
            font=('Jockey One', 16), 
            foreground=self.mainColorOrange
        )

        self.currentCanvas.create_window(440, 245, window=self.username_entry)

        password_label = tk.Label(
            self.root,
            text="Code:",
            font=('Jockey One', 24),
            fg="white", 
            background=self.mainColorOrange
        )

        self.currentCanvas.create_window(230, 300, anchor=tk.W, window=password_label)

        self.password_entry = ttk.Entry(
            self.root, 
            style='TEntry', 
            width="25", 
            font=('Jockey One', 16), 
            foreground=self.mainColorOrange
        )

        self.currentCanvas.create_window(440, 305, window=self.password_entry)

        confirmPassword_label = tk.Label(
            self.root,
            text="C. Code:",
            font=('Jockey One', 24),
            fg="white", 
            background=self.mainColorOrange
        )

        self.currentCanvas.create_window(210, 350, anchor=tk.W, window=confirmPassword_label)

        self.confirmPassword_entry = ttk.Entry(
            self.root, 
            style='TEntry', 
            width="25", 
            font=('Jockey One', 16), 
            foreground=self.mainColorOrange
        )
        
        self.currentCanvas.create_window(440, 355, window=self.confirmPassword_entry)

        signup_button = tk.Button(
        self.root,
        text="Sign Up",
        font=('Jockey One', 16),
        bg=self.mainColorOrange,
        fg="white",
        relief="flat",
        width="15",
        command=self.signup
        )

        self.currentCanvas.create_window(775, 500, anchor=tk.SE, window=signup_button)

        AlreadyUserLabel = tk.Label(
            self.root,
            text="Already a user?",
            font=('Jockey One', 14),
            fg="white", 
            background=self.mainColorOrange
        )

        self.currentCanvas.create_window(30, 475, anchor=tk.W, window=AlreadyUserLabel)

        goToLogin_button = tk.Button(
        self.root,
        text="Log in",
        font=('Jockey One', 10),
        bg=self.mainColorOrange,
        fg="white",
        relief="flat",
        width="10",
        height="1",
        command=self.goToLogInScreen
        )
        
        self.currentCanvas.create_window(213, 491, anchor=tk.SE, window=goToLogin_button)

    def gameScreen(self):
        self.currentCanvas = tk.Canvas(self.root, width=810, height=530, bg="#141414")
        self.currentCanvas.pack()   

        self.currentCanvas.create_image(90, -10, image=self.logo_image, anchor=tk.NW)

        burger_button = tk.Button(
            self.root,
            background="#141414",
            relief="flat",
            image=self.burger_image,
            borderwidth=0,
            activebackground="#141414",
            command=self.playerClick
        )
        
        self.currentCanvas.create_window(425, 430, anchor=tk.SE, window=burger_button)

        upgradesListCords = (525, 0, 810,  530)

        self.currentCanvas.create_rectangle(upgradesListCords, fill=self.mainColorOrange)

        burgerDataCords = (0, 430, 445, 485)

        self.currentCanvas.create_rectangle(burgerDataCords, fill=self.mainColorOrange)

        burgersLabel = tk.Label(
            self.root,
            text="Borglars",
            font=('Jockey One', 19),
            fg="white", 
            background="#141414"
        )

        self.currentCanvas.create_window(360, 505, anchor=tk.W, window=burgersLabel)

        self.scoreLabel = tk.Label(
            self.root,
            text=str(self.player.borglars),
            font=('Jockey One', 24),
            fg="white", 
            background=self.mainColorOrange
        )

        self.currentCanvas.create_window(110, 458, anchor=tk.W, window=self.scoreLabel)

        userLoggedLabel = tk.Label(
            self.root,
            text="Logged as: ",
            font=('Jockey One', 16),
            fg="black", 
            background=self.mainColorOrange
        )

        self.currentCanvas.create_window(550, 55, anchor=tk.W, window=userLoggedLabel)

        userLoggedLabel = tk.Label(
            self.root,
            text=self.player.name,
            font=('Jockey One', 20),
            fg="white", 
            background=self.mainColorOrange
        )

        self.currentCanvas.create_window(640, 55, anchor=tk.W, window=userLoggedLabel)

        openMenu_button = tk.Button(
        self.root,
        text="Open the Menu",
        font=('Jockey One', 15),
        bg="#141414",
        fg="white",
        relief="flat",
        width="20",
        height="1",
        command=self.menu
        )
        
        self.currentCanvas.create_window(763, 484, anchor=tk.SE, window=openMenu_button)

        upgrade1_button = tk.Button(
        self.root,
        text="+1 Borglar per click",
        font=('Jockey One', 15),
        bg="white",
        fg=self.mainColorOrange,
        relief="flat",
        width="20",
        height="1",
        command=self.buyUpgrade1
        )
        
        self.currentCanvas.create_window(763, 185, anchor=tk.SE, window=upgrade1_button)

        upgrade2_button = tk.Button(
        self.root,
        text="Borglar factory",
        font=('Jockey One', 15),
        bg="white",
        fg=self.mainColorOrange,
        relief="flat",
        width="20",
        height="1",
        command=self.buyUpgrade2,
        )
        
        self.currentCanvas.create_window(763, 285, anchor=tk.SE, window=upgrade2_button)

        upgrade3_button = tk.Button(
        self.root,
        text="Borglar multiplier",
        font=('Jockey One', 15),
        bg="white",
        fg=self.mainColorOrange,
        relief="flat",
        width="20",
        height="1",
        command=self.buyUpgrade3
        )
        
        self.currentCanvas.create_window(763, 385, anchor=tk.SE, window=upgrade3_button)

        self.upgrade1_Label = tk.Label(
            self.root,
            text="Cost: " + str(self.player.up1Cost) + " Have: " + str(self.player.up1),
            font=('Jockey One', 14),
            fg="white", 
            background=self.mainColorOrange
        )

        self.currentCanvas.create_window(570, 120, anchor=tk.W, window=self.upgrade1_Label)
        
        self.upgrade2_Label = tk.Label(
            self.root,
            text="Cost: " + str(self.player.up2Cost) + " Have: " + str(self.player.up2),
            font=('Jockey One', 14),
            fg="white", 
            background=self.mainColorOrange
        )

        self.currentCanvas.create_window(570, 220, anchor=tk.W, window=self.upgrade2_Label)

        self.upgrade3_Label = tk.Label(
            self.root,
            text="Cost: " + str(self.player.up3Cost) + " Have: " + str(self.player.up3),
            font=('Jockey One', 14),
            fg="white", 
            background=self.mainColorOrange
        )

        self.currentCanvas.create_window(570, 320, anchor=tk.W, window=self.upgrade3_Label)
        self.updateScore()


    def gameMenu(self):
        self.currentCanvas = tk.Canvas(self.root, width=810, height=530, bg=self.mainColorOrange)
        self.currentCanvas.pack()  

        sideMenuCords = (380, 0, 810, 530)
        self.currentCanvas.create_rectangle(sideMenuCords, fill="#141414")

        self.currentCanvas.create_image(435, 190, image=self.logo_image, anchor=tk.NW)

        menu_Label = tk.Label(
            self.root,
            text="Menu",
            font=('Jockey One', 45),
            fg="white", 
            background=self.mainColorOrange
        )

        self.currentCanvas.create_window(50, 100, anchor=tk.W, window=menu_Label)

        resumeGame_button = tk.Button(
        self.root,
        text="Resume",
        font=('Jockey One', 16),
        bg="#141414",
        fg=self.mainColorOrange,
        relief="flat",
        width="20",
        height="1",
        command=self.goToGameScreen
        )
        
        self.currentCanvas.create_window(260, 220, anchor=tk.SE, window=resumeGame_button)

        changeAccount_button = tk.Button(
        self.root,
        text="Change account",
        font=('Jockey One', 16),
        bg="#141414",
        fg=self.mainColorOrange,
        relief="flat",
        width="20",
        height="1",
        command=self.goToLogInScreen
        )
        
        self.currentCanvas.create_window(260, 280, anchor=tk.SE, window=changeAccount_button)

        saveGame_button = tk.Button(
        self.root,
        text="Save game",
        font=('Jockey One', 16),
        bg="#141414",
        fg=self.mainColorOrange,
        relief="flat",
        width="20",
        height="1",
        command=self.save
        )
        
        self.currentCanvas.create_window(260, 340, anchor=tk.SE, window=saveGame_button)

        saveQuitGame_button = tk.Button(
        self.root,
        text="Save and quit",
        font=('Jockey One', 16),
        bg="red",
        fg="white",
        relief="flat",
        width="20",
        height="1",
        command=self.saveExit
        )
        
        self.currentCanvas.create_window(260, 400, anchor=tk.SE, window=saveQuitGame_button)

        madeBy_Label = tk.Label(
            self.root,
            text="Made by Luis",
            font=('Jockey One', 14),
            fg="#141414", 
            background=self.mainColorOrange
        )

        self.currentCanvas.create_window(20, 500, anchor=tk.W, window=madeBy_Label)