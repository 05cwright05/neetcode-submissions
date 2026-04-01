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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int count = 1;
        int sum = 0;
        cout << "jawn";
        while (l1 != nullptr) {
            sum += count * l1->val;
            count *= 10;
            l1 = l1->next;
        }
        cout << "made it 1 \n";
        count = 1;
        while (l2 != nullptr) {
            sum += count * l2->val;
            count *= 10;
            l2 = l2->next;
        }
        if (sum == 0) {
            return new ListNode(0, nullptr);
        }
        cout << "made it 2 \n";
        int place = 10;

        ListNode *head = nullptr;
        ListNode *curr = head;
        while (sum > 0) {
            int value = sum % place;
            sum -= value;
            value = value / (place/10);
            place *= 10;
            ListNode *new_node = new ListNode(value, nullptr);
            if (!head) {
                head = new_node;
                curr = head;
            } else {
                curr->next = new_node;
                curr = curr->next;
            }
        }
        return head;


    }
};
