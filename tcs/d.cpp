#include <iostream>
#include <vector>
#include <queue>
#include <set>       // For visited set
#include <map>       // For adjacency list
#include <string>
#include <algorithm> // For std::rotate

// Using 1-based indexing for graph nodes to match problem description
int N, M;
std::map<int, std::vector<int>> adj;
std::vector<int> start_state;
std::vector<int> target_state;

// Set of all possible rotations (simple cycles)
// We store the canonical form (sorted) to avoid duplicates
std::set<std::vector<int>> simple_cycles;

/**
 * Helper function to apply a rotation (a cycle) to a state
 */
std::vector<int> apply_rotation(const std::vector<int>& state, const std::vector<int>& cycle) {
    std::vector<int> next_state = state;
    
    // We are moving the animal from cycle[i] to cycle[i-1]
    // Get the animal that starts at the beginning of the cycle
    // Note: state is 0-indexed (state[0] = enclosure 1)
    // cycle is 1-indexed (cycle[0] = enclosure 1, 2, etc.)
    int animal_to_move = state[cycle.back() - 1]; // Animal at the last node in the cycle

    for (size_t i = 0; i < cycle.size(); ++i) {
        int current_node_idx = cycle[i] - 1; // 0-based
        int next_animal = state[current_node_idx];
        next_state[current_node_idx] = animal_to_move;
        animal_to_move = next_animal;
    }
    return next_state;
}


/**
 * DFS to find all simple cycles (our "generators")
 * u: current node
 * start_node: the node we started from
 * path: list of nodes in the current path
 * visited: set of nodes in the current path
 */
void find_cycles_dfs(int u, int start_node, std::vector<int>& path, std::set<int>& visited) {
    path.push_back(u);
    visited.insert(u);

    for (int v : adj[u]) {
        if (v == start_node) {
            // Found a cycle
            if (path.size() >= 2) { // Only store cycles of length 2 or more
                simple_cycles.insert(path);
            }
        } else if (visited.find(v) == visited.end()) {
            // Continue DFS
            find_cycles_dfs(v, start_node, path, visited);
        }
    }
    
    // Backtrack
    path.pop_back();
    visited.erase(u);
}

int main() {
    // === Fast I/O ===
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    std::cout.tie(NULL);

    // === 1. Parse Input ===
    std::cin >> N >> M;

    for (int i = 0; i < M; ++i) {
        int u, v;
        std::cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    start_state.resize(N);
    for (int i = 0; i < N; ++i) {
        std::cin >> start_state[i];
    }

    target_state.resize(N);
    for (int i = 0; i < N; ++i) {
        std::cin >> target_state[i];
    }

    // === 2. Find All Rotations (Generators) ===
    for (int i = 1; i <= N; ++i) {
        std::vector<int> path;
        std::set<int> visited;
        find_cycles_dfs(i, i, path, visited);
    }
    
    // Create a vector of all generators (cycles + their inverses)
    std::vector<std::vector<int>> generators;
    for (const auto& cycle : simple_cycles) {
        generators.push_back(cycle);
        // Add the inverse rotation
        std::vector<int> inverse_cycle = cycle;
        std::reverse(inverse_cycle.begin() + 1, inverse_cycle.end());
        generators.push_back(inverse_cycle);
    }

    // === 3. Perform BFS ===
    std::queue<std::pair<std::vector<int>, int>> q;
    std::set<std::vector<int>> visited_states;

    q.push({start_state, 0});
    visited_states.insert(start_state);

    while (!q.empty()) {
        std::vector<int> current_state = q.front().first;
        int cost = q.front().second;
        q.pop();

        // --- Check for Target ---
        if (current_state == target_state) {
            std::cout << cost << "\n";
            return 0;
        }

        // --- Generate Next States ---
        for (const auto& cycle : generators) {
            std::vector<int> next_state = apply_rotation(current_state, cycle);
            
            // if (visited_states.find(next_state) == visited_states.end())
            if (visited_states.insert(next_state).second) {
                // If insert was successful (state is new)
                q.push({next_state, cost + 1});
            }
        }
    }

    // If target is unreachable (shouldn't happen based on problem)
    std::cout << -1 << "\n"; 
    return 0;
}
