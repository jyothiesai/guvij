import java.util.*;
class bitwise
{
    public static void main(String[] args) {
        Scanner in=new Scanner(System.in);
        int num1=in.nextInt();
        int num2=in.nextInt();
        int res=num1^num2;
        String byt=Integer.toBinaryString(res);
        int count=0;
        for(int i=0;i<byt.length();i++)
        {
            if(byt.charAt(i)=='1')
            {
                count++;
            }
        }
        System.out.println(count);
        in.close();
    }
}
