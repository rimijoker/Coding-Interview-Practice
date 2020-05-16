class Solution {
public:
    string removeKdigits(string num, int k) {
        if(num.length() <= k) return "0";
        vector <char> stack;
        int size = num.length(), counter = 0;
    
        while(counter<size){
            while(k > 0 && !stack.empty() && stack.back() > num[counter]){
                stack.pop_back();
                k--;
            }
            stack.push_back(num[counter]);
            counter++;
        }
        while(k > 0){
            stack.pop_back();
            k--;
        }
        num.clear();
        
        for(int i=0; i<stack.size(); i++){
            num.push_back(stack[i]);
        }
        stack.clear();
        while(num.length() > 1 && (int) num[0] == (int) '0')
            num.erase(0, 1);
        
        return num;
    }
};