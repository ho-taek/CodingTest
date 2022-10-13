class Solution {
    fun solution(clothes: Array<Array<String>>): Int {
        val hash = clothes.groupBy{it[1]}.values
        .fold(1){total, i -> total * (i.size+1)} - 1
        return hash
    }
}