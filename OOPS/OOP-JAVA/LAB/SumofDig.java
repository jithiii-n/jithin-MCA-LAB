class SumofDig{
public static void main(String args[]){
int num=123;
int n=num;
int sum=0;
while(num!=0)
{
 int d=num%10;
 sum+=d;
 num=num/10;
}
System.out.println("Sum of Digits of "+n+" is:"+sum);
}
}
