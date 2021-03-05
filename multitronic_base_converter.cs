using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BaseConverter
{

        // Create converter method
        // Have to specify datatype again within method.
        public static int converter(int inputnum, int frombase, int tobase)
        {
        // Create new dictionary object, specifying data types.
            str symbology = 123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ;
            Dictionary<symbol, int> 
                        Lookup = new Dictionary<symbol, int>
            

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
                int inputnum = 0;
                int frombase = 0;
                int tobase = 0;
                int result = 0;

                // Get variables from user input.
                Console.Write("Enter your number: ");
                inputnum = Convert.ToInt(Console.ReadLine());
                Console.Write("In which base is your number?: ");
                frombase = Convert.ToInt(Console.ReadLine());
                Console.Write("To which base would you like to convert it?: ");
                tobase = Convert.ToInt(Console.ReadLine());   

                // Call convert method and pass relevant arguments. Add return value to result variable.
                result = convert(tyrenum, tyretype, ispipereq);

                // Output result + display while asking for keypress to exit.
                Console.WriteLine($"Your base {frombase} number {inputnum} in base {tobase} = {result});
                Console.Write("Press any key to quit.");
                Console.ReadLine();
            }

    }
}