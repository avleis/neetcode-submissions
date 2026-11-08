class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        hash_email = {}
        clear_email = list[str]
        counter = 0

        for index, email in enumerate(emails):
            local_name, domain = email.split('@')
            local_name = local_name.split('+')[0]
            local_name = local_name.replace('.', '')

            emails[index] = local_name + '@' + domain

        for email in emails:
            if email not in hash_email:
                counter += 1
                hash_email[email] = emails

        return counter