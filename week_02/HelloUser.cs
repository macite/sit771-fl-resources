using System;
using SplashKitSDK;

namespace MyProgram
{
    public class Program
    {
        public static void Main()
        {
            string name;
            int yearOfBirth, currentYear;

            Console.Write("Please enter your name: ");
            name = Console.ReadLine();

            Console.Write("Please enter your year of birth: ");
            string yearOfBirthString = Console.ReadLine();

            yearOfBirth = Convert.ToInt32(yearOfBirthString);

            currentYear = DateTime.Now.Year;
            int age = currentYear - yearOfBirth;

            Console.WriteLine("OK " + name + ", You are " + age + " years old this year!");
        }
    }
}