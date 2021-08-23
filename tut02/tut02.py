def get_memory_score(input_list):
    is_valid = True
    invalid_ListElements = []
    for i in input_list:
        if(isinstance(i, int) == False):
            is_valid = False
            invalid_ListElements.append(i)
    if is_valid:
        score = 0
        memory = []
        for i in input_list:
            if i in memory:
                score += 1
            else:
                memory.append(i)
                if(len(memory) > 5):
                    memory.pop(0)
        print("Score: ", score)
    else:
        print("Please enter a valid input list. Invalid inputs detected:",
              invalid_ListElements)


input_nums = [3, 4, 5, 3, 2, 1]
get_memory_score(input_nums)
