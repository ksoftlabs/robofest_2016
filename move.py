class Control:
    def __init__(self):
        self.motor_l=0
        self.motor_r=0

    def forward(self,speed):
        self.motor_l=speed
        self.motor_r=speed

    def reverse(self,speed):
        self.motor_l=speed
        self.motor_r=speed

    def left(self,speed):
        self.motor_l=0
        self.motor_r=speed

    def right(self,speed):
        self.motor_l=speed
        self.motor_r=0

    def turn_around(self,speed):
        self.motor_l=speed
        self.motor_r=-speed