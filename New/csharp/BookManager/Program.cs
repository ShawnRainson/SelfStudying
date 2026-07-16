using System;

List<string> books = new List<string>();

static void AddBook()
{
    string book = Console.Write("Enter book title: ");
    books.Append(book);
};

static void ShowBooks()
{
    foreach(string book in books)
    {
        Console.WriteLine($"Book: {book}");
    };
};

static void SearchBook()
{
    string book = book.ToLower();
    foreach(string title in books)
    {
        if (book == title.ToLower())
        {
            Console.WriteLine($"Found book: {title}");
        } else
        {
            Console.WriteLine("Book list have no this book!");
        };
    };
};

static void RemoveBook()
{
    foreach(string book in books)
    {
        Console.WriteLine($"Book: {book}");
    };

    string remBook = Console.Write("Choose book for remove: ");
    foreach(string checkBook in books)
    {
        if (remBook.ToLower() == checkBook.ToLower())
        {
            books.Remove(checkBook);
            Console.WriteLine("Book was removed!");
        };
    };

};

int choice = Console.Write("Menu:\n1. Add book\n2. Show all books\n3. Search book\n 4. Remove book\n5. Exit");

switch(choice)
{
    case 1:
        AddBook();
    
    case 2:
        ShowBooks();
    
    case 3:
        SearchBook();
    
    case 4:
        RemoveBook();
    
    case 5:
        Console.WriteLine("Bye-bye!");
        break;
}