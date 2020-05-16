class Solution {
public:
    int singleNonDuplicate(vector<int>& nums) {
        
        int nonduplicate = nums[0];
            
        for(int i = 1; i < nums.size(); i++)
            nonduplicate ^= nums[i];
        
        return nonduplicate;
    }
};