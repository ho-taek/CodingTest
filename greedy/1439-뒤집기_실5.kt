fun main(args: Array<String>){
    val sc = Scanner(System.'in')
    eng = sc.next()
    print(result(eng))

}

fun result(s : String) : Int{
    var one = 0
    var zero = 0
    stack = mutableListOf(s[0])
    if s[0] == "0" one++ else zero ++

    if s.length == s.count {c -> c == '1' or c == '0'} return 0

    for(i in 1..s.length){
        if s[i] == "1" and stack[0] == "0"{
            stack.removeAt(0)
            one++
            stack.add("1")
        }
            
        
        if s[i] == "0" and stack[0] == "1"{
            stack.removeAt(0)
            zero++
            stack.add("0")
        }

    }

    return min(one,zero)
}