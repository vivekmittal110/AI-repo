class Bca:
    def set_name(self,name):
        self.name = name    # class attribute
    
    def get_name(self):
        return self.name
    
student1 = Bca()
student1.set_name("vivek")
print(student1.get_name())
student1.eng_marks = 98  # instance attribute (for a specific entity)
print(student1.eng_marks)

student2 = Bca()
student2.set_name("sumit")
print(student1.get_name())