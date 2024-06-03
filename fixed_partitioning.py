from utils import exists

class FixedPartitioning:
    def __init__(self, total_memory, partition_size):
        self.total_memory = total_memory
        self.partition_size = partition_size
        self.partitions = [None] * (total_memory // partition_size)  # Fixed-size partitions
        self.processes = {}  # Dictionary to hold process allocations

    def add_process(self, process_id, memory_required):
        num_partitions = -(-memory_required // self.partition_size)  # Round up to the nearest partition
        for i in range(len(self.partitions) - num_partitions + 1):
            if all(p is None for p in self.partitions[i:i + num_partitions]):
                for j in range(num_partitions):
                    self.partitions[i + j] = process_id
                self.processes[process_id] = (i, num_partitions)
                print(f"Process {process_id} allocated from partition {i} to {i + num_partitions - 1}")
                return
        print(f"Process {process_id} could not be allocated")

    def remove_process(self, process_id):
        if process_id in self.processes:
            start, num_partitions = self.processes.pop(process_id)
            for i in range(num_partitions):
                self.partitions[start + i] = None
            print(f"Process {process_id} removed from partition {start} to {start + num_partitions - 1}")
        else:
            print(f"Process {process_id} not found")

    def display_memory_status(self):
        print("Memory Status (Fixed-sized Partitions):")
        for i, partition in enumerate(self.partitions):
            status = partition if partition is not None else "Free"
            print(f"Partition {i}: {status}")
            
    def p_exists(self, process_id):
        return exists(self.processes, process_id)
