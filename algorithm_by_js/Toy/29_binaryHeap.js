// 아래 코드는 수정하지 마세요.
function swap(idx1, idx2, arr) {
  // 두 변수를 바꾸는 방법
  // arr이 reference type이라 가능
  [arr[idx1], arr[idx2]] = [arr[idx2], arr[idx1]];
}

function getParentIdx(idx) {
  // TODO: 여기에 코드를 작성합니다.
	return parseInt((idx-1)/2);
}

function insert(heap, item) {
  // TODO: 여기에 코드를 작성합니다.
	heap.push(item);
	let curIdx = heap.length -1;
	let parIdx = getParentIdx(curIdx);
	while(parIdx >= 0 && heap[curIdx] > heap[parIdx]){
		swap(curIdx,parIdx,heap);
		curIdx = parIdx;
		parIdx = getParentIdx(curIdx); 
	}
	return heap;
}
// 아래 코드는 수정하지 마세요.
const binaryHeap = function (arr) {
  return arr.reduce((heap, item) => {
    return insert(heap, item);
  }, []);
};

// let output = binaryHeap([4, 10, 3, 5, 1]);
// // console.log(output); // --> [10, 5, 3, 4, 1]

output = binaryHeap([ 9, 6, 5, 7, 10, 2, 4 ]);
console.log(output); // --> [ 10, 6, 9, 4, 5, 2, 7 ]