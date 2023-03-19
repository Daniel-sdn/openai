import os
import json
import time, copy



            #calculatempo
            def calculaTempo(since, fase):
                elapsed = (time.time() - since) * 1000
                minutes, seconds = divmod(elapsed / 1000, 60)
                milliseconds = elapsed % 1000
                return elapsed, minutes, seconds, milliseconds 


def calcula_algo(since):
    a = 0
    for i in range(1,100000):
        a += 1
        print(i)
    # mensagem1 = "Maria tinha um coelhinho"
    t_elapsed1 = (time.time() - since) * 1000
    minutes1, seconds1 = divmod(t_elapsed1 / 1000, 60)
    milliseconds1 = t_elapsed1 % 1000
    return t_elapsed1, minutes1, seconds1, milliseconds1 
 
tempo = {} 
since = time.time()
fase = "request"

  
    obj[a+b] = None
    print obj #{"column_number_url1": None}
    
    
    
a = "column_number"
b = "_url1"
obj = {}
obj[a+b] = None
print obj #{"column_number_url1": None}