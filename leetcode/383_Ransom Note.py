# The code iterates through each character in the ransomNote. 
# For each character, it checks if it is present in the magazine. 
# If the character is not found in the magazine, the function immediately returns False, indicating that the ransom note cannot be constructed. 
# If the character is found, it removes the first occurrence of that character from the magazine using the replace method.
# If the loop completes without encountering any issues, it means that each character in the ransomNote has been found in the magazine, and the function returns True, indicating that the ransom note can be constructed.

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for character in ransomNote: 
            if character not in magazine: 
                return False
            magazine = magazine.replace(character,'', 1)
        return True