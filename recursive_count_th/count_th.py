'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    string = "th" 
    if string not in word:
        return 0
    # TBC
    
    if string in word:
        new_word = word.replace(string, "", 1)
    return count_th(new_word) + 1


print(count_th("abcthefthghith"))
print(count_th("THtHThth"))