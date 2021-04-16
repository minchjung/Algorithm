// 000<String2>p04_[열개씩끊어출력]11721_java
import java.util.Scanner;
public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        String[] str = sc.nextLine().split("");
        int cnt=0;
        for(int i =0; i < str.length; i++){
            System.out.print(str[i]);
            cnt++;
            if(cnt>=10){
                cnt=0;
                System.out.println();
            }
        }
    }//main
}
