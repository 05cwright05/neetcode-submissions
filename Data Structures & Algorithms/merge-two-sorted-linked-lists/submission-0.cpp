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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode *root = nullptr;
        //first step make that root not null
        if (list1 && list2) {
            if (list2->val < list1->val) {
                root = list2;
                list2 = list2->next;
            } else {
                root = list1;
                list1 = list1->next;
            }
        } else {
            if (list1) {
                root = list1;
                list1 = list1->next;
            }
            if (list2) {
                root = list2;
                list2 = list2->next;
            }
        }
        if (!root) {
            return nullptr;
        }
        ListNode *curr = root;
        while (list1 && list2) {
            if (list1->val < list2->val) {
                curr->next = list1;
                list1 = list1->next;
            } else {
                curr->next = list2;
                list2 = list2->next;
            }
            curr = curr->next;
        }
        while(list1) {
            curr->next = list1;
            list1 = list1->next;
            curr = curr->next;

        }
        while(list2) {
            curr->next = list2;
            list2 = list2->next;
            curr = curr->next;

        }
        return root;
    }
};
