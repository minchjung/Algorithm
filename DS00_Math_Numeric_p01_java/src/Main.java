//000<Math_Numeric>p01_[소수]2581_java
// Dont forget 2 is Prime Number !! 
import java.util.*;
public class Main {
    static ArrayList<Integer> primeNum = new ArrayList<>();
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);

        int m = sc.nextInt();
        int n = sc.nextInt();
        int sum=0;
        for(int i=m; i<=n; i++){    
            if(i!=1){  sum+=prime(i); }
        }
        Collections.sort(primeNum);
        if(sum==0){
            System.out.println(-1);
        }else{
            System.out.println(sum);
            System.out.println(primeNum.get(0));  
        }
    }
    public static int prime(int a){
        int check =0 ;
        for(int i =2; i <= (int)Math.pow(a, 0.5)+1 ; i++ ){
            if(a==2){break;}// DONT FORGET 2 = PRIME NUMBER
            else if( a % i ==0){   check++;  }
        }
        if(check ==0){  
            primeNum.add(a);  
            return a ;
        }else{return 0;}
    }
}
