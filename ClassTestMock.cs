using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ClassTestMock
{
    class Calculator
    {
            public static double jobprice(double tyrenum, string tyretype, string ispipereq)
            {
                Dictionary<string, double> pricing =
                                new Dictionary<string, double>();
                pricing.Add("b", 29.99);
                pricing.Add("p", 49.99);
                pricing.Add("exhaust", 69.99);

                double totalprice = 0;
                if (tyrenum <= 3)
                {totalprice = pricing[tyretype] * tyrenum;}
                if (tyrenum >= 4)
                {totalprice = pricing[tyretype] * tyrenum * 0.8;}
                if (ispipereq == "y")
                {totalprice += pricing["exhaust"];}
                if (tyrenum > 0 && ispipereq == "y")
                {totalprice -= 10;}
                return totalprice;
            }
    }
    
    class Program
    {
            static void Main(string[] args)
            {
                // Declare variables, set to 0 or empty.
                double tyrenum = 0;
                string tyretype = "";
                string ispipereq = "";
                double result = 0;

                Console.Write("How many tyres are required (max 5)?: ");
                tyrenum = Convert.ToDouble(Console.ReadLine());
                Console.Write("Are (b)udget or (p)remium tyres required?: ");
                tyretype = Console.ReadLine();
                Console.Write("Is an exhaust pipe required, y/n?: ");
                ispipereq = Console.ReadLine();   

                result = Calculator.jobprice(tyrenum, tyretype, ispipereq);

                Console.WriteLine("The total price is: £"+result);
                Console.Write("Press any key to quit.");
                Console.ReadLine();
            }

    }
}