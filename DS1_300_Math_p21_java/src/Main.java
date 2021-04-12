// Data Structure1_300<Math>p21_[lcm]1934
import java.util.*;
public class Main {
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in); 
		int n = sc.nextInt();

		for(int i=0; i<n ; i++){
			int a = sc.nextInt();
			int b = sc.nextInt();
			if(a < b){
				int tem = a ; 
				a = b ; 
				b = tem; 
			}
			int a2=a;
			int b2=b;
			while(b2>0){
				int t = b2;
				b2= a2 % b2 ; 
				a2 = t ;
			}
			if (a ==1){System.out.println(a*b);}
			else{System.out.println(a/a2*b);}
		}
	}//main String
}//Main
