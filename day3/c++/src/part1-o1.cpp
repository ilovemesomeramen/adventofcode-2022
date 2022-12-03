#include <iostream>
#include <fstream>
#include <string>

inline unsigned char convertToPrio(char c){
  unsigned char lowercase = (c - 65) / 32;
  return c - ((96 * lowercase) + (38 * (1 - lowercase)));
}


int main(int argc, char *argv[]) {
  std::string input_path = argc > 1 ? argv[1] : "input";
  std::string line;
  int score = 0;
  std::ifstream input (input_path);

  while (std::getline(input, line)){
    unsigned long long bitmap = 0;
    for(size_t i = 0; i < line.size()/2; i++){
      bitmap |= 1ULL << convertToPrio(line[i]);
    }

    for (size_t i = line.size()/2; i < line.size(); i++){
      unsigned char p = convertToPrio(line[i]);
      if (bitmap & (1ULL << p)){
        score += p;
        break;
      }
    }
  }

  input.close();
  std::cout << score << std::endl;
  return 0;
}
