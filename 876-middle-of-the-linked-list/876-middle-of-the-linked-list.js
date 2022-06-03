/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var middleNode = function(head) {
    let bam = head;
    let counter = 0;
    while(head) {
          counter++;
        head = head.next;
          }
    counter = Math.floor(counter / 2);
    while (counter) {
        counter--;
        bam = bam.next;
    }
    return bam;
};