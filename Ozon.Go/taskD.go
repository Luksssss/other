package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main2() {
	var (
		nums, res          []string
		sum                uint64
		minRanks, maxRanks *[]uint64
		r                  = 18 // максимально допустимые количество разрядов
		minL, maxL         int
		elStr              string
		overflow           bool // есть ли переполнение при сложении
		ll                 int
	)
	in := bufio.NewScanner(os.Stdin)

	for in.Scan() {
		nums = strings.Fields(in.Text())
	}

	ranks1, l1 := getMasNums(nums[0], &r)
	ranks2, l2 := getMasNums(nums[1], &r)

	if *l1 > *l2 {
		minRanks, maxRanks = ranks2, ranks1
		minL, maxL = *l2, *l1
	} else {
		minRanks, maxRanks = ranks1, ranks2
		minL, maxL = *l1, *l2
	}

	for i := 0; i < maxL; i++ {
		if overflow {
			(*maxRanks)[i]++
		}

		if i < minL {
			sum = (*minRanks)[i] + (*maxRanks)[i]
		} else {
			sum = (*maxRanks)[i]
		}

		elStr = strconv.FormatUint(sum, 10)

		ll = len(elStr)
		// переполнение
		if ll > r && maxL != i+1 {
			res = append(res, elStr[1:])
			overflow = true
			// были ведущие нули
		} else if ll < r && maxL != i+1 {
			res = append(res, strings.Repeat("0", r-ll)+elStr)
			overflow = false
		} else {
			res = append(res, elStr)
			overflow = false
		}

	}
	// зеркалим
	i := 0
	j := len(res) - 1
	for i < j {
		res[i], res[j] = res[j], res[i]
		i++
		j--
	}

	fmt.Println(strings.Join(res, ""))
}

// вернет массив цифр без переполнения типа uint64
func getMasNums(num string, r *int) (*[]uint64, *int) {
	var (
		ranks []uint64
		l     int
	)

	end := len(num)
	beg := end - *r
	if beg < 0 {
		beg = 0
	}

	for {
		if end > 0 {
			val, err := strconv.ParseUint(num[beg:end], 10, 64)
			if err != nil {
				fmt.Println("обработка ошибки")
			}
			ranks = append(ranks, val)
			l++
			end = beg
			if end < 0 {
				end = 0
			}
			beg = end - *r
			if beg < 0 {
				beg = 0
			}
			continue
		}

		break
	}

	return &ranks, &l
}
