class MyString:
    def __init__(self, value=''):
        self._value = value

    def get_value(self):
        return self._value

    def set_value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")

    value = property(get_value, set_value)

    def is_sentence(self):
        return self._value.endswith('.')

    def is_question(self):
        return self._value.endswith('?')

    def is_exclamation(self):
        return self._value.endswith('!')

    def count_sentences(self):
        sentence_endings = ['.', '?', '!']
        count = 0
        for i in range(len(self._value)):
            if self._value[i] in sentence_endings and (i == len(self._value) - 1 or self._value[i + 1] == ' '):
                count += 1
        return count