//Data Structure1_201<Queue>p09_[��ū��]17298_java �ð��ʰ� ��� 
import java.util.*;
// ���� �ڷᱸ�� Ȱ�뿡�� ������ ����.
// ������ ť �� �������� ���� �����ϰ� ������ �ڵ�� ������ �ð��� �� ª��.
// �ᱹ ��¹� �� ���� ó�� Ȱ�뿡�� �ð��ʰ� �� ��Ÿ�� ������ ����ߴµ� .. ���� �ƽ��� ����ó�� ��ü��..
// �� ������ �ε����� ���� �ڷ�� Ȱ���ϴ°� Ű�� �ƴϴ� 
// 0��° ���� �ظ� ã�������� ��� Ž���ϴ°��� �ƴ϶� �ذ� �ƴϸ� �� �������� �Ѿ�� 
// �Ѿ �� ���� (ū��)�ظ� ã�� �Ǹ� �ٽ� �ظ� ��ã�Ҵ� ���� �������� Ž���� ������ �ؿ� ���ϴ°�  <--�̰��� Ű ����Ʈ�� 
// ������ ������ �ش� ���� ���� ū ���� ���ʰ��̹Ƿ� ������ �ȴ�.
// �ᱹ �ϳ��� �ε����� �����ϰ� ū���� ã�������� Ž���ϴ� ���� �ƴ϶� ū ���� �߰��ϰԵǸ� ū ���� ���� ��Ű��
// �Ųٷ� Ž�����ִ� ���̴�
// �ᱹ ���� �ڷ��� �ٽ����� �κ��� Ȱ���ϴ� �� 
// �ε��� �ִ°� ���� �ð� �ʰ� ���ų� �ڷᱸ���� �� ������ �ִٰ� �����ϴ°��� ���� �ΰ� ����. 

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
