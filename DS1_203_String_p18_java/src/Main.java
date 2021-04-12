// Data Structure1_203<String>p18_[FourDigits]10824
import java.util.*;
public class Main {
	// the input value  is the oversize of int 
	// so nextLong and pareLong'd be used from the String 
	public static void main(String[] args){
		long[] arr = new long[4];
		Scanner sc = new Scanner(System.in); 
		for (int i =0; i <4 ; i++){
			arr[i]=sc.nextLong(); // <--should be long 
		}
		long a = Long.parseLong(arr[0]+""+arr[1]);
		long b = Long.parseLong(arr[2]+""+arr[3]);
		System.out.print(a+b);

	}//main String
}//Main
