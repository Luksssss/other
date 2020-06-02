package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	taskA()
	// taskB()
	// taskD()
	// taskF()
	// taskE()
}

// На вход программе подается большое количество целых чисел. Все числа, кроме одного,
// имеют пару, причем может быть несколько одинаковых пар. Найдите число без пары.
func taskA() {
	couple := make(map[string]int)

	f, err := os.Open("input-201.txt")

	if err != nil {
		fmt.Println(err)
		return
	}
	defer f.Close()

	fw, err := os.Create("input-201.a.txt")

	if err != nil {
		fmt.Println(err)
		return
	}
	defer fw.Close()

	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		couple[scanner.Text()]++
	}

	for el, val := range couple {
		if val == 1 {
			fw.WriteString(el)
			break
		}
	}

}

// В БД имеется таблица с товарами goods (id INTEGER, name TEXT),
// таблица с тегами tags (id INTEGER, name TEXT) и таблица связки товаров и тегов
// tags_goods (tag_id INTEGER, goods_id INTEGER, UNIQUE (tag_id, goods_id)).
// Выведите id и названия всех товаров, которые имеют все возможные теги в этой базе.
func taskB() {
	sql := `with tmp  AS (select count(id) AS cnt_tags
	from tags) 
	
	select g.id, g.name
	from goods AS g, tmp
	inner join tags_goods AS tg ON g.id = tg.goods_id
	group by g.name, g.id
	having count(tg.tag_id) = tmp.cnt_tags`

	fmt.Println(sql)

}

// Дано целое положительное число "target". Также дана последовательность из целых положительных
// чисел. Необходимо записать в выходной файл "1", если в последовательности есть два числа сумма,
// которых равна значению "target" или "0" если таких нет.
// NOTE: Все числа используемы в задаче находятся в диапазоне 0 < N < 999999999
func taskF() {
	var (
		tmp       = make(map[int]int)
		nums      []string
		key       int
		firstLine = true
		target    int
		res       = "0"
		num       int
	)

	f, err := os.Open("inputF.txt")

	if err != nil {
		fmt.Println(err)
		return
	}
	defer f.Close()

	fw, err := os.Create("outputF.txt")

	if err != nil {
		fmt.Println(err)
		return
	}
	defer fw.Close()

	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		if firstLine {
			target, err = strconv.Atoi(scanner.Text())
			if err != nil {
				fw.WriteString(res)
				return
			}
			firstLine = false
			continue
		}

		nums = strings.Fields(scanner.Text())

	}

	for ind, el := range nums {
		num, err = strconv.Atoi(el)

		if err != nil {
			fmt.Println(err)
			fw.WriteString(res)
			return
		}

		key = target - num

		_, ok := tmp[key]
		if ok {
			res = "1"
			break
		} else {
			tmp[num] = ind
		}
	}

	fw.WriteString(res)
}

// сложение больших чисел
// uint64 max:  18 446 744 073 709 551 615 (20 разрядов)
func taskD() {
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
	f, err := os.Open("inputD.txt")

	if err != nil {
		fmt.Println(err)
		return
	}
	defer f.Close()

	fw, err := os.Create("outputD.txt")

	if err != nil {
		fmt.Println(err)
		return
	}
	defer fw.Close()

	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		nums = strings.Fields(scanner.Text())
	}

	ranks1, l1 := getMasNums2(nums[0], &r)
	ranks2, l2 := getMasNums2(nums[1], &r)

	fmt.Println(*ranks1, *ranks2)

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
			fmt.Println("SUM 1", (*minRanks)[i], (*maxRanks)[i])
			sum = (*minRanks)[i] + (*maxRanks)[i]
		} else {
			fmt.Println("SUM 2", (*maxRanks)[i])
			sum = (*maxRanks)[i]
		}
		// 1 999 998
		// 1 999 998

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

	// fmt.Println(strings.Join(res, ""))
	fw.WriteString(strings.Join(res, ""))

}

// вернет массив цифр без переполнения типа uint64
func getMasNums2(num string, r *int) (*[]uint64, *int) {
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
			// fmt.Println(beg, end)
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

func taskE() {
	Merge2Channels(f, in1, in2, out, n)
}

// E
// описание см. Readme_E.md
func Merge2Channels(f func(int) int, in1 <-chan int, in2 <-chan int, out chan<- int, n int) {
	go func() {
		for i := 0; i < n; i++ {
			x1 := <-in1
			x2 := <-in2

			tmpCh := make(chan int, 2)
			go worker(f, x1, tmpCh)
			go worker(f, x2, tmpCh)

			sum := 0
			for j := 0; j < 2; j++ {
				sum += <-tmpCh
			}
			out <- sum
			close(tmpCh)
		}
	}()
}

func worker(f func(int) int, x int, tmpCh chan<- int) {
	tmpCh <- f(x)
}
