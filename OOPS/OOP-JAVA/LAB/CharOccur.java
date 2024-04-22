class CharOccur{
public static void main(String args[]){
String word="banana";
char c='a';
int l=word.length();
int i=0;
int count=0;
while(i<=l)
{
 if(word.charAt(i)==c){
 count+=1;
 i++;
}
}
System.out.println("number of "+c+" in "+word+" is "+count);
}
}
