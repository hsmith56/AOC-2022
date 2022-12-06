use std::fs;

fn part_1(input: &String) {
    
    let idk = input
        .lines()
        .filter(|line| !line.is_empty())
        .map(|line| ((line.as_bytes()[0] - b'A') as u16, (line.as_bytes()[2] - b'X') as u16))
        .map(|(a, b)| match (a, b) {
            (0, 2) => 1 + b,
            (2, 0) => 7 + b,
            (a, b) if a > b => 1 + b,
            (a, b) if a < b => 7 + b,
            (a, b) if a == b => 4 + b, 
            (_, _) => 0
        })
        .sum::<u16>();
        
    println!("Day 1 Part 2: {:?}", idk);
    
}

fn part_2(input: &String) {
    let idk = input
    .lines()
    .filter(|line| !line.is_empty())
    .map(|line| ((line.as_bytes()[0] - b'A') as i32, (line.as_bytes()[2] - b'X') as i32))
    .map(|(a, b)| match (a, b) {
        (0, 0) => 3,
        (2, 2) => 7,
        (a, 0) => a,
        (a, 1) => 4 + a,
        (a, 2) => 8 + a,
        (_, _) => 0
    }).sum::<i32>();
    println!("Day 1 Part 2: {:?}", idk);
}

fn main() {
    let file_path = "example.txt";
    println!("In file {}", file_path);

    let input = fs::read_to_string(file_path)
        .expect("Should have been able to read the file");

    part_1(&input);
    part_2(&input);
}