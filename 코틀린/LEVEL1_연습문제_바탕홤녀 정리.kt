class Solution {
    fun solution(wallpaper: Array<String>): IntArray {
        var answer = intArrayOf(51,51,0,0) 
        
        for(i in 0 .. wallpaper.size-1){
            for(j in 0 .. wallpaper[i].length-1){
                if(wallpaper[i][j] == '#'){
                    if(answer[0] > i) answer[0] = i
                    if(answer[1] > j) answer[1] = j
                    if(answer[2] < i+1) answer[2] = i+1
                    if(answer[3] < j+1) answer[3] = j+1
                }
            }
        }
        
        return answer
    }
}