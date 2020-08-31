#include "headers.h" //get functions from other file
main(){
int choice;
float a, b, answer; //declare all integers
printf("Welcome!\n");
while(choice!=5){
    printf("Press 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division, and 5 for exit: ");
    scanf("%d", &choice);
    if(choice!=1 && choice!=2 && choice!=3 && choice!=4 && choice!=5){ //if it's not a number from 1-5
        printf("This is an invalid command, please try again.\n");
        continue; //go to bottom of loop
    }
    else if(choice==5){ //if they want to exit the program
        printf("Have a good day!");
        break; //exit while loop
    }
    else{ //if it is for computing answers
        printf("Please provide the first number: ");
        scanf("%f", &a);
        printf("Please provide the second number: ");
        scanf("%f", &b); //get two numbers
        }
        if(choice==1){ //addition
            answer=addition(a, b);
            printf("The result of (%g + %g) is %g\n", a, b, answer);
        }
        else if(choice==2){ //subtraction
            answer=subtraction(a, b);
            printf("The result of (%g - %g) is %g\n", a, b, answer);
        }
        else if(choice==3){ //multiplication
        answer=multiplication(a, b);
            printf("The result of (%g * %g) is %g\n", a, b, answer);
        }
        else if(choice==4){ //division
            answer=division(a, b);
            if(answer==0){
                printf("There is no answer for %g / %g since the denominator is 0\n", a, b);
        }
            else{
                printf("The result of (%g / %g) is %g\n", a, b, answer);
        }
    }
}
return 0;
}
