# Class-Generator
A class skeleton generator with textual interface.

Usage:

From this usage
```
Insert method name (end to terminate):
>> method_1
Insert method name (end to terminate):
>> method_2
Insert method name (end to terminate):
>> method_3
Insert method name (end to terminate):
>> end
Insert attribute name (end to terminate):
>> attrib_1
Insert attribute name (end to terminate):
>> attrib_2
Insert attribute name (end to terminate):
>> attrib_3
Insert attribute name (end to terminate):
>> end
```

It creates a new Python file 
```
# class class_1 automatic-generated  


def class_1(): 

    def __init__ (self, attrib_1, attrib_2, attrib_3):
        self.attrib_1 = attrib_1
        self.attrib_2 = attrib_2
        self.attrib_3 = attrib_3

    def method_1(self):
        return True


    def method_2(self):
        return True


    def method_3(self):
        return True

    def get_attrib_1(self):
        return self.attrib_1
    def get_attrib_2(self):
        return self.attrib_2
    def get_attrib_3(self):
        return self.attrib_3

    def set_attrib_1(self, new_value):
        self.attrib_1 = new_value
    def set_attrib_2(self, new_value):
        self.attrib_2 = new_value
    def set_attrib_3(self, new_value):
        self.attrib_3 = new_value
        ```