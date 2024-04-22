def find_next_state(pattern, state, letter):
    if state < len(pattern) and letter == pattern[state]:
        return state + 1

    current_pattern = pattern[:state] + letter
    for comparison_length in range(state, 0, -1):
        prefix = current_pattern[:comparison_length]
        suffix = current_pattern[-comparison_length:]
        if prefix == suffix:
            return comparison_length

    return 0


def build_finite_automata(pattern):
    letters_of_pattern = list(set(pattern))
    finite_automata = [[0 for i in letters_of_pattern] for j in range(len(pattern) + 1)]

    for cur_state in range(len(pattern) + 1):
        for cur_letter in range(len(letters_of_pattern)):
            finite_automata[cur_state][cur_letter] = find_next_state(pattern, cur_state, letters_of_pattern[cur_letter])

    return finite_automata


def find_needle(haystack, needle):
    finite_automata = build_finite_automata(needle)
    letters_of_pattern = list(set(needle))

    found_occurrences = []
    state = 0
    for i in range(len(haystack)):
        if haystack[i] in needle:
            state = finite_automata[state][letters_of_pattern.index(haystack[i])]
            if state == len(needle):
                if len(found_occurrences) == 0 or found_occurrences[-1] + len(needle) <= i - len(needle) + 1:
                    found_occurrences.append(i - len(needle) + 1)
        else:
            state = 0

    return found_occurrences
