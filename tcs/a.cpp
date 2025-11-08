#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <utility> // For std::make_pair
#include <sstream> // For std::stringstream (to convert vector to string)

/**
 * Helper function to convert a vector state into a
 * string key for our 'visited' set.
 * This is necessary for old C++03 compilers.
 */
std::string vec_to_string(const std::vector<int>& v) {
    std::stringstream ss;
    for (size_t i = 0; i < v.size(); ++i) {
        ss << v[i] << ","; // Delimiter is important
    }
    return ss.str();
}

int main() {
    // 1. === Fast I/O Setup ===
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    std::cout.tie(NULL);

    // 2. === Read N ===
    int N;
    std::string line; 
    
    std::cin >> N;
    std::getline(std::cin, line); 

    // 3. === Handle Edge Cases (N=0, N=1) ===
    if (N <= 1) {
        std::getline(std::cin, line); // "shuffled"
        if (N == 1) std::getline(std::cin, line);
        std::getline(std::cin, line); // "original"
        if (N == 1) std::getline(std::cin, line);
        std::cout << 0 << "\n";
        return 0;
    }

    // 4. === Read Shuffled List ===
    std::getline(std::cin, line); // Skip "shuffled" line
    std::vector<std::string> shuffled_list(N);
    for (int i = 0; i < N; ++i) {
        std::getline(std::cin, shuffled_list[i]);
    }

    // 5. === Read Original List & Create Mapping ===
    std::getline(std::cin, line); // Skip "original" line
    std::map<std::string, int> mapping;
    std::vector<int> target_vec(N); // The vector form of the target
    for (int i = 0; i < N; ++i) {
        std::getline(std::cin, line);
        mapping[line] = i; 
        target_vec[i] = i; 
    }
    // Create the string form of the target
    std::string target_key = vec_to_string(target_vec);


    // 6. === Create Integer-based Start State ===
    std::vector<int> start_vec(N);
    for (int i = 0; i < N; ++i) {
        start_vec[i] = mapping[shuffled_list[i]];
    }
    // Create the string form of the start state
    std::string start_key = vec_to_string(start_vec);

    // 7. === Handle Cost 0 Case ===
    if (start_key == target_key) {
        std::cout << 0 << "\n";
        return 0;
    }

    // 8. === Initialize BFS ===
    // The queue *can* hold vectors, it doesn't compare them
    std::queue<std::pair<std::vector<int>, int> > q; 
    q.push(std::make_pair(start_vec, 0));

    // The visited set MUST use strings
    std::set<std::string> visited;
    visited.insert(start_key);

    // 9. === Run the BFS ===
    while (!q.empty()) {
        std::pair<std::vector<int>, int> current = q.front();
        q.pop();

        std::vector<int> current_vec = current.first;
        int cost = current.second;

        for (int i = 0; i < N; ++i) {
            for (int j = i; j < N; ++j) {
                
                std::vector<int> block;
                for (int b_idx = i; b_idx <= j; ++b_idx) {
                    block.push_back(current_vec[b_idx]);
                }

                std::vector<int> remaining;
                for (int r_idx = 0; r_idx < i; ++r_idx) {
                    remaining.push_back(current_vec[r_idx]);
                }
                for (int r_idx = j + 1; r_idx < N; ++r_idx) {
                    remaining.push_back(current_vec[r_idx]);
                }

                for (int k = 0; k <= (int)remaining.size(); ++k) {
                    
                    std::vector<int> new_vec = remaining;
                    new_vec.insert(new_vec.begin() + k, block.begin(), block.end());

                    // Convert new vector to its string key
                    std::string new_key = vec_to_string(new_vec);

                    // --- Check for target ---
                    if (new_key == target_key) {
                        std::cout << (cost + 1) << "\n";
                        return 0;
                    }

                    // --- Add to queue if new (using string key) ---
                    if (visited.find(new_key) == visited.end()) {
                        visited.insert(new_key);
                        q.push(std::make_pair(new_vec, cost + 1));
                    }
                }
            }
        }
    }

    return 0;
}
