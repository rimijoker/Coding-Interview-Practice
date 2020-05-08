/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
using namespace std;
int getLevel(TreeNode* root, int x,int level){
            if(root == NULL) return 0;
    
            if(root->val == x)
                return level;
    
            int l = getLevel(root->left, x, level+1);
            if(l) return l;
    
            return(getLevel(root->right, x, level+1));
}
int isSibling(TreeNode* root, int a, int b) 
{ 
    if(root==NULL)  return 0; 
    if (root->left==NULL || root->right==NULL)
        return(isSibling(root->left, a, b) || isSibling(root->right, a, b)); 
    
    else
        return ((root->left->val==a && root->right->val==b)|| 
            (root->left->val==b && root->right->val==a)|| 
            isSibling(root->left, a, b)|| 
            isSibling(root->right, a, b)); 
} 
class Solution {
public:
    bool isCousins(TreeNode* root, int x, int y) {
        if((getLevel(root,x,1) == getLevel(root,y,1)) && !(isSibling(root,x,y))) 
            return 1; 
        else
            return 0; 
    }
};
