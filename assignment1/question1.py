
def common_words(filename):
    """question 1a

    Write a function that takes a path to a text file as input. The function
    should open the file, count the number of occurrences of each word, and
    return a sorted list of the most common words.
    """
    f = open(filename)
    allthings = f.read()
    f.close()
    
    L = []
    word = ""
    start = False
    for i in allthings:

        if i.isalpha() and start == False: #means we got to a new word, start new word
            word = i.lower()
            start = True

        elif (i.isalpha() or i == '\'' or i == '-') and start == True:
            word += i.lower()

        elif not (i.isalpha() or i == '\'' or i == '-') and start == True: #means we finished a word
            #print word
            L.append(word)
            word = ""
            start = False

        else: #if i not isalpha() and start == False
            pass #do nothing, just move to next letter

    Lout = sorted(list(set(L)), key=L.count, reverse = True)
    return Lout

def common_words_min(filename, min_chars):
    """question 1b

Modify this function to take a second argument that specifies the
    minimum number of characters long a word can be to be counted.
    """
    f = open(filename)
    allthings = f.read() #puts it in a string
    f.close()
    
    L = []
    word = ""
    ct = 0
    start = False
    for i in allthings:

        if i.isalpha() and start == False: #means we got to a new word, start new word
            word = i.lower()
            start = True
            ct = 1

        elif (i.isalpha() or i == '\'' or i == '-') and start == True:
            word += i.lower()
            ct += 1

        elif not (i.isalpha() or i == '\'' or i == '-') and start == True: #means we finished a word
            if ct >= min_chars:
                L.append(word)
            word = ""
            start = False

        else: #if i not isalpha() and start == False
            pass #do nothing, just move to next letter

    Lout = sorted(list(set(L)), key=L.count, reverse = True)

    return Lout

def common_words_tuple(filename, min_chars):
    """question 1c

    Modify this function to return a list of tuples rather than just a list
    of strings. Each tuple should be of the format
        (word, number of occurrences)
    Of course, the list of tuples should still be sorted as in part a.
    """

    f = open(filename)
    allthings = f.read() #puts it in a string
    f.close()
    
    L = []
    word = ""
    ct = 0
    start = False
    for i in allthings:

        if i.isalpha() and start == False: #means we got to a new word, start new word
            word = i.lower()
            start = True
            ct = 1

        elif (i.isalpha() or i == '\'' or i == '-') and start == True:
            word += i.lower()
            ct += 1

        elif not (i.isalpha() or i == '\'' or i == '-') and start == True: #means we finished a word
            if ct >= min_chars:
                L.append(word)
            word = ""
            start = False

        else: #if i not isalpha() and start == False
            pass #do nothing, just move to next letter

    Lout = sorted(list(set(L)), key=L.count, reverse = True)

    Ltup = []
    prev = Lout[0]
    tup = (prev, Lout.count(prev))
    
    Ltup.append(tup)

    for curr in Lout:
        if curr != prev: # new word
            tup = (curr, L.count(curr))
            Ltup.append(tup)
    
    return Ltup

def common_words_safe(filename, min_chars):
    """question 1d

    Modify your function so that it catches the IOError exception and prints
    a friendly error message.
    """
    try:
        f = open(filename)
    except IOError:
        print('Sorry!  File {} could not be found'.format(filename))
            break

    allthings = f.read() #puts it in a string
    f.close()
    
    L = []
    word = ""
    ct = 0
    start = False
    for i in allthings:

        if i.isalpha() and start == False: #means we got to a new word, start new word
            word = i.lower()
            start = True
            ct = 1

        elif (i.isalpha() or i == '\'' or i == '-') and start == True:
            word += i.lower()
            ct += 1

        elif not (i.isalpha() or i == '\'' or i == '-') and start == True: #means we finished a word
            if ct >= min_chars:
                L.append(word)
            word = ""
            start = False

        else: #if i not isalpha() and start == False
            pass #do nothing, just move to next letter

    Lout = sorted(list(set(L)), key=L.count, reverse = True)

    Ltup = []
    prev = Lout[0]
    tup = (prev, Lout.count(prev))
    
    Ltup.append(tup)

    for curr in Lout:
        if curr != prev: # new word
            tup = (curr, L.count(curr))
            Ltup.append(tup)
    
    return Ltup
