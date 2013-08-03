#Christopher M. Church
#PhD Candidate, UC Berkeley, History
#Social Science D-Lab, UC Berkeley

#this is a simple example with multiprocessing using map() and reduce() on an NLTK text
#it makes all the tokens in the Moby Dick text uppercase
#you can change the number of processes in the Pool by changing the variable chunks
#  n.b. 
#    with multiple cores / logical processors, you'll see an increase in performance as you up the chunks (to your number of cores), afterward it'll decrease in performance
#      -- on my QuadCore, the program took 0.81s with one process; 0.58s with two process; 0.38s with four processes; and 0.4s with eight processes
#    however, with a single core, you'll see a decrease in performance with more chunks
#      -- on a single CPU, it took .97s with one process; 1.2s with four processes

def chunker(tokens, chunks):
    '''this function -- generator -- chunks a set of tokens based on a number of chunks; each "chunk" of tokens will be sent to a separate process'''
    length = len(tokens) #the total number of tokens in the original
    chunk_size = len(tokens) / chunks #the size of each chunk (num of tokens / chunk)
    for x in xrange(0, length, chunk_size): #go through the original tokens in an increment equal to the size of each chunk
        yield tokens[x:x+chunk_size] #and return subsets equal to the size of the chunks

def worker(tokens):
    '''worker function for each process in the pool -- receives a chunk of tokens (tokens) and returns that chunk uppercase'''
    uppercase=[] #make an uppercase list
    for token in tokens: #for each token in the chunk, make it uppercase
        uppercase.append(token.upper())
    return uppercase #return the chunk of tokens

def parallel_process(chunks):
    '''how many chunks do we want; equals the number of processes'''
    partitioned_text = list(chunker(text1.tokens, chunks)) #partition the tokens up into X number of chunks [it's a nested list]
    p = multiprocessing.Pool(chunks) #create a pool of processes equal to the number of chunks
    start_time=time.time() #begin timer
    uppercase_text = p.map(func=worker,iterable=partitioned_text) #using map, send the partitioned_chunk nested list to the processes in the pool
    p.close() #close the pool of processes
    uppercase_text = reduce(operator.add,uppercase_text) #now reduce the returned chunks (now uppercase) into a single list again
    end_time=time.time() #end the timer
    print "---%s CHUNKS---" %(chunks)
    print "\tOriginal: ", text1.tokens[100:105] #see 5 arbitary tokens from the original
    print "\tUPPERCASE: ", uppercase_text[100:105] #see the same 5 tokens now uppercase
    print "\ttime: ", end_time-start_time #print the time it took to run the process
    
if __name__ == '__main__':
    '''this is the main function that will set up our pool of processes -- the { if __name ___ '__main__': } is need in order for multiprocessing to work on Windows OS'''
    #imports were put here because they were loading twice under Windows when put at the top of the file -- this is not an issue in Linux
    import multiprocessing #import the multiprocessing library
    import nltk #import the nltk library
    from nltk.book import text1 #import Moby Dick as an nltk text
    import operator #import the operator library (used during the reduce function)
    import time #import the time library; used for determining how quickly the code completed
    #nltk.download() #this is needed if the nltk books have net yet been downloaded 
    
    #RUN THE PROGRAM WITH ONE CHUNK AND ONE PROCESS
    test_runs = [1,2,4,8]
    for test in test_runs:
        parallel_process(test)