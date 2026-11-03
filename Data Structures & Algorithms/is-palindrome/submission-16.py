class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = "".join([char.lower() for char in s if char.isalnum()])
        left, right = 0, len(s) - 1

        if (len(s) == 0):
            return True

 

        print(f"This is len s {len(s)}")

        while(left < right):
            print(f"{s[left]}, {s[right]}")
            if (s[left] != s[right]):
                
                print(f"{s[left]} != {s[right]}")
                return False
            else:
                left += 1
                right -= 1
        return True