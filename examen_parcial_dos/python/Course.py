class Course:

    def __init__ (self, id, code, name, professor, price, size):
         self.id = id
         self.code = code
         self.name = name
         self.professor = professor
         self.price = price
         self.size = size
    
    def welcome(self):
        return "Welcome student "
    
    def goodbye(self):
        return "Goodbay student"
    
    def new_professor(self, new_professor_name):
        return "This is your new professor "+new_professor_name

    def total_price(self, discount):
        total_price = self.size * self.price
        total_price = total_price - discount
        return total_price

######Out of class#######

new_course = Course(1, 1000, "Pr Or Ob", "Luis Guerra", 5, 10)
print(new_course.welcome())
print(new_course.goodbye())
print(new_course.new_professor("Nefertari"))
print(new_course.total_price(0))
print (new_course.total_price(10))