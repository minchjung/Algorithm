// 아래 코드는 수정하지 마세요.
function swap(idx1, idx2, arr) {
  [arr[idx1], arr[idx2]] = [arr[idx2], arr[idx1]];
}

function getParentIdx(idx) {
  // TODO: 여기에 코드를 작성합니다.
	return parseInt((idx-1)/2);
}

// let output = heapSort([5, 4, 3, 2, 1]);
function insert(heap, item) {
  // TODO: 여기에 코드를 작성합니다.
	heap.push(item);
	let curIdx = heap.length -1;
	let parIdx = getParentIdx(curIdx);
	while(parIdx >= 0 && heap[curIdx] < heap[parIdx]){
		swap(curIdx,parIdx,heap);
		curIdx = parIdx;
		parIdx = getParentIdx(curIdx); 
	}
	return heap;
}

function removeRoot(heap) { 
  // TODO: 여기에 코드를 작성합니다.
	swap(0, heap.length-1, heap); // root = maxVal, heap[lastIdx] = maxVal 
	heap.pop();
	if(heap.length > 1){
		let minIdx = 0  // supposed to be Min value on root position
		let curIdx = 1; // Just give temporal idx for the While-loop below 
		while(minIdx !== curIdx){
			curIdx = minIdx; // Give current position as it starts from root( or newer root) 
			let left = curIdx*2 +1; // left childe
			let right = curIdx*2 +2; // right one of the root(, that currently has min Value)
			if(left < heap.length && heap[left] < heap[minIdx]){
				minIdx = left // swap as it supposed to be
			}
			if(right < heap.length && heap[right] < heap[minIdx]){
				minIdx = right // swap as it spussoed to be 
			}
			swap(curIdx,minIdx,heap);
		}
	}
	return heap;
}

// 아래 코드는 수정하지 마세요.
const binaryHeap = function (arr) {
  return arr.reduce((heap, item) => {
    return insert(heap, item);
  }, []);
};

const heapSort = function (arr) {
	let minHeap = binaryHeap(arr); // First to make the Max-Heap
  // TODO: 여기에 코드를 작성합니다.
	let ans = []
	while(minHeap.length > 0){
		ans.push(minHeap[0]);
		minHeap = removeRoot(minHeap);
	}
	return ans;
};

// let output = heapSort([5, 4, 3, 2, 1]);
// console.log(output); // --> [1, 2, 3, 4, 5]

// output = heapSort([3, 1, 21]);
// console.log(output); // --> [1, 3, 21]

// output = heapSort([4, 10, 3, 5, 1]);
// console.log(output); // --> [1, 3, 4, 5, 10]

// output = heapSort([4, 10, 3, 5, 1])
// console.log(output); // --> [1, 3, 4, 5, 10]

// let output = heapSort([9, 6, 7, 4, 5, 2, 10]);
// console.log(output)

// output = heapSort([4,11,3,31,21,20,99,14,8,6,27,51,9,1]);
// console.log(output); // --> [1, 3, 4, 5, 10]
