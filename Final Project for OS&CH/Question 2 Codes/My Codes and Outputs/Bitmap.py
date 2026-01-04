# Total number of disk blocks
TOTAL_BLOCKS = 16

# Bitmap representation of the harddrive
# 0 means empty block, and 1 means that block is allocated
disk_bitmap = [0] * TOTAL_BLOCKS


def allocate_bitmap(required_blocks):
    """
    :param required_blocks:
    :return:
    This function allocates the consecutive free blocks using bitmap allocation.
    Returns the starting index of allocated blocks.
    """

    counter = 0  # counts free spaces
    for index in range(TOTAL_BLOCKS):
        if disk_bitmap[index] == 0:  # if the block is free
            counter += 1

            # if enough consecutive area is found
            if counter == required_blocks:
                # Mark those blocks as allocated
                for j in range(index, index - required_blocks, -1):
                    disk_bitmap[j] = 1

                return index - required_blocks + 1
        else:
            # reset counter if an allocated block is found
            counter = 0
    # allocation failed
    return -1


def free_bitmap(start_index, size):
    """
    :param start_index:
    :param size:
    :return:
    Frees previously allocated blocks by setting bitmap values back to 0:
    """
    for i in range(start_index, start_index + size):
        disk_bitmap[i] = 0


def print_bitmap():
    """ Prints the current bitmap state."""
    print("Bitmap: ", disk_bitmap)


# Example usage
start = allocate_bitmap(3)
print_bitmap()

free_bitmap(start, 3)
print_bitmap()
