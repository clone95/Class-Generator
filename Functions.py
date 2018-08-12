# class generator python 3.6


def class_builder(class_name, class_methods, basic_attributes):

    file = open("python_class_generated.py", "w+")
    file.write("# class %s automatic-generated  \n\n\n" % class_name)
    file.write("def %s(): \n\n" % class_name)
    ris = ""                                            # parameters string for constructor
    for el in range(0, len(basic_attributes)):
        ris = ris + ", " + basic_attributes[el]
    ris1 = ris[2:]              # clear from first ','
    file.write("    def __init__ (self, %s):\n" % ris1)
    for el in range(0, len(basic_attributes)):              # constructor
        print(len(basic_attributes))
        file.write("        self." + basic_attributes[el] + " = " + basic_attributes[el] + "\n")
    for el in range(0, len(class_methods)):                     # methods
        file.write("\n    def %s(self):" % class_methods[el])
        file.write("\n        return True\n\n")
    for el in range(0, len(basic_attributes)):                              # default get methods for each attribute
        file.write("    def get_%s(self):\n" % basic_attributes[el])
        file.write("        return self.%s\n" % basic_attributes[el])
    for el in range(0, len(basic_attributes)):                                      # default set methods ..
        file.write("\n    def set_%s(self, new_value):\n" % basic_attributes[el])
        file.write("        self.%s = new_value" % basic_attributes[el])


def main():
    welcome = "Welcome to class generator 1.0"
    end = True
    methods = []
    attributes = []
    print(welcome)
    class_name = input("Insert the class name:\n")
    while end:
        method = input("Insert method name (end to terminate):\n")
        if method == "end":
            end = False
        else:
            methods.append(method)
    end = True
    while end:
        attribute = input("Insert attribute name (end to terminate):\n")
        if attribute == "end":
            end = False
        else:
            attributes.append(attribute)

    class_builder(class_name, methods, attributes)      # let's generate the python file


main()
