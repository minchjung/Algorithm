const largestRectangularArea = function (hist) {
// stack !! 
  let stack = []; 
	let idx = 0; 
	let ans = 0; 
// 	get Area
	const getArea = (top,idx) => 
		hist[top]* ( stack.length > 0 
			? idx - stack[stack.length-1] -1 : idx )
// the option to get max area is either of higher height with proper width, 
// or lower height with max width,
// we know that higher one can't go with lower one, So 
// 	first to get rect area with higher height 
//   we can push higher one till it meets lower height
//   otherwise, pop it out and get area with higher one with 
//  difference of current position and the top of the stack,
//  if it got higher, push'em all into the stack till it meets lower one  
	while(idx < hist.length){
		if(stack.length === 0 || hist[stack[stack.length -1]] <= hist[idx])
			stack.push(idx++);
		else ans = Math.max(ans, getArea(stack.pop(), idx))
	}
// Now we get the area of lower heights (since we pushed only if its higher than prev)
// the stack is sorted by ascending order
// get area with lower heights with difference of current and top stack   
	while(stack.length > 0) ans = Math.max(ans, getArea(stack.pop(), idx))
	// console.log(ans)
	return ans
};
