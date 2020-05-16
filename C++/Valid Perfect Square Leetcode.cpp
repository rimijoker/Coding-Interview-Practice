class Solution {
public:
    bool isPerfectSquare(int num) {
        long int left = 1, right = num==1?num:num/2, mid, sq;
        while(right >= left){
            mid = (left+right)/2;
            sq = mid*mid;
            if(sq == num){
                break;
            }
            else if(sq > num){
                right = mid-1;
            }
            else{
                left = mid+1;
            }
        }
        return sq == num;
    }
};