package main

import "fmt"

func main() {
	tests := []struct {
		nums []int
		want bool
	}{
		{[]int{1, 2, 3, 1}, true},
		{[]int{1, 2, 3, 4}, false},
		{[]int{1, 1, 1, 3, 3, 4, 3, 2, 4, 2}, true},
	}

	for _, tc := range tests {
		got1 := containDuplicate(tc.nums)
		got2 := containDuplicateStruct(tc.nums)
		fmt.Printf("nums=%v want=%v map[bool]=%v map[struct]=%v ok=%v\n",
			tc.nums, tc.want, got1, got2, got1 == tc.want && got2 == tc.want)
	}
}

func containDuplicate(nums []int) bool {
	seen := map[int]bool{}
	for _, num := range nums {
		if _, ok := seen[num]; ok {
			return true
		}
		seen[num] = true
	}
	return false
}

func containDuplicateStruct(nums []int) bool {
	seen := make(map[int]struct{}, len(nums))
	for _, num := range nums {
		if _, ok := seen[num]; ok {
			return true
		}
		seen[num] = struct{}{}
	}
	return false
}
