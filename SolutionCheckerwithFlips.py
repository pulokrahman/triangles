import Puzzle
def SolutionCheckerwithflips(MainPuzzle):
    k = 0


    while (k < len(MainPuzzle.puzzle) and k != -1):

        bad = MainPuzzle.check(k)

        if bad == 0:
            k += 1
        elif bad == 1:

            MainPuzzle.rotate(k)

            if MainPuzzle.rotationindex(k) == 0:

                MainPuzzle.flipit(k)
                if MainPuzzle.FlipIndex(k)==0:

                    k -= 1
                    if (k == -1):
                        break
                    MainPuzzle.gobackup(k)

                    checkbool = 1

                    while (checkbool == 1 and k != -1):

                        while (True):

                            MainPuzzle.rotate(k)
                            if MainPuzzle.rotationindex(k)== 0:
                                MainPuzzle.flipit(k)
                                if MainPuzzle.FlipIndex(k) == 0:
                                    k -= 1
                                    if (k > -1):
                                        MainPuzzle.gobackup(k)
                                    break
                                checkbool = MainPuzzle.check(k)

                                if (checkbool == 0):
                                    break

                        if checkbool == 0:
                            k += 1

    if k == len(MainPuzzle.puzzle):
        print("solutiion")
        MainPuzzle.ChangeSolution(1)
        # print(puzzle)
    elif k == -1:
         print("nosolution")
         MainPuzzle.ChangeSolution(0)
