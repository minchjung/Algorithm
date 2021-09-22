function solution(s){
    let stack = [] 
    for(let i = 0 ; i < s.length ; i++){
        if(stack.length !== 0 && stack[stack.length -1] === s[i]) stack.pop();
        else stack.push(s[i])
    }
    return stack.length ? 0 : 1 ;
}

// function solution(s){
//     let i = 0;
//     while(i+1 < s.length){
//         if(s[i] === s[i+1]){
//             s = s.replace(s[i]+s[i], "")
//             i = 0;
//         }
//         else i++;
//     }
//     return s.length === 0 ? 1 : 0
// }

// 효율성 통과 NO 
// Pair 문자열 => stack 자료형 !! 