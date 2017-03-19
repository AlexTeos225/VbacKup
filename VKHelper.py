import vk
import time

class TVKHelper:

    def __init__(self, parent, params):
        self.api = self.authorize(params)

    def authorize(self, params):
        if __debug__:
            print("[TVKHelper::authorize] Try to authorize with parameters:", params)

        session = vk.AuthSession(app_id='5874117', user_login = params["login"]["login"], user_password = params["login"]["password"],
                                 scope = 'messages')
        api = vk.API(session)

        return api

    def get_user_messages(self, uid, count = 0):
        try:
            if (count == 0):
                messages_count = self.api.messages.getHistory(count=0, user_id=uid)[0]
            else:
                messages_count = count
        except vk.exceptions.VkAPIError:
            time.sleep(3)
            messages_count = self.api.messages.getHistory(count=0, user_id=uid)[0]

        messages = []
        offset = 0
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

            except vk.exceptions.VkAPIError:
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
