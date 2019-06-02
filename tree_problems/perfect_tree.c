/*
This problem was asked by me.

Given a binary search tree, return True if the tree is perfect otherwise False.

For example, given the following tree:

    5
   / \
  3   8
 / \ / \
2  4 6  10

return True.
*/
#include "tree_lib.h"

int pw(int p, int power){
	int s = 1;
	for(int i = 0;i < power;i++){
		s *= p;
	}
	return s;
}

int number_of_nodes_if_perfect(int l){
	int s = 0;
	for(int i = 0;i < l;i++){
		s += pw(2,i);
	}
	return s;
}

int number_of_nodes(Node n){
	if(n)
		return 1 + number_of_nodes(n->left) + number_of_nodes(n->right);
	else
		return 0;
}

int is_perfect(Node n){
	float f_level = levels(n, 1);
	int level = (int) f_level;
	if(level < f_level)
		level += 1;
	printf("level %d\n",level);
	int nodes = number_of_nodes(n);
	printf("nodes %d\n",nodes);
	int perfect_nodes = number_of_nodes_if_perfect(level);
	printf("perfect nodes %d\n", perfect_nodes);
	return nodes == perfect_nodes;
}

int main(){
        Node n = NULL;
        int tab[] = {5,8,2,4,6,3,10};
        for(int i = 0;i < 7;i++){
                add_node_void(&n,tab[i]);
        }
        printf("%d\n",is_perfect(n));
        freeNode(n);
        return 0;
}
