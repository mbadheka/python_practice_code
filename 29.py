#word counter using dictionary 

def word_counter(a):
    count = {}
    for i in a:
        count[i]= a.count(i)
    return count

print(word_counter("MalhAr"))