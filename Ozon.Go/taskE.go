package main

// import (
// 	"fmt"
// 	"time"
// )

// func producer(ch chan<- int) {
// 	v := 0
// 	for {
// 		ch <- v
// 		fmt.Println("Sent value:", v)
// 		v++
// 	}
// }

// func myfunc(v int) int {
// 	time.Sleep(1 * time.Second)
// 	return v
// }

// func main() {
// 	in1, in2, out := make(chan int), make(chan int), make(chan int)

// 	go producer(in1)
// 	go producer(in2)

// 	Merge2Channels(myfunc, in1, in2, out, 6)

// 	for v := range out {
// 		fmt.Println("Merged value:", v)
// 	}
// }

// func Merge2Channels(f func(int) int, in1 <-chan int, in2 <-chan int, out chan<- int, n int) {
// 	go func() {
// 		for i := 0; i < n; i++ {

// 			go func() {

// 				x1 := <-in1
// 				x2 := <-in2

// 				tmpCh := make(chan int, 2)

// 				go worker(f, x1, tmpCh)
// 				go worker(f, x2, tmpCh)

// 				sum := 0
// 				for j := 0; j < 2; j++ {
// 					sum += <-tmpCh
// 				}
// 				close(tmpCh)

// 				out <- sum
// 			}()
// 		}
// 	}()
// 	//close(out)

// }

// func worker(f func(int) int, x int, tmpCh chan<- int) {
// 	tmpCh <- f(x)
// }
