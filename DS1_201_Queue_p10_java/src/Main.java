//Data Structure1_201<Queue>p09_[오큰수]17298_java 시간초과
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
			ans[i]=-1;
		}
		stack.add(0);
		int i =1;
		while(i < n) {
			while(!stack.isEmpty()) {
				if(arr[stack.peek()] < arr[i]) {
					ans[stack.pop()] = arr[i];
				}else {break;}
			}
			stack.add(i);
			i++;
		}
		for(int j =0; j<n; j++) {
			System.out.print(ans[j]+" ");
		}
	}//main String
}//Main
