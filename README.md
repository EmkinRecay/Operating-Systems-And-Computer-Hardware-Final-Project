# Disk and Memory Allocation Algorithms

**Operating Systems Assignment**

This repository contains implementations and experiments for **disk allocation** and **memory allocation** algorithms as part of an Operating Systems assignment.

---

## 📁 Repository Structure

```text
.
├── Question 2 Codes/
│   ├── AI's Codes and Outputs/
│   │   ├── AI'S Code for LinkedList.txt
│   │   ├── AI'S Code for Bitmap.txt
│   │   ├── Bitmap AI Output.PNG
│   │   └── LinkedList AI Output.PNG
│   │
│   └── My Codes and Outputs/
│       ├── Bitmap.py
│       ├── LinkedList.py
│       ├── Bitmap Output.PNG
│       └── Linked_List Output.PNG
│
├── Question 3 Linked-List Codes/
│   └── Linked_ListAll.py
│
└── README.md
```

---

## Question 2 – Disk Allocation Algorithms

### Implemented Algorithms

* **Bitmap Allocation**
* **Linked-List Allocation**

---

### Bitmap Allocation (Explanation)

Bitmap allocation represents the disk as a sequence of bits where each bit corresponds to a disk block.

* `0` → free block
* `1` → allocated block

When a file requests space, the operating system scans the bitmap to find a sequence of consecutive `0`s large enough for the request and marks them as `1`. When a file is deleted, the corresponding bits are reset to `0`.

---

### Linked-List Allocation (Explanation)

Linked-list allocation stores disk blocks as nodes containing data and a pointer to the next block. Blocks do **not** need to be contiguous. During allocation, the system links together available free blocks. When a file is deleted, the system follows the pointer chain and returns each block to the free list.

---

## Question 2 – Experiments

### Speed Test

Both algorithms were run 100 times for allocation and deallocation. **Linked-list allocation was faster** because it does not need to search for consecutive blocks, while bitmap allocation must scan the bitmap.

### Fragmentation Test

After random allocations and frees, **bitmap allocation failed** to allocate a large block due to external fragmentation. **Linked-list allocation succeeded** because it does not require contiguous blocks.

### Allocation Trace

Using the same allocation sequence showed that bitmap allocation tends to **cluster blocks together**, while linked-list allocation **spreads blocks across the disk**.

---

## Question 3 – Memory Allocation with Linked Lists

### Implemented Algorithms

* **Best Fit**
* **Worst Fit**
* **Next Fit**

Memory is simulated as **100 units (0–99)** using a linked list of free segments in the form:

```
[start, length]
```

---

### Algorithm Explanations

**Best Fit**
Selects the smallest free block that is large enough. This minimizes wasted space but quickly creates many small fragments.

**Worst Fit**
Selects the largest free block. This preserves larger blocks for future allocations but may waste memory.

**Next Fit**
Starts searching from the last allocation position. This improves speed but can cause uneven memory usage.

---

## Question 3 – Experiments

### Experiment 1 – Allocation Trace

Using a fixed allocation/free sequence:

* Best Fit fragmented memory fastest
* Worst Fit preserved large blocks longer
* Next Fit spread allocations based on pointer position

---

### Experiment 2 – Fragmentation Test

After random allocations and frees:

* Best Fit and Next Fit often failed to allocate a large block due to **external fragmentation**
* Worst Fit had a higher success rate because it preserved large free segments

---

### Experiment 3 – Speed Test

After 200 allocation/free cycles:

* **Fastest:** Next Fit
* **Slowest:** Best Fit

Next Fit scans less of the free list, while Best Fit scans the entire list each time.

---

## ▶ How to Run the Code

Make sure **Python 3** is installed.

### Run Question 2 (Disk Allocation)

```bash
python "Question 2 Codes/My Codes and Outputs/Bitmap.py"
python "Question 2 Codes/My Codes and Outputs/LinkedList.py"
```

### Run Question 3 (Memory Allocation)

```bash
python "Question 3 Linked-List Codes/Linked_ListAll.py"
```

