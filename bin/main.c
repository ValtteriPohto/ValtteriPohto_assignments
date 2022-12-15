#include <stdio.h>
#include "conversion.h"

int main(){
  double inch, cm;
  printf("How tall are you (Inches)?");
  if (scanf("%.2lf", &inches)){
    cm = cmToInch(inches);
    printf("%.2lf inches is%.2lf cm\n",inch, cm);
  }else{
    prinf("invalid input. Plase input valid numbers.\n"
	  }
      return 0;
  }
  
