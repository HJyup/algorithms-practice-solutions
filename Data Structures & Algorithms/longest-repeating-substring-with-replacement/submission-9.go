func characterReplacement(s string, k int) int {
    wnd := make(map[byte]int)
    ans := 0

    l := 0 
    freq := 0
    for r := 0; r < len(s); r++ {
        val, ok := wnd[s[r]]
        if !ok {
            wnd[s[r]] = 1
        } else {
            wnd[s[r]] = val + 1
        }

        freq = max(freq, wnd[s[r]])

        if (r - l + 1) - freq > k {
            wnd[s[l]]--
            l += 1
        }

        ans = max(ans, r - l + 1)
    }

    return ans
}
