using System;

class Program
{
    static void Main()
    {
        int score = 77;
        if (score >= 90)
        {
            Console.WriteLine("Excellent!");
        }
        else if (score >= 50 && score <= 89)
        {
            Console.WriteLine("Good job!");
        }
        else
        {
            Console.WriteLine("Try again!");
        }

    }
}