function drop(num, arr) {
  if( num >= arr.length) return [];
  if(num === 0) return arr ; 
  return drop(num-1, arr.slice(1) )
}
