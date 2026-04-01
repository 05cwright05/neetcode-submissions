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
    bool hasCycle(ListNode* head) {
        ListNode* hare = head;
        ListNode* turtoise = head;

        while (hare != nullptr && hare->next != nullptr) {
            hare=hare->next;
            if (hare == turtoise) return true;
            hare=hare->next;
            if (hare == turtoise) return true;
            turtoise = turtoise->next;
        }
        return false;
    }
};
