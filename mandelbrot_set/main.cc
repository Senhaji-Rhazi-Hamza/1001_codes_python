#include "timer.h"
#include "mandelbrot.hh"
#include <string.h>
int get_width(int argc, char *argv[]);
int get_height(int argc, char *argv[]);
char get_arg(int argc, char *argv[]);
void help();
int main(int argc, char *argv[])
{
  char arg = get_arg(argc, argv);
  int width = get_width(argc, argv);
  int height = get_height(argc, argv);
  //geting arg parameters
  if ((arg == 'h'))
    help();
  else if (arg == 'n')
    compute_mandel(width, height, mandel_bw);
  else if (arg == 'r')
    compute_mandel(width, height, mandel_rl);
  else
    help();

  return 0;
}
int get_width(int argc, char *argv[])
{
  if (argc == 4)
    return atoi(argv[2]);
  else if (argc == 3)
    return atoi(argv[1]);
  else
  {
    help();
    exit(-1);
  }
}
int get_height(int argc, char *argv[])
{
  if (argc == 4)
    return atoi(argv[3]);
  else if (argc == 3)
    return atoi(argv[2]);
  else
  {
    help();
    exit(-1);
  }
}
char get_arg(int argc, char *argv[])
{
  for (int i = 1; i < argc; i++)
  {
    if (strcmp(argv[i],"-h") == 0)
      return 'h';
    else if (strcmp(argv[i],"-n") == 0)
      return 'n';
    else if (strcmp(argv[i],"-r") == 0)
      return 'r';
    else
      return 'n';
  }
  return 'h';
}
void help()
{
  std::cout << "usage: ./mandel [- option] width height\n";
  std::cout << "options are :\n";
  std::cout << "-h display help :\n";
  std::cout << "-n draw a black and white mandel :\n";
  std::cout << "-r having another drawing colors :\n";
  std::cout << "u could use your own color by implementing a mandel_bw type";
  std::cout << " function and pass it as pointer function do compute mandel\n";
}
