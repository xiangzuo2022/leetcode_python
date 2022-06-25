Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.

In one step, you can delete exactly one character in either string.

 

Example 1:
Input: word1 = "sea", word2 = "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".

Example 2:
Input: word1 = "leetcode", word2 = "etco"
Output: 4

Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.

In one step, you can delete exactly one character in either string.

 

Example 1:
Input: word1 = "sea", word2 = "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".

Example 2:
Input: word1 = "leetcode", word2 = "etco"
Output: 4

// leetcode   etco 
// 2d matrix 


public int min_steps(String word,String word2){

   int[][] dp = new int[word.length()][word2.length()];
   if(word.length()===0)
        return word2.length();
   if(word2.length()===0)
        return word.length();
   
   if(word.charAt(0)!=word2.charAt(0){
          dp[0][0] = 1;
   }
   for(int i=1;i<word.length;i++){
      if(word.charAt(i)!=word2.charAt(0)){
           dp[i][0] = dp[i-1][0]+1;
      } else{
           dp[i][0] = dp[i-1][0];
      }
   }
   
   for(int i=1;i<word2.length;i++){
      if(word.charAt(0)!=word2.charAt(i)){
           dp[0][i] = dp[0][i-1]+1;
      } else{
          dp[0][i] = dp[0][i-1]; 
      }
      
   }
   
   for(int i=1;i<word.length();i++)
      for(int j=1;j<word2.length();j++){
      
           if(word.charAt(i)!=word2.charAt(j)){
              dp[i][j] = dp[i-1][j-1] +1;
           } else{
           
               dp[i][j] = dp[i-1][j-1];
           }
           
        
      }
   
   
   
   return dp[word.length()-1][word2.length()-1];
   

}




You are given an array of binary strings strs and two integers m and n.

Return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.

A set x is a subset of a set y if all elements of x are also elements of y.

 

Example 1:
Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
Output: 4
Explanation: The largest subset with at most 5 0's and 3 1's is {"10", "0001", "1", "0"}, so the answer is 4.
Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
{"111001"} is an invalid subset because it contains 4 1's, greater than the maximum of 3.

Example 2:
Input: strs = ["10","0","1"], m = 1, n = 1
Output: 2
Explanation: The largest subset is {"0", "1"}, so the answer is 2.