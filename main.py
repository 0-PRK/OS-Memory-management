from fixed_partitioning import FixedPartitioning
from unequal_partitioning import UnequalPartitioning
from dynamic_allocation import DynamicAllocation
from buddy_system import BuddySystem
from paging import Paging

def main():
    print("Memory Management Simulator")
    total_memory = int(input("Enter total memory size: "))
    print("Select memory management technique:")
    print("1. Fixed-sized Memory Partitioning")
    print("2. Unequal-sized Fixed Partitioning")
    print("3. Dynamic Memory Allocation")
    print("4. Buddy System")
    print("5. Paging")
    choice = int(input("Enter choice: "))

    if choice == 1:
        partition_size = int(input("Enter partition size: "))
        simulator = FixedPartitioning(total_memory, partition_size)
    elif choice == 2:
        partition_sizes = list(map(int, input("Enter partition sizes separated by space: ").split()))
        simulator = UnequalPartitioning(total_memory, partition_sizes)
    elif choice == 3:
        simulator = DynamicAllocation(total_memory)
    elif choice == 4:
        simulator = BuddySystem(total_memory)
    elif choice == 5:
        page_size = int(input("Enter page size: "))
        simulator = Paging(total_memory, page_size)
    else:
        print("Invalid choice")
        return

    while True:
        print("\nMenu:")
        print("1. Add Process")
        print("2. Remove Process")
        print("3. Display Memory Status")
        print("4. Display Metrics")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            process_id = input("Enter process ID: ")
            memory_required = int(input("Enter memory required (in units): "))
            if simulator.p_exists(process_id):
                print(f"Process {process_id} already exists!")
                continue
            simulator.add_process(process_id, memory_required)
        
        elif choice == "2":
            process_id = input("Enter process ID to remove: ")
            simulator.remove_process(process_id)
        
        elif choice == "3":
            simulator.display_memory_status()
        
        elif choice == "4":
            simulator.display_metrics()
        
        elif choice == "5":
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
