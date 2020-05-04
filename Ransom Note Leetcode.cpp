class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        unordered_map <char, int> mag, note;
        for(auto ch : magazine)
            mag[ch]++;
        for(auto ch: ransomNote)
            if(mag[ch]-- < 1)
                return false;
        return true;
    }
};