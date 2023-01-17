
#Function to check if a string is a palindrome
def isPalindrome(string): 
  
    # Run loop from 0 to len/2 
    for i in range(0, int(len(string)/2)): 
        if string[i] != string[len(string)-i-1]: 
            return False
    return True
  
# Driver code 
string = "malayalam"
ans = isPalindrome(string) 
  
if (ans): 
    print("Yes") 
else: 
    print("No")