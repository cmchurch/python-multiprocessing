#Christopher M. Church
#PhD Candidate, UC Berkeley, History
#Social Science D-Lab, UC Berkeley

import time #import the time library to time the entire job

def worker(num):
    '''worker function'''
    for i in range(20000000): number=0 #count to 20000000, this is for benchmarking purposes
    print "Pass Finished"
    return

def go():
    for i in range(3):
        worker(i)

start_time = time.time()
go()
end_time=time.time()
print end_time-start_time #print the time it took for the process to finish
