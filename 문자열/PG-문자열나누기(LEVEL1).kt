class Solution {
    fun solution(s: String): Int {
        var answer: Int = 0
        var alphabet : Char = s[0]
        var one: Int = 0
        var other : Int = 0
        s.forEach{it ->
            if(alphabet == 'A'){
                alphabet = it
            }
            if(it == alphabet) one++ else other++
            if(one == other){
                answer++
                one = 0
                other = 0
                alphabet = 'A'
            }
        }
        if(one != 0 || other != 0){
            answer++
        }
        return answer
    }
}