/*
This problem was asked by me.

Given a binary search tree, return the number of levels of the binary search tree.

For example, given the following tree:

    5
   / \
  3   8
 / \ / \
2  4 6  10

return 3.
*/
#include "tree_lib.h"
/*
float levels(Node n, float level){
        if(n != NULL){
                if(n->left != NULL && n->right != NULL){
                        return level + levels(n->left,level/2) + levels(n->right, level/2);
                }else if(n->left == NULL && n->right == NULL){
                        return level;
                }else if(n->left == NULL && n->right != NULL){
                        return level + levels(n->right, level);
                }
                else if(n->left != NULL && n->right == NULL){
                        return level + levels(n->left, level);
                }
        }
}
*/
int main(){
	Node n = NULL;
	int tab[] = {5,8,2,4,6,3,10};
	for(int i = 0;i < 7;i++){
		add_node_void(&n,tab[i]);
	}

	int level = (int) levels(n,1);
	if (level < levels(n,1))
		level += 1;
	printf("%f %d\n",levels(n,1),level);
	freeNode(n);
	return 0;
}
