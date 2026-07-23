using System;

static void CountVowels(string text)
{
    int counter = 0;
    foreach(char letter in text)
    {
        if (letter.ToString() == "a" || letter.ToString() == "o" || letter.ToString() == "e" || letter.ToString() == "i" || letter.ToString() == "u")
        {
            counter += 1;
        };
    };
    Console.WriteLine($"Count of vowels: {counter}");
};

static void CountDigits(string text)
{
    int counter = 0;
    foreach(char digit in text)
    {
        if (digit.ToString() == "0" || digit.ToString() == "1" || digit.ToString() == "2" || digit.ToString() == "3" || digit.ToString() == "4" || digit.ToString() == "5" || digit.ToString() == "6" || digit.ToString() == "7" || digit.ToString() == "8" || digit.ToString() == "9")
        {
            counter += 1;
        }
    };
    Console.WriteLine($"Count of digits: {counter}");
}

static void IsEmail(string text)
{
    bool email = false;
    foreach(char sign in text)
    {
        if (sign.ToString() == "@")
        {
            email = true;
            Console.WriteLine("This is email");
            break;
        }
    };
    if (email == false)
    {
        Console.WriteLine("This is not email!");
    }
};

CountVowels("programming");
CountDigits("Python 3.14");
IsEmail("chatgpt@gmail.com");
//Знаю что надо было сделать список, но я не знаю как на C# реализовать проверку нахождения символа в списке, помоги.