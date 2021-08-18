# func to detect meraki number

def meraki_helper(n):
    lengthOfList = len(n)  # size of input list
    countMeraki = 0  # counter for number of mearki numbers

    # iterating through list of input
    for i in range(lengthOfList):
        meraki_yes = True
        # type casting each number to string for easier navigation through digits
        element = str(n[i])
        lengthOfString = len(element)  # length of string

        if(lengthOfString == 1):
            meraki_yes = True
            countMeraki += 1
        else:
            for i in range(0, lengthOfString-1):
                # checking if the diff between adjacent digits is 1 by casting string back into integer
                if(abs(int(element[i])-int(element[i+1])) == 1):
                    meraki_yes = True
                    countMeraki += 1
                    break

        ans = "Yes" if meraki_yes else "No"
        x = " not" if meraki_yes != True else ""
        print("{} - {} is{} a Meraki number".format(ans, element, x))

    non_meraki = lengthOfList - countMeraki  # count of non-meraki numbers
    print("The input list contains {} Meraki and {} Non-Meraki numbers".format(countMeraki, non_meraki))


input = [12, 14, 56, 78, 98, 54, 678, 134,
         789, 0, 7, 5, 123, 45, 76345, 987654321]
meraki_helper(input)  # passing list into the function
