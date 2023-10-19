from typing import Callable, Any, List


def split_default(text):
    return text.split()


def draw_default(enums):
    pass
    # print(enums)


class Translator():
    name = "default"

    def split_function(self, text):
        return split_default(text)

    def symbols_to_enum(self, symbols):
        return split_default(symbols)

    def draw_function(self, enums):
        return draw_default(enums)

    def process_text(self, text: str):
        split_text = self.split_function(text)
        # print("split text:", split_text)
        enums = self.symbols_to_enum(split_text)
        result = self.draw_function(enums)
        return result




    # split_function: Callable[[str], List[Any]]
    # symbols_to_enum: Callable[[List[Any]], List[Any]]
    # draw_function: Callable[[List[Any]], Any]

    # def init(self, name: str, split_function, symbols_to_enum, draw_function):
    #     self.name = name
    #     if split_function:
    #         self.split_function = split_function
    #     self.symbols_to_enum = symbols_to_enum
    #     self.draw_function = draw_function
