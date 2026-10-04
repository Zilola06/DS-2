#include <iostream>
#include <vector>
using namespace std;

void subsets(vector<int>& nums, int index, vector<int>& current) {
    //base case
    if (index == nums.size()) {
        cout << "{ ";

        for (int x : current)
            cout << x << " ";

        cout << "}" << endl;
        return;
    }

    //include nums[index]
    current.push_back(nums[index]);
    subsets(nums, index + 1, current);

    //skip nums[index]
    current.pop_back();
    subsets(nums, index + 1, current);
}

int main() {
    vector<int> nums = {1, 2};
    vector<int> current;

    subsets(nums, 0, current);

    return 0;
}
