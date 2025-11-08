import sys
from collections import deque

def solve():
    # 1. Read N
    try:
        # Use sys.stdin.readline for faster I/O in competitive programming
        n_line = sys.stdin.readline()
        if not n_line:
            return  # Handle empty input
        N = int(n_line.strip())
    except Exception:
        return

    # Handle edge case of N=0 or N=1
    if N <= 1:
        # Consume the remaining lines
        for _ in range(2 + 2 * N):
            sys.stdin.readline()
        print(0)
        return

    # 2. Read shuffled list
    sys.stdin.readline()  # Skip "shuffled" line
    shuffled_list = []
    for _ in range(N):
        shuffled_list.append(sys.stdin.readline().strip())

    # 3. Read original list and create mapping
    sys.stdin.readline()  # Skip "original" line
    mapping = {}
    for i in range(N):
        line = sys.stdin.readline().strip()
        mapping[line] = i

    # 4. Create integer-based start and target states
    # We use tuples because they are hashable and can be added to a set
    start_state = tuple(mapping[instr] for instr in shuffled_list)
    target_state = tuple(range(N))

    # 5. Handle cost 0 case
    if start_state == target_state:
        print(0)
        return

    # 6. Initialize BFS queue and visited set
    # The queue stores (state_tuple, cost)
    queue = deque([(start_state, 0)])
    visited = {start_state}

    # 7. Run the BFS
    while queue:
        current_tuple, cost = queue.popleft()

        # Convert tuple to list for easier manipulation
        current_list = list(current_tuple)

        # --- Generate all possible next states ---
        
        # i = start index of the cut block
        for i in range(N):
            # j = end index of the cut block
            for j in range(i, N):
                
                # The contiguous block to cut
                block = current_list[i : j+1]
                
                # The list that remains after cutting
                remaining = current_list[0 : i] + current_list[j+1 : N]
                
                len_rem = len(remaining)
                
                # k = insertion point
                for k in range(len_rem + 1):
                    
                    # Create the new list by inserting the block
                    new_list = remaining[0:k] + block + remaining[k:]
                    
                    # Convert back to a tuple for visited set and queue
                    new_tuple = tuple(new_list)
                    
                    # --- Check for target ---
                    if new_tuple == target_state:
                        print(cost + 1)
                        return
                    
                    # --- Add to queue if new ---
                    if new_tuple not in visited:
                        visited.add(new_tuple)
                        queue.append((new_tuple, cost + 1))

# Run the main function to solve the problem
solve()
