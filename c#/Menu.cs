using System;
using System.Collections.Generic;

public class MenuOption
{
    public Func<object, bool>? Action { get; set; }
    public object? Context { get; set; }
    public string Description { get; set; }

    public MenuOption(Func<object, bool>? action, object? context, string description)
    {
        Action = action;
        Context = context;
        Description = description;
    }
}

public class Menu
{
    private Dictionary<string, MenuOption> _options = new();
    public Action<string, string> PrintOptionFunction { get; set; }
    public Func<bool>? InvalidSelectionFunction { get; set; }

    public Menu()
    {
        PrintOptionFunction = DefaultPrintOptionFunction;
        InvalidSelectionFunction = DefaultInvalidSelectionFunction;
    }

    public void AddOption(string key, Func<object, bool>? function, object? context, string description)
    {
        _options[key] = new MenuOption(function, context, description);
    }

    public object? Run(string? promptMessage = null)
    {
        foreach (var kvp in _options)
        {
            PrintOptionFunction(kvp.Key, kvp.Value.Description);
        }

        Console.Write(promptMessage ?? "> ");
        string? keyChoice = Console.ReadLine();

        if (keyChoice != null && _options.ContainsKey(keyChoice))
        {
            var option = _options[keyChoice];
            if (option.Action != null)
            {
                return option.Action(option.Context);
            }
        }
        else if (InvalidSelectionFunction != null)
        {
            return InvalidSelectionFunction();
        }

        return null;
    }

    private static void DefaultPrintOptionFunction(string key, string description)
    {
        Console.WriteLine($"{key}: {description}");
    }

    private static bool DefaultInvalidSelectionFunction()
    {
        Console.WriteLine("Invalid selection.");
        return true;
    }
}
