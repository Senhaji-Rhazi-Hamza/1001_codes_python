#ifndef MANDEL_HH
#define LIMIT 500
#define DIV 2
# include <iostream>
# include <fstream>
# include <math.h>
typedef struct
{
  int r;
  int g;
  int b;
}pixel;
pixel *(bw)(int);
double scale_mandel_x(double x, double width);
double scale_mandel_y(double x, double width);
int is_mandelbrot(double x, double y);
bool compute_mandel_bw(int height, int width);
pixel mandel_bw(int i);
pixel mandel_rl(int i);
bool compute_mandel(int height, int width, pixel (*mandel)(int));

#endif /* MANDEL_HH definition*/
