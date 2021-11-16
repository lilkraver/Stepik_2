class LoggableList(list, Loggable):
    def append(self, n):
        self += [n]
        self.log(n)
        
        
 
class LoggableList(list, Loggable):
    def append(self, x):
        self.log(x)
        super().append(x)
