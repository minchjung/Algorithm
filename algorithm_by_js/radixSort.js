function radixSort(arr) {
  // todo: 여기에 코드를 작성합니다.
  const max = arr.reduce((tot, ele) => tot < ele ? ele : tot, -1e11); // 양수 최대값
  const min = arr.reduce((tot, ele) => tot > ele ? ele : tot, 1e11); // 음수로 최소값 (음수 없어도 상관x)
  
  const p = (max+"").length;  // 자릿 수
  const n = (min +"").length;
  
  let l = p > n ? p : n; // 양수 음수 자릿수 둘중 큰 자릿수
  let posit  = new Array(10).fill(0).map(ele => []); // 양수 0~9 인덱스 배열
  let negat  = new Array(10).fill(0).map(ele => []); // 음수 0~9 인덱스 배열
  
  let maxD = 1; 
  while(l--) maxD *= 10; // 최대 자릿수 (10의 자리가 최대 자리면 => 100)

  for(let d = 1; d < maxD; d= d*10){ // 최대 자리까지 (100이하니 d=10까지)
    for(let i = 0 ; i < arr.length; i++){
      if(arr[i] < 0){ // 음수면 음수로 따로처리
        arr[i] = -arr[i]; // 양수로 만들고
        let k = arr[i] < d ? 0 : parseInt(arr[i]/d) % 10; 
        //자리수 보다 작으면 0 !!  크면 해당 자리수로 나누고 10으로 나눈 나머지가 그 자릿수의 숫자 
        negat[9-k].push(-arr[i]); // 그 숫자를 0이면 맨뒤 9면 맨앞으로 거꾸로 넣는다(음수)
      }
      else{// 양수 처리
        let k = arr[i] < d ? 0 : parseInt(arr[i]/d) % 10; //같은 로직
        posit[k].push(arr[i]) // 그 자릿 수 그대로 인덱싱
      }
    }
    let idx= 0; // 실제 arr를 다시 조절
    for(let i = 0 ; i < 10; i++){ // 음수 부터
      while(negat[i].length > 0){ // 0~9까지 탐색 (빈배열 아니면 빈배열 될때까지)
        arr[idx] = negat[i].shift();// 순서대로 앞에서 빼서 다시 arr로 할당
        idx ++;
      }
    }// idx는 연결!!
    for(let i = 0 ; i < 10; i++){ // 양수 처리
      while(posit[i].length > 0){
        arr[idx] = posit[i].shift();
        idx++
      }
    }
  }
  return arr;
}
