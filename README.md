python-multiprocessing
======================

Multiprocessing (Parallel Processing) in Python


Three files are quick numeric examples of multiprocessing -- these were a proof of concept as I learned how to use the multiprocessing library
      
      1. two with the direct creation of processes 
         a. sequential-numeric-example.py 
            (counts to 200 mil three times sequentially (no parallel processing) to act as a baseline)
         b. multiprocess-numeric-example.py 
            (counts to 200 mil in three processes simultaneously; simply a proof of concept)
      2. multiprocess-basic-pool-example.py 
         (uses map and a process pool to double a list of numbers)
  
This file is my proof of concept for the use of multiprocessing in my natural language processing work
      
      1. multiprocess-pool-nltk.py
    

Some great intro tutorials about Parallel Processing can be found at

     http://mikecvet.wordpress.com/2010/07/02/parallel-mapreduce-in-python/ 
     (Good overview of using map() and reduce() with a pool of processes)

     http://doughellmann.com/2009/04/pymotw-multiprocessing-part-1.html 
     (Great intro, but note that the code examples have the indents missing)
