'''
Lets consider digits = "253"
We would form the combinations one-by-one as follows -

1.                                                                                   [""]
                             ___________________________________________________________________________________________________________________
                            /     								        		      |    								        		        \
2.[                        "a"                                                       "b"                                                         "c"  ]
            __________________________________                       ___________________________________                        ____________________________________
	       /      	        |                 \                     /     	          |                 \                      /     	          |                 \
3.[     "aj"               "ak"               "al"                "bj"               "bk"               "bl"                "cj"                "ck"                "cl"  ]
     ___________        ___________        ___________         __________         __________          __________          __________          __________          __________
    /     |     \      /     |     \      /     |     \       /    |     \       /    |     \        /    |     \        /    |     \        /    |     \        /    |     \
4["ajd"  "aje"  "ajf" "akd" "ake" "akf" "ald"  "ale" "alf"  "bjd"  "bje"  "bjf" "bjd"  "bje"  "bjf" "bjd" "bje" "bjf"  "cjd"  "cje"  "cjf" "cjd"  "cje"  "cjf" "cjd" "cje" "cjf"  ]

1. We are starting with empty array.
2. We take the first digit from 'digits' and form all the possible combinations with it. 
3. Now, the main thing you must notice is that, we are just extending the previous combination. We are taking  "a" from the previous combination and combining it with each letter mapped with digit 5, 
   then we take "b" from previous combination and again combine it with each letter mapped with digit 5 and repeat the same process for "c".
4. Again, extend previous combination by taking from each previously formed combination and combining it with all the letters mapped with the digit under current iteration (3).
In this way, we are able to build all the combinations by simply -
  ✦ Taking previous combinations
  ✦ Extend the combination by appending it with all letters corresponding to current digit
  ✦ Repeat for all digits
'''
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        LetterMap = {
            '1':"",    '2':"abc", '3':"def",
            '4':"ghi", '5':"jkl", '6':"mno",
            '7':"pqrs", '8':"tuv", '9':"wxyz"
        }
        deque = [""]
        for i in digits:
            CorrespondingLetter = LetterMap[i]
            for j in range (len(deque)):
                FirstElement=deque[0]
                del deque[0]
                for k in range (len(CorrespondingLetter)):
                    CombinedString = FirstElement + CorrespondingLetter[k]
                    deque.append(CombinedString)
        if (deque==[""]):
            deque=[]
        return (deque)
      
      
      '''
      Time Complexity: O(K^n) ; n=Length Of String & K= Character Provided on a numpad digit.
      Space Complexity:O(K^n) ; n=Length Of String & K= Character Provided on a numpad digit.
      '''
