function shadowOfPapers(papers) {
  let container = [];
  let maxY = 0;
  // Get the container-array to have the segment line for all sorted by X-ponit, 
  // We'd also like to know that its starting point or not. <-- since counting value soley on it 
  // So it gives the boolean flag as isStart, 
  // and, differentiate every single X, with same appropiate Y range
  for(let i = 0 ; i < papers.length; i++){
    const obj = {
      x : papers[i][0],
      y : [papers[i][1], papers[i][1]+papers[i][3]-1],
      isStart : true
    }
    const obj2 = {
      x : papers[i][0] + papers[i][2],
      y : [papers[i][1], papers[i][1]+papers[i][3]-1],
      isStart : false
    }
    maxY = Math.max(maxY, obj.y[1]);
    container.push(obj, obj2)
  }  
  container.sort((a,b) => a.x - b.x); // Make sure it sorted for X
  
  // Set y-range array, and count +1 for the first y-range as we start from second one (i=1)
  // Obviously very first one is the starting line
  let ycnt = new Array(maxY+1).fill(0).map( (ele, idx) => 
    idx >= container[0].y[0] && idx <= container[0].y[1] 
    ? 1 : 0 )
  /*
   We get the Area of each section on every next line 
   First count marked Y on ycnt-array, 
   that is the height for that section-area
   Simply get the width, (current X position - prev X position )
   area += w * h 

   AFTER !! THAT !! 
   Mark the y-range,
   1) if its starting line => ycnt +1 in that range of y-line
   2) if its ending line => ycnt -1 in that range of y-line
   This is key to calculate every segment of area along with X
   */ 
  let area = 0; 
  for(let i = 1 ; i < container.length; i++){
    const h = ycnt.reduce( (tot, ele) => ele >= 1? tot + 1 : tot, 0); // counting y for Height
    const w = container[i].x - container[i-1].x;  // simply have Width
    const v = container[i].isStart ? 1 : -1; // decide the value to give dis- or just counting
    area += h * w 
    for(let j = container[i].y[0]; j <= container[i].y[1]; j++) ycnt[j] += v; // counting y after all
  }
  return area 
}
