import Puzzle
def SolutionChecker(mainPuzzle):
    k = 0


    while (k < len(mainPuzzle.puzzle) and k != -1):

        bad = mainPuzzle.check(k)

        if bad == 0:
            k += 1
        elif bad == 1:

            mainPuzzle.rotate(k)

            if mainPuzzle.rotationindex(k) == 0:

                k -= 1
                if (k == -1):
                    break
                mainPuzzle.gobackup(k)

                checkbool = 1

                while (checkbool == 1 and k > -1):

                    while (True):

                        mainPuzzle.rotate(k)
                        if mainPuzzle.rotationindex(k)== 0:
                            k -= 1
                            if (k>-1):
                                mainPuzzle.gobackup(k)
                            break
                        checkbool = mainPuzzle.check(k)

                        if (checkbool == 0):
                            break

                    if checkbool == 0:
                        k += 1

    if k == len(mainPuzzle.puzzle):
        #print("solutiion")
        mainPuzzle.ChangeSolution(1)


        #print(puzzle)
    elif k == -1:
        #print("nosolution")
        mainPuzzle.ChangeSolution(0)
