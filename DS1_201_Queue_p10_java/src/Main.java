//Data Structure1_201<Queue>p09_[오큰수]17298_java 시간초과
import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		Queue<Integer> q1 = new LinkedList<>();
		Queue<Integer> q2 = new LinkedList<>();
		
		int n = sc.nextInt();
 
		for(int i =0; i < n; i++) { 
			int a = sc.nextInt();
			q1.add(a); 
		} 
		while(!q1.isEmpty()) {
			int now = q1.poll();
			while (!q1.isEmpty()){
				int nxt = q1.poll();
				q2.offer(nxt);
				if (nxt > now) {
					System.out.print(nxt+" ");
					while(!q2.isEmpty()) {
						q1.offer(q2.poll());
					}
					break;
				}
				if(!q1.isEmpty()) {
					System.out.print(-1+" ");
					while(!q2.isEmpty()) {
						q1.offer(q2.poll());
					}
					break;
				}
			}
		}
		System.out.print(-1);
	}//main String
}//Main
