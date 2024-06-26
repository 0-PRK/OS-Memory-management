from utils import print_memory_layout, print_allocation_table, exists

class DynamicAllocation:
    def __init__(self, total_memory):
        self.total_memory = total_memory
        self.free_blocks = [(0, total_memory)]  # List of free memory blocks (start, size)
        self.processes = {}  # Dictionary to hold process allocations (process_id: (start, size))

    def add_process(self, process_id, memory_required):
        for i, (start, size) in enumerate(self.free_blocks):
            if size >= memory_required:
                self.processes[process_id] = (start, memory_required)
                if size == memory_required:
                    self.free_blocks.pop(i)
                else:
                    self.free_blocks[i] = (start + memory_required, size - memory_required)
                print(f"Process {process_id} allocated memory from {start} to {start + memory_required - 1}")
                print(self.free_blocks)
                return
        print(f"Process {process_id} could not be allocated")
        
    # def merge_fblocks(self):
    #     for i, (start, size) in enumerate(self.free_blocks):
    #         if(i==(len(self.free_blocks)-1)):
    #             break
    #         else:
    #             self.free_blocks.sort()
    #             startf, sizef = self.free_blocks[i+1]
    #             if((start+size) == (startf)):
    #                 nstart = start
    #                 nsize = size+sizef
    #                 self.free_blocks.pop(i)
    #                 self.free_blocks.pop(i)
    #                 self.free_blocks.append((nstart,nsize))


    def merge_fblocks(self):
        self.free_blocks.sort()
        merged_blocks = []
        for block in self.free_blocks:
            if merged_blocks and merged_blocks[-1][1] == block[0]:
                merged_blocks[-1] = (merged_blocks[-1][0], merged_blocks[-1][1] + block[1])
            else:
                merged_blocks.append(block)
        self.free_blocks = merged_blocks

    def remove_process(self, process_id):
        if process_id in self.processes:
            start, size = self.processes.pop(process_id)
            self.free_blocks.append((start, size))
            print(self.free_blocks)
            self.merge_fblocks()  # Optional: merge contiguous free blocks here
            print(f"Process {process_id} removed from memory block {start} to {start + size - 1}")
            
        else:
            print(f"Process {process_id} not found")

    def display_memory_status(self):
        print("Memory Status (Dynamic Allocation):")
        allocated_memory = [0] * self.total_memory
        for start, size in self.processes.values():
            for i in range(start, start + size):
                allocated_memory[i] = 1
        print_memory_layout(allocated_memory, 10)  # Assuming block size of 10 for display
        print_allocation_table(self.processes)


    def display_metrics(self):
        used_memory = sum(size for _, size in self.processes.values())
        free_memory = sum(size for _, size in self.free_blocks)
        
        memory_utilization = (used_memory / self.total_memory) * 100
        internal_fragmentation = 0  # No internal fragmentation in dynamic allocation
        external_fragmentation = (free_memory / self.total_memory) * 100
        
        print(f"\nMetrics:")
        print(f"Memory Utilization: {memory_utilization:.2f}%")
        print(f"Internal Fragmentation: {internal_fragmentation:.2f}%")
        print(f"External Fragmentation: {external_fragmentation:.2f}%")
        # print(f"Allocation Flexibility: High")            
        
    def p_exists(self, process_id):
        return exists(self.processes, process_id)
    
    

