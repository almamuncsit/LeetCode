package main

import "fmt"

func climb(i, n int, memo map[int]int) int {
	if i == n {
		return 1
	} else if i > n {
		return 0
	}

	data, ok := memo[i]
	if ok {
		return data
	}
	memo[i] = climb(i+1, n, memo) + climb(i+2, n, memo)

	return memo[i]
}

func climbStairs(n int) int {
	memo := make(map[int]int)

	return climb(0, n, memo)
}

func main() {
	n := 30
	fmt.Println(climbStairs(n))
}
