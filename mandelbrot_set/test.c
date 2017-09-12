#include <math.h>
#include <stdio.h>
#include "timer.h"
int main()
{
  int a = log(100)/log(10);
  double t = 1;
  {
  scoped_timer timer(t);
  std::out << "the value of a is %d\n" ; 
  }
}
