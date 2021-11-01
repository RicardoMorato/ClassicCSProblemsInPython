use rand::prelude::*;

/// This program generates a "maze-like" pattern
/// this was a very common demo on oldschool computers.
fn main() {
    let mut rng = rand::thread_rng();
    let (w, h) = term_size::dimensions().unwrap_or_default();

    for _ in 0..h {
        for _ in 0..w {
            let dir = rng.gen_bool(0.5);

            print!("{}", if dir { "/" } else { "\\" });
        }
        println!("");
    }
}
