from pages.page3 import page3


class page2:
    def __init__(self, a):
        self.a = a

    def page2(self):
        print("in page 2")
        print(self.a)
        return page3(self.a)