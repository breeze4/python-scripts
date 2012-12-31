#http://www.reddit.com/r/dailyprogrammer/comments/xdx4o/7302012_challenge_83_intermediate_indexed_file/

big_dictionary = {}

def index():
    
    #import sys
    #print sys.argv
    filenames = "pg11.txt", "pg62.txt", "pg74.txt"
    
    for filename in filenames:
        rawwords, allwords = [], []
        #open file and read it in as individual words
        with open("./" + filename) as f:
            rawwords = f.read().split()
        #sanitize the words    
        for word in rawwords:
            stripped_word = word.strip('|;:.,!$?\n')
            stripped_word = stripped_word.lower()
            allwords.append(stripped_word)
    
        word_index = list(set(allwords))

        for word in word_index:
            if word not in big_dictionary:
                big_dictionary[word] = [filename]
            else:
                temp_list_of_filenames = list(big_dictionary[word])
                temp_list_of_filenames.append(filename)
                big_dictionary[word] = list(set(temp_list_of_filenames))
        f.close()

def search():
    words_to_find = "and", "or", "huck"

    answer_list = []
    
    for search_word in words_to_find:
        if (search_word in big_dictionary) and len(answer_list) == 0:
            answer_list.extend(big_dictionary[search_word])
        elif search_word in big_dictionary:
            answer_list = list(set(answer_list).intersection(big_dictionary[search_word]))
        
    print answer_list
    

    
index()
search() 
