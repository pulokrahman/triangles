import itertools
import Puzzle
import SolutionCheckerNoFlips


def findsubsets(s, n):
    return list(itertools.combinations(s, n))


class MinObstacle:
    def __init__(self):
        self.MO = Puzzle.Puzzle([], 0)

    def changeMin(self, puzzle):
        self.MO = puzzle


def MO(MainPuzzle):
    Min = MinObstacle()
    for j in range(len( MainPuzzle.puzzle)):
        subsetcheck = findsubsets(MainPuzzle.puzzle, len(MainPuzzle.puzzle) - j)

        booleanFoundObstacle = 1
        for i in range(len(subsetcheck)):
            newPuzzle = Puzzle.Puzzle(list(subsetcheck[i]), len(MainPuzzle.colorcount))

            SolutionCheckerNoFlips.SolutionChecker(newPuzzle)

            if newPuzzle.HasSolution == 0:
                Min.changeMin(Puzzle.Puzzle(list(subsetcheck[i]), len(MainPuzzle.colorcount)))
                del newPuzzle
                booleanFoundObstacle = 0
                break
            del newPuzzle
        if booleanFoundObstacle == 1:
            break
    print(len(Min.MO.puzzle))

    print(Min.MO.puzzle)

