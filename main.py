from LogInForm import *
from MainForm import *

if __name__ == '__main__':

    root = Tk()

    login_form = TLoginForm(root)

    #while(login_form.quit != True):
    while(0):
        root.update()

    #params = {"login", "scope"}
    params = {}
    params["login"] = {}
    params["scope"] = {}

    params["login"]["login"] = login_form.text_login.get("1.0", "1.end")
    params["login"]["password"] = login_form.text_password.get("1.0", "1.end")

    root.destroy()

    root = Tk()

    main_form = TMainForm(root, params)

    root.mainloop()
    #while (main_form.quit != True):
    #    root.update()