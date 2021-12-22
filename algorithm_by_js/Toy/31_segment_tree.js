const rangeMinimum = function (arr, ranges) {
	// TODO: 여기에 코드를 작성합니다.
	const H = Math.ceil(Math.log(arr.length)/Math.log(2));
	const N = Math.pow(2, H)*2;
	let tree ={node:1, val:1e10 ,start:0, end:arr.length-1, left: null, right:null};
	
	const setTree =(tree) => {
		if(tree.start === tree.end){
			tree.val = arr[tree.start];
			return tree.val
		}
		tree.left = {
			node: parseInt(tree.node*2), 
			val:1e10, 
			start:tree.start, 
			end:parseInt((tree.start+tree.end)/2),
			left :null, right:null
		}
		tree.right = {
			node: parseInt(tree.node*2)+1, 
			val:1e10, 
			start:parseInt((tree.start+tree.end)/2)+1, 
			end:tree.end,
			left:null, right:null
		}
		tree.val = Math.min(setTree(tree.left),setTree(tree.right));
	}
	setTree(tree)
	tree.val = Math.min(tree.left.val, tree.right.val);
	const query = (tree, from, to) => {
		if(tree.start > to || tree.end < from){
			return 1e11;
		}
		if(tree.start >= from && tree.end <= to){
			return tree.val;
		}
		return Math.min(
			query(tree.left,from,to),
			query(tree.right,from,to)
		)
	}
	console.log(tree.left.val)
	console.log(tree.right.val)
	return query(tree,0,3)
	// return ranges.map(ele=>
	// 	query(tree,ele[0],ele[1])
	// )

}

const arr = [1, 3, 2, 7, 9, 11];
const mins = rangeMinimum(arr, [
  [1, 4],
  [0, 3],
]);
console.log(mins); // --> [2, 1]