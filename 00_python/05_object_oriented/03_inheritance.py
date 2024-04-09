class parent:
    def __init__(self):
        print("this is parent class")
        self.super_attribute = True

    def get_print(self):
        print("this is function of parent")


class child(parent):
    def __init__(self):
        super().__init__()
        super().get_print()
        print(self.super_attribute)
        print("this is constructor of child class")


child1 = child()

# levels of inheritance

# single -> one parten one child

# miltuple -> many parents one child -> class A, class B, class(A,B)

# multilevel ->grandparent > parent > child -> class A, class B(A), class C(B)

# Hierarchial -> one parent many child-> class A: class B(A) class C(A) class D(A)

# Hybrid -> mix of multiple and multilevel ->
        # class A:
            
        # class B:
     
        # class C(A,B):
        
        # class D(C)

