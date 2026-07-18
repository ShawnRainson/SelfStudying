using System;

List<string> books = new() {"Harry Potter", "1984", "The Hobbit"};

static void ShowBooks(List<string> books)
{
    foreach(string book in books)
    {
        Console.WriteLine($"Book: {book}");
    };
};

static void AddBook(List<string> books)
{
    Console.Write("Enter book title: ");
    string newBook = Console.ReadLine();
    books.Add(newBook);
    foreach(string book in books)
    {
        Console.WriteLine($"Book: {book}");
    };
};

static void FindBook(List<string> books)
{
    Console.Write("Enter book title: ");
    string bookTitle = Console.ReadLine();
    bookTitle = bookTitle.ToLower();
    foreach(string book in books)
    {
        if (book.ToLower() == bookTitle)
        {
            Console.WriteLine($"Book: {book}");
        };
    };
};

static void RemoveBook(List<string> books)
{
    Console.Write("Enter book for remove: ");
    string bookTitle = Console.ReadLine();
    bookTitle = bookTitle.ToLower();
    foreach(string book in books)
    {
        if (book.ToLower() == bookTitle)
        {
            books.Remove(book);
            Console.WriteLine($"Book {book} was removed!");
        };
    };
};



ShowBooks(books);
FindBook(books);
AddBook(books);
ShowBooks(books);
RemoveBook(books);
ShowBooks(books);
