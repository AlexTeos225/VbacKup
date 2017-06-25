from tkinter import *
from VKHelper import *

class TMainForm:

    quit = False

    def __init__(self, parent, params):

        if __debug__:
            print("[TMainForm::Init] Begin Show Main Form")

        self.text = Text()
        self.text.config(width=40, height=24)
        self.text.pack(expand=YES, fill=BOTH)

        if __debug__:
            print("[TMainForm::Init] Finish Show Main Form")

        self.vk_helper = TVKHelper(self, params)

        UserMessages = self.vk_helper.get_user_messages("15637879", 30, 0)

        for message in UserMessages:
            self.text.insert(END, message['body'])
            self.text.insert(END, "\n")