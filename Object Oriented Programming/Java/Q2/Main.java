package Q2;
import java.util.*;
public class Main {
    /*
     * NOTE: Create helper functions here if required
     */
     static void input(int arr[],int p,int n,int m,int ans){
        if(n>0){
            ans=inputval(arr,p,m);
            System.out.println(ans);
            n--;
            Scanner scn1 = new Scanner(System.in);
            int sz=scn1.nextInt();
            input(arr,sz,n,sz,ans);
        }
     }
     static int inputval(int arr[],int p,int m){
        if(p>0){
            Scanner scn1 = new Scanner(System.in);
            arr[m-p]=scn1.nextInt();
            p--;
            inputval(arr,p,m);
        }
        int result=calculate(arr,0,m-1);
        return result;
     }

    //  }
    //  static int inputarray(int sum,int e){
    //     if(e>=0)
    //     {
    //     Scanner scn2 = new Scanner(System.in);
    //     int ele=scn2.nextInt();
    //     sum=sum+(ele*ele);
    //     e--;
    //     sum=sum+inputarray(sum,e);
    //     }
    //     return sum;
    //  }
    static int calculate(int arr[],int left,int right){
        if(left==right){
            return arr[left]*arr[left];
        }
        int mid=left+(right-left)/2;
        return calculate(arr,left,mid)+calculate(arr,mid+1,right);
    }
    public static void main(String args[]) {
        /*
         * TODO: Complete this method
         * NOTE: Take input from STDIN and print the output to STDOUT
         */
        int n,m;
        Scanner scn = new Scanner(System.in);
        n=scn.nextInt();
        m=scn.nextInt();
        int arr[];
        arr=new int[m];
        input(arr,m,n,m,0);
        }
}
