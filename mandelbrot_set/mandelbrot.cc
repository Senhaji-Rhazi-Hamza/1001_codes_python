#include "mandelbrot.hh"
double scale_mandel_x(double x, double width)
{
  double maxr = 2;
  double minr = -2;
  return (minr + x * (maxr - minr) /width );
}//i need to scal the y axis to an interval
//where mandelbrot wil appear
double scale_mandel_y(double y, double height)
{
  double maxi = 2;
  double mini = -2;
  return (mini + y * (maxi - mini) /height );
}//i need to scal the y axis to an interval
//where mandelbrot wil appear
int is_mandelbrot(double x, double y)
{
  int i = 0;
  double zx = 0;
  double zy = 0;
  double tmp = 0;
  double modz2 = 0; //declared as global, to not change
  //the general prototype of mandel function
  //because i dont need modz2 in all functions
  for (i = 0; (i < LIMIT) && ( modz2 < DIV); i++)
  { 
    tmp = zx * zx - zy * zy + x;
    zy = 2 * zx * zy + y;
    zx = tmp;
    modz2 = zx * zx + zy * zy;
  }
    return i;
}//test if a point(x,y) belong to mandelbrot set
//and if not return when it diverge by returning
//i < LIMIT
bool compute_mandel_bw(int height, int width)
{
  std::ofstream file;
  file.open("mandel.ppm");
  if (!file.is_open())
  {
    std::cout<<"usage : unnable to create file mandel.ppm";
  return false;
  }
  else
  {
    file << "P3\n";
    file << width << " " << height << "\n";
    file << "255\n";
    for (int j = 0; j < height; j++)
    {
      double y = scale_mandel_y(j, height);
      for (int i = 0; i < width; i++)
      {
        double x = scale_mandel_x(i, width);
        int is_mandel = is_mandelbrot(x,y);
        if (is_mandel == LIMIT)
          file << "0" << " " << "0" << " " << "0" "\n";
        else
          file << "255" << " " << "255" << " " << "255" "\n"; 
      }
      file << "\n"; 
    }
    file << std::endl; 
    return true;
  }
}
// browse the screen pixel by pixel and will chose the color
//depending on the function mandel
bool compute_mandel(int height, int width, pixel (*mandel)(int))
{
  std::ofstream file;
  file.open("mandel.ppm");
  if (!file.is_open())
  {
    std::cout<<"usage : unnable to create file mandel.ppm";
    return false;
  }
  else
  {
    file << "P3\n";
    file << width << " " << height << "\n";
    file << "255\n";
    for (int j = 0; j < height; j++)
    {
      double y = scale_mandel_y(j, height);
      for (int i = 0; i < width; i++)
      {
        double x = scale_mandel_x(i, width);
        int is_mandel = is_mandelbrot(x,y);
        pixel color = mandel(is_mandel);
        file << color.r << " " << color.g << " " << color.b << "\n";
      }
      file << "\n"; 
    }
    file << std::endl; 
    return true;
  }
}
//
pixel mandel_bw(int i)
{
  pixel color;
  color.r = 0;
  color.g = 0;
  color.b = 0;
  if (i != LIMIT)
  {
    color.r = 255;
    color.g = 255;
    color.b = 255;
  }
  return color;
}
pixel mandel_rl(int i)
{
  pixel color;
  color.r = 0;
  color.g = 0;
  color.b = 0;
  if (i != LIMIT)
  {
    color.r = i % 255;
    color.g = (i * 2555) % 255;
    color.b = 125;
  }
return color;
}
