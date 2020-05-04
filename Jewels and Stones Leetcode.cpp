class Solution {
public:
    int numJewelsInStones(string J, string S) {
        unordered_set<char> n(J.begin(),J.end());
        int jewels=0;
        for(int i=0;i<S.length();i++){
            if(n.count(S[i])!=0)jewels++;
        }
        return jewels;
    }
};