//Data Structure1_201<Queue>p09_[오큰수]17298_java 시간초과 통과 
import java.util.*;

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
		// i 가 항상 stack의 값보다 1만 크다! 
		//바로 옆의 값만 조회 비교하고 넘어간다.
		while(i < n) {// 마지막 인덱스까지 돌린다.
			while(!stack.isEmpty()) {
				if(arr[stack.peek()] < arr[i]) {
					ans[stack.pop()] = arr[i];//큰값이 나타면 stack 최상단 값과 거꾸로 비교
				}else {break;}// 스택이 비거나, 스택값이 (크다고 고정한 비교)값 보다 더 크면 탈출한다
			}// +1옆자리에 계속 작은값이면 stack에 쌓이게 된다. 
			//위의 while문 조건에 맞으면 stack값을 털어준다. 
			//결국 큰 값이 없으면 stack 에 쌓이게 되고, 아래 1번에서 정리해준다.  
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
