import itertools


def findsubsets(s, n):
    return list(itertools.combinations(s, n))



puzzle =[[0, 1, 2], [1, 3, 0] , [3,2,1],[4,4,3], [0,2,4]]
min =[]
issolution=0



colornum=15

colorcount = []

rotation = []
flip=[]

def gobackup(currentindex):
    global colorcount

    for j in range(3):
        colorcount[puzzle[currentindex][j]][j] -= 1  # go backup


def check(currentindex):


    for j in range(3):

        colorcount[puzzle[currentindex][j]][j] += 1

        if colorcount[puzzle[currentindex][j]][j] > 1:
            for x in range(j + 1):
                colorcount[puzzle[currentindex][x]][x] -= 1  # go backup
            return 1

    return 0


def rotate(index):

    puzzlepiece = puzzle[index]
    puzzlepiecerotated = [0, 0, 0]
    for j in range(3):
        puzzlepiecerotated[(j + 1) % 3] = puzzlepiece[j]

    puzzle[index] = puzzlepiecerotated

    rotation[index] = (rotation[index] + 1) % 3

def flip(index):
    global puzzle
    global flip
    puzzlepiece = puzzle[index]
    puzzlepiecefliped= [0, 0, 0]
    puzzlepiecefliped[0]=puzzlepiece[1]
    puzzlepiecefliped[1]=puzzlepiece[0]
    puzzlepiecefliped[2]=puzzlepiece[2]

    puzzle[index]=puzzlepiecefliped
    flip[index]=(flip[index]+1)%2





def SolutionChecker():
    k = 0
    global issolution
    while (k < len(puzzle) and k != -1):

        bad = check(k)

        if bad == 0:
            k += 1
        elif bad == 1:

            rotate(k)

            if rotation[k] == 0:

                k -= 1
                if (k == -1):
                    break
                gobackup(k)

                checkbool = 1

                while (checkbool == 1 and k > -1):

                    while (True):

                        rotate(k)
                        if rotation[k] == 0:
                            k -= 1
                            if (k>-1):
                                gobackup(k)
                            break
                        checkbool = check(k)

                        if (checkbool == 0):
                            break

                    if checkbool == 0:
                        k += 1

    if k == len(puzzle):
        #print("solutiion")


        issolution=1
        #print(puzzle)
    elif k == -1:
        #print("nosolution")

        issolution=0

def MO(MainPuzzle):

    for j in range(len(MainPuzzle)):
         subsetcheck = findsubsets(MainPuzzle, len(MainPuzzle)-j)


         for i in range(len(subsetcheck)):
             global puzzle
             puzzle=list(subsetcheck[i])
             global colorcount
             colorcount = [[0 for x in range(3)] for y in range(colornum)]
             global rotation
             rotation = [0] * len(puzzle)
             SolutionChecker()

             if issolution==0:
                 global min
                 min=puzzle
                 break

         if issolution == 1:
             break

    print(len(min))
    print(min)




def SolutionCheckerwithflips():
    k = 0
    global issolution

    while (k < len(puzzle) and k != -1):

        bad = check(k)

        if bad == 0:
            k += 1
        elif bad == 1:

            rotate(k)

            if rotation[k] == 0:

                flip(k)
                if flip[k]==0:

                    k -= 1
                    if (k == -1):
                        break
                    gobackup(k)

                    checkbool = 1

                    while (checkbool == 1 and k != -1):

                        while (True):

                            rotate(k)
                            if rotation[k] == 0:
                                flip(k)
                                if flip[k] == 0:
                                    k -= 1
                                    if (k > -1):
                                        gobackup(k)
                                    break
                                checkbool = check(k)

                                if (checkbool == 0):
                                    break

                        if checkbool == 0:
                            k += 1

    if k == len(puzzle):
        print("solutiion")
        issolution = 1
        # print(puzzle)
    elif k == -1:
         print("nosolution")

         issolution = 0

def PuzzleCheck(MainPuzzle):
    global puzzle
    puzzle= MainPuzzle
    global colorcount
    colorcount= [[0 for x in range(3)] for y in range(colornum)]
    global rotation
    rotation = [0] * len(puzzle)
    global flip
    flip = [0]*len(puzzle)
    SolutionCheckerwithflips()
    print(puzzle)


#BigPuzzle=[[0,1,2],[3,0,1],[1,3,0]]
#PuzzleCheck(BigPuzzle)
#BigPuzzle=[[0,1,2],[3,2,1],[3,1,2]]
#MO(BigPuzzle)
BigPuzzle=[[4, 9, 7], [1, 4, 3], [8, 3, 4], [3, 6, 5],[7,5,10],[7,5,2]]
#PuzzleCheck(BigPuzzle)
MO(BigPuzzle)
#subsetcheck=findsubsets(PS,5)
#print(subsetcheck)
#print(subsetcheck[0])


#X=[1,1,1,2,2,2,3,3,3,4,4,4,5,5,5]
#Y=list(itertools.permutations(X))

