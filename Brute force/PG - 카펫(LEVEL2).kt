class Solution {
    fun solution(brown: Int, yellow: Int): IntArray {
        var answer = IntArray(2)
        val count = brown + yellow
        var width = 0
        var height = 0
        for(i in 2..count){
            if(count % i == 0){
                if(count/i <= i ){
                width = i
                height = count/i
                if((width-2)*(height-2) == yellow){
                    answer[0] = width
                    answer[1] = height
                    break
                }
            }   
            }
        }
        return answer
    }
}