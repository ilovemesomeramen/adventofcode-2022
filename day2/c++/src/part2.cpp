#include <iostream>
#include <fstream>
#include <string>

int main(int argc, char *argv[]) {
  std::string input_path = argc > 1 ? argv[1] : "input";
  std::string line;
  std::ifstream input (input_path);
  int score = 0;
  while (std::getline(input, line)){
    char o = line[0] - 64;
    char m = (line[2] - 88) * 3;
    if (m == 6){
      score += (o % 3) + 1 ;
    } else if (m == 3) {
      score += o;
    } else {
      score += ((o + 1) % 3) + 1;
    }
    score += m;
  }
  input.close();
  std::cout << score << std::endl;
  return 0;
}
