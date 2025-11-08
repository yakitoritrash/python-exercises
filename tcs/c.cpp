#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <utility>  // For std::pair and std::make_pair
#include <algorithm> // For std::min and std::max
#include <climits>   // For INT_MAX (used as infinity)

// C++ struct is like a Python class with all public members
struct Slide {
    int x1, y1, x2, y2;
    int x_min, x_max;
    int slope, c; // y-intercept

    // Constructor to initialize the slide
    Slide(int_x1, int_y1, int_x2, int_t_y2) {
        x1 = int_x1;
        y1 = int_y1;
        x2 = int_x2;
        y2 = int_t_y2;

        x_min = std::min(x1, x2);
        x_max = std::max(x1, x2);

        if (x2 - x1 == 0) {
            slope = 0; // Should not happen
        } else {
            slope = (y2 - y1) / (x2 - x1); // Integer division
        }
        
        c = y1 - slope * x1;
    }

    // Check if (x, y) is on this slide segment
    bool is_on_slide(int x, int y) {
        if (x < x_min || x > x_max) {
            return false;
        }
        // Use integer math, as logic is all integer-based
        return y == (slope * x + c);
    }
};

int main() {
    // === Fast I/O Setup ===
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    std::cout.tie(NULL);

    // === Read Input ===
    int N;
    std::cin >> N;

    std::vector<Slide> slides;
    for (int i = 0; i < N; ++i) {
        int x1, y1, x2, y2;
        std::cin >> x1 >> y1 >> x2 >> y2;
        slides.push_back(Slide(x1, y1, x2, y2));
    }

    int x, y, energy;
    std::cin >> x >> y >> energy;

    // Use a C++03/11 compatible set for position tracking
    // This is equivalent to your set<tuple(x, y, energy)>
    std::set<std::pair<int, std::pair<int, int>>> position_history;

    // === Main Simulation Loop ===
    while (x > 0 && y > 0) {
        
        // --- 0. Infinite Loop Check ---
        std::pair<int, std::pair<int, int>> current_state = 
            std::make_pair(x, std::make_pair(y, energy));
        
        if (position_history.count(current_state)) {
            break; // We are stuck in a true loop
        }
        position_history.insert(current_state);

        // Find all slides at the current point
        // We store pointers to avoid copying large objects
        std::vector<Slide*> slides_at_point;
        for (size_t i = 0; i < slides.size(); ++i) {
            if (slides[i].is_on_slide(x, y)) {
                slides_at_point.push_back(&slides[i]);
            }
        }

        bool is_stuck = slides_at_point.size() > 1;
        Slide* on_slide = (slides_at_point.size() == 1) ? slides_at_point[0] : nullptr;

        // --- 1. Handle "Stuck" ---
        if (is_stuck) {
            int unlock_cost = x * y;
            if (energy < unlock_cost) {
                break; // Stuck permanently
            }
            energy -= unlock_cost;

            // Find the best slide to take
            Slide* best_slide = nullptr;
            int min_next_y = INT_MAX; // Use INT_MAX for infinity

            for (size_t i = 0; i < slides_at_point.size(); ++i) {
                Slide* s = slides_at_point[i];
                int next_x = -1;
                if (s->slope == 1) {
                    next_x = x - 1;
                } else { // slope == -1
                    next_x = x + 1;
                }

                // Check if this move is valid
                if (next_x >= s->x_min && next_x <= s->x_max) {
                    int next_y = s->slope * next_x + s->c;
                    if (next_y < min_next_y) {
                        min_next_y = next_y;
                        best_slide = s;
                    }
                }
            }

            on_slide = best_slide; // This is the slide we will take
            if (on_slide == nullptr) {
                break; // Unlocked but nowhere to slide? Stuck.
            }
            // else, the loop will continue to the "Slide" block
        }
        
        // --- 2. Handle "Fall" ---
        else if (on_slide == nullptr) {
            int max_hit_y = 0; // Ground
            for (size_t i = 0; i < slides.size(); ++i) {
                Slide& s = slides[i]; // Use reference
                if (x >= s.x_min && x <= s.x_max) {
                    int y_slide = s.slope * x + s.c;
                    if (y_slide > max_hit_y && y_slide < y) {
                        max_hit_y = y_slide;
                    }
                }
            }
            if (y == max_hit_y) {
                 break; // Can't fall, stuck
            }
            y = max_hit_y;
            continue; // Restart loop from new fallen position
        }

        // --- 3. Handle "Slide" ---
        // This block runs if (on_slide != nullptr)
        int slide_cost = 1;
        if (energy < slide_cost) {
            break; // Stuck, not enough energy to slide
        }

        // Determine "downhill" direction
        int next_x = -1;
        if (on_slide->slope == 1) {
            next_x = x - 1;
        } else { // slope == -1
            next_x = x + 1;
        }

        // Check if we are sliding off the slide
        if (next_x < on_slide->x_min || next_x > on_slide->x_max) {
            // Slide off. We will fall from (x, y). Find next hit.
            int max_hit_y = 0; // Ground
            for (size_t i = 0; i < slides.size(); ++i) {
                Slide& s = slides[i];
                if (x >= s.x_min && x <= s.x_max) {
                    int y_slide = s.slope * x + s.c;
                    if (y_slide > max_hit_y && y_slide < y) {
                        max_hit_y = y_slide;
                    }
                }
            }
            if (y == max_hit_y) {
                 break; // Can't fall, stuck
            }
            y = max_hit_y;
            continue; // Restart loop from new fallen position
        } else {
            // Normal slide
            int next_y = on_slide->slope * next_x + on_slide->c;
            x = next_x;
            y = next_y;
            energy -= slide_cost;
            continue; // Restart loop from new sliden position
        }
    }

    // Print the final position
    std::cout << x << " " << y << "\n";

    return 0;
}
