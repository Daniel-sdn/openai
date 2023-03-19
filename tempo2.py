import openai
import os
import json
import time, copy
import modules.tempo1 as t1

since = time.time()

t_elapsed2, minutes2, seconds2, milliseconds2 = t1.calcula_algo(since)


#print(t_elapsed2)

for a in range(1,100000):
    print(a)



print(f"\nPrimeira tomada de tempo1: \nTime Elapsed: {t_elapsed2} minutes: {minutes2:.0f}m  {seconds2:.0f}s  {milliseconds2:.0f}ms")

# Calcular somente o tempo de tempo2
time_elapsed3 = ((time.time() - since) * 1000)
minutes3, seconds3 = divmod(time_elapsed3 / 1000, 60)
milliseconds3 = time_elapsed3 % 1000

print(f"\nSegunda tomada de tempo2: \nTime Elapsed: {time_elapsed3} minutes: {minutes3:.0f}m  {seconds2:.0f}s  {milliseconds2:.0f}ms")


time_elapsed4 = t_elapsed2 + time_elapsed3
minutes4, seconds4 = divmod(time_elapsed4 / 1000, 60)
milliseconds4 = time_elapsed4 % 1000

print(f"\nTempo total: \nTime Elapsed: {time_elapsed4} minutes: {minutes4:.0f}m  {seconds4:.0f}s  {milliseconds4:.0f}ms")



