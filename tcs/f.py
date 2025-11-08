import sys

BIT_MASK = 0xFFFFFFFF

def pattern_to_binary(p1, p2, p3):
    full_pattern = p1 + p2 + p3
    return full_pattern.replace('*', '1').replace('.', '0').replace(' ', '0')

def get_precedence(op):
    if op == 'NOT':
        return 3
    elif op == 'OR':
        return 2
    elif op == 'AND':
        return 1
    return 0

def apply_op(op, b, a):
    if op == 'OR':
        return a | b
    elif op == 'AND':
        return a & b
    else:
        raise ValueError(f"Unknown binary operator: {op}")

def apply_unary_op(op, a):
    if op == 'NOT':
        return (~a) & BIT_MASK
    else:
        raise ValueError(f"Unknown unary operator: {op}")

def evaluate_expression(tokens):
    values = []
    ops = []

    def process_op():
        if not ops:
            return
            
        op = ops.pop()
        
        if op == 'NOT':
            if not values: raise IndexError("Missing operand for NOT")
            val = values.pop()
            values.append(apply_unary_op(op, val))
        else:
            if len(values) < 2: raise IndexError(f"Missing operand(s) for {op}")
            b = values.pop()
            a = values.pop()
            values.append(apply_op(op, b, a))

    i = 0
    
    while i < len(tokens):
        token = tokens[i]

        if isinstance(token, int):
            values.append(token)
        elif token == '(':
            ops.append(token)
        elif token == ')':
            while ops and ops[-1] != '(':
                process_op()
            if not ops or ops[-1] != '(':
                raise ValueError("Mismatched parentheses")
            ops.pop()
        elif token in ('AND', 'OR', 'NOT'):
            precedence = get_precedence(token)
            
            if token == 'NOT' and (i == 0 or tokens[i-1] == '(' or tokens[i-1] in ('AND', 'OR', 'NOT')):
                pass
            else:
                while (ops and ops[-1] != '(' and 
                       get_precedence(ops[-1]) >= precedence):
                    process_op()
            
            ops.append(token)
        else:
            raise ValueError(f"Unknown token: {token}")
        
        i += 1

    while ops:
        if ops[-1] == '(':
            raise ValueError("Mismatched parentheses at end of expression")
        process_op()

    if values:
        return values[0] & BIT_MASK
    return 0 

def solve_expression():
    try:
        lines = [sys.stdin.readline().strip() for _ in range(9)]
        
        if len(lines) < 9 or not all(line is not None for line in lines):
            return

        digit_lines = lines[0:3]
        op_bracket_lines = lines[3:6]
        expression_lines = lines[6:9]

    except Exception as e:
        print(f"Error reading input: {e}", file=sys.stderr)
        return

    symbol_map = {}
    
    input_symbols_order = [str(i) for i in range(10)] + ['OR', 'AND', 'NOT', '(', ')']

    def extract_and_map(lines, symbols_list):
        line_segments = [line.split(' ') for line in lines]
        
        num_patterns = len(line_segments[0])
        
        for i in range(min(num_patterns, len(symbols_list))):
            symbol = symbols_list[i]
            
            p1 = line_segments[0][i]
            p2 = line_segments[1][i]
            p3 = line_segments[2][i]
            
            if len(p1) == 3 and len(p2) == 3 and len(p3) == 3:
                 binary_string = pattern_to_binary(p1, p2, p3)
                 symbol_map[binary_string] = symbol

    extract_and_map(digit_lines, input_symbols_order[0:10])

    extract_and_map(op_bracket_lines, input_symbols_order[10:])

    expression_tokens = []
    
    exp_segments_top = expression_lines[0].split(' ')
    exp_segments_mid = expression_lines[1].split(' ')
    exp_segments_bot = expression_lines[2].split(' ')
    
    num_exp_tokens = len(exp_segments_top)
    if not (len(exp_segments_mid) == num_exp_tokens and len(exp_segments_bot) == num_exp_tokens):
        print("ERROR: Expression lines have mismatched number of segments.", file=sys.stderr)
        return

    i = 0
    while i < num_exp_tokens:
        p1 = exp_segments_top[i]
        p2 = exp_segments_mid[i]
        p3 = exp_segments_bot[i]
        
        if len(p1) != 3 or len(p2) != 3 or len(p3) != 3:
            i += 1
            continue

        binary_string = pattern_to_binary(p1, p2, p3)
        symbol = symbol_map.get(binary_string)
        
        if symbol is None:
            i += 1
            continue

        if symbol.isdigit():
            current_number_str = symbol
            j = i + 1
            while j < num_exp_tokens:
                next_p1 = exp_segments_top[j]
                next_p2 = exp_segments_mid[j]
                next_p3 = exp_segments_bot[j]
                
                if len(next_p1) != 3 or len(next_p2) != 3 or len(next_p3) != 3:
                    break
                    
                next_binary_string = pattern_to_binary(next_p1, next_p2, next_p3)
                next_symbol = symbol_map.get(next_binary_string)
                
                if next_symbol and next_symbol.isdigit():
                    current_number_str += next_symbol
                    j += 1
                else:
                    break
            
            expression_tokens.append(int(current_number_str))
            i = j
        else:
            expression_tokens.append(symbol)
            i += 1
            
    try:
        final_result = evaluate_expression(expression_tokens)

        print(str(final_result))
    except Exception as e:
        print(f"ERROR: Evaluation failed: {e}", file=sys.stderr)

if __name__ == "__main__":
    solve_expression()

