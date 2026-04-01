#include <iostream>
class Solution {
public:
    bool canFunction(int k, vector<int> piles, int h) {
        int index = 0;
        while (index < piles.size()) {
            //std::cout << k << piles[index] << h << std::endl;
            //how many hours to take
            int num_hours = piles[index] / k;
            piles[index] -= num_hours * k;
            h-=num_hours;
            if (piles[index] > 0) {
                h--;
            }
            index++;
        }
        if (h < 0) {
          return false;
        }
        return true;
    }
    int minEatingSpeed(vector<int>& piles, int h) {
        // first thought is to try a bsta where my answer space is between
        // 1 and 1,000,000,000 
        // but is the can function efficient i would have to go thru the whole pile a numbner of times. It's a good start though

        int left = 1;
        int right = 1000000000;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (canFunction(mid, piles, h)) {
                // this jawn works so we dont need anything bigger but might need it
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        int mid = left + (right - left) / 2;
        return mid;
    }
};
