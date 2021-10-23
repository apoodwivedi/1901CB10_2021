import shutil
import os
import re

inputFolder = os.path.join(os.getcwd(), "wrong_srt")
outputFolder = os.path.join(os.getcwd(), "corrected_srt")


def rename_BreakingBad():
    breakingbad = "Breaking Bad"
    breakingbad_input = os.path.join(inputFolder, breakingbad)
    breakingbad_output = os.path.join(outputFolder, breakingbad)

    if os.path.exists(breakingbad_output):
        shutil.rmtree(breakingbad_output)
    os.mkdir(breakingbad_output)

    for name in os.listdir(breakingbad_input):
        removeUnrequired = re.split("\s720.*dr", name)
        seriesNamesplit = re.split("\sse?", removeUnrequired[0])

        seasonNepisode = list(map(int, re.split("e",  seriesNamesplit[1])))

        correctedName = (seriesNamesplit[0] + " Season " + str(seasonNepisode[0]).zfill(
            season_padding) + " Episode " + str(seasonNepisode[1]).zfill(episode_padding) + removeUnrequired[1])

        correctAnswer = os.path.join(breakingbad_output, correctedName)
        wrongAnswer = os.path.join(breakingbad_input, name)
        shutil.copy(wrongAnswer, correctAnswer)

    return


def rename_gameOfThrones():
    got = "Game of Thrones"
    got_input = os.path.join(inputFolder, got)
    got_output = os.path.join(outputFolder, got)

    if os.path.exists(got_output):
        shutil.rmtree(got_output)
    os.mkdir(got_output)

    for name in os.listdir(got_input):
        removeUnrequired = re.split("\..*en", name)
        seriesNamesplit = re.split("\s\- ", removeUnrequired[0])

        seasonNepisode = list(
            map(int, re.split("x", seriesNamesplit[1])))

        correctedName = (got + " - Season " + str(int(seasonNepisode[0])).zfill(season_padding) + " Episode " + str(
            int(seasonNepisode[1])).zfill(episode_padding) + " - " + seriesNamesplit[2] + removeUnrequired[1])

        correctAnswer = os.path.join(got_output, correctedName)
        wrongAnswer = os.path.join(got_input, name)
        shutil.copy(wrongAnswer, correctAnswer)

    return


def rename_Lucifer():
    lucifer = "Lucifer"
    lucifer_input = os.path.join(inputFolder, lucifer)
    lucifer_output = os.path.join(outputFolder, lucifer)

    if os.path.exists(lucifer_output):
        shutil.rmtree(lucifer_output)
    os.mkdir(lucifer_output)

    for name in os.listdir(lucifer_input):
        removeUnrequired = re.split("\..*en", name)
        seriesNamesplit = re.split("\s\- ", removeUnrequired[0])

        seasonNepisode = list(map(int, re.split("x", seriesNamesplit[1])))

        correctedName = (seriesNamesplit[0] + " - Season " + str(int(seasonNepisode[0])).zfill(season_padding) + " Episode " + str(
            int(seasonNepisode[1])).zfill(episode_padding) + " - " + seriesNamesplit[2] + removeUnrequired[1])

        correctAnswer = os.path.join(lucifer_output, correctedName)
        wrongAnswer = os.path.join(lucifer_input, name)
        shutil.copy(wrongAnswer, correctAnswer)

    return


def regex_renamer():

    # Taking input from the user

    print("1. Breaking Bad")
    print("2. Game of Thrones")
    print("3. Lucifer")

    global season_padding, episode_padding
    webseries_num = int(
        input("Enter the number of the web series that you wish to rename. 1/2/3: ")
    )
    season_padding = int(input("Enter the Season Number Padding: "))
    episode_padding = int(input("Enter the Episode Number Padding: "))

    if not os.path.exists(outputFolder):
        os.mkdir(outputFolder)
    if webseries_num == 1:
        rename_BreakingBad()
    elif webseries_num == 2:
        rename_gameOfThrones()
    elif webseries_num == 3:
        rename_Lucifer()
    else:
        print("Please enter a valid input.")


regex_renamer()
