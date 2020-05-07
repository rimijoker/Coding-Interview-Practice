class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int p;
        int count = 0;
        for(auto num : nums){
            if(count == 0)
                p = num;
            count += (num == p)? 1: -1;
        }
        return p;
    }
};