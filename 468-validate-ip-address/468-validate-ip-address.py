class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        
        def check_ipv4(ip):
            ip_arr = ip.split('.')
            if len(ip_arr) != 4:
                return "Neither"
            for i in range(0, len(ip_arr)):
                x = ip_arr[i]
                if not x.isnumeric():
                    return "Neither"
                if int(x) > 255 or int(x) < 0:
                    return "Neither"
                elif x[0] == '0' and x != '0':
                    return "Neither"
            return "IPv4"
                
        def check_ipv6(ip):
            letters = ['a', 'b', 'c', 'd', 'e', 'f']
            for char in ip:
                if char != ':' and not char.isnumeric():
                    if char.lower() not in letters:
                        return "Neither"
            ip_arr = ip.split(':')
            if len(ip_arr) != 8:
                return "Neither"
            for i in range(0, len(ip_arr)):
                chunk = ip_arr[i]
                if len(chunk) > 4 or len(chunk) <= 0:
                    return "Neither"
            return "IPv6"
            
        output = ''
        
        if '.' in queryIP:
            output = check_ipv4(queryIP)
        else:
            output = check_ipv6(queryIP)
        return output