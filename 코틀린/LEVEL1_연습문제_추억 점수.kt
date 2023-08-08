class Solution {
    fun solution(name: Array<String>, yearning: IntArray, photo: Array<Array<String>>): MutableList<Int> {
        val result = mutableListOf<Int>()
        
        val nameScore = mutableMapOf<String,Int>()
        name.forEachIndexed{index, score ->
            nameScore.put(score, yearning[index])
        }
        
        photo.forEach{list ->
            var score = 0
            list.forEach{ name ->
                score += nameScore[name] ?: 0
            }
            result.add(score)
        }
        
        return result
    }
}