#include<stdio.h>
#include<stdlib.h>
int main(){

int a1[50],a2[50],a3[100];
int n1,n2,i,j,k;

printf("enter the number of elements of first array");
scanf("%d",&n1);

printf("enter the number of elements of second array");
scanf("%d",&n2);

printf("enter the elements of first array");

for(int i=0;i<n1;i++){

scanf("%d",&a1[i]);
}


printf("enter the elements of second array");
for(int j=0;j<n2;j++){

scanf("%d",&a2[j]);
}

 i=0;
j=0;
k=0;

while(i<n1 && j<n2){

if(a1[i]<a2[j]){

a3[k++]=a1[i++];


}
else{
a3[k++]=a2[j++];

}
}

while(i<n1){
a3[k++]=a1[i++];
}
while(j<n2){
a3[k++]=a2[j++];
}


printf("the sorted merged array is\n");

for(int i=0;i<n1+n2;i++){
printf("%d",a3[i]);

}
}
