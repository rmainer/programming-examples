use std::cmp::min;

fn levenshtein(w1: String, w2: String) -> u8 {
	let w1c: Vec<char> = w1.to_lowercase().chars().collect();
	let w2c: Vec<char> = w2.to_lowercase().chars().collect();
	let n1: usize = w1c.len() + 1;
	let n2: usize = w2c.len() + 1;
	let mut d = [[0u8; 100]; 100];
	
	for y in 1..n1 {
		d[y][0] = y as u8;
	}
		for x in 1..n2 {
		d[0][x] = x as u8;
	}
	
	for y in 1..n1 {
		for x in 1..n2 {
			if w1c[y-1] == w2c[x-1] { d[y][x] = d[y-1][x-1]; }
			else { d[y][x] = min(d[y-1][x-1], min(d[y-1][x], d[y][x-1])) + 1; }
		}
	}
	
	d[n1-1][n2-1]
}


fn main() {
	let w1: String = "Roman".to_string();
	let w2: String = "Ramo".to_string();
	println!("{}", levenshtein(w1, w2));
}