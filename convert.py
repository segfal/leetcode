


x = -1234; y = -4321;


def intostring(x : int) -> str: ## TODO:
    
    table = {## reverse table
        0: '0',
        1: '1',
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6',
        7: '7',
        8: '8',
        9: '9',
    } 
    result = ''## empty string
    while x > 0:## while x is not 0
        result = table[x % 10] + result; ## add the last digit to the result
        x //= 10; ## remove the last digit
    return result ## return the result




def stringtoint(x : str) -> int: ## TODO:
    table = { ## reverse table
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
    }
    result = 0 ## empty string
    for i in range(len(x)): ## for each digit in the string
        result += table[x[i]] * 10 ** (len(x) - i - 1);## add the digit to the result
    return result ## return the result


print(type(x), type(y));
print(type(intostring(x)),type(intostring(y)));
print(type(stringtoint(intostring(x))) , type(stringtoint(intostring(y))));
print(intostring(x), intostring(y));
print(stringtoint(intostring(x)), stringtoint(intostring(y)));
print(intostring(stringtoint(intostring(x))), intostring(stringtoint(intostring(y))));





