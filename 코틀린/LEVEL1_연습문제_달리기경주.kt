class Solution {
    fun solution(players: Array<String>, callings: Array<String>): Array<String> {
        val rank = mutableMapOf<String, Int>()
        players.forEachIndexed {index, s -> rank[s] = index}
        
        callings.forEachIndexed {index ,s ->
            val callRank = rank[s] ?: 0
            val frontPlayer = players[callRank - 1]
            
            players[callRank - 1] = s
            players[callRank] = frontPlayer
            
            rank[s] = callRank - 1
            rank[frontPlayer] = callRank
        }
        return players
 }
}