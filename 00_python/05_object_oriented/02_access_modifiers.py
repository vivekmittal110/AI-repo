# public
# private
# protected
# by default attributes/functions are public

# public modifier
# class ABC:
    
#     def __init__(self):
#         self.public_attribute = None # this is a public attribute

#     def public_function():   # this is a public function
#         pass

# obj1 = ABC()
# obj1.public_attribute
# obj1.public_function()



# private modifier
# class ABC:
    
#     def __init__(self):
#         self.__private_attribute = None   # this is a private attribute (add two underscore before attribute)

#     def __private_function():   # this is a private function (add two underscore before function)
#         pass

# obj1 = ABC()
# obj1.private_attribute
# obj1.private_function()



# proctected modifier
class ABC:
    
    def __init__(self):
        self._proctected_attribute = None   # this is a proctected attribute (add one underscore before attribute)

    def _proctected_function():   # this is a proctected function (add one underscore before function)
        pass


