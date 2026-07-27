class Solution {
public:
    int lengthOfLongestSubstring(string s) {

        int left= 0;
        int right= 0;
        int maxlen=0;

        unordered_set <char> chars;
        while(right<s.size()){
            if (chars.count(s[right])==0){
                chars.insert(s[right]);

                maxlen= max(maxlen, right-left+1);
                right++;

            }
            else{
                chars.erase(s[left]);
                left++;
            }
        }
        
        return maxlen;
        
    }
};