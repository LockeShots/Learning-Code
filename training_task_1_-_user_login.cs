using System;

class MainClass {
  public static void Main (string[] args) {
    string okusername = "Allan";
    string okpassword = "butt";
    string entered_username = "";
    string entered_password = "";
    int count = 0;
    while (count < 3) {
      Console.WriteLine ("Please enter your username:");
      entered_username = Console.ReadLine();
      if (entered_username == okusername) {
        Console.WriteLine ("Correct username");
        Console.WriteLine ("Please enter your password:");
        entered_password = Console.ReadLine();
      }
      else {
        Console.WriteLine ("Incorrect username");
        break;
      }
      if (entered_username == okusername && entered_password == okpassword) {
        Console.WriteLine ("Correct");
        break;
      }
      else {
        Console.WriteLine ("Incorrect password");
        count += 1;
      }
    if (count > 2) {
      Console.WriteLine ("Too many incorrect passwords");
      }
    }
  }
}