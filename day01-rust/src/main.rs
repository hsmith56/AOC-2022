use std::{fs, cmp};

fn part_1(input: &String) {
    let mut max: u32 = 0;
    let mut record: u32 = 0;
    for line in input.lines() {
        if !line.is_empty() {
            max += line.parse::<u32>().unwrap();
        } else {
            record = cmp::max(record, max);
            max = 0;
        }
    }
    println!("Day 1 Part 1: {}", record);
}

fn part_2(input: &String) {
    let mut top_3: Vec<u32> = vec![0,0,0];
    let mut max: u32 = 0;
    for line in input.lines() {
        if !line.is_empty() {
            max += line.parse::<u32>().unwrap();
        } else {
            if top_3.iter().any(|f| max >= *f) {
                top_3.insert(0, max);
                top_3.pop();
                top_3.sort_by(|a, b| b.cmp(a));
            } 
            max = 0;
        }
    }
    println!("Day 1 Part 2: {}", top_3.iter().sum::<u32>());
}

fn main() {
    let file_path = "input.txt";
    println!("In file {}", file_path);

    let input = fs::read_to_string(file_path)
        .expect("Should have been able to read the file");

    part_1(&input);
    part_2(&input);
}