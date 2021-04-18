//000<Math_Numeric>p03_[Prime factorization]11653_java
import java.util.*;
public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for(int i=2; i*i <= n; i++){
            while (n % i == 0){
                System.out.println(i);
                n /= i ;
            }
        }
        if(n !=1){  System.out.println(n);  }
    }
}
