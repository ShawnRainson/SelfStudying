using System.Text;

class Program
{
    static void Main()
    {
        string[] terms = {"Loop ", "OOP ", "List ", "Integer"};
        StringBuilder sb = new StringBuilder();

        foreach(string term in terms)
        {
            sb.Append(term);
        }
        string result = sb.ToString();
        Console.WriteLine(result);
    }
}