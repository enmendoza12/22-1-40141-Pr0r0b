class Course:
    name = "Object Oriented Programming"
    classroom = 5202
    
<<<<<<< HEAD
    def __init__(self, name,hour, teacher,classroom):
=======
    def __init__(self, name, hour, teacher,classroom):
>>>>>>> de322880a00d083ce60418f29a83aabf8b05d5c2
        self.name = name
        self.hour = hour
        self.teacher = teacher
        self.classroom = classroom

c1 = Course("OPP", "19:00-20:40", "Luis Guerra",5202)
c2 = Course("Bases de Datos", "20:40-10:10", "Silvia Barrera",3205)

def welcome_message():
    print("Bienvenido al sistema de materias")

def show info (c1,c2)
        print("Materias dadas de alta: ")
        print(c1.name + " y "+ c2.name)
