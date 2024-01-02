# The task is to check weather by removing at most one character, 
# the string matches with its reversed counterpart. 
# When s = ‘radkar’ the function returns Trueas by excluding the ‘k’ 
# we obtain the word ‘radar’ that is a palindrome.

#word = input("")
word = "refer"

def CheckPail(w):
    is_palindrome = False

    re_word_front = ""
    re_word_last = ""
    re_word = ""

    for i in range(len(w)):
        if i == 0:
          re_word = word[1:]
        else:
            re_word_front = word[:(i-1)]
            re_word_last = word[i:]

            re_word = (re_word_front + re_word_last)

        if re_word == re_word[::-1]:
            print(word, "is a palindrome just remove the letter", word[i - 1])
            is_palindrome = True
    if not is_palindrome:
        print(word, "is not a palindrome")

    exit()
    
     
CheckPail(word)

#DONE