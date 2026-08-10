
class Solution {
public:

    string encode(vector<string>& strs) {

        string output = "";

        for (const auto& str : strs) {
            string strLength = to_string(str.length());
            output += strLength + '#' + str;
        }

        return output;
     
    }

    vector<string> decode(string s) {
        int currIdx = 0;
        string strLength;
        int intLength;
        string str;
        vector<string> output;

        while (currIdx < s.length()) {
            strLength = "";
            intLength = 0;
            str = "";
            while (s[currIdx] != '#') {
                strLength += s[currIdx];
                currIdx++;
            }
            intLength = stoi(strLength);
            currIdx++;
            str = s.substr(currIdx, intLength);
            output.push_back(str);
            currIdx += intLength;
        }

        return output;

    }
};
