def _default_print_option_function(key, description):
    print(f"{key}: {description}")

def _default_invalid_selection_function():
    print(f"Invalid selection.")
    return True

class Menu:
    def __init__(self):
        self.options = {}
        self.print_option_function = _default_print_option_function
        self.invalid_selection_function = _default_invalid_selection_function

    def add_option(self, key: str, context, description: str):
        self.options[key] = {
            "context": context,
            "description": description
        }

    def add_function_option(self, key: str, function, context, description: str):
        self.options[key] = {
            "function": function,
            "context": context,
            "description": description
        }

    def run(self, prompt_message: str = None):
        '''
        Display all the menu choices, accept an input from the user, and return either a value based on the function
        tied to the option, a value based on the function tied to an invalid option, or None.
        '''
        for key, option in self.options.items():
            self.print_option_function(key, option["description"])

        if prompt_message is not None:
            key_choice = input(prompt_message)
        else:
            key_choice = input()
        if key_choice in self.options:
            option = self.options[key_choice]
            if "function" in option:
                return option["function"](option["context"])
            else:
                return option["context"]
        elif self.invalid_selection_function is not None:
            return self.invalid_selection_function()

        return None

if __name__ == "__main__":
    def set_value(value):
        print(f'Value set to {value}.')
        return True

    menu = Menu()

    menu.add_option('0', '0', 'Non-function option.')
    menu.add_function_option('1', set_value, '1', 'Set the value to 1.')
    menu.add_function_option('2', set_value, '2', 'Set the value to 2.')
    menu.add_function_option('3', set_value, '3', 'Set the value to 3.')
    menu.add_option('q', None, 'Quit to next section.')

    while True:
        print('')
        result = menu.run()
        print('Result: ', result)
        if result is None:
            break

    while True:
        print('')
        result = menu.run(
            prompt_message='Prompt message added.'
        )
        print('Result: ', result)
        if result is None:
            break

    def new_print_function(key, description):
        print(f"{key.upper()}: {description.upper()}")
    menu.print_option_function = new_print_function
    while True:
        print('')
        result = menu.run(
            prompt_message='New print function.'
        )
        print('Result: ', result)
        if result is None:
            break

    def new_invalid_selection_function():
        for i in range(3):
            print('INVALID SELECTION!')
        return True

    menu.invalid_selection_function = new_invalid_selection_function
    while True:
        print('')
        result = menu.run(
            prompt_message='New invalid selection function.'
        )
        print('Result: ', result)
        if result is None:
            break
