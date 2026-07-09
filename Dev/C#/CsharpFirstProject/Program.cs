using System;
using System.Runtime.CompilerServices;

class Program
{
    static void Main()
    {
        int[] grades = {4, 5, 3, 2, 3};
        int sum = 0;
        foreach(int grade in grades)
        {
            Console.WriteLine($"Grade: {grade}");
            sum += grade;
        }
        Console.WriteLine($"Sum: {sum}");
    }
}