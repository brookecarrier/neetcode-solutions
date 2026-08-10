class Solution {
public:
    vector<int> countBits(int n) {

        vector<int> output;
        
        for (int i = 0; i < n+1; i++) {
            int count = 0;
            int num = i;
            while (num) {
                if (num & 1) count++;
                num = num >> 1;
            }
            output.push_back(count);
        }
     
        return output;
    }

};
