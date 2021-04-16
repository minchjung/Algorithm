// 000<String2>p02_[OX퀴즈]8958_java

public class Main{
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in); 
        int n = sc.nextInt(); 
        sc.nextLine();
        for( int i=0; i<n ; i++){
            List<String> arr = Arrays.asList(sc.nextLine().split("")); 
            System.out.println(count(arr));
        }
    }//main 
    public static int count(List<String> arr){
        int[] cnt = new int[arr.size()];
        int c = 0 ;
        for(int i =0; i < arr.size(); i++){
            if (!arr.get(i).equals("O")){
                cnt[i]=0;
                c=0;
            }else{
                c++;
                cnt[i]=c;
            }
        }
        int sum=0;
        for(int a : cnt){
            sum+=a;
        }
        return sum;
    }
}
