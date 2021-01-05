using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ClassTestMock
{
    // Create calculator class.
    class Calculator
    {
            // Create jobprice method within Calculator class.
            // Have to specify datatype again within method.
            // This time method is not static.
            public double jobprice(double tyrenum, string tyretype, string ispipereq)
            {
            // Create new dictionary object, specifying data types.
                Dictionary<string, double> pricing =
                                new Dictionary<string, double>();
                pricing.Add("b", 29.99);
                pricing.Add("p", 49.99);
                pricing.Add("exhaust", 69.99);

            // Create if statements. Very similar syntax to Python here.
                double totalprice = 0;
                if (tyrenum <= 3)
                {totalprice = pricing[tyretype] * tyrenum;}
                if (tyrenum >= 4)
                {totalprice = pricing[tyretype] * tyrenum * 0.8;}
            // NB being mindful the difference between "" for string declaration and '' for single character declaration.
                if (ispipereq == "y")
                {totalprice += pricing["exhaust"];}
                if (tyrenum > 0 && ispipereq == "y")
                {totalprice -= 10;}
                return totalprice;
            }
    }
    
    // Created seperate class for the sake of clear context.
    class Program
    {
            static void Main(string[] args)
            {
                // Declare variable types here, set to 0 or empty.
                double tyrenum = 0;
                string tyretype = "";
                string ispipereq = "";
                double result = 0;

                // Get variables from user input.
                Console.Write("How many tyres are required (max 5)?: ");
                tyrenum = Convert.ToDouble(Console.ReadLine());
                Console.Write("Are (b)udget or (p)remium tyres required?: ");
                tyretype = Console.ReadLine();
                Console.Write("Is an exhaust pipe required, y/n?: ");
                ispipereq = Console.ReadLine();   

                // As jobprice is a non-static method, it can only be called through an instance of the Calculator class, not the class itself/
                // Create an object instance of Calculator called res.
                // Call method from within new res instance of Calculator class.
                Calculator res = new Calculator();
                result = res.jobprice(tyrenum, tyretype, ispipereq);

                // Output result + display while asking for keypress to exit.
                Console.WriteLine("The total price is: £"+result);
                Console.Write("Press any key to quit.");
                Console.ReadLine();
            }

    }
}