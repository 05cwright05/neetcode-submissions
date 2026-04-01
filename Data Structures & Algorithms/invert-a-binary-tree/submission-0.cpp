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
    void swapChildren(TreeNode* curr) {
        if (!curr) {
            return;
        }
        swapChildren(curr->left);
        swapChildren(curr->right);
        TreeNode *temp_node = curr->left;
        curr->left = curr->right;
        curr->right = temp_node;
    }

    TreeNode* invertTree(TreeNode* root) {
        // ight first thought is to recurse down to the first non leaf swap its children. Obviously we gonna have to use postorder to get to bottom and not access
        // roots on the way, also i suckass at recursion so wish me luck
        swapChildren(root);
        return root;
    }
};
