use std::collections::HashSet;

fn dfs(cur: usize, graph: &Vec<(usize, Vec<usize>)>, visited: &mut HashSet<usize>) -> u32 {
    let mut nvis = 1;
    visited.insert(cur);

    println!("visiting {}", cur);

    for neighbour in &graph[cur].1 {
        if !visited.contains(neighbour) {
            nvis += dfs(*neighbour, graph, visited);
        }
    }

    return nvis;
}

fn main() {

    let graph = vec![
        (0, vec![2, 1]),
        (1, vec![0, 2, 3]),
        (2, vec![5]),
        (3, vec![4]),
        (4, vec![5]),
        (5, vec![]),
    ];

    let mut visited = HashSet::new();

    println!("Visited {} nodes in total", dfs(0, &graph, &mut visited));

}
