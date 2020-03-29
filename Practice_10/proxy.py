class CEO(object):
    def __init__(self):
        self.is_available = True
    def occupied(self):
        self.is_available = False
        print("CEO is busy in meeting")
    def available(self):
        self.is_available = True
        print("CEO is available for meeting")
    
    @property
    def status(self):
        return self.is_available

class PersonalAssistant(object):
    def talk(self):
        self.ceo = CEO()
        if self.ceo.status:
            self.ceo.occupied()
        else:
            self.ceo.available()


pa = PersonalAssistant()
pa.talk()