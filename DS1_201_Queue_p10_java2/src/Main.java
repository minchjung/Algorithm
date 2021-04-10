//Data Structure1_201<Queue>p09_[��ū��]17298_java �ð��ʰ� ��� 
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
		// i �� �׻� stack�� ������ 1�� ũ��! 
		//�ٷ� ���� ���� ��ȸ ���ϰ� �Ѿ��.
		while(i < n) {// ������ �ε������� ������.
			while(!stack.isEmpty()) {
				if(arr[stack.peek()] < arr[i]) {
					ans[stack.pop()] = arr[i];//ū���� ��Ÿ�� stack �ֻ�� ���� �Ųٷ� ��
				}else {break;}// ������ ��ų�, ���ð��� (ũ�ٰ� ������ ��)�� ���� �� ũ�� Ż���Ѵ�
			}// +1���ڸ��� ��� �������̸� stack�� ���̰� �ȴ�. 
			//���� while�� ���ǿ� ������ stack���� �о��ش�. 
			//�ᱹ ū ���� ������ stack �� ���̰� �ǰ�, �Ʒ� 1������ �������ش�.  
			stack.push(i);
			i++;
		}  
		//ans�� �̸� �������� �ʰ� �� �κи� ���� <--1 
		while(!stack.isEmpty()) {
			ans[stack.pop()]=-1;
		}  
		//StrubgBuilder�� ��¹� Ȱ�� <--2   : 1,2 �� �ΰ��� �������� ���� �ð��ʰ��� ��� �ȴ�. 
		StringBuilder sb = new StringBuilder();
		for(int j =0; j<n; j++) {
			sb.append(ans[j]).append(' ');
		}
		// �̰� ���� �˰��� üũ �������� �𸣰ʹ�.
		System.out.println(sb);
	}//main String
}//Main
