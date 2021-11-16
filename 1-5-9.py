class Buffer:

    def __init__(self):
        self.current_part = []

    def add(self, *a):
        self.current_part.extend(a)
        while len(self.current_part) - 5 >= 0:
            print(sum(self.current_part[0:5]))
            self.current_part = self.current_part[5:]

    def get_current_part(self):
        return self.current_part
      
      
      
class Buffer:
    def __init__(self):
        self.buff = []
        
    def add(self, *a):
        self.buff.extend(a)
        while len(self.buff) > 4:
            print(sum(self.buff[:5]))
            self.buff = self.buff[5:]
            
    def get_current_part(self):
        return self.buff
