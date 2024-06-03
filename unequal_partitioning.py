# class UnequalPartitioning:
#     def __init__(self, total_memory):
#         self.total_memory = total_memory
#         self.partitions = []  # Define unequal-size partitions here
#         self.processes = {}  # Dictionary to hold process allocations

#     def add_process(self, process_id, memory_required):
#         # Implement allocation based on partition sizes
#         pass

#     def remove_process(self, process_id):
#         # Implement process removal
#         pass

#     def display_memory_status(self):
#         # Display the memory allocation status
#         pass


class UnequalPartitioning:
    def __init__(self, total_memory, partition_sizes):
        self.total_memory = total_memory
        self.partition_sizes = partition_sizes
        self.partitions = [(size, None) for size in partition_sizes]  # [(size, allocated_process)]
        self.processes = {}  # Dictionary to hold process allocations

    def add_process(self, process_id, memory_required):
        for i, (size, allocated_process) in enumerate(self.partitions):
            if allocated_process is None and size >= memory_required:
                self.partitions[i] = (size, process_id)
                self.processes[process_id] = i
                print(f"Process {process_id} allocated to partition {i} (size {size})")
                return
        print(f"Process {process_id} could not be allocated")

    def remove_process(self, process_id):
        if process_id in self.processes:
            partition_index = self.processes.pop(process_id)
            size, _ = self.partitions[partition_index]
            self.partitions[partition_index] = (size, None)
            print(f"Process {process_id} removed from partition {partition_index}")
        else:
            print(f"Process {process_id} not found")

    def display_memory_status(self):
        print("Memory Status (Unequal-sized Partitions):")
        for i, (size, allocated_process) in enumerate(self.partitions):
            status = allocated_process if allocated_process is not None else "Free"
            print(f"Partition {i} (size {size}): {status}")
