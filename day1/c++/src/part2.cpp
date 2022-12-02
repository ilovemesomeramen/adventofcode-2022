#include <iostream>
#include <fstream>
#include <string>

int main() {
  std::string line;
  std::ifstream input ("input");
  int max[] = {0, 0, 0};
  while (std::getline(input, line)){
    int cal_count = 0;
    do{
      cal_count += std::stoi(line);
    } while (std::getline(input, line) && !line.empty());

    if(cal_count > max[0]){
      max[2] = max[1];
      max[1] = max[0];
      max[0] = cal_count;
    } else if (cal_count > max[1]){
      max[2] = max[1];
      max[1] = cal_count;
    } else if (cal_count > max[2]){
      max[2] = cal_count;
    }
  }
  input.close();
  std::cout << max[0] + max[1] + max[2] << std::endl;
  return 0;
}
