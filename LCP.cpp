  #include<bits/stdc++.h>
    using namespace std; 

    #define loop(i,a,b) for(int i=a; i<b; i++)
    #define in1(a) cin >> a ;
    #define in2(a, b) cin >> a >> b; 
    #define out1(a) cout << a << "\n" ; 
    #define out2(a,b) cout << a << " "<< b << "\n" ; 

    int N, a, b, M ; 
    vector<int> board[50005]; // board[node] = {child1, child2, ...}
    int depth[50005]; // depth[node] = distance from root
    int parents[50005]; // parents[node] = parent

    void dfs(int root){
        vector <int> st;  // <-- vec same func as stack [more usable]
        st.push_back(root); // we know the roof of tree = 1 
        while(!st.empty()){// DFS
            int cur = st.back(); st.pop_back(); 
            loop(i,0,board[cur].size()){ // search every next node that edged to current
                int nxt = board[cur][i]; // since its tree!!(Acyclic undirected)
                if(nxt == parents[cur]) continue; // you can check its Parent as vis array 
                st.push_back(nxt); // if its not his parent, stack push nxt node
                parents[nxt] = cur; // Memo its parent 
                depth[nxt] = depth[cur]+1; // Memo its depth by adding 1 from his parent
            }
        }// done to save parents and depth of every node  
        st.clear(); // <--ISSUE, without this, you get Runtime Error(double free) 
    }
    int main(void){
        ios::sync_with_stdio(0); cin.tie(0);
        in1(N); // num of node
        loop(i,0,N-1){ // problem says N-1 edge info btw two (Be careful!!) 
            in2(a,b); // edge goes to both direction since its Tree 
            board[a].push_back(b);
            board[b].push_back(a);
        }
        in1(M); // number of pairs to find out LCA  
        dfs(1); // First we need to find out depth and parents of every node by DFS

        loop(i,0,M){ // Now that you got Tree's parents & depth of every node
            in2(a,b); // Find out Lowest Common Ancestor
            if(depth[a] > depth[b]) swap(a,b); // Set the deeper one first
            while(depth[a] != depth[b]) b = parents[b]; // Make that to same depth(position)
            while(a != b){ // Go now to check the same parents
                a = parents[a]; // Break soon after a=b (smae parents)
                b = parents[b];
            } // ,than any of them = LCA
            out1(a);
        }
    }
}