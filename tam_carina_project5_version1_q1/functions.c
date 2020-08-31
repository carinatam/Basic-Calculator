#include "headers.h" //definition of functions from header file
float addition (float x, float y){return x+y;}
float subtraction (float x, float y){return x-y;}
float multiplication (float x, float y){return x*y;}
float division (float x, float y){
    if(y==0){
        return 0;
    }
    else{
        return x/y;
    }
}
