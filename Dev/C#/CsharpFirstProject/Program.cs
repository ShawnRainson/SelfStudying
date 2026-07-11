using System.Collections.Generic;

class Program
{
    static void Main()
    {
        List<string> shoppingList = new List<string>();
        shoppingList.Add("Milk");
        shoppingList.Add("Bread");
        shoppingList.Add("Eggs");

        foreach(string product in shoppingList)
        {
            Console.WriteLine($"Product: {product}");
        }
    }
}