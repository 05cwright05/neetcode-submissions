/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        //need to do this in O(n) time with no tail

        // 1 2 3 4
        // 2 1 3 4
        ListNode *c = head;
        if (!c) {
            return c;
        }
        ListNode *p = nullptr; // the previous pointer

        while (c) {
            ListNode *next = c->next;
            c->next = p;
            p = c;
            c = next;
        }
        return p;

    }
};
