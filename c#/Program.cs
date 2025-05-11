class Program
{
    static void Main()
    {
        bool SetValue(object value)
        {
            Console.WriteLine($"Value set to {value}.");
            return true;
        }

        Menu menu = new();

        menu.AddOption("1", SetValue, "1", "Set the value to 1.");
        menu.AddOption("2", SetValue, "2", "Set the value to 2.");
        menu.AddOption("3", SetValue, "3", "Set the value to 3.");
        menu.AddOption("q", null, null, "Quit to next section.");

        while (true)
        {
            Console.WriteLine();
            var result = menu.Run();
            if (result == null) break;
        }

        while (true)
        {
            Console.WriteLine();
            var result = menu.Run("Prompt message added: ");
            if (result == null) break;
        }

        menu.PrintOptionFunction = (key, description) =>
        {
            Console.WriteLine($"{key.ToUpper()}: {description.ToUpper()}");
        };

        while (true)
        {
            Console.WriteLine();
            var result = menu.Run("New print function: ");
            if (result == null) break;
        }

        menu.InvalidSelectionFunction = () =>
        {
            for (int i = 0; i < 3; i++)
            {
                Console.WriteLine("INVALID SELECTION!");
            }
            return true;
        };

        while (true)
        {
            Console.WriteLine();
            var result = menu.Run("New invalid selection function: ");
            if (result == null) break;
        }
    }
}
