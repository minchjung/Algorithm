//Data Structure1_201<Queue>p09_[오큰수]17298_java 시간초과
import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		ArrayList<Integer> arr = new ArrayList<Integer>();
		Stack<Integer> stack = new Stack<Integer>();
		
		int n = sc.nextInt();
 
		for(int i =0; i < n; i++) { 
			int a = sc.nextInt();
			arr.add(a); 
		} 
		for(int i = 0 ; i < n-1; i++) {
			int check=0;
			for (int j = i+1 ; j < n; j++) {
				if(arr.get(i) < arr.get(j)) {
					int nxt = arr.get(j);
					stack.add(nxt);
					check = -1;
		 			break; }
				if(j==n-1 && check==0) {
					stack.add(-1);}
			}
		}
		stack.add(-1);
		for(int s :stack) {
			System.out.print(s+" ");
		} 
		
	}//main String
}//Main
