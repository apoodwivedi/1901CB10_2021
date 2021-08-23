def get_memory_score(input_list):
    # checking if list has only integer
    # boolean variable that stores true if list is valid and false if invalid (default value=true)
    is_valid = True
    # empty list to store any invalid inputs (if present)
    invalid_ListElements = []
    for i in input_list:        # iterating through the list
        if(isinstance(i, int) == False):    # checking if an element of list is int or not
            is_valid = False
            # if element = non int, store it in the invalid element list
            invalid_ListElements.append(i)
    if is_valid:     # if the list is valid calculate score
        score = 0
        memory = []   # empty list to store user memory
        for i in input_list:  # iterating through the list
            if i in memory:  # if the number is already in memory
                score += 1  # score increases by 1
            else:
                memory.append(i)    # if number not present add into the list
                if(len(memory) > 5):  # the player can remember a maximum of 5 previously called out numbers
                    # so removed the number which stayed in the memory for longest time i.e. first element
                    memory.pop(0)
        return "Score: " + str(score)  # return score
    else:
        # if invalid list display appropriate msg and invalid list elements
        return "Please enter a valid input list. Invalid inputs detected:"+str(invalid_ListElements)


input_nums = [3, 4, 5, 3, 2, 1]
# printing score by invoking the function with the input list
print(get_memory_score(input_nums))
