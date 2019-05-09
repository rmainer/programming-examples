package main

import (
	"fmt"
	"math"
	"strings"
)

func levenshtein(w1, w2 string) int {
	w1 = strings.ToLower(w1)
	w2 = strings.ToLower(w2)
	var n1 = len(w1) + 1
	var n2 = len(w2) + 1
	
	d := make([][]int, n1)
	for y := 0; y<n1; y++ {
		 d[y] = make([]int, n2)
	}

	for y:=0; y<n1; y++ {
		for x:=0; x<n2; x++ {
			d[y][x] = 0
		}
	}
	for y:=1; y<n1; y++ {
		d[y][0] = y
	}
	for x:=1; x<n2; x++ {
		d[0][x] = x
	}
	
	for y:=1; y<n1; y++ {
		for x:=1; x<n2; x++ {
			if string([]rune(w1)[y-1]) == string([]rune(w2)[x-1]) {
				d[y][x] = d[y-1][x-1]
			} else {
				d[y][x] = int(math.Min(float64(d[y-1][x-1]), math.Min(float64(d[y-1][x]), float64(d[y][x-1]))) + 1)
			}
		}
	}

	return d[n1-1][n2-1]
}


func main() {
	fmt.Println(levenshtein("Roman", "Ramo"))
}