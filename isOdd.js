function isOdd(num) {
  return num === 0 ? false 
       : num === 1 ? true 
       : num < 0 ? isOdd(-num)
       : isOdd(num-2)
}