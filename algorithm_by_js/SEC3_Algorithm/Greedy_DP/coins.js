function fun_A(k) {
	coin = [5000,1000,500,100,50,10,5,1];
	let point = 0;
	let ans = 0;
	while(k > 0){
		const cur = coin[point];
		while(k - cur >= 0){
			k -= cur
			ans++;
		}
		point++;
	}
	return ans
}
let a = partTimeJob(11215523)
console.log(a)