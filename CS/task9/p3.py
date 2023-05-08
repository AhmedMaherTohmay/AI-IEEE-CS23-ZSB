class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:

        res = set()
        for email in emails:
            local, domain = email.split('@')
            tmp = ""
            for i in local:
                if i == ".":
                    continue
                elif i == "+":
                    break
                else:
                    tmp += i
            res.add(tmp+"@"+domain)

        return len(res)
