#include <vector>

inline int sequentialSearch(const std::vector<int> &list, const int value) {
    for(int i = 0; i < list.size(); i++) {
        if(list[i] == value) {
            return i;
        }
    }
    return -1;
}