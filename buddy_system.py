from utils import print_memory_layout, print_allocation_table, exists

class BuddySystem:
    def __init__(self, total_memory):
        self.total_memory = total_memory
        self.free_blocks = {total_memory: [0]}  # Dictionary of free blocks by size
        self.processes = {}  # Dictionary to hold process allocations (process_id: (start, size))

    def add_process(self, process_id, memory_required):
        # size = 1
        while size < memory_required:
            size *= 2
        for s in range(size, self.total_memory + 1, size * 2):
            if s in self.free_blocks and self.free_blocks[s]:
                start = self.free_blocks[s].pop(0)
                if not self.free_blocks[s]:
                    del self.free_blocks[s]
                if size < s:
                    self.free_blocks.setdefault(s // 2, []).append(start + size)
                self.processes[process_id] = (start, size)
                print(f"Process {process_id} allocated {size} bytes from {start} to {start + size - 1}")
                return
        print(f"Process {process_id} could not be allocated")

    def remove_process(self, process_id):
        if process_id in self.processes:
            start, size = self.processes.pop(process_id)
            while size <= self.total_memory:
                buddy = start ^ size
                if buddy in self.free_blocks.get(size, []):
                    self.free_blocks[size].remove(buddy)
                    start = min(start, buddy)
                    size *= 2
                else:
                    self.free_blocks.setdefault(size, []).append(start)
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
        print_memory_layout(allocated_memory, 10)  # Assuming block size of 10 for display
        print_allocation_table(self.processes)
        
    def p_exists(self, process_id):
        return exists(self.processes, process_id)