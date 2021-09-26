let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const N= Number(input[0]);

let tree = new Array(27).fill(0);
let ans = [];

for(let i = 1 ; i <= N ; i++){
    let [a,b,c] = input[i].split(" ");
    let obj = {left : b.charCodeAt(0) - 'A'.charCodeAt(0), right : c.charCodeAt(0) - 'A'.charCodeAt(0)}
    tree[a.charCodeAt(0) - 'A'.charCodeAt(0)] = obj
  }

const DFS1 = (node) => {
  if(node === -19){
    return 
  } 
  ans.push(String.fromCharCode(65 + node))
  DFS1(tree[node].left)
  DFS1(tree[node].right)
}

const DFS2 = (node) =>{
  if(node === -19){
    return 
  } 
  DFS2(tree[node].left)
  ans.push(String.fromCharCode(65 + node))
  DFS2(tree[node].right)
}

const DFS3 = (node) =>{
  if(node === -19){
    return
  }
  DFS3(tree[node].left)
  DFS3(tree[node].right)
  ans.push(String.fromCharCode(node + 65))
}

DFS1(0)
console.log(ans.join(""))
ans = []
DFS2(0)
console.log(ans.join(""))
ans = []
DFS3(0)
console.log(ans.join(""))