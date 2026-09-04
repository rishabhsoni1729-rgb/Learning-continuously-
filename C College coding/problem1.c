//write a program to take principal, rate and time as input and calculate a) simple interest b) compound interest.

#include<stdio.h>

int main()
{
    float Principal_Amount;
    float Rate;
    float Time;
    float Simple_Interest;

    printf("Enter the prinicipal amount :");
    scanf("%f",& Principal_Amount);

    printf("Enter the Rate :");
    scanf("%f",& Rate);

    printf("Enter the time :");
    scanf("%f",& Time);

    Simple_Interest = (Principal_Amount*Rate*Time)/100;

    printf("Simple_Interest is 0.2%f" , Simple_Interest);
     

}