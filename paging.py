# class Paging:
#     def __init__(self, total_memory, page_size=4):
#         self.total_memory = total_memory
#         self.page_size = page_size
#         self.frames = [None] * (total_memory // page_size)  # List of frames
#         self.processes = {}  # Dictionary to hold process allocations

#     def add_process(self, process_id, memory_required):
#         # Implement paging allocation strategy
#         pass

#     def remove_process(self, process_id):
#         # Implement process removal
#         pass

#     def display_memory_status(self):
#         # Display the memory allocation status
#         pass
from utils import exists

class Paging:
    def __init__(self, total_memory, page_size=4):
        self.total_memory = total_memory
        self.page_size = page_size
        self.frames = [None] * (total_memory // page_size)  # List of frames
        self.processes = {}  # Dictionary to hold process allocations (process_id: [frame_indices])

    def add_process(self, process_id, memory_required):
        num_pages = -(-memory_required // self.page_size)  # Round up to the nearest page
        allocated_frames = []
        for i, frame in enumerate(self.frames):
            if frame is None:
                allocated_frames.append(i)
                if len(allocated_frames) == num_pages:
                    break
        if len(allocated_frames) == num_pages:
            for frame_index in allocated_frames:
                self.frames[frame_index] = process_id
            self.processes[process_id] = allocated_frames
            print(f"Process {process_id} allocated to frames {allocated_frames}")
        else:
            print(f"Process {process_id} could not be allocated")

    def remove_process(self, process_id):
        if process_id in self.processes:
            for frame_index in self.processes.pop(process_id):
                self.frames[frame_index] = None
            print(f"Process {process_id} removed from frames")
        else:
            print(f"Process {process_id} not found")

    def display_memory_status(self):
        print("Memory Status (Paging):")
        for i, frame in enumerate(self.frames):
            status = frame if frame is not None else "Free"
            print(f"Frame {i}: {status}")
            
    def p_exists(self, process_id):
        return exists(self.processes, process_id)
