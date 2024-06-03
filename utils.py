# def print_memory_layout(memory, block_size):
#     for i in range(0, len(memory), block_size):
#         block = memory[i:i + block_size]
#         print(f"{i}-{i + block_size - 1}: {' '.join(str(x) for x in block)}")

# def print_allocation_table(processes):
#     print("Process ID | Memory Allocated")
#     for pid, mem in processes.items():
#         print(f"{pid}       | {mem}")


def print_memory_layout(memory, block_size):
    for i in range(0, len(memory), block_size):
        block = memory[i:i + block_size]
        print(f"{i}-{i + block_size - 1}: {' '.join(str(x) for x in block)}")

def print_allocation_table(processes):
    print("Process ID | Memory Allocated")
    for pid, (start, size) in processes.items():
        print(f"{pid}       | {start} - {start + size - 1}")
        
def exists(processes, p_id):
    if p_id in processes.keys(): 
        return True
    else:
        return False
