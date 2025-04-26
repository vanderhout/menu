class Menu:
    def __init__(self):
        self.options = {}
        self.last_choice = None

    def add_option(self, key: str, function, context, description: str):
        self.options[key] = {
            "function": function,
            "context": context,
            "description": description
        }

    def run(self, prompt_message: str, invalid_option_message: str):
        for key, option in self.options.items():
            print(f'{key}: {option["description"]}')

        self.last_choice = input(prompt_message).strip()
        if self.last_choice in self.options:
            option = self.options[self.last_choice]
            if option["function"] is not None:
                option["function"](option["context"])
        elif invalid_option_message is not None:
            print(invalid_option_message)

if __name__ == "__main__":
    def set_value(value):
        print(f'Value set to {value}.')

    while True:
        menu = Menu()
        menu.add_option('1', set_value, '1', 'Set the value to 1.')
        menu.add_option('2', set_value, '2', 'Set the value to 2.')
        menu.add_option('3', set_value, '3', 'Set the value to 3.')
        menu.add_option('q', None, None, 'Quit.')

        print('')
        menu.run(
            prompt_message='Select an option: ',
            invalid_option_message='Invalid selection.'
        )
        if menu.last_choice == 'q':
            break