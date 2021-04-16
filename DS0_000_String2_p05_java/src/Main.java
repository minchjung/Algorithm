// 000<String2>_p05_[Sort_Inside]1427_java
// descending 
import java.util.*;
public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        char[] str = sc.nextLine().toCharArray();

        Arrays.sort(str);
        String ans="";
        for(char a : str){
            ans = a + ans;
        }
        System.out.print(ans);
    }
}
