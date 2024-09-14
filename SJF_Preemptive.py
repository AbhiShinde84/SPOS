from tabulate import tabulate
process = int(input("Enter the number of processes: "))

process_list1 = []
for i in range(process):
    process_list1.append(f"P{i}")

Burst_time1 = []
Arrival_time1 = []

print("Enter burst time for processes:")
for i in range(process):
    Burst_time1.append(int(input(f"P{i} = ")))

print("Enter arrival time (Enter 0 if not stated):")
for i in range(process):
    Arrival_time1.append(int(input(f"P{i} = ")))

combined = list(zip(Arrival_time1, Burst_time1, process_list1))
combined.sort()
Arrival_time, Burst_time, process_list = zip(*combined)

# -----------------------------------------------------------------------------------------------------------

ready_queue = []
ready_kt = []
running =[]
start =[]
finish=[]

max_arrival = max(Arrival_time)
print(max_arrival)
j=0
for i in range(max_arrival+1):
    if Arrival_time[j] == i :
        ready_queue.append((process_list[j]))
        ready_kt.append(Burst_time[j])
        j += 1
        
        combined = list(zip(ready_kt, ready_queue))
        combined.sort()    
        ready_kt, ready_queue = zip(*combined)
        ready_kt = list(ready_kt)
        ready_queue = list(ready_queue)
        
    print(f"{i}{ready_queue}")
    
    if len(ready_queue) >= 1:
        running.append(ready_queue[0])

        ready_kt[0] = ready_kt[0]-1
        if ready_kt[0]== 0:
            ready_queue.pop(0)
            ready_kt.pop(0)

        combined = list(zip(ready_kt, ready_queue))
        combined.sort()    
        ready_kt, ready_queue = zip(*combined)
        ready_kt = list(ready_kt)
        ready_queue = list(ready_queue)
    else :
        continue

# -------------------------------------------------------------------------------------------------

while (len(ready_kt)>=1):
    running.append(ready_queue[0])
    ready_kt[0] = ready_kt[0]-1
    if ready_kt[0]== 0:
        ready_queue.pop(0)
        ready_kt.pop(0)

sftemp=[]
if min(Arrival_time)!= 0:
    for i in range(min(Arrival_time)):
        sftemp.append(-1)
    running = sftemp + running

print(running)
for i in range(process):
    start.append(running.index(f"P{i}"))
    temp=running[::-1]
    finish.append(len(temp)-(temp.index(f"P{i}")))

print(start)
print(finish)


turnaround_time = []
waiting_time = []

for i in range(process):
    turnaround_time.append(finish[i] - Arrival_time1[i])
    waiting_time.append(turnaround_time[i] - Burst_time1[i])


table_data = [process_list1, Burst_time1, Arrival_time1, start, finish, turnaround_time, waiting_time]
table_data = list(zip(*table_data))

print(tabulate(table_data, headers=["Process", "Burst Time", "Arrival Time", "Start Time", "Finish Time", "Turnaround Time", "Waiting Time"], tablefmt="simple"))
