// Data Structure1_300<Math>p20_[gcf/lcm]10430
// Greatest common factor / Least common multiple
import java.util.*;
public class Main {
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in); 
		int a = sc.nextInt();
		int b = sc.nextInt();
		if(a < b){
			int tem = a ; 
			a = b ; 
			b = tem; 
		}
		int c = gcf(a,b);
		System.out.println(c);
		System.out.println(a*b/c);
	}//main String
	public static int gcf(int a, int b){
		while(b!=0){
			int r = a % b ; 
			a = b ;
			b = r ; 
		}
		return a ; 
	}
}//Main
