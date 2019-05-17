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

int sum(Node n, int a, int b){
	int s1 = 0;
	int s2 = 0;
	if(n != NULL){
		if(n->x <= b){
			s1 = sum(n->right,a,b);
		}
		if(n->x >= a){
			s2 = sum(n->left,a,b);
		}
		if(n->x >= a && n->x <= b){
			return n->x + s1 + s2;
		}else{
			return s1 + s2;
		}
	}
}

int main(){
	Node n = NULL;
	int tab[] = {5,8,3,2,4,6,10};
	int a = 4;
	int b = 9;
	for(int i = 0;i < 7;i++){
		add_node_void(&n,tab[i]);
	}
	printInOrder(n);
	printf("%d\n",sum(n,a,b));
	freeNode(n);
	return 0;
}