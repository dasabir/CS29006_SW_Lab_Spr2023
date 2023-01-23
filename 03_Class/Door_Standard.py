class Door:
    def __init__(self, number, status):
        self._number = number
        self._status = status
    
    def get_number(self):
        return self._number
    
    def set_number(self, number):
        self._number = number
    
    def get_status(self):
        return self._status
    
    def set_status(self, status):
        self._status = status
    
    def open(self):
        self.status = 'open'
    
    def close(self):
        self.status = 'closed'
    
    
        
        
        