// 000<String2>_p08_[제로]10773_java
import java.util.*;
public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in); 
        Stack<Integer> st = new Stack<>();

        int t = sc.nextInt();
        for(int i =0; i < t; i++){ 
            int a= sc.nextInt();
            if(a==0){  st.pop();  }
            else{st.add(a);}
        }
        int sum=0;
        if(st.isEmpty()){  st.add(0);  }
        while(!st.isEmpty()){  sum+=st.pop();  }
        System.out.print(sum);
    }
}
