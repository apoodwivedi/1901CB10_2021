
import os
import sys
import shutil

os.system("cls")


input_file = "regtable_old.csv"
firstRow = "rollno,register_sem,sub_no,sub_type\n"


def output_by_subject():
    outputFolder = "output_by_subject"
    file = open(input_file)

    if(os.path.exists(outputFolder)):
        shutil.rmtree(outputFolder)
    os.mkdir(outputFolder)

    for idx, line in enumerate(file.readlines()):
        if idx == 0:
            continue
        outputLst = line.split(',')  # split the contents of a `line` by comma

        # output file name
        output_file = os.path.join(outputFolder, outputLst[3] + ".csv")

        if not os.path.exists(output_file):
            with open(output_file, "w") as headerInput:
                headerInput.write(firstRow)

        outputFile = open(output_file, "a")
        rows = outputLst[0] + "," + outputLst[1] + \
            "," + outputLst[3] + "," + outputLst[8]
        outputFile.write(rows)
    outputFile.close()
    return


def output_individual_roll():
    file = open(input_file)
    outputFolder = "output_individual_roll"

    if(os.path.exists(outputFolder)):
        shutil.rmtree(outputFolder)
    os.mkdir(outputFolder)

    for j, line in enumerate(file.readlines()):
        if j == 0:
            continue
        outputlst = line.split(',')

        output_file = os.path.join(outputFolder, outputlst[0] + ".csv")

        if not os.path.exists(output_file):
            with open(output_file, "w") as header:
                header.write(firstRow)

        outputFile = open(output_file, "a")
        rows = outputlst[0] + "," + outputlst[1] + \
            "," + outputlst[3] + "," + outputlst[8]
        outputFile.write(rows)
    outputFile.close()
    return


output_by_subject()
output_individual_roll()
