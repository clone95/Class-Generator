import os

welcome = "Welcome to class generator 1.0"

def class_builder (class_name, class_methods, basic_parameters):

    file = open("python_class_generated.py", "w+")
    file.write("# class %s automatic-generated  \n\n\n" % class_name)
    file.write("def %s(): \n" % class_name)
    ris = ""
    for el in range (0, len(basic_parameters)):
        ris = ris + ", " + basic_parameters[el]
    print(ris)
    file.write("    def __init__ (self, basic_parameters[0):\n")
    for el in range(0, len(basic_parameters)):
        print(len(basic_parameters))
        file.write("        self." + basic_parameters[el] + " = " + basic_parameters[el] + "\n")

class_builder("cancella",0,["uno", "due", "tre"])