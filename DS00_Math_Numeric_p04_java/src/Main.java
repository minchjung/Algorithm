//000<Math_Numeric>p04_[약수]]1037_java
import java.util.*;
public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int a = 0 ; 
        int b = 100000;
        for(int i=0; i < n; i++){
            int num = sc.nextInt();
            if (a < num){   a = num;   }
            if (b > num){   b = num;   }
        }
        System.out.println(a*b);
    }
}
