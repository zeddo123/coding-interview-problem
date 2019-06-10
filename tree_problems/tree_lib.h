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

