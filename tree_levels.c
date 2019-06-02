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
#include <stdlib.h>
#include <stdio.h>

struct node{
	int x;
	struct node* right;
	struct node* left;
};

typedef struct node* Node;

Node create_node(int value){
	Node n = NULL;
	n = malloc(sizeof(struct node));
	if(n == NULL){
		printf("Ereur allocation dynamique\n");
		exit(1);
	}

	n->x = value;
	n->left = NULL;
	n->right = NULL;

	return n;
}

Node add_node(Node n, int value){
	if(n != NULL){
		if(value > n->x){
			n->right = add_node(n->right,value);
		}else{
			n->left = add_node(n->left,value);
		}
	}else{
		return create_node(value);
	}
}

void add_node_void(Node* n, int value){
	if(*n != NULL){
		if(value > (*n)->x){
			add_node_void(&(*n)->right,value);
		}else{
			add_node_void(&(*n)->left,value);
		}
	}else{
		*n = create_node(value);
	}
}

void printInOrder(Node n){
	if(n != NULL){
		printInOrder(n->left);
		printf(":%d\n", n->x);
		printInOrder(n->right);
	}
}

void freeNode(Node n){
	if(n != NULL){
		freeNode(n->right);
		freeNode(n->left);
		free(n);
	}
}

float levels(Node n, float level){
	if(n != NULL){
		if(n->left != NULL && n->right != NULL){
			printf("code : 1\n");
			return level + levels(n->left,level/2) + levels(n->right, level/2);
		}else if(n->left == NULL && n->right == NULL){
			printf("code : 2\n");
			return level;
		}else if(n->left == NULL && n->right != NULL){
			printf("code : 3\n");
			return level + levels(n->right, level);
		}
		else if(n->left != NULL && n->right == NULL){
			printf("code : 4\n");
			return level + levels(n->left, level);
		}
	}
}

int main(){
	Node n = NULL;
	int tab[] = {5,8,2,4,6,10};
	int a = 4;
	int b = 9;
	for(int i = 0;i < 7;i++){
		add_node_void(&n,tab[i]);
	}
	printf("%d\n",(int) levels(n,1));
	freeNode(n);
	return 0;
}
