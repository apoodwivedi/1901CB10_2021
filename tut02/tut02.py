def get_memory_score(n):
    score = 0
    memory = []           # empty list to store numbers in memory
    for i in n:         # iterating through the input list
        if i in memory:    # checking if the element is already in memory and increase the score if present
            score += 1
        else:
            # if element already not present , add that element in the memory
            memory.append(i)
            if (len(memory) > 5):   # the player can remember a maximum of 5 previously called out numbers , so if memory size >5
                # remove the number that has been in the player's memory the longest time i.e first element
                memory.pop(0)

    print("Score: ", score)  # print the final score


input_nums = [3, 4, 5, 3, 2, 1]
# checking if list has only integers
# boolean variable that stores true if list is valid and false if invalid (default value=true)
is_valid = True
# empty list to store any invalid inputs (if present)
invalid_ListElements = []
for i in input_nums:          # iterating through the list
    if(isinstance(i, int) == False):   # checking if an element of list is int or not
        is_valid = False
        # if element = non int, store it in the invalid element list
        invalid_ListElements.append(i)
if is_valid:
    # if the list is valid, pass it to the get memory func to execute the required program
    get_memory_score(input_nums)
else:
    # if invalid list, display appropriate msg along with invalid elements
    print("Please enter a valid input list. Invalid inputs detected:",
          invalid_ListElements)
