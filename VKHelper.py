import vk
import time
import json

class TVKHelper:

    def __init__(self, parent, params):
        self.api = self.authorize(params)

    def authorize(self, params):
        if __debug__:
            print("[TVKHelper::authorize] Try to authorize with parameters:", params)

        try:
            if "token" in params["login"]:
                session = vk.Session(access_token=params["login"]["token"])
            else:
                session = vk.AuthSession(app_id='5874117', user_login = params["login"]["login"], user_password = params["login"]["password"], scope = params["scope"])
        except vk.exceptions.VkAuthError as e:
            if __debug__:
                print("[TVKHelper::authorize] VkAuthError Exeption: ", e)
            return 0

        if __debug__:
            print("[TVKHelper::authorize] Authorize succeed")

        self.update_params("settings.json", session.access_token)

        api = vk.API(session)

        return api

    def get_user_messages(self, uid, count = 0, _offset = 0):
        try:
            if (count == 0):
                messages_count = self.api.messages.getHistory(count=0, user_id=uid)[0]
            else:
                messages_count = count
        except vk.exceptions.VkAPIError as e:
            if __debug__:
                print("[TVKHelper::get_user_messages] VkAPIError: ", e)
            time.sleep(3)
            messages_count = self.api.messages.getHistory(count=0, user_id=uid)[0]

        messages = []
        offset = _offset
        if messages_count < 200:
            offset_size = messages_count
        else:
            offset_size = 200

        while offset < messages_count:

            try:
                res = self.api.messages.getHistory(count=offset_size, offset=offset, user_id=uid)

                i = 0
                while i < len(res) - 1:
                    messages.append(res[i + 1])
                    i = i + 1

            except vk.exceptions.VkAPIError as e:
                if __debug__:
                    print("[TVKHelper::get_user_messages] VkAPIError: ", e)
                time.sleep(1)
            else:
                offset = offset + offset_size

        return messages

    def get_dialogs_users_ids(self):
        ids = []
        try:
            dialog_count = self.api.messages.getDialogs(count=0, preview_length=0)[0]
        except vk.exceptions.VkAPIError:
            time.sleep(3)
            dialog_count = self.messages.getDialogs(count=0, preview_length=0)[0]

        offset = 0
        offset_size = 200
        while offset < dialog_count:

            try:
                res = self.api.messages.getDialogs(count=offset_size, offset=offset, preview_length=0)

                i = 0
                while i < len(res) - 1:
                    ids.append(res[i + 1]['uid'])
                    i = i + 1

            except vk.exceptions.VkAPIError:
                time.sleep(1)
            else:
                offset = offset + offset_size

        return ids

    def update_params(self, filename, _params):

        if __debug__:
            print("[TVKHelper::update_params] Begin Update Start Parameters")

        try:
            with open(filename, "r") as json_data:
                try:
                    params = json.load(json_data)
                except:
                    if __debug__:
                        print("[TVKHelper::update_params] Incorrect Setting File")
                    return
        except FileNotFoundError:
            if __debug__:
                print("[TVKHelper::update_params] Setting File Not Found")
            return

        if "login" not in params:
            params["login"] = {}

        params["login"]["token"] = _params

        with open(filename, "w") as json_data:
            json.dump(params, json_data)

        if __debug__:
            print("[TVKHelper::update_params] Finish Update Start Parameters")