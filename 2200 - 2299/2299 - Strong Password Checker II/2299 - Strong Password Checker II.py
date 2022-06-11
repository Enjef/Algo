class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False
        one_lowercase = False
        one_uppercase = False
        one_digit = False
        one_special = False
        for i, char in enumerate(password[:-1]):
            if char == password[i+1]:
                return False
            if char.islower():
                one_lowercase = True
            if char.isupper():
                one_uppercase = True
            if char.isdigit():
                one_digit = True
            if char in "!@#$%^&*()-+":
                one_special = True
        if password[-1].islower():
            one_lowercase = True
        if password[-1].isupper():
            one_uppercase = True
        if password[-1].isdigit():
            one_digit = True
        if password[-1] in "!@#$%^&*()-+":
            one_special = True
        return one_lowercase and one_uppercase and one_digit and one_special

    def strongPasswordCheckerII_v2(self, password: str) -> bool:  # 20% 100% (fresh problem)
        return len(password) > 7 and len(set(['lower' if char.islower() else 'upper' if char.isupper() else 'digit' if char.isdigit() else 'special' if char in "!@#$%^&*()-+" else  '' for char in password])) == 4 and not any(1 for a, b in pairwise(password) if a == b)

    def strongPasswordCheckerII_v3(self, password: str) -> bool:  # 80.00% 100.00%
        return len(password) > 7 and len(set(['lower' if char.islower() else 'upper' if char.isupper() else 'digit' if char.isdigit() else 'special' if char in "!@#$%^&*()-+" else  '' for char in password])) == 4 and not any(1 for a, b in zip(password, password[1:]) if a == b)

    def strongPasswordCheckerII_v4(self, password: str) -> bool:  # 80.00% 100.00%
        return len(password) > 7 and len(set(['lower' if char.islower() else 'upper' if char.isupper() else 'digit' if char.isdigit() else 'special' if char in "!@#$%^&*()-+" else  '' for char in password])) == 4 and not any(1 for i in range(len(password)-1) if password[i] == password[i+1])
