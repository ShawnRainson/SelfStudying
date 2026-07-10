using System;

interface IReviewable
{
    void Review();
}

class Program: IReviewable
{
    public void Review()
    {
        Console.WriteLine("Code review is passed!");
    }

    static void Main()
    {
        Program myProgram = new Program();

        myProgram.Review();
    }
}