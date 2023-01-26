import pandas as pd
import csv
import re
import time
import os, psutil
start_time = time.time()
process = psutil.Process(os.getpid())

def result_fun():
    print("File text Replace Success")
    memory_bytes = process.memory_info().rss
    mb = memory_bytes/1048576
    memory_mb = "{} MB".format(mb)
    print("Memory Taken in Bytes",memory_bytes)
    print("Memory Taken in Mb",memory_mb)
    time_secs = (time.time() - start_time)
    time_mins = time.strftime("%M minutes %S seconds",time.gmtime(time_secs))
    print("Time Taken process --- %s" % time_secs)
    print("Time Taken process --- %s" % time_mins)

    performance = open("/Users/apple/Downloads/performance.txt","w+")
    performance.write("Time to process: %s" % time_mins)
    performance.write("\nMemory used: %s" % memory_mb)
    performance.close()

    #df = pd.read_csv("/Users/apple/Downloads/translatewords/t8shakespeare.txt",on_bad_lines='skip',sep=" ")
    #print(df)
    #df1 = pd.read_csv(r'/Users/apple/Downloads/translatewords/french_dictionary.csv')
    #print(df1)

def word_replace_fun(stext,rtext):
    search_text = stext
    replace_text = rtext
    with open(r'/Users/apple/Downloads/translatewords/t8shakespeare.txt', 'r') as file:
        data = file.read()

    #get number of occurrences of the substring in the string
    redata = re.compile(re.escape(stext),re.IGNORECASE)
    new_text = redata.sub(stext,data)
    occurrences = new_text.count(stext)
    if occurrences > 0:
        print('Number of times replace of the word ',stext,' :', occurrences)
        data2 = [stext,rtext,occurrences]
        array.append(data2)
        with open('/Users/apple/Downloads/frequency.csv', 'w+') as f:
            frequency = csv.writer(f)
            frequency.writerows(array)
        data = new_text.replace(search_text, replace_text)
        
        with open(r'/Users/apple/Downloads/t8.shakespeare.translated.txt', 'w+') as file:
            file.write(data)

def main():
    header = ['English word','French word','Frequency']
    array.append(header)
    with open("/Users/apple/Downloads/translatewords/french_dictionary.csv") as csvfile:
        reader = csv.reader(csvfile)    
        for row in reader: 
            word_replace_fun(row[0],row[1])
    result_fun()

array = []
main()

  


