class human:
    def __init__(self,n,o):
        self.name = n
        self.occupation = o

    def do_work(self):
        if self.occupation == "tennis player":
            print(self.name,"plays tennis")
        elif self.occupation == "actor":
            print(self.name,"shoots a film")


    def speaks(self):
        print(self.name,"says how are you")

tom = human("tom cruise","actor")
tom.do_work()
tom.speaks()

