class Foo():
    def __init__(self):
        pass

    def __str__(self) -> str:
        return "super().__str__()"


f = Foo()
print(f)
