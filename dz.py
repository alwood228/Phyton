class MyClass:
    def Call(self, param):
        self.check_type(param)

    def check_type(self, param):
        if isinstance(param, int):
            print("its int .")
        elif isinstance(param, float):
            print("its float.")
        elif isinstance(param, str):
            print("its str")