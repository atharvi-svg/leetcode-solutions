class Solution {
public:

    int solve(vector<int>& arr, int i, vector<int>& dp) {

        if (i < 0) return 0;
        if (i == 0) return arr[0];

        if (dp[i] != -1)
            return dp[i];

        int pick = arr[i] + solve(arr, i - 2, dp);

        int notPick = solve(arr, i - 1, dp);

        return dp[i] = max(pick, notPick);
    }

    int rob(vector<int>& nums) {

        int n = nums.size();

        vector<int> dp(n, -1);

        return solve(nums, n - 1, dp);
    }
};