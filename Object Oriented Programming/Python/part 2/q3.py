from exception import Lab5Exception
def set_union(collection_one, collection_two):
    """
        This function, as the name implies, should output 
        the result of union of two sets. Note that the input might not
        be valid sets. You are to check the validity. 

        You are expected to think of all possible corner cases of 
        you code and raise Exception accordingly.
    # """
    if((type(collection_one))!=list) and (type(collection_one)!=tuple):
         raise Lab5Exception("Exception Occured: Incorrect type")
    if((type(collection_two))!=list) and (type(collection_two)!=tuple):
         raise Lab5Exception("Exception Occured: Incorrect type")
    answer_list = []
    for x in collection_one:
        answer_list.append(x)
    for y in collection_two:
        if y not in answer_list:
            answer_list.append(y)

    # print(answer_list)
    return answer_list
    pass
    

def set_intersection(collection_one, collection_two):
    """
        This function, as the name implies, should output 
        the result of intersection of two sets. Note that the input might not
        be valid sets. You are to check the validity. 

        You are expected to think of all possible corner cases of 
        you code and raise Exception accordingly.
    """
    if((type(collection_one))!=list) and (type(collection_one)!=tuple):
         raise Lab5Exception("Exception Occured: Incorrect type")
    if((type(collection_two))!=list) and (type(collection_two)!=tuple):
         raise Lab5Exception("Exception Occured: Incorrect type")
    answer_list = []
    for x in collection_one:
        for y in collection_two:
            if x == y:
                answer_list.append(x)
    # print(answer_list)
    return answer_list
    pass

def set_equality(collection_one, collection_two):
    """
        This function, as the name implies, should check whether
        or not two sets are equal. Note that the input might not
        be valid sets. You are to check the validity. 

        You are expected to think of all possible corner cases of 
        you code and raise Exception accordingly.
    """
    if((type(collection_one))!=list) and (type(collection_one)!=tuple):
         raise Lab5Exception("Exception Occured: Incorrect type")
    if((type(collection_two))!=list) and (type(collection_two)!=tuple):
         raise Lab5Exception("Exception Occured: Incorrect type")
    min_len = min(len(collection_one),len(collection_two))
    for i in range(min_len):
        if collection_one[i] != collection_two[i]:
            return False
    return True
    pass

def parse_file(file_name):
    """
        This function is expected to parse a text (.txt) file
        and extract pairs of collections from it.

        Note that the parsed collections might not be valid sets.
        Please check and accordingly raise Exception. You should also
        think about other corner cases of your code and raise the Exception
        accordingly.
    """
    substr=".txt"
    if(substr not in file_name):
        raise Lab5Exception("Exception Occured: Incorrect File type")
    txt_file = open(file_name, "r")
    file_content = txt_file.read()

    content_list = file_content.split("    ")

    content_list_1 = list(content_list[0])
    content_list_2 = list(content_list[1])
    if ((content_list_1[0]=='[' and content_list_1[len(content_list_1)-1]==']') or (content_list_1[0]=='(' and content_list_1[len(content_list_1)-1]==')')) ==0:
        raise Lab5Exception("Exception Occured: Incorrect type")

    while '[' in content_list_1:
        content_list_1.remove('[')
    while ']' in content_list_1:
        content_list_1.remove(']')    
    while '(' in content_list_1:
        content_list_1.remove('(')
    while ')' in content_list_1:
        content_list_1.remove(')')
    while ',' in content_list_1:
        content_list_1.remove(',')
    while ' ' in content_list_1:
        content_list_1.remove(' ')
    while '\'' in content_list_1:
        content_list_1.remove('\'')
    
    if ((content_list_2[0]=='[' and content_list_2[len(content_list_2)-1]==']') or (content_list_2[0]=='(' and content_list_2[len(content_list_2)-1]==')')) ==0: 
        raise Lab5Exception("Exception Occured: Incorrect type")

    while '[' in content_list_2:
        content_list_2.remove('[')
    while ']' in content_list_2:
        content_list_2.remove(']')    
    while '(' in content_list_2:
        content_list_2.remove('(')
    while ')' in content_list_2:
        content_list_2.remove(')')
    while ',' in content_list_2:
        content_list_2.remove(',')
    while ' ' in content_list_2:
        content_list_2.remove(' ')
    while '\'' in content_list_2:
        content_list_2.remove('\'')
    
    parsed_content_list = []
    parsed_content_list.append(content_list_1)
    parsed_content_list.append(content_list_2)
    return parsed_content_list
    pass
