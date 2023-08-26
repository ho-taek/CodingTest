class Solution {
    fun solution(n: Int, m: Int, section: IntArray): Int {
        var answer: Int = 0
        var count = 0
        for(i in section){
            if(i >= count){
                count = m + i
                answer ++
            }
        }
        return answer
    }
}