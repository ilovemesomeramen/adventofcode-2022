#include <iostream>
#include <fstream>
#include <string>
#include <unordered_set>

int main(int argc, char *argv[]) {
  std::string input_path = argc > 1 ? argv[1] : "input";
  std::string line;
  int score = 0;
  std::ifstream input (input_path);

  while (std::getline(input, line)){
    std::unordered_set<char> b1(line.c_str(), line.c_str() + line.size()/2);

    for (size_t i = line.size()/2; i < line.size(); i++){
      char c = line[i];
      if (b1.count(c)){
        if(c >= 'a')
          score += c - 96;
        else
          score += c - 64 + 26;
        break;
      }
    }
  }

  input.close();
  std::cout << score << std::endl;
  return 0;
}
