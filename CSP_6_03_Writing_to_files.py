import random

#You need to create your own test file for this assignment.
#Because we are dealing with both reading and writing to files.
# Your test file will be more complicated than it has been.

def writeFile(inputList, fileName):
    #Creates a file of the given name and adds each value from
    # the list to said file with each line being an index from the list.
    with open(fileName, "w") as f:
        for item in inputList:
            f.write(str(item) + "\n")

    pass


def sortNames(fileName, targetFile):
    #Modify the below function such that it takes in source file and a target file.
    #Sort all of the values from the source file and write them to the target file
    #I recommend using .sort() for this. You do not need to write the sorting algorithm yourself.
    with open(fileName, "r") as f:
        names = f.read().splitlines()
    names.sort()
    with open(targetFile, "w") as f:
        for name in names:
            f.write(name + "\n")
    pass

sortNames("6_03_test_names.txt","namesNew.txt")



def highScore( newScore: int):
    #Modify the function such that it adds a new score to the file scores.txt
    #Then return the average score from all of the scores in scores.txt
    with open("scores.txt", "a") as f:
        f.write(str(newScore) + "\n")
    with open("scores.txt", "r") as f:
        scores = f.read().splitlines()
    total = sum(int(score) for score in scores if score.strip() != "")
    average = total / len(scores)
    return average
    pass


