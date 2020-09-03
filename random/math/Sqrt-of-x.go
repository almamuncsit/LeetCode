package main

import "fmt"

func mySqrt(x int) int {
	left := 0
	right := x
	for left <= right {
		mid := (left + right) / 2
		next := mid + 1
		if mid*mid == x || (mid*mid < x && next*next > x) {
			return mid
		} else if mid*mid > x {
			right = mid - 1
		} else {
			left = mid + 1
		}
	}

	return left
}

func main() {
	x := 8
	fmt.Println(mySqrt(x))
}
