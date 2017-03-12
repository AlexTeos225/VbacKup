from tkinter import *
import json

class LoginForm:

    def __init__(self, parent):

        if __debug__:
            print("Begin Show Login Form")

        # ------------------------------------------- FRAMES ----------------------------------------------------------
        self.frame_login_credentials = Frame(bd=5)
        self.frame_login_parameters  = Frame(bd=5)
        self.frame_login_button      = Frame(bd=5)

        self.frame_login_credentials.pack()
        self.frame_login_parameters.pack()
        self.frame_login_button.pack()

        # ------------------------------------------- CHECK BUTTONS ----------------------------------------------------------
        self.checkbox_messages_res = IntVar()
        self.checkbox_friends_res  = IntVar()
        self.checkbox_groups_res   = IntVar()
        self.checkbox_video_res    = IntVar()
        self.checkbox_audio_res    = IntVar()
        self.checkbox_photos_res   = IntVar()

        self.checkbox_messages = Checkbutton(self.frame_login_parameters, text = u'Messages', variable=self.checkbox_messages_res, onvalue=1, offvalue=0)
        self.checkbox_friends  = Checkbutton(self.frame_login_parameters, text = u'Friends ', variable=self.checkbox_friends_res , onvalue=1, offvalue=0)
        self.checkbox_groups   = Checkbutton(self.frame_login_parameters, text = u'Groups  ', variable=self.checkbox_groups_res  , onvalue=1, offvalue=0)
        self.checkbox_video    = Checkbutton(self.frame_login_parameters, text = u'Video   ', variable=self.checkbox_video_res   , onvalue=1, offvalue=0)
        self.checkbox_audio    = Checkbutton(self.frame_login_parameters, text = u'Audio   ', variable=self.checkbox_audio_res   , onvalue=1, offvalue=0)
        self.checkbox_photos   = Checkbutton(self.frame_login_parameters, text = u'Photos  ', variable=self.checkbox_photos_res  , onvalue=1, offvalue=0)

        self.checkbox_messages.grid(row = 0, column = 0, padx = 5, pady = 5)
        self.checkbox_friends. grid(row = 0, column = 1, padx = 5, pady = 5)
        self.checkbox_groups.  grid(row = 0, column = 2, padx = 5, pady = 5)
        self.checkbox_video.   grid(row = 1, column = 0, padx = 5, pady = 5)
        self.checkbox_audio.   grid(row = 1, column = 1, padx = 5, pady = 5)
        self.checkbox_photos.  grid(row = 1, column = 2, padx = 5, pady = 5)

        # ------------------------------------------- LOGIN CREDENTIALS ----------------------------------------------------------
        self.text_login    = Text(self.frame_login_credentials, height=1, width=20, font='Arial 10')
        self.text_password = Text(self.frame_login_credentials, height=1, width=20, font='Arial 10')

        self.label_login    = Label(self.frame_login_credentials, text='Login:', width=6, height=1, font='arial 10')
        self.label_password = Label(self.frame_login_credentials, text='Password:', width=9, height=1, font='arial 10')

        self.label_login   .grid(row = 0, column = 0, padx = 5, pady = 10)
        self.text_login    .grid(row = 0, column = 1, padx = 5, pady = 10)
        self.label_password.grid(row = 0, column = 2, padx = 5, pady = 10)
        self.text_password .grid(row = 0, column = 3, padx = 5, pady = 10)

        # ------------------------------------------- LOGIN BUTTON ----------------------------------------------------------
        self.button_login = Button(self.frame_login_button, text='Log In', width=10, height=1, font='arial 10', command=self.SaveParams)

        self.button_login.pack(padx = 10, pady = 10)

        self.LoadParams("settings.json")

        if __debug__:
            print("Finish Show Login Form")

    def LoadParams(self, filename):

        if __debug__:
            print("Begin Load Start Parameters")

        try:
            with open(filename, "r") as json_data:
                try:
                    params = json.load(json_data)
                except:
                    if __debug__:
                        print("Incorrect Setting File")
                    return
        except FileNotFoundError:
            if __debug__:
                print("Setting File Not Found")
            return

        if "login" in params:

            if "login" in params["login"]:
                self.text_login.insert(END, params["login"]["login"])

            if "password" in params["login"]:
                self.text_password.insert(END, params["login"]["password"])

        if "access" in params:

            if "messages" in params["access"]:
                if(params["access"]["messages"] == "true"):
                    self.checkbox_messages.select()

            if "friends" in params["access"]:
                 if(params["access"]["friends"] == "true"):
                    self.checkbox_friends.select()

            if "groups" in params["access"]:
                 if(params["access"]["groups"] == "true"):
                    self.checkbox_groups.select()

            if "video" in params["access"]:
                 if(params["access"]["video"] == "true"):
                    self.checkbox_video.select()

            if "audio" in params["access"]:
                 if(params["access"]["audio"] == "true"):
                    self.checkbox_audio.select()

            if "photos" in params["access"]:
                 if(params["access"]["photos"] == "true"):
                    self.checkbox_photos.select()

        if __debug__:
            print("Finish Load Start Parameters")

    def SaveParams(self, filename = "settings.json"):

        if __debug__:
            print("Begin Save Start Parameters")

        params = {}

        if(self.text_login.get("1.0", "1.end") != ""):
            if "access" not in params:
                params["login"] = {}
            params["login"]["login"] = self.text_login.get("1.0", "1.end")

        if (self.text_password.get("1.0", "1.end") != ""):
            if "access" not in params:
                params["login"] = {}
            params["login"]["password"] = self.text_password.get("1.0", "1.end")

        if(self.checkbox_messages_res.get()):
            if "access" not in params:
                params["access"] = {}
            params["access"]["messages"] = "true"

        if (self.checkbox_friends_res.get()):
            if "access" not in params:
                params["access"] = {}
            params["access"]["friends"] = "true"

        if (self.checkbox_groups_res.get()):
            if "access" not in params:
                params["access"] = {}
            params["access"]["groups"] = "true"

        if (self.checkbox_video_res.get()):
            if "access" not in params:
                params["access"] = {}
            params["access"]["video"] = "true"

        if (self.checkbox_audio_res.get()):
            if "access" not in params:
                params["access"] = {}
            params["access"]["audio"] = "true"

        if (self.checkbox_photos_res.get()):
            if "access" not in params:
                params["access"] = {}
            params["access"]["photos"] = "true"

        with open(filename, "w") as json_data:
            json.dump(params, json_data)

        if __debug__:
            print("Finish Save Start Parameters")