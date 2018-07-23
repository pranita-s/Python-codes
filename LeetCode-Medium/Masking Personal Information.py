# TIME - O(1)
# SPACE  - O(1)

def mask(S):
  if '@' in S:
            first, after = S.split('@')
            t = "%s*****%s@%s"%(first[0],first[-1],after)
            return t.lower()
        
        digits = filter(lambda x:x.isdigit(),S)
        local  = "***-***-%s"%(digits[-4:])
        if len(digits)==10:
            return local
        
        return "+%s-%s"%('*'*(len(digits)-10),local)
