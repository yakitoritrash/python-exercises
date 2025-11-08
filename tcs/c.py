import sys

# Define a class to hold slide information
class Slide:
    def __init__(self, x1, y1, x2, y2):
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2
        
        # Ensure x_min and x_max are set correctly
        self.x_min = min(x1, x2)
        self.x_max = max(x1, x2)
        
        # Calculate slope (will be 1 or -1)
        if (x2 - x1) == 0:
            # This case shouldn't happen based on 45-degree angle
            self.slope = 0 
        else:
            self.slope = (y2 - y1) // (x2 - x1)
            
        # Calculate y-intercept 'c' from y = (slope*x) + c
        self.c = y1 - self.slope * x1

    def is_on_slide(self, x, y):
        """Check if (x, y) is on this slide segment."""
        if not (self.x_min <= x <= self.x_max):
            return False
        # Use integer math, round to handle potential float issues
        return y == round(self.slope * x + self.c)

def solve():
    try:
        N = int(sys.stdin.readline().strip())
        slides = []
        for _ in range(N):
            x1, y1, x2, y2 = map(int, sys.stdin.readline().strip().split())
            slides.append(Slide(x1, y1, x2, y2))
        
        x, y, energy = map(int, sys.stdin.readline().strip().split())
        
        # This set tracks our (x, y) position to detect infinite loops
        position_history = set()

        while x > 0 and y > 0:
            
            # --- 0. Infinite Loop Check ---
            if (x, y, energy) in position_history:
                break # We are stuck in a true loop
            position_history.add((x, y, energy))

            slides_at_point = []
            for s in slides:
                if s.is_on_slide(x, y):
                    slides_at_point.append(s)
            
            is_stuck = len(slides_at_point) > 1
            on_slide = slides_at_point[0] if len(slides_at_point) == 1 else None
            
            # --- 1. Handle "Stuck" ---
            if is_stuck:
                unlock_cost = x * y
                if energy < unlock_cost:
                    break # Stuck permanently
                energy -= unlock_cost
                
                # Find the best slide to take
                best_slide = None
                min_next_y = float('inf')
                
                for s in slides_at_point:
                    next_x = -1
                    if s.slope == 1:
                        next_x = x - 1
                    else: # slope == -1
                        next_x = x + 1
                    
                    # Check if this move is valid
                    if s.x_min <= next_x <= s.x_max:
                        next_y = s.slope * next_x + s.c
                        if next_y < min_next_y:
                            min_next_y = next_y
                            best_slide = s
                
                on_slide = best_slide # This is the slide we will take
                if on_slide is None:
                    # Unlocked but nowhere to slide? Stuck.
                    break 

            # --- 2. Handle "Fall" ---
            elif on_slide is None:
                max_hit_y = 0 # Ground
                for s in slides:
                    if s.x_min <= x <= s.x_max:
                        y_slide = round(s.slope * x + s.c)
                        if max_hit_y < y_slide < y:
                            max_hit_y = y_slide
                
                if y == max_hit_y:
                    break # Can't fall, stuck
                y = max_hit_y
                continue # Restart loop from new fallen position

            # --- 3. Handle "Slide" ---
            # This block runs if (on_slide is not None)
            
            slide_cost = 1
            if energy < slide_cost:
                break # Stuck, not enough energy to slide
            
            # Determine "downhill" direction
            next_x = -1
            if on_slide.slope == 1:
                next_x = x - 1
            else: # slope == -1
                next_x = x + 1
            
            # Check if we are sliding off the slide
            if not (on_slide.x_min <= next_x <= on_slide.x_max):
                # Slide off. We will fall from (x, y) on the next loop.
                # Find the next hit *now*
                max_hit_y = 0 # Ground
                for s in slides:
                    if s.x_min <= x <= s.x_max:
                        y_slide = round(s.slope * x + s.c)
                        if max_hit_y < y_slide < y:
                            max_hit_y = y_slide
                
                if y == max_hit_y:
                    break # Can't fall, stuck
                y = max_hit_y
                continue # Restart loop from new fallen position
            else:
                # Normal slide
                next_y = round(on_slide.slope * next_x + on_slide.c)
                x = next_x
                y = next_y
                energy -= slide_cost
                continue # Restart loop from new sliden position

        # Print the final position
        print(f"{x} {y}")

    except EOFError:
        pass
    except Exception as e:
        # print(f"An error occurred: {e}", file=sys.stderr)
        pass

solve()
