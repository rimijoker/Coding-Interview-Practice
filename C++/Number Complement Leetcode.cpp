class Solution {
public:
    int findComplement(int num) {
        int res = 0;
        for(int shift = 0; num; ++shift, num >>= 1)
            res |= !(num & 1) << shift;
        return res;
    }
};