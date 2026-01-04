# Total number of disk blocks
TOTAL_BLOCKS = 16


class DiskBlock:
    """
    Represents a single disk block.
    allocated: 0 = free, 1 = used
    next: index of the next block in the linked list
    """
    def __init__(self):
        self.allocated = 0
        self.next = -1


# Create disk with empty blocks
disk = [DiskBlock() for _ in range(TOTAL_BLOCKS)]


def allocate_linked(block_count):
    """
    Allocates blocks using linked-list allocation.
    Blocks do NOT need to be consecutive.
    Returns the first block index or -1 if allocation fails.
    """
    first = -1     # First block of the file
    prev = -1      # Previous allocated block

    # Scan disk blocks
    for index in range(TOTAL_BLOCKS):
        if block_count == 0:
            break

        # Only use free blocks
        if disk[index].allocated == 0:
            disk[index].allocated = 1
            disk[index].next = -1

            # Set first block
            if first == -1:
                first = index

            # Link previous block to current block
            if prev != -1:
                disk[prev].next = index

            prev = index
            block_count -= 1

    # Allocation fails if not enough blocks were found
    if block_count > 0:
        return -1

    return first


def free_linked(start_block):
    """
    Frees all blocks of a file by following the linked list.
    """
    current = start_block

    while current != -1:
        next_block = disk[current].next
        disk[current].allocated = 0
        disk[current].next = -1
        current = next_block


def print_disk_state():
    """Prints allocation status of disk blocks."""
    state = [block.allocated for block in disk]
    print("Disk:", state)


# Example usage
start1 = allocate_linked(9)
print_disk_state()

start2 = allocate_linked(3)
print_disk_state()

free_linked(start2)
print_disk_state()
