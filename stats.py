def num_of_words(body):
    words = body.split()
    result = len(words)
    return result

def character_count(body):
    letter_frequency = {}
    letters = body.lower()
    for letter in letters:
        if letter in letter_frequency: 
            letter_frequency[letter] += 1
        else : 
         letter_frequency[letter] = 0
         letter_frequency[letter] += 1 
    return letter_frequency

def num_return(item):
    return item["num"] 

def sorted_list(letter_frequency):
    dict_list = []
    for char, count in letter_frequency.items():
        new_dict = {"char": char, "num": count}
        dict_list.append(new_dict)     
    dict_list.sort(reverse=True, key = num_return)
    return dict_list