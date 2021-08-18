# func to detect meraki number

def meraki_helper(n):
    lengthOfList = len(n)  # size of input list
    countNonMeraki = 0  # counter for number of non meraki numbers

    # iterating through list of input
    for i in range(lengthOfList):
        is_meraki = True     
        element = str(n[i])   # type casting each number to string for easier navigation through digits
        lengthOfString = len(element)  # length of string

        if(lengthOfString == 1):
            is_meraki = True  # single digit number is always meraki
        else:
            for i in range(0, lengthOfString-1):      # checking if the diff between adjacent digits is 1 by casting string back into integer
              
                if(abs(int(element[i])-int(element[i+1])) != 1):
                    is_meraki = False
                    countNonMeraki += 1
                    break

        if is_meraki:
            ans = "Yes"
        else:
            ans = "No"

        if is_meraki == False:
            x = " not"
        else:
            x = ""

        print("{} - {} is{} a Meraki number".format(ans, element, x))

    countMeraki = lengthOfList - countNonMeraki  # count of meraki numbers
    print("The input list contains {} Meraki and {} Non-Meraki numbers".format(countMeraki, countNonMeraki))


input = [12, 14, 56, 78, 98, 54, 678, 134,
         789, 0, 7, 5, 123, 45, 76345, 987654321]

meraki_helper(input)  # passing list into the function
