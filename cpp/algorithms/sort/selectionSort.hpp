#pragma once
#include <vector>

inline std::vector<int> selectionSort(std::vector<int> list) {
    for(int i = 0; i < list.size(); i++) {
        int lower = i;
        for(int j = i + 1; j < list.size(); j++) {
            if(list[j] < list[i]) {
                lower = j;
            }
        }
        if(lower != i) {
            int aux = list[i];
            list[i] = list[lower];
            list[lower] = aux;
        }
    }
    return list;
}