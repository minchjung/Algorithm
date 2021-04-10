//Data Structure1_201<Queue>p09_[오큰수]17298_java 시간초과 통과 
import java.util.*;
// 스텍 자료구조 활용에는 변함이 없다.
// 앞전에 큐 와 스택으로 조금 복잡하게 구현한 코드는 오히려 시간이 더 짧다.
// 결국 출력문 과 예외 처리 활용에서 시간초과 와 런타임 에러로 고생했는데 .. 조금 아쉽다 정답처리 자체가..
// 이 문제는 인덱스를 스텍 자료로 활용하는게 키가 아니다 
// 0번째 부터 해를 찾을때까지 모두 탐색하는것이 아니라 해가 아니면 그 다음으로 넘어가고 
// 넘어간 곳 에서 (큰값)해를 찾게 되면 다시 해를 못찾았던 곳을 역순으로 탐색해 지금의 해와 비교하는것  <--이것이 키 포인트다 
// 문제의 조건이 해당 숫자 보다 큰 가장 왼쪽값이므로 성립이 된다.
// 결국 하나의 인덱스를 고정하고 큰값을 찾을때까지 탐색하는 것이 아니라 큰 값을 발견하게되면 큰 값을 고정 시키고
// 거꾸로 탐색해주는 것이다
// 결국 스택 자료의 핵심적인 부분을 활용하는 것 
// 인덱스 넣는걸 몰라서 시간 초과 나거나 자료구조를 잘 못쓰고 있다고 생각하는것은 착각 인것 같다. 

public class Main {
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		Stack<Integer> stack = new Stack<>();
		int[] ans = new int[n];
		int[] arr = new int[n];
		for(int i = 0 ; i < n ; i++) {
			arr[i]=sc.nextInt();
		}
		stack.add(0);
		int i =1;
		while(i < n) {
			while(!stack.isEmpty()) {
				if(arr[stack.peek()] < arr[i]) {
					ans[stack.pop()] = arr[i];
				}else {break;}
			}
			stack.push(i);
			i++;
		}  
		//ans를 미리 세팅하지 않고 빈 부분만 세팅 <--1 
		while(!stack.isEmpty()) {
			ans[stack.pop()]=-1;
		}  
		//StrubgBuilder로 출력문 활용 <--2   : 1,2 이 두가지 수정으로 인해 시간초과가 통과 된다. 
		StringBuilder sb = new StringBuilder();
		for(int j =0; j<n; j++) {
			sb.append(ans[j]).append(' ');
		}
		// 이게 무슨 알고리즘 체크 문제인지 모르것다.
		System.out.println(sb);
	}//main String
}//Main
