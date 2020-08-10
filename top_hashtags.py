import string
def detect_tweet(N):
    # Opening and reading the tweet file
    file_handle1 = open("twitter_data.txt", "r", encoding = 'utf8') 
    lines = file_handle1.readlines()
    
    # Creating a new file, which contains the top hashtags.
    f = open("top_hashtags.txt", "w", encoding = "utf-8")
    
    d = {}
    l = []
    
    # Traversing through each word in the line and if each word in the line starts with a '#', then append it to the list and add it to the dictionary with a value of 1
    for line in lines:
        for word in line.split():
            if word[0] == '#':
                l.append(word)
                d[word] = 1
    
    # Traversing through every key in the dictionary and every word in the list and comparing the two; if any key is encountered in the list, the value of that key is incremented by 1
    for key in d.keys():
        for line in l:
            if key == line:
                d[key] += 1
    
    # Converting the counts of the each hashtag into a list and sorting it in descending order
    max_vals = sorted(list(set(d.values())), reverse=True)
    
    # Selecting only the N top hashtags
    req_max_vals = max_vals[0:N]
    
    # Writing the top N hashtags into the file
    for i in req_max_vals:
        for key, val in d.items():
            if i == val:
                print(key, ": ", val, file=f)
        
    f.close()
