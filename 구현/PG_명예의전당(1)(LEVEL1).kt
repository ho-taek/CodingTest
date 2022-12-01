class Solution {
    fun solution(k: Int, score: IntArray): IntArray {
        val check : MutableList<Int> = mutableListOf()
        var answer: IntArray = intArrayOf()
        for(i in 0..k-1){
            if(i < score.size){
                check.add(score[i])
                check.sort()
                answer = answer + check[0]
            }
            if(score.size < k && check.size == score.size) return answer
        }
        
        for(i in k..score.size-1){
            if(score[i] > check[0]) check[0] = score[i]
            check.sort()
            answer = answer + check[0]
        }
        return answer
    }
}