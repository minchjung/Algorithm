// 000<String2>_p07_[A+B-6]10953_java
import java.util.Scanner;
public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in); 
        int t = sc.nextInt();
        sc.nextLine();
        for(int i =0; i < t; i++){ 
            String[] str = sc.nextLine().split(",");
            int ans = Integer.parseInt(str[0]) + Integer.parseInt(str[1]);
            System.out.println(ans);
        }
    }
}
