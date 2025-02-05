#include <algorithm>
#include <cmath>


// Optimal (O(log(n))) time
class Solution {
public:

    int findHeaterWarmth(int heaterPosition, const vector<int>& houses, int left, int right) {
        int mid = 0;
        int distance = 0;
        while (left < right) {
            mid = left + (right - left) / 2;
            if (heaterPosition == houses[mid]) {
                distance = max(distance, abs(houses[mid] - houses[left]));
                distance = max(distance, abs(houses[mid] - houses[right]));
            }
            else if (heaterPosition > houses[mid]) {
                distance = max(distance, abs(houses[mid] - houses[left]));
                distance = max(distance, abs(houses[mid] - houses[right]));
                left = mid + 1;
            }
            else {
                distance = max(distance, abs(houses[mid] - houses[left]));
                distance = max(distance, abs(houses[mid] - houses[right]));
                right = mid - 1;
            }
        }

        return distance;
    }

    int findRadius(vector<int>& houses, vector<int>& heaters) {
        // Make sure the houses are sorted in order so that
        // we can place our heater in order.
        houses.sort();
        heaters.sort();

        int minWarmRadius = MAX_INT;

        for (auto& heater : heaters) {
            // See if we can track distance for each heater
            minWarmRadius = min(minWarmRadius, findHeaterWarmth(heater, houses, 0, houses.size() - 1));
        }

        return minWarmRadius;
    }
};