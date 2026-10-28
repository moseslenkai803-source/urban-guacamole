import time

def up_to_n(n):
    sum = 0
    for i in range (1,n+1):
        #print("I is",i, "Sum is",sum)
        sum=sum+1

    print(f"When is n is {n} sum is {sum}")
    return sum

start_time =time.pref__counter()
up_to_n(50000)
end_time=time.perf_counter()

diff_ms=(end_time-start_time)*1000

print(f"\n Execution time:{diff_ms} ms")