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

class Solution {
public:
    int getRecHeight(TreeNode *curr) {
        if (!curr) {
            return 0;
        }
        return max(getRecHeight(curr->left) + 1, getRecHeight(curr->right) + 1);
    }
    int maxDepth(TreeNode* root) {
        //aka count height + 1
        if (!root) return 0;
        return max(maxDepth(root->left) + 1, maxDepth(root->right) + 1);
    }
};
