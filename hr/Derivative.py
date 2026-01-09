if __name__ == '__main__':
    
    s = input().split()
    result = []
    
    for i in range(len(s)):
        if 'x' in s[i]:
            if '^' in s[i]:
                
                coeff_str, pwr_str = s[i].split('x^')
                num = int(coeff_str) if coeff_str else 1
                pwr = int(pwr_str)
                
                new_coeff = num * pwr
                new_pwr = pwr - 1
                
                if new_pwr > 1:
                    result.append(f"{new_coeff}x^{new_pwr}")
                elif new_pwr == 1:
                    result.append(f"{new_coeff}x")
                else: # power is 0
                    result.append(f"{new_coeff}")
            else:
                
                coeff = s[i].replace('x', '')
                if coeff == '': coeff = '1' # handle just 'x'
                result.append(coeff)
        elif (s[i] == '+') and ('x' in s[i+1]):
            result.append('+')
        
            
    
    if result and result[-1] == '+':
        result.pop()
        
    print(" ".join(result))
