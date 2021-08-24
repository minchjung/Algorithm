function recursion(arr){
  if(arr.length === 0 ) return [] ; 
  return Array.isArray(arr[0])
        ? recursion(arr[0].concat(arr.slice(1)))
        : [arr[0]].concat(recursion(arr.slice(1)))
}
