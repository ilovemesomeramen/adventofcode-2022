#include <iostream>
#include <fstream>
#include <string>

int main() {
  std::string line;
  std::ifstream input ("input");
  int max = 0;
  while (std::getline(input, line)){
    int cal_count = 0;
    do{
      cal_count += std::stoi(line);
    } while (std::getline(input, line) && !line.empty());
    if(cal_count > max)
      max = cal_count;
  }
  input.close();
  std::cout << max << std::endl;
  return 0;
}
