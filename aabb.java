/* package whatever; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Ideone
{
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
		Scanner sc=new Scanner(System.in);
		String s=sc.next();
		StringBuilder sb=new StringBuilder();
		for(int i=0;i<=s.length()-1;i=i+2)
		{
			char a=s.charAt(i);
            int c=s.charAt(i+1)-'0';
            for(int j=0;j<c;j++)
            {
                sb.append(a);
            }
		}
		System.out.print(sb.toString());
	}
}
