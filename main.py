from LogInForm import *
from MainForm import *

if __name__ == '__main__':

    root = Tk()

    if __debug__:
        print("[Main::main] Create Login Form")

    login_form = TLoginForm(root)

    i = 0
    while(login_form.quit != True):
    #while(i < 100):
        i = i + 1
        root.update()

    #params = {"login", "scope"}
    params = {}
    params["login"] = {}

    if(login_form.text_login.get("1.0", "1.end") != ""):
        params["login"]["login"] = login_form.text_login.get("1.0", "1.end")
        params["login"]["password"] = login_form.text_password.get("1.0", "1.end")

    if (login_form.text_token.get("1.0", "1.end") != ""):
        params["login"]["token"] = login_form.text_token.get("1.0", "1.end")

    scope = ""
    if (login_form.checkbox_messages_res.get()):
        scope = scope + "messages"

    if (login_form.checkbox_friends_res.get()):
        if (scope != ""):
            scope = scope + ","
        scope = scope + "friends"

    if (login_form.checkbox_groups_res.get()):
        if (scope != ""):
            scope = scope + ","
        scope = scope + "groups"

    if (login_form.checkbox_video_res.get()):
        if (scope != ""):
            scope = scope + ","
        scope = scope + "video"

    if (login_form.checkbox_audio_res.get()):
        if (scope != ""):
            scope = scope + ","
        scope = scope + "audio"

    if (login_form.checkbox_photos_res.get()):
        if (scope != ""):
            scope = scope + ","
        scope = scope + "photos"

    params["scope"] = scope

    if __debug__:
        print("[Main::main] Destroy Login Form")

    root.destroy()

    if __debug__:
        print("[Main::main] Create Main Form")

    root2 = Tk()

    main_form = TMainForm(root2, params)

    root2.mainloop()

    if __debug__:
        print("[Main::main] Destroy Login Form")

    #while (main_form.quit != True):
    #    root.update()