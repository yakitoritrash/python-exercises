import sys
from collections import deque

# Set higher recursion depth for DFS
sys.setrecursionlimit(2000)

def solve():
    try:
        N, M = map(int, sys.stdin.readline().strip().split())
        grid = [list(sys.stdin.readline().strip().split()) for _ in range(N)]
    except Exception:
        return

    # --- 1. Find all Cable Components (using BFS) ---
    visited_cables = [[False for _ in range(M)] for _ in range(N)]
    all_cables = [] # List of cable components (each is a set of (r, c) tuples)

    for r in range(N):
        for c in range(M):
            if grid[r][c] == 'C' and not visited_cables[r][c]:
                # Start a new BFS for a new cable component
                new_cable = set()
                q = deque([(r, c)])
                visited_cables[r][c] = True
                new_cable.add((r, c))
                
                while q:
                    curr_r, curr_c = q.popleft()
                    
                    # Check 4 directions
                    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        nr, nc = curr_r + dr, curr_c + dc
                        
                        if 0 <= nr < N and 0 <= nc < M and \
                           not visited_cables[nr][nc] and grid[nr][nc] == 'C':
                            
                            visited_cables[nr][nc] = True
                            new_cable.add((nr, nc))
                            q.append((nr, nc))
                
                all_cables.append(new_cable)

    # --- 2. Find all Rods (lines with at least one 'R') ---
    all_rods = []
    # Find row rods
    for r in range(N):
        has_r = False
        for c in range(M):
            if grid[r][c] == 'R':
                has_r = True
                break
        if has_r:
            all_rods.append(('row', r))
            
    # Find col rods
    for c in range(M):
        has_r = False
        for r in range(N):
            if grid[r][c] == 'R':
                has_r = True
                break
        if has_r:
            # Avoid double-counting if a row rod was already found
            # (This is unlikely given problem constraints, but safe)
            # This logic assumes rods don't cross, which seems true
            all_rods.append(('col', c))


    # --- 3. Calculate Total Cost ---
    total_cost = 0
    
    for rod_type, rod_idx in all_rods:
        for cable in all_cables:
            count_over = 0
            count_under = 0
            
            # Find all intersections for this (rod, cable) pair
            for (r, c) in cable:
                is_intersection = False
                if rod_type == 'row' and r == rod_idx:
                    is_intersection = True
                elif rod_type == 'col' and c == rod_idx:
                    is_intersection = True
                
                if is_intersection:
                    # Cell (r, c) is on the cable AND on the rod line
                    # We must check the *original* grid, since (r,c)
                    # is part of a 'C' component, but the grid
                    # value at (r,c) might be 'R' (from a different cable)
                    # No, this is simpler: if (r,c) is in the cable component,
                    # grid[r][c] must be 'C'.
                    # This means we must check the *rod* line for C's and R's
                    
                    # Re-think: The intersection cell (r,c) is part of the cable.
                    # But the *rod line itself* has 'C's and 'R's.
                    # Let's check all cells on the rod line.
                    pass # This logic is flawed.
            
            # --- Logic v3 (Corrected) ---
            # We iterate through the *cable* and see where it hits the rod line
            
            count_over = 0
            count_under = 0
            
            for (r, c) in cable:
                if rod_type == 'row' and r == rod_idx:
                    # This cable cell is on the rod row.
                    # The cable *itself* is 'C', so this is OVER
                    count_over += 1
                elif rod_type == 'col' and c == rod_idx:
                    # This cable cell is on the rod col.
                    # The cable *itself* is 'C', so this is OVER
                    count_over += 1
            
            # Now find the 'R' intersections
            # Iterate all cells on the rod line
            if rod_type == 'row':
                for c_rod in range(M):
                    if grid[rod_idx][c_rod] == 'R':
                        # Check if this 'R' cell is adjacent to our cable
                        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                            nr, nc = rod_idx + dr, c_rod + dc
                            if (nr, nc) in cable:
                                count_under += 1
                                break # Count this R-intersection only once
            elif rod_type == 'col':
                 for r_rod in range(N):
                    if grid[r_rod][rod_idx] == 'R':
                        # Check if this 'R' cell is adjacent to our cable
                        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                            nr, nc = r_rod + dr, rod_idx + dc
                            if (nr, nc) in cable:
                                count_under += 1
                                break # Count this R-intersection only once

            total_crossings = count_over + count_under
            if total_crossings > 1:
                total_cost += min(count_over, count_under)

    print(total_cost)

solve()
