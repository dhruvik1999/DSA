#include<bits/stdc++.h>

using namespace std;

struct Node{
	char data;
	int frq;

	Node *left, *right;

	Node(char data,char frq){
		this->left=NULL;
		this->right=NULL;
		this->data=data;
		this->frq=frq;
	} 
};

struct cmp{
	bool operator()(Node* l,Node* r){
		return l->frq > r->frq;
	}
};

void printc(Node* top,string ans){

	if(!top)
		return;
	
	if(top->data != '$'){
		cout << top->data << " : " << ans  << "\n";
	}

	printc(top->left,ans+"0");
	printc(top->right,ans+"1");
}


void hof(char a[],int f[],int n){
	priority_queue < Node* , vector<Node*> , cmp > pq; 
	for(int i=0;i<n;i++){
		pq.push(new Node(a[i],f[i]));
	}

	Node *left,*right,*top;

	while(pq.size() != 1){
		right = pq.top();
		pq.pop();
		left = pq.top();
		pq.pop();

		top = new Node('$',right->frq + left->frq);
		top->left = left;
		top->right = right;

		pq.push(top);
	}

	printc(pq.top() , "");
}

int main(){

	int n;
	cin >> n;

	char a[n];
	int f[n];

	for(int i=0;i<n;i++){
		cin >> a[i] >> f[i];
	}


	hof(a,f,n);

	return 0;
}