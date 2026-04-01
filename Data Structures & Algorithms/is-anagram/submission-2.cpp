class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.length() != t.length()){
            return false;
        };

        unordered_map<char,int> f;
        unordered_map<char,int> g;

        for(char i:s){
            f[i]++;
        }
        for(char i:t){
            g[i]++;
        }
        for(int i=0;i<f.size();i++){
            if(f[i] != g[i])return false;
        }

        return true;
    }
};
