type FreqStack struct {
    freq    map[int][]int
    values  map[int]int
    maxFreq int
}

func Constructor() FreqStack {
    return FreqStack{
        freq:    map[int][]int{},
        values:  map[int]int{},
        maxFreq: 0,
    }
}

func (this *FreqStack) Push(val int) {
    this.values[val] += 1
    if this.values[val] > this.maxFreq {
        this.maxFreq += 1
    }

    this.freq[this.values[val]] = append(this.freq[this.values[val]], val)
}

func (this *FreqStack) Pop() int {
    val := this.freq[this.maxFreq][len(this.freq[this.maxFreq]) - 1]

    this.freq[this.maxFreq] = this.freq[this.maxFreq][:len(this.freq[this.maxFreq])-1]
    this.values[val] -= 1

    if len(this.freq[this.maxFreq]) == 0 {
        this.maxFreq -= 1
    }

    return val
}

/**
 * Your FreqStack object will be instantiated and called as such:
 * obj := Constructor()
 * obj.Push(val)
 * param2 := obj.Pop()
 */
 