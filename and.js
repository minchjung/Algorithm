function and(arr) {
  return arr.length === 0 ? true : arr[0] && and(arr.slice(1)) ;
}
