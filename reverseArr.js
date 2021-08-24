function reverseArr(arr) {
  if(arr.length === 0) return [];
  return [arr[arr.length -1]].concat(reverseArr(arr.slice(0,-1)))
}