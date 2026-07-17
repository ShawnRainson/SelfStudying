using System;

List<string> books = new() {"Harry Potter", "1984", "The Hobbit"};

static void ShowBooks(List<string> newList)
{
    foreach(string book in newList)
    {
        Console.WriteLine($"Book: {book}");
    };
};

static void AddBook(List<string> newList2)
{
    Console.Write("Enter book title: ");
    string newBook = Console.ReadLine();
    newList2.Add(newBook);
    foreach(string book in newList2)
    {
        Console.WriteLine($"Book: {book}");
    };
};

ShowBooks(books);
AddBook(books);
ShowBooks(books);