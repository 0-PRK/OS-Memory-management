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
            
    def display_metrics(self):
        total_partitions = len(self.partitions)
        used_partitions = sum(1 for p in self.partitions if p is not None)
        free_partitions = total_partitions - used_partitions
        
        memory_utilization = (used_partitions / total_partitions) * 100
        internal_fragmentation = (free_partitions / total_partitions) * 100
        external_fragmentation = 0  # No external fragmentation in fixed partitions
        
        print(f"\nMetrics:")
        print(f"Memory Utilization: {memory_utilization:.2f}%")
        print(f"Internal Fragmentation: {internal_fragmentation:.2f}%")
        print(f"External Fragmentation: {external_fragmentation:.2f}%")
        # print(f"Allocation Flexibility: Low")            
            
    def p_exists(self, process_id):
        return exists(self.processes, process_id)