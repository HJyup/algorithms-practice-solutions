type StockSpanner struct {
	st [][]int
}

func Constructor() StockSpanner {
	return StockSpanner{
		st: [][]int{},
	}
}

func (this *StockSpanner) Next(price int) int {
	span := 1

	for len(this.st) > 0 && this.st[len(this.st) - 1][1] <= price {
		span += this.st[len(this.st) - 1][0]
		this.st = this.st[:len(this.st) - 1]
	}

	this.st = append(this.st, []int{span, price})
	return span 
}

/**
 * Your StockSpanner object will be instantiated and called as such:
 * obj := Constructor()
 * param1 := obj.Next(price)
 */
 