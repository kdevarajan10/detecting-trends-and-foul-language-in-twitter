import string
def bad_word_detector(twitter_file):
    
    # Reading tweet file and swear word file
    file_handle1 = open(twitter_file, "r", encoding = 'utf8')
    file_handle2 = open("swear_words.txt", "r", encoding = 'utf8')
    
    l = file_handle2.readlines()
    l1 = []
    
    # Traverse through the list of swear words and remove the '\n' and add a space after each word
    for ln in l:
        l1.append(ln.strip("\n") + " ")
        
    lines = file_handle1.readlines()
    
    # Open the new file and if a swear word is found in the tweet, add tweet to new file
    with open("potentially_offensive_tweets.txt", "a", encoding = "utf-8") as f:
        f.truncate(0)
        cnt  = 0
        for line in lines:
            for word in l1:
                if word in line.lower():
                    #print(word, "->", line)
                    f.write(line)
                    #print("Wrote 1 tweet to file")
                    cnt += 1
        
    #print("Total number of offensive tweets = {}".format(cnt))            

    # close files
    file_handle2.close()
    file_handle1.close()
    
