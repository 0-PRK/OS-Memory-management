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
        print("\n1. Add process")
        print("2. Remove process")
        print("3. View memory allocation status")
        print("4. Exit")
        action = int(input("Enter action: "))

        if action == 1:
            process_id = input("Enter process ID: ")
            if not simulator.p_exists(process_id=process_id):
                memory_required = int(input("Enter memory required: "))
                simulator.add_process(process_id, memory_required)
            else:
                print("Duplicate Process ID.")
        elif action == 2:
            process_id = input("Enter process ID: ")
            simulator.remove_process(process_id)
        elif action == 3:
            simulator.display_memory_status()
        elif action == 4:
            break
        else:
            print("Invalid action")

if __name__ == "__main__":
    main()
