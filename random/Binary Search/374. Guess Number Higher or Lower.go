package Binary

/**
* Forward declaration of guess API.
* @ param  num   your guess
* @ return -1 if num is lower than the guess number
*			      1 if num is higher than the guess number
*               otherwise return 0
* func guess(num int) int
 */

func guessNumber(n int) int {
	left := 0
	right := n
	for right >= left {
		mid := int((right + left) / 2)
		if guess(mid) == 0 {
			return mid
		}
		if guess(mid) == 1 {
			left = mid + 1
		}
		if guess(mid) == -1 {
			right = mid - 1
		}
	}

	return 0
}
