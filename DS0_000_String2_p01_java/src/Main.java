// DS000<Stringp>p01_[더하기사이클]1110_java
import java.util.Scanner;
public class Main {
    static int n;
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();
        if (n >=10 ){   System.out.print(number(n));  }
        else{ 
            n = n*10 + n ;
            System.out.print(number(n));
         } 
    }
    public static int number(int number){
        int cnt=0;
        while(true){
            int num = (number / 10) + (number % 10) ; 
            number = (number % 10)*10 + (num % 10 ) ;
            cnt++;
            if(number == n ){
                return cnt;
            }
        }
    }
}
