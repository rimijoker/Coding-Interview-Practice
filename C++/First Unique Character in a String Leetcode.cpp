class Solution {
public:
    int firstUniqChar(string s) {
        map<char, int> times;
        for(auto ch : s) times[ch]++;
        int length = s.size();
        for(int i=0; i<length; i++){
            if(times[s[i]] == 1)
                return i;
        }
        return -1;
    }
};