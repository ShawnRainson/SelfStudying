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
    string bookToRemove = null;
    foreach(string book in books)
    {
        if (book.ToLower() == bookTitle)
        {
            bookToRemove = book;
            break;
        };
    };

    if (bookToRemove != null)
    {
        books.Remove(bookToRemove);
        Console.WriteLine($"Book {bookToRemove} was removed!");
    }else
    {
        Console.WriteLine("Book not found!");
    };
};

static void UpdateBook(List<string> books)
{
    Console.Write("Enter book title: ");
    string bookTitle = Console.ReadLine();
    bookTitle = bookTitle.ToLower();
    string bookToUpdate = null;
    foreach(string book in books)
    {
        if (book.ToLower() == bookTitle)
        {
            bookToUpdate = book;
            break;
        };
    };
    if (bookToUpdate != null)
    {
        books.Remove(bookToUpdate);
        Console.Write("Enter new title: ");
        string newBookTitle = Console.ReadLine();
        books.Add(newBookTitle);
        Console.WriteLine("Book title was update!");
    } else
    {
        Console.WriteLine("Book not found!");
    };
};

ShowBooks(books);
FindBook(books);
AddBook(books);
ShowBooks(books);
RemoveBook(books);
ShowBooks(books);
UpdateBook(books);
ShowBooks(books);
