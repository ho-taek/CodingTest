class Solution {
    fun solution(park: Array<String>, routes: Array<String>): IntArray {
        var answer: IntArray = intArrayOf(0,0)
        var order = HashMap<String,IntArray>()
        order.put("N", intArrayOf(-1,0))
        order.put("S", intArrayOf(1,0))
        order.put("W", intArrayOf(0,-1))
        order.put("E", intArrayOf(0,1))
        
        for(i in 0 .. park.size-1){
            for(j in 0 .. park[i].length-1){
                if(park[i][j] == 'S'){
                    answer = intArrayOf(i,j)
                }
            }
        }
        
        routes.forEach {
            var move = order[it.split(" ")[0]]
            var count = it.split(" ")[1].toInt()
            var nr = answer[0]
            var nc = answer[1]
            
            for(i in 1..count){
                nr += move!![0]
                nc += move!![1]
                if(nr < 0 || nc < 0 || nr >=park.size || nc >= park[0].length
                   || park[nr][nc] == 'X'){
                    nr = answer[0]
                    nc = answer[1]
                    break
                }
            }
            answer[0] = nr
            answer[1] = nc
        }
        
        return answer
    }
}