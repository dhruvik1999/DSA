#include<bits/stdc++.h>

using namespace std;




struct cmp{
	bool operator()(pair<int,int> i , pair<int,int> j){
		return i.first > j.first;
	}
};


int main(){
	
	int aa[100][100];

	int n,e;
	cin >> n >> e;

	
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			aa[i][j] = 0;
		}
	}

	int p,q,w;

	for(int i=0;i<e;i++){
		cin >> p >> q >> w;
		aa[p][q]=w;
		aa[q][p]=w;
	}

	

	priority_queue < pair<int,int> , vector< pair<int,int> > , cmp > pq;


	pq.push(make_pair(0,0));
	//cout << pq.top().first << " " << pq.top().second;

	int parent[n];
	int inmst[n];
	int val[n];

	for(int i=0;i<n;i++){
		inmst[i]=-1;
		val[i]=100000;
		parent[i]=-1;
	}

	parent[0]=-1;
	inmst[0]=1;
	val[0]=0;


	while(pq.size() !=0){
		pair<int,int> t = pq.top();
		pq.pop();

		int u = t.second;
		inmst[u]=1;
		for(int i=0;i<n;i++){
			//cout << i << " " << aa[u][i] << " " << inmst[i] << " " << aa[u][i] << " " <<  val[i] << "\n";
			if(aa[u][i] && inmst[i]!=1 && aa[u][i] < val[i] ){
				val[i] = aa[u][i];
				t.first = aa[u][i];
				t.second = i;
				parent[i]=u;
				pq.push(t);
			}
		}
	}

	for(int i=0;i<n;i++){
		cout << i << " " << parent[i] << "\n";
	}

	return 0;
}