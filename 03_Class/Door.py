class Door:
    def __init__(self, number, status):
        self.number = number
        self.status = status
    
    def open(self):
        self.status = 'open'
    
    def close(self):
        self.status = 'closed'

class SecurityDoor(Door):
    def __init__(self, number, status, locked=True):
        super().__init__(number, status)
        self.locked=locked
    
    def lockDoor(self):
        self.locked=True
    
    def unlockDoor(self):
        self.locked=False
    
    def open(self):
        if self.locked:
            return
        super().open()

if __name__ == '__main__':
    door1 = Door(1, 'closed')
    print(door1.number)
    print(door1.status)
    print(type(door1))
    
    door1.open()
    print(door1.status)
    
    door2 = Door(1, 'closed')
    print("Address of door1 object: {}".format(hex(id(door1))))
    print("Address of door2 object: {}".format(hex(id(door2))))
    
    print("Address of class of door1 object: {}".format(hex(id(door1.__class__))))
    print("Address of class of door2 object: {}".format(hex(id(door2.__class__))))
    
    print(Door.__dict__)
    print(door1.__dict__)
    print(door1.__dict__['status'])
    
    sdoor1 = SecurityDoor(2,'closed')
    print(sdoor1.status) # prints 'closed'
    # Remember that the door is locked,
    # so open will not have any effect
    sdoor1.open()
    print(sdoor1.status) # prints 'closed'
    # Now unlock the door
    sdoor1.unlockDoor()
    sdoor1.open()
    print(sdoor1.status) # prints 'open'
    
#     sdoor2 = SecurityDoor(2,'closed',False)
#     print(sdoor2.status)
#     # Remember that the door is unlocked, so open will have effect
#     sdoor2.open()
#     print(sdoor2.status)