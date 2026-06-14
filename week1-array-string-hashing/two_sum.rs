use std::collections::HashMap;

fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
    let mut seen: HashMap<i32, i32> = HashMap::new();
    for (i, &num) in nums.iter().enumerate() {
        let complement = target - num;
        if let Some(&j) = seen.get(&complement) {
            return vec![j, i as i32];
        }
        seen.insert(num, i as i32);
    }
    vec![]
}

fn main() {
    println!("{:?}", two_sum(vec![2, 7, 11, 15], 9)); // [0, 1]
    println!("{:?}", two_sum(vec![3, 2, 4], 6)); // [1, 2]
    println!("{:?}", two_sum(vec![3, 3], 6)); // [0, 1]
}
