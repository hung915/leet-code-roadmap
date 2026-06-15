package main

import "fmt"

func two_sum(nums []int, target int) []int {
	seen := map[int]int{}
	for i, num := range nums {
		complement := target - num
		if j, ok := seen[complement]; ok {
			return []int{j, i}
		}
		seen[num] = i
	}
	return []int{}
}

func main() {
	fmt.Println(two_sum([]int{2, 7, 11, 15}, 9)) // [0 1]
	fmt.Println(two_sum([]int{3, 2, 4}, 6))      // [1 2]
	fmt.Println(two_sum([]int{3, 3}, 6))         // [0 1]
}
