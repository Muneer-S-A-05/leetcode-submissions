/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode *sum = (struct ListNode *)malloc(sizeof(struct ListNode));
    sum->next=NULL;
    int r=0;
    sum->val = l1->val+l2->val;
    if (sum->val>9)
        r=1,sum->val%=10;
    struct ListNode *temp= (struct ListNode *)malloc(sizeof(struct ListNode));
    temp=sum;
    while (l1->next!=NULL && l2->next!=NULL){
        struct ListNode *p=(struct ListNode *)malloc(sizeof(struct ListNode));
        l1=l1->next,l2=l2->next;
        temp->next=p;
        temp=p;
        p->next=NULL;
        temp->val = l1->val+l2->val+r;
        if (temp->val>9)
            r=1,temp->val%=10;
        else
            r=0;
    }
    while (l1->next!=NULL){
        struct ListNode *p=(struct ListNode *)malloc(sizeof(struct ListNode));
        l1=l1->next;
        temp->next=p;
        temp=p;
        p->next=NULL;
        temp->val = l1->val+r;
        if (temp->val>9)
            r=1,temp->val%=10;
        else
            r=0;
    }
    while (l2->next!=NULL){
        struct ListNode *p=(struct ListNode *)malloc(sizeof(struct ListNode));
        l2=l2->next;
        temp->next=p;
        temp=p;
        p->next=NULL;
        temp->val = l2->val+r;
        if (temp->val>9)
            r=1,temp->val%=10;
        else
            r=0;
    }
    if (r==1){
        struct ListNode *p=(struct ListNode *)malloc(sizeof(struct ListNode));
        p->next=NULL;
        p->val=1;
        temp->next=p;
    }
    return sum;
}
