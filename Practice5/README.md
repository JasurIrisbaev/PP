# Practice 5 – Python Regular Expressions

## Student
Name: Irisbaev Jasurbek  
Course: Programming Principles 2

---

## Description

This practice demonstrates the use of Python Regular Expressions using the `re` module.

The project includes:

- Basic RegEx examples
- Practical exercises from W3Schools
- Receipt parsing using regex

---

## Folder Structure

### python-basics
Examples of Python regex functions:

- re.match()
- re.search()
- re.findall()
- re.split()
- re.sub()
- Quantifiers
- Character sets
- Special sequences
- Flags

### python-examples
Solutions for 10 regex tasks:

1. a followed by zero or more b  
2. a followed by 2–3 b  
3. lowercase words joined with underscore  
4. uppercase followed by lowercase  
5. string starting with a and ending with b  
6. replace spaces/commas/dots  
7. snake_case → camelCase  
8. split at uppercase letters  
9. insert spaces before capitals  
10. camelCase → snake_case  

### receipt_parser_solution
Regex parsing of receipt file.

Functions:

- extract product names
- extract prices
- extract date/time
- extract payment method
- calculate total

---

## Technologies

- Python 3
- re module

---

## Run examples

Example:

```bash
python python-basics/Rematch.py