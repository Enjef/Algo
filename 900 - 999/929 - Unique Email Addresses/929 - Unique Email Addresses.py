class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:  # 8.89% 86.09%
        unique = set()
        for email in emails:
            local_name, domain_name = email.split('@')
            local_name = local_name.split('+')[0].replace('.', '')
            unique.add('@'.join([local_name, domain_name]))
        return len(unique)

    def numUniqueEmails_short(self, emails: List[str]) -> int:  # 22.70% 62.80%
        return len(
            {'@'.join(
                [email.split('@')[0].split('+')[0].replace('.', ''),
                email.split('@')[1]]) for email in emails}
        )

    def numUniqueEmails_best_speed(self, emails: List[str]) -> int:
        valid_emails = set([])
        for email in emails:
            user_name, domain = email.split("@")
            if "+" in user_name:
                user_name, _  = user_name.split("+", 1)
            user_name = user_name.replace(".", "")
            final_email = f"{user_name}@{domain}"
            if final_email not in valid_emails:
                valid_emails.add(final_email)
        return len(valid_emails)

    def numUniqueEmails_best_memory(self, emails: List[str]) -> int:
        res = set()
        for email in emails:
            arr = email.split('@')
            local = arr[0].replace('.','').split('+')[0]
            new = local + '@' + arr[1]
            res.add(new)
        return len(res)
