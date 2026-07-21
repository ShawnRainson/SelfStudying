using System;
using System.Xml;

static void CountWords(string text)
{
    int counter = 1;
    string spaceInWord = " ";
    foreach(char space in text)
    {
        spaceInWord = space.ToString();
        if (spaceInWord == " ")
        {
            counter += 1;
        }
    }
    Console.WriteLine($"Count words: {counter}");
}

CountWords("Hello world!");

//Подсчёт реализовал, а вот как сделать реверс без встроенного метода, не знаю