class father():
    def gardening(self):
        print("I enjoy gardening")

class mother():
    def cooking(self):
        print("I enjoy cooking")

class child(father,mother):
    def sports(self):
        print("i enjoy sports")

c = child()
c.gardening()
c.cooking()
c.sports()
