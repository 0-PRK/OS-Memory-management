from utils import print_memory_layout, print_allocation_table, exists
import math

class BuddySystem:
    def __init__(self, total_memory):
        self.total_memory = total_memory
        self.size = math.ceil(math.log2(total_memory)) + 1
        self.free_list = [[] for _ in range(self.size)]
        self.processes = {}
        self.initialize(total_memory)

    def initialize(self, total_memory):
        n = math.ceil(math.log2(total_memory))
        self.free_list[n].append((0, total_memory - 1))

    def add_process(self, process_id, memory_required):
        size = 1
        while size < memory_required:
            size *= 2
        n = math.ceil(math.log2(size))
        
        if any(self.free_list[n:]):
            self.allocate(process_id, size)
        else:
            print(f"Process {process_id} could not be allocated")

    def allocate(self, process_id, size):
        n = math.ceil(math.log2(size))

        for i in range(n, self.size):
            if self.free_list[i]:
                start, end = self.free_list[i].pop(0)
                while i > n:
                    i -= 1
                    mid = (start + end) // 2
                    self.free_list[i].append((mid + 1, end))
                    end = mid
                self.processes[process_id] = (start, size)
                print(f"Process {process_id} allocated {size} bytes from {start} to {start + size - 1}")
                return

        print(f"Process {process_id} could not be allocated")

    def display_metrics(self):
        used_memory = sum(size for _, size in self.processes.values())
        free_memory = sum(len(addrs) * size for size, addrs in self.free_blocks.items())
        
        memory_utilization = (used_memory / self.total_memory) * 100
        internal_fragmentation = 0  # No internal fragmentation in buddy system
        external_fragmentation = (free_memory / self.total_memory) * 100
        
        print(f"\nMetrics:")
        print(f"Memory Utilization: {memory_utilization:.2f}%")
        print(f"Internal Fragmentation: {internal_fragmentation:.2f}%")
        print(f"External Fragmentation: {external_fragmentation:.2f}%")
        # print(f"Allocation Flexibility: Medium")
    def remove_process(self, process_id):
        if process_id in self.processes:
            start, size = self.processes.pop(process_id)
            while size <= self.total_memory:
                buddy = start ^ size
                buddy_found = False

                for i, (free_start, free_end) in enumerate(self.free_list[math.ceil(math.log2(size))]):
                    if free_start == buddy:
                        self.free_list[math.ceil(math.log2(size))].pop(i)
                        start = min(start, buddy)
                        size *= 2
                        buddy_found = True
                        break

                if not buddy_found:
                    self.free_list[math.ceil(math.log2(size))].append((start, start + size - 1))
                    break
            print(f"Process {process_id} removed from memory block {start} to {start + size - 1}")
        else:
            print(f"Process {process_id} not found")

    def display_memory_status(self):
        print("Memory Status (Buddy System):")
        allocated_memory = [0] * self.total_memory
        for start, size in self.processes.values():
            for i in range(start, start + size):
                allocated_memory[i] = 1
        print_memory_layout(allocated_memory, 10)
        print_allocation_table(self.processes)

    def p_exists(self, process_id):
        return exists(self.processes, process_id)

