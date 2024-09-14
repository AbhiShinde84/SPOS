from tabulate import tabulate

process = int(input("Enter the number of processes: "))

process_list = []
for i in range(process):
    process_list.append(f"P{i}")

Burst_time = []
Arrival_time = []

print("Enter burst time for processes:")
for i in range(process):
    Burst_time.append(int(input(f"P{i} = ")))

print("Enter arrival time (Enter 0 if not stated):")
for i in range(process):
    Arrival_time.append(int(input(f"P{i} = ")))

#--------------------------------- SORTING According To Arrival Time ------------------------------------------------------

combined = list(zip(Arrival_time, Burst_time, process_list))
combined.sort()
Arrival_time, Burst_time, process_list = zip(*combined)

#---------------------------------------------------------------------------------------

start_time = []
finish_time = []

for i in range(len(Burst_time)):
    if i == 0:
        start_time.append(Arrival_time[i])
        finish_time.append(Burst_time[i])
    else:
        start_time.append(start_time[i-1] + Burst_time[i-1])
        finish_time.append(finish_time[i-1] + Burst_time[i])

turnaround_time = []
waiting_time = []

for i in range(process):
    turnaround_time.append(finish_time[i] - Arrival_time[i])
    waiting_time.append(turnaround_time[i] - Burst_time[i])

table_data = [process_list, Burst_time, Arrival_time, start_time, finish_time, turnaround_time, waiting_time]
table_data = list(zip(*table_data))

print(tabulate(table_data, headers=["Process", "Burst Time", "Arrival Time", "Start Time", "Finish Time", "Turnaround Time", "Waiting Time"], tablefmt="simple"))
