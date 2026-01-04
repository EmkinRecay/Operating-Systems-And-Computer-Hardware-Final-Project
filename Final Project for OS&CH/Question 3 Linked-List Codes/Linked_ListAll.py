# Total memory size
MEMORY_SIZE = 100

# Free list represented as a list of [start, length]
free_list = [[0, MEMORY_SIZE]]

# Pointer for Next Fit algorithm
next_fit_index = 0


def allocate_best_fit(size):
    """
    Best Fit allocation:
    Chooses the smallest free block that is large enough.
    """
    best_index = -1
    best_size = float('inf')

    # Search for the smallest suitable block
    for i, (start, length) in enumerate(free_list):
        if length >= size and length < best_size:
            best_size = length
            best_index = i

    if best_index == -1:
        return -1  # Allocation failed

    start, length = free_list[best_index]
    allocated_start = start

    # Split the block
    if length == size:
        free_list.pop(best_index)
    else:
        free_list[best_index] = [start + size, length - size]

    return allocated_start


def allocate_worst_fit(size):
    """
    Worst Fit allocation:
    Chooses the largest available free block.
    """
    worst_index = -1
    worst_size = -1

    # Search for the largest free block
    for i, (start, length) in enumerate(free_list):
        if length >= size and length > worst_size:
            worst_size = length
            worst_index = i

    if worst_index == -1:
        return -1  # Allocation failed

    start, length = free_list[worst_index]
    allocated_start = start

    # Split the block
    if length == size:
        free_list.pop(worst_index)
    else:
        free_list[worst_index] = [start + size, length - size]

    return allocated_start


def allocate_next_fit(size):
    """
    Next Fit allocation:
    Starts searching from the last allocation position.
    """
    global next_fit_index
    n = len(free_list)

    # Circular scan of free list
    for i in range(n):
        index = (next_fit_index + i) % n
        start, length = free_list[index]

        if length >= size:
            allocated_start = start

            # Split block
            if length == size:
                free_list.pop(index)
            else:
                free_list[index] = [start + size, length - size]

            next_fit_index = index % len(free_list) if free_list else 0
            return allocated_start

    return -1  # Allocation failed


def free(start, size):
    """
    Frees a block and merges adjacent free blocks.
    """
    free_list.append([start, size])
    free_list.sort()  # Sort by start address

    # Merge adjacent blocks
    merged = []
    for block in free_list:
        if not merged:
            merged.append(block)
        else:
            last_start, last_size = merged[-1]
            current_start, current_size = block

            if last_start + last_size == current_start:
                # Merge blocks
                merged[-1][1] += current_size
            else:
                merged.append(block)

    free_list.clear()
    free_list.extend(merged)


def print_free_list():
    """Prints the current free memory blocks."""
    print("Free list:", free_list)
