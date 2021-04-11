//Data Structure1_201<Stack>p11_[후위연산자2]1935_java
//Postfix Operator2
import java.util.*;
public class Main {
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in); 
		
		int n = sc.nextInt(); 
		sc.nextLine();
		// stack = stack the number;    problem = all string info;   alphNum = save numbers coresponds to each character  
		Stack <Double> stack = new Stack<>();
		String problem = sc.nextLine().trim();
		int[] alphNum = new int[26];
		//alphNum[0] = input number ('A'= input number).... 
		for(int i=0; i<n; i++){
			alphNum[i]= sc.nextInt();
		}
		// Search all char one by one from all String 
		for(int i=0; i < problem.length();i++){
			char c = problem.charAt(i);
			// if its operator, pop two items from the stack and operate them
			if(c=='*' || c== '/' || c=='+' || c=='-'){
				// calculate them and push back into the stack
				double a = stack.pop() ; 
				double b = stack.pop() ; // make sure its double not float..;;
				if(c=='*'){stack.push(b*a);}
				else if(c == '/'){stack.push(b/a);}
				else if(c == '+'){stack.push(b+a);}
				else{stack.push(b-a);}
			}
			else{ // push the number into the stack
				stack.push((double)(alphNum[c-'A']));}
		}
		// there should be only one item in the stack but.. yea 		
		while(!stack.isEmpty()){
			System.out.printf("%.2f",stack.pop());
		}
	}//main String
}//Main
