# Mad Libs Game (Python)

Mad Libs is a game with a basic story template that has blank spaces which is filled by the user.
The fun part is that the user inputs words without knowing the story ahead of time. The asks the user for different types of words (e.g., noun, verb, adjective) and 
then inserts those words into the story template to create a funny and often nonsensical story.

This project is an interactive Mad Libs game developed in Python as part of a TUMO Labs GSL program task.

---
## Task Requirements

The program was developed according to the following requirements:

Allow the user to choose one of the available templates
Ask the user to input words (e.g., "type a number", "type a noun")
Generate and display a story based on the inputs

Additional constraints:

The program uses the random library
Only basic functions such as print() and input() are used, along with custom helper functions

## Objective

The goal of this project is to practice:

* Working with user input
* Writing clean and reusable functions
* Implementing input validation
* Using loops and conditional logic
* Structuring a small Python program

---

## Features

* Three story templates:

  * Hospital
  * Camping
  * Castle
* Random template selection option
* Input validation:
  * Ensures numeric inputs are valid
  * Ensures word inputs contain only letters
* Replay functionality (user can play multiple times)

---

## How to Run

1. Make sure Python is installed:

   ```bash
   python --version
   ```

2. Run the program:

   ```bash
   python main.py
   ```

---

## Project Structure

```
mad-libs/
│
├── main.py
└── README.md
```

---

## Implementation Details

* `get_number_input()`
  Validates that the input is not empty and contains only digits.

* `get_word_input()`
  Validates that the input contains only alphabetic characters and spaces.

* The program uses a loop to allow the user to play multiple times.

---

## Author

Shaghik Torosian

---

## Notes

This project was created as part of a learning exercise in the TUMO Labs GSL program.
