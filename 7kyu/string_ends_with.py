#Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).
#
#Examples:
#
#solution('abc', 'bc') # returns true
#solution('abc', 'd') # returns false

#my solution
def solution(string, ending):
    if string.endswith(ending):
        return True 
    else: 
         return False  
solution("abcde" , "abcde")


def solution(string, ending):
    string1 = len(string) - len(ending)
    string2 = len(string) - string1
    string3 = string[string1:]
    if string3 == ending:
        return True
    else:
        return False