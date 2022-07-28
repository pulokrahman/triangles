class Puzzle:
    def __init__(self,puzzle,colornum):

        self.puzzle=puzzle
        self.rotation= [0] * len(puzzle)
        self.colorcount = [[0 for x in range(3)] for y in range(colornum)]
        self.flip =[0] * len(puzzle)
        self.HasSolution=0
    def gobackup(self,currentindex):


        for j in range(3):
            self.colorcount[self.puzzle[currentindex][j]][j] -= 1  # go backup

    def check(self,currentindex):

        for j in range(3):

            self.colorcount[self.puzzle[currentindex][j]][j] += 1

            if self.colorcount[self.puzzle[currentindex][j]][j] > 1:
                for x in range(j + 1):
                    self.colorcount[self.puzzle[currentindex][x]][x] -= 1  # go backup
                return 1

        return 0

    def rotate(self,index):

        puzzlepiece = self.puzzle[index]
        puzzlepiecerotated = [0, 0, 0]
        for j in range(3):
            puzzlepiecerotated[(j + 1) % 3] = puzzlepiece[j]

        self.puzzle[index] = puzzlepiecerotated

        self.rotation[index] = (self.rotation[index] + 1) % 3

    def flipit(self,index):

        puzzlepiece = self.puzzle[index]
        puzzlepiecefliped = [0, 0, 0]
        puzzlepiecefliped[0] = puzzlepiece[1]
        puzzlepiecefliped[1] = puzzlepiece[0]
        puzzlepiecefliped[2] = puzzlepiece[2]

        self.puzzle[index] = puzzlepiecefliped
        self.flip[index] = (self.flip[index] + 1) % 2

    def rotationindex(self,index):
        return self.rotation[index]

    def ChangeSolution(self,solution):
        self.HasSolution=solution

    def FlipIndex(self,index):
        return self.flip[index]

