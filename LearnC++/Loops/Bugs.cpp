// In C++, there are many different ways of classifying errors, but they can be boiled down to four categories:
//
//     Compile-time errors: Errors found by the compiler.
//     Link-time errors: Errors found by the linker when it is trying to combine object files into an executable program.
//     Run-time errors: Errors found by checks in a running program.
//     Logic errors: Errors found by the programmer looking for the causes of erroneous results.

# include <iostream>
int main () {


    // Compile-time errors:
            //Syntax errors: Errors that occur when we violate the rules of C++ syntax. e.g missing semicolon
            //Type errors: Errors that occur when there are mismatch between the types we declared. e.g not declaring variable
    char answer;
    int score = 0;

    std::cout << "Who Wants To Be a Millionaire\n\n"

    std::cout << "Question 1)\n\n";

    std::cout << "For ordering his favorite beverages on demand, LBJ had four buttons installed in the Oval Office labeled 'Coffee', 'Tea', 'Coke', and what?\n\n";

    std::cout << "A. Fresca   B. V8  \n";
    std::cout << "C. Yoo-hoo  D. A&W \n\n";

    std::cout << "Enter your answer: ";
    std::cin >> answer;

    if (answer == 'A' || answer == 'a') {

        score = score + 100;
        std::cout << "Correct!\n";

    }


    // Runs in a syntax error since a semicolon (;) is missing on line 18



    // Link Time error: When code compiles fine but there's an error message when the program needs some function of library that it cant find
    // Programs may be split into separate files as they get larger. After compiling, the linker will combine separate object files into one executable file
    // Link time errors found when trying to combine object files into an executable file


    // E.g Using a function that is never defined, Writing Main() instead of main()
        // $ g++ example.cpp
        // /usr/lib/gcc/x86_64-linux-gnu/7/../../../x86_64-linux
        // Scrtl.o:
        // In function `_start':
        // (
        // .text+0x20): undefined reference to `main'
        // collect2: error: ld returned 1 exit status






    // Run Time error: errors which happen during program execution after successful compilation
    // When a program with no compile or link time errors asks the computer to do something that the computer is unable tor reliably do
    // E.g   Division by zero, opening a file that doesn't exist

    int width = 20;
    int length = 0;

    int ratio = width / length;

    std::cout << ratio << "\n";

    // causes a floating point exception error because its divided by 0 instead of 30





    // Finally Logical error: when program doesnt do what we want it to do or no output is produced
    // e.g program logic is flawed, some mistake in an if statement or a for/while loop
    // They dont have error messages, usually detected by test-driven development

    // Output from 1 to steps:

    int steps = 10;

    for (int i = 0; i <= steps; i++) {

        std::cout << "Step #";
        std::cout << i << "\n";

    }

    // no error detected but it starts from 0 instead of 1
}



