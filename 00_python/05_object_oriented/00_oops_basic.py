class Bca:
    def set_name(self,name):
        self.name = name
    
    def get_name(self):
        return self.name
    
student1 = Bca()
student1.set_name("vivek")
print(student1.get_name())