//000<Math_Numeric>p02_[베르트랑공준]4928_java
// time exceed !!   
// 1~ 123456 * 2 까지 소수 인지 아닌지 먼저 에라토스테네스로 구하고 조회로 해결  
import java.util.*;
public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        ArrayList <Integer>ans = new ArrayList<>(); 
        // set 1,  if index number is Prime Number or set 0  
        ans.add(0);  
        ans.add(0); 
        ans.add(1);
        for(int i =3; i<=123456*2; i++){  ans.add(  prime( i )  ) ;  }
        // To get input value and evaluate it, till to get 0 as input 
        while( true ){ 
            int n = sc.nextInt();
            if (n==0){  break; }
            else{
                int sum = 0 ;
                // sum of Prime Number of n+1 ~ n*2
                for(int i =n+1 ; i <= n*2; i++){
                    sum += ans.get(i); 
                }
                System.out.println(sum);
            }
        }

    }
    public static int prime(int a){
        int check =0;
        for(int i =2; i <= Math.pow(a,0.5)+1; i++){
            if(a % i==0){   check++; }
        }
        if(check ==0){  
            return 1;
        }return 0 ;
    }
}
