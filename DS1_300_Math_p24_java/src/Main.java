// Data Structure1_300<Math>p24_[Factorial]10827
import java.util.*;
public class Main {
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in); 
		long n= sc.nextLong();
		
		System.out.print(factorial(n));
	}//main String
	
	public static long factorial (long n ){
		if (n <=1){return 1;}
		return n * factorial(n-1);
	} 
}//Main
