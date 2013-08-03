#Christopher M. Church
#PhD Candidate, UC Berkeley, History
#Social Science D-Lab, UC Berkeley

import multiprocessing #import the multiprocessing library
import time #import the time library to time the entire job

start_time = time.time() #set the start time for the job

#this is the function that will be run as a process
def worker(num):
    """worker function"""
    process_name = multiprocessing.current_process().name
    print '%s: Worker %s Started' %(process_name,num)
    for i in range(20000000): number=0 #count to 20000000, this is for benchmarking purposes
    print process_name," Finished"
    end_time=time.time()
    print end_time-start_time #print the time it took for the process to finish
    return


def go():
    if __name__ == '__main__': #this is needed to insert the process on Windows -- not needed in Linux
        for i in range(3): #run three processes
            arguments_tuple=(i,) #(num,) -- arguements are passed to the process function in the form of a tuple
            p = multiprocessing.Process(target=worker,args=arguments_tuple) # define the process
            p.start() # start the process
            p.join()

go() #start the whole program (main function)