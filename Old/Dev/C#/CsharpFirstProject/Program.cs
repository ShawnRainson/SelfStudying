using System;

class Program
{
    static void Main()
    {
        DateTime today = DateTime.Now;
        DateTime futureDay = today.AddDays(7);

        string str_today = today.ToString("yyyy.MM.dd");
        string str_futureDate = futureDay.ToString("yyyy.MM.dd");

        Console.WriteLine($"Today: {str_today}\nFuture day: {str_futureDate}");
    }
}