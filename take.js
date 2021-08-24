function take(num, arr) {
  if( num > arr.length) num = arr.length  
  if( num === arr.length ) return arr; 
  return take(num, arr.slice(0,-1))
}
