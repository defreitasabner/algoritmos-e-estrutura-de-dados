#include <iostream>
#include <vector>
#include <string>
#include "lib/search/sequentialSearch.hpp"
#include "lib/sort/selectionSort.hpp"

int main() {

    std::vector<int> example {5, 4, 3, 2, 1};

    std::vector<int> result = selectionSort(example);

    std::cout << sequentialSearch(example, 5) << std::endl;

    return 0;
}