import time
starttime = time.time() 

run = 0 
for i in range(1, 5000):
    for j in range(1, 5000):
        run += i + j

print(f"The result is {run}")

endtime = time.time() 
print(f"It took {endtime-starttime:.2f} seconds to compute") 




