class tv:
    def __init__(self, chanel, value_level, on):
        self.chanel = chanel
        self.value_level = value_level
        self.on = on
    def turn_on(self, turn_on=True):
        self.turn_on= turn_on
        
    def turn_on(self, turn_of=False):
        self.turn_of= turn_of
        
chanel = tv()
chanel.tu