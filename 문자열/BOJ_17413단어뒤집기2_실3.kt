package com.example.example.util

import java.util.*

fun main(args: Array<String>) = with(Scanner(System.`in`)) {
    val sentence = nextLine()

    val stack = mutableListOf<String>()
    val answer = mutableListOf<String>()
    var str = ""
    var count = 0
    sentence.forEach {
        count ++
        if(count == sentence.length && it.toString() != ">"){
            str += it.toString()
            answer.add(str.reversed())
        }

        if(it.toString() == "<"){
            stack.add(it.toString())
            if(str.isNotEmpty()){
                answer.add(str.reversed())
                str = ""
            }
        }

        if(stack.isNotEmpty()){
            str += it.toString()
            if(it.toString() == ">"){
                stack.removeAt(0)
                answer.add(str)
                str = ""
            }
        }else{
            if(it.toString() == " "){
                answer.add(str.reversed())
                answer.add(it.toString())
                str = ""
            }else{
                str += it.toString()
            }

        }
    }

    println(answer.joinToString(""))
}