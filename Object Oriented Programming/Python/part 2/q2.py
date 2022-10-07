from exception import Lab5Exception
def weirdProblem(num):
    # for row in num:
    #     for i in range(len(row)):
    #         print(row[i])
    if(type(num))!=list:
         raise Lab5Exception("Exception Occured: Incorrect type")
    max_length=-1
    for i in range(len(num)):
        if len(num[i]) > max_length:
            max_length = len(num[i])
    ans_list = []
    for j in range(max_length):
        for i in range(len(num)):
            if j < len(num[i]):
                ans_list.append(num[i][j])
    ans_list_string = ' '.join(ans_list)
    return ans_list_string

if __name__ == "__main__":

    """
    Main function

    Example call:
    You can use the following list of lists "L" for testing your solution.
    For running the code, use the command "python q2.py" 
    
    L = [ ["this", "programming", "is"], ["is", "assignment", "kinda"], ["a", "which", "weird"]  ]
    converted_string = weirdProblem(L)
    print(converted_string)

    Console output should be: this is a programming assignment which is kinda weird

    """
