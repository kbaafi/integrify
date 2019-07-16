
class VideoApp:
    participants_online = 0
    action = ["speaking", "silent"]

    @classmethod
    def show_participants_online(cls):
        print(f"There are currently {cls.participants_online} participants online")

    def __init__(self, username, company):
        self._username = username
        self._company = company
        VideoApp.participants_online = VideoApp.participants_online+1

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        self._username = value

    @property
    def company(self):
        return self._company

    @company.setter
    def company(self, value):
        self._company = value

    @classmethod
    def go_online(cls):
        cls.participants_online += 1

    @classmethod
    def go_offline(cls):
        cls.participants_online -= 1

    @classmethod
    def status(cls, action):
        if action in VideoApp.action:
            return f"{cls.username} is {action}"
        raise ValueError(f"The user must either be {VideoApp.action[0]} or {VideoApp.action[1]}")

    def __repr__(self):
        return f"""Video App
            username: {self.username}
            company: {self.company}
            number of participants: {VideoApp.participants_online}
            """

    __status = status


class Message:
    def __init__(self, username, message):
        self._user_name = username
        self._message = message

    @property
    def username(self):
        return self._user_name

    @username.setter
    def username(self, value):
        self._user_name = value

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value

    def _status(self):
        return f"{self._user_name} sent the message {self._message}"

    __status = _status


class ChatApp(VideoApp, Message):

    def __init__(self, username, message, company):
        self._user_name = username
        self._company = company
        self._message = message

