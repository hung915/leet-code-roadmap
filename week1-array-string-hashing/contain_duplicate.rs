use std::collections::HashSet;

fn contain_duplicate(nums: Vec<i32>) -> bool {
    let mut seen: HashSet<i32> = HashSet::new();
    for &num in nums.iter() {
        if seen.contains(&num) {
            return true;
        }
        seen.insert(num);
    }
    false
}

fn contain_duplicate_iterator(nums: Vec<i32>) -> bool {
    let mut seen = HashSet::new();
    nums.iter().any(|&num| !seen.insert(num))
}

fn main() {
    println!("{:?}", contain_duplicate(vec![2, 7, 11, 15]));
    println!("{:?}", contain_duplicate(vec![3, 2, 2, 4]));
    println!("{:?}", contain_duplicate(vec![3, 3]));
}
