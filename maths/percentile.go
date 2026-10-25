// Package maths is M A T H
package maths

import (
	"math"
	"math/rand/v2"
)

// function partition(list, left, right, pivotIndex) is
//
//	pivotValue := list[pivotIndex]
//	swap list[pivotIndex] and list[right]  // Move pivot to end
//	storeIndex := left
//	for i from left to right − 1 do
//	    if list[i] <= pivotValue then
//	        swap list[storeIndex] and list[i]
//	        increment storeIndex
//	swap list[right] and list[storeIndex]  // Move pivot to its final place
//	return storeIndex
func partition(list []float64, left int, right int, pivotIndex int) int {
	pivotValue := list[pivotIndex]

	list[pivotIndex], list[right] = list[right], list[pivotIndex]

	storeIndex := left

	for i := left; i <= right; i++ {
		if list[i] <= pivotValue {
			list[storeIndex], list[i] = list[i], list[storeIndex]
		}
	}

	list[right], list[storeIndex] = list[storeIndex], list[right]

	return storeIndex
}

// Returns the k-th smallest element of list within left..right inclusive
// (i.e. left <= k <= right).
//
// function select(list, left, right, k) is
//
//	if left = right then   // If the list contains only one element,
//	    return list[left]  // return that element
//	pivotIndex  := ...     // select a pivotIndex between left and right,
//	                       // e.g., left + floor(rand() % (right − left + 1))
//	pivotIndex  := partition(list, left, right, pivotIndex)
//	// The pivot is in its final sorted position
//	if k = pivotIndex then
//	    return list[k]
//	else if k < pivotIndex then
//	    return select(list, left, pivotIndex − 1, k)
//	else
//	    return select(list, pivotIndex + 1, right, k)
//
// https://en.wikipedia.org/wiki/Quickselect
func quickselect(list []float64, left int, right int, k int) float64 {
	if left == right {
		return list[left]
	}

	pivotIndex := left + int(math.Floor(math.Mod(rand.Float64(), float64(right-left+1))))
	pivotIndex = partition(list, left, right, pivotIndex)

	if k == pivotIndex {
		return list[k]
	} else if k < pivotIndex {
		return quickselect(list, left, pivotIndex-1, k)
	} else {
		return quickselect(list, pivotIndex+1, right, k)
	}
}

func Percentile(percent int, input []float64) (percentile float64) {
	k := int(float64(percent) / 100.0 * (float64(len(input)) - 1))

	return quickselect(input, 0, len(input)-1, k)
}
