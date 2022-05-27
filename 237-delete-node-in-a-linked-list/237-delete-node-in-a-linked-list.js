/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} node
 * @return {void} Do not return anything, modify node in-place instead.
 */
var deleteNode = function(node) {
  if (node.next) {
	prev = node;
	node.val = node.next.val;
	deleteNode(node.next, prev);
} else {
	prev.next = null;
}
};