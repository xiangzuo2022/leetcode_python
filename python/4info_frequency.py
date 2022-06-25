# Interview questions:

# Q1
# your goal is to aggregate the following text into a frequecy table of
# the letters (1-gram) and 2-grams vs their frequency

def get_one_grams(article):

    d = dict()           
    words = article.split()

    for word in words:
        for letter in word:            
            if 'a' <= letter <='z' or 'A'<= letter <= 'Z':                
                lower_letter = letter.lower()
                if lower_letter not in d:
                    d[lower_letter] = 1
                else:
                    d[lower_letter] += 1    
    return d


def get_two_grams(article):

    d = dict()
    words = article.split() 
    
    for word in words: 
        new = []
        for i in range(0,len(word)):
            if 'a' <= word[i] <='z' or 'A'<= word[i] <= 'Z':
                lower_letter = word[i].lower()
                new.append(lower_letter)

        for i in range(0,len(new)-1):
            tmp = new[i]+ new[i+1]
            if tmp not in d:
                d[tmp] = 1
            else:
                d[tmp] += 1  
    return d


# def find_most_popular_gram(d):
    
#     ans = []
#     for key in d:
#         if d[key] == max(d.values()):
#             ans.append(key)
#     return ans


if __name__ == '__main__':

    article = """Alice was beginning to get very tired of sitting by her sister on the
bank, and of having nothing to do. Once or twice she had peeped into the
book her sister was reading, but it had no pictures or conversations in
it, "and what is the use of a book," thought Alice, "without pictures or
conversations?"

So she was considering in her own mind (as well as she could, for the
day made her feel very sleepy and stupid), whether the pleasure of
making a daisy-chain would be worth the trouble of getting up and
picking the daisies, when suddenly a White Rabbit with pink eyes ran
close by her.

There was nothing so very remarkable in that, nor did Alice think it so
very much out of the way to hear the Rabbit say to itself, "Oh dear! Oh
dear! I shall be too late!" But when the Rabbit actually took a watch
out of its waistcoat-pocket and looked at it and then hurried on, Alice
started to her feet, for it flashed across her mind that she had never
before seen a rabbit with either a waistcoat-pocket, or a watch to take
out of it, and, burning with curiosity, she ran across the field after
it and was just in time to see it pop down a large rabbit-hole, under
the hedge. In another moment, down went Alice after it!"""

    get_one_grams(article)    
    get_two_grams(article)
    
# Q2
# find the most popular element (the 1-gram) in the frequency table
# The following program is written with Spark in python 

from pyspark import SparkConf, SparkContext
from operator import add


APP_NAME = "populargram"

def main(sc):
    text = sc.textFile("article.txt").map(lambda x:x.replace(',',' ').replace('.',' ').replace('-',' ').replace('?',' ').replace('!',' ').replace('-',' ').replace('(',' ').replace(')',' ').replace('"',' ')\
        .lower())\
    .map(lambda x:" ".join(x)).flatMap(lambda x:x.split()) 
    wc = text.map(lambda x:(x)).map(lambda x:(x,1))
    counts = wc.reduceByKey(add)
    output = counts.collect()
    sorts = sorted(output,key=lambda word:word[1],reverse=True)    
    print 'the most popular gram: ', sorts[0]
    print 'all grams list and frequency:' 
    for (letter,freq) in sorts:
        print letter, freq

   

if __name__ == "__main__":
    
    conf = SparkConf().setAppName(APP_NAME)
    conf = conf.setMaster("local[*]")
    sc   = SparkContext(conf=conf)   
    main(sc)
    sc.stop()

