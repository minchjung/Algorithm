var fs = require("fs");
var input = fs.readFileSync("dev/stdin").toString().trim().split("\n");

const N = Number(input[0]);
const M = Number(input[2]);

const base = input[1].split(" ").map(Number);
const search = input[3].split(" ").map(Number);
base.sort((a,b) => a - b);  // base !! needs sort !! 

const upper_binary =(arr, target, last) => {
  let start = 0 ; 
  let end = last -1; 

  while(end > start){
    const half = parseInt( (start + end)/2 )
    if(arr[half] > target) end = half; 
    else start = half + 1; 
  }
  return end; 
}

const lower_binary = (arr, target, last) => {
  let start = 0; 
  let end = last  -1;
  while(end > start){
    let half = parseInt( (start + end)/2 );
    if(arr[half] >= target) end = half; 
    else start = half + 1; 
  }
  return end;
}

let result = [] 
for(let i = 0 ; i < M ; i++){
  let upper = upper_binary(base, search[i], N);
  let lower = lower_binary(base, search[i], N);
  if(upper === N -1 && base[N -1] === search[i]) upper++; // 예외 처리!!
  // base 의 제일 마지막 요소가 찾고자 하는 요소일때 인덱스 1개 차이의 예외가 발생함 !!
  result.push(upper - lower);
}
console.log(result.join(' '))