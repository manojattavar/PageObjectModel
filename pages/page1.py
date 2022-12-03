from pages.page2 import page2


class page1:
    def __init__(self, a):
        self.a = a

    def page1(self):
        print("in page 1")
        print(self.a)
        return page2(self.a)