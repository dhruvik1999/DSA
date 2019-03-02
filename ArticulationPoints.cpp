#include <iostream>
#include <bits/stdc++.h>

using namespace std;

vector<int> ans(100,0);
int timee = 0;
void DFS(vector< vector<int> > &graph,vector<int> &low,vector<int> &parent,vector<int> &disc,vector<bool> &visited,int vertex,int n){
    disc[vertex] = timee;
    timee++;
    low[vertex]=timee;
    visited[vertex]=true;
    int child = 0;

    for(int i=0;i<n;i++){
        if(graph[vertex][i]==1){
            if(visited[i]==false){
                parent[i]=vertex;
                child++;
                DFS(graph,low,parent,disc,visited,i,n);
                low[vertex] = min(low[vertex],low[i]);

                if(parent[vertex]==-1 && child>1){
                    ans[vertex]=1;
                }
                if(parent[vertex] != -1 && low[i] >= disc[vertex]){
                    ans[vertex]=1;
                }
            }else if(parent[vertex] != i){
                low[vertex] = min(low[vertex],disc[i]);
            }
        }
    }

}

int main(){
    int n,e;
    cin >> n >> e;

    vector< vector<int> > graph(n,vector<int>(n));

    int p,q;

    for(int i=0;i<e;i++){
        cin >> p >> q;
        graph[p][q]=1;
        graph[q][p]=1;
    }


    vector<int> low(n,INT_MAX),parent(n,-1),disc(n,INT_MAX);
    vector<bool> visited(n,false);

    DFS(graph,low,parent,disc,visited,0,n);

    for(int i=0;i<n;i++){
        if(ans[i]==1){
            cout << i << "\n";
        }
    }



    return 0;
}
