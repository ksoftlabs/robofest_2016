import move
class Maze:
    def __init__(self):
        self.frontsonar=0
        self.backsonar=0
        self.rightsonar=0
        self.leftsonar=0
        self.path_count=0
        self.path=[]

    def move(self):
        mv=move.Control()

        f=self.frontsonar
        b=self.backsonar
        r=self.rightsonar
        l=self.leftsonar

        if l>5:
            mv.left(50)
        elif f>5:
            mv.forward(50)
        elif r>5:
            mv.forward(50)
        else:
            mv.turn_around(50)

    def record_path(self,move):
        self.path.append(move)
        if len(self.path)>2:
            last_moves=self.path[-3:]
            if last_moves==["L","B","R"]:
                self.path.pop()
                self.path.pop()
                self.path.pop()
                self.path.append("B")
            elif last_moves==["L","B","S"]:
                self.path.pop()
                self.path.pop()
                self.path.pop()
                self.path.append("R")
            elif last_moves==["L","B","L"]:
                self.path.pop()
                self.path.pop()
                self.path.pop()
                self.path.append("S")
            elif last_moves==["S","B","L"]:
                self.path.pop()
                self.path.pop()
                self.path.pop()
                self.path.append("R")
            elif last_moves==["S","B","S"]:
                self.path.pop()
                self.path.pop()
                self.path.pop()
                self.path.append("B")
            elif last_moves==["R","B","L"]:
                self.path.pop()
                self.path.pop()
                self.path.pop()
                self.path.append("B")

