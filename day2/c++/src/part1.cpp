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
    char m = line[2] - 87;
    if (o == m){
      score += 3;
    } else if (m == (o % 3) + 1){
      score += 6;
    }
    score += m;
  }
  input.close();
  std::cout << score << std::endl;
  return 0;
}
