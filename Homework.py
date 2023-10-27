class MainClass:
    def __init__(self, text):
        self.text_field = text

    def set_text(self, text):
        self.text_field = text

class ChildClass(MainClass):
    def __init__(self, text, number):
        super().__init__(text)
        self.number_field = number

main_obj = MainClass("Привет, мир!")
print("Значение поля в MainClass:", main_obj.text_field)

main_obj.set_text("Измененный текст в MainClass")
print("Измененное значение поля в MainClass:", main_obj.text_field)

child_obj = ChildClass("Привет из ChildClass!", 42)
print("Значение текстового поля в ChildClass:", child_obj.text_field)
print("Значение числового поля в ChildClass:", child_obj.number_field)
