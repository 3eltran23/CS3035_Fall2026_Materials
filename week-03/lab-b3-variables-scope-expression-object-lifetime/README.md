# Lab B3: Variables, Scope, Expressions, and Object Lifetime

**Date:** September 9, 2026  
**Estimated time:** 60 minutes  
**Languages:** Python and Kotlin/JVM

## Overview

In this laboratory, you will investigate how Python and Kotlin represent
variables, share references to objects, determine the visibility of names, and
manage the lifetime of objects. You will also compare conditional expressions
in both languages.

For each exercise:

1. Predict the result before running the code.
2. Run the program and record the actual result.
3. Explain the result using the vocabulary from the lecture.

## Learning Objectives

After completing this laboratory, you should be able to:

- Explain how Python assignment binds a name to an object.
- Compare Python assignment with Kotlin `val` and `var` declarations.
- Distinguish reassignment from mutation.
- Identify aliases and independent copies of mutable objects.
- Compare Python function scope with Kotlin block scope.
- Use conditional expressions in Python and Kotlin.
- Explain when an object becomes eligible for garbage collection.

## Suggested Schedule

| Time | Activity |
|---:|---|
| 0-5 minutes | Setup and instructions |
| 5-12 minutes | Exercise 1: Python and immutable values |
| 12-19 minutes | Exercise 2: Python and mutable objects |
| 19-27 minutes | Exercise 3: Aliasing and copying |
| 27-37 minutes | Exercise 4: Kotlin values and references |
| 37-47 minutes | Exercise 5: Scope in Python and Kotlin |
| 47-54 minutes | Exercise 6: Conditional expressions |
| 54-60 minutes | Exercise 7 and exit ticket |

## Setup

You will need:

- Python 3 in Visual Studio Code. You may use a Jupyter notebook or Python
  scripts.
- Kotlin/JVM in IntelliJ IDEA, a Kotlin notebook, or the Kotlin Playground.

Prepare your submission as follows:

1. Make a copy of `LabB03.ipynb`.
2. Rename the copy using the format `your_name_LabB03.ipynb`. Replace
   `your_name` with your own name.
3. Record your predictions, code, results, and explanations in the copied
   notebook.
4. Run the Python and Kotlin programs in one of the approved environments.
5. Add screenshots to the notebook showing your completed Python and Kotlin
   programs running successfully with their output visible. If you use Python
   or Kotlin scripts outside the notebook, paste the relevant code into a
   Markdown cell before the screenshot.

Do not depend on a particular numeric value from Python's `id()` function. The
value identifies an object during its lifetime, but the number can differ each
time the program runs.

## Before You Begin: Equality and Object Identity

Python and Kotlin provide separate operators for comparing values and comparing
object references.

| Question | Python | Kotlin |
|---|---|---|
| Do these values or objects have equal contents? | `a == b` | `a == b` |
| Do these variables refer to the same object? | `a is b` | `a === b` |
| Are the contents different? | `a != b` | `a != b` |
| Do the variables refer to different objects? | `a is not b` | `a !== b` |

### Python example

```python
first = [10, 20]
second = [10, 20]
alias = first

print(first == second)  # True: equal contents
print(first is second)  # False: different list objects
print(first is alias)   # True: same list object
```

In Python:

- `==` compares values or contents.
- `is` compares object identity.
- Use `is` for identity checks such as `value is None`.
- Do not use `is` to compare the values of strings or numbers. Python may reuse
  some immutable objects as an implementation optimization, so use `==` when
  the values are what matter.

### Kotlin example

```kotlin
fun main() {
    val first = mutableListOf(10, 20)
    val second = mutableListOf(10, 20)
    val alias = first

    println(first == second)   // true: equal contents
    println(first === second)  // false: different list objects
    println(first === alias)   // true: same list object
}
```

In Kotlin:

- `==` checks structural equality. It compares values or contents using
  `equals()`.
- `===` checks referential equality. It determines whether two variables refer
  to the same object.
- Use `==` for numeric and string value comparisons.
- Use `===` when object identity is the question, especially with mutable
  collections or class instances.

Remember:

> Equal contents do not necessarily mean that two variables refer to the same
> object. Two references to the same object are aliases.

## Exercise 1: Python and an Immutable Value

Create a name bound to a floating-point object. Examine its identity, type, and
value. Update the variable by adding 20 and examine it again.

```python
number = 12.5

before_id = id(number)

print(f"Before ID: {before_id}")
print(f"Before type: {type(number).__name__}")
print(f"Before value: {number}")

number += 20

after_id = id(number)

print(f"After ID: {after_id}")
print(f"After type: {type(number).__name__}")
print(f"After value: {number}")
```

Record your answers:

1. What did you predict?
2. Did the value change?
3. Did the type change?
4. Did the object ID change?
5. Did Python mutate the original float or bind `number` to another float?
6. What does this result tell you about immutable objects?

## Exercise 2: Python and a Mutable Object

Create a name bound to an empty list. Examine its identity, type, and value.
Append `300` and examine the list again.

```python
numbers = []

before_id = id(numbers)

print(f"Before ID: {before_id}")
print(f"Before type: {type(numbers).__name__}")
print(f"Before value: {numbers}")

numbers.append(300)

after_id = id(numbers)

print(f"After ID: {after_id}")
print(f"After type: {type(numbers).__name__}")
print(f"After value: {numbers}")
```

Record your answers:

1. What did you predict?
2. Did the value change?
3. Did the type change?
4. Did the object ID change?
5. Did `append()` mutate the existing list or bind `numbers` to another list?
6. How does this result differ from Exercise 1?

## Exercise 3: Aliasing and Copying

First, predict the results of every comparison and the final contents of each
list.

### Python

```python
first = [10, 20]
second = first
third = first.copy()

print(f"Equal contents: {first == third}")
print(f"first is second: {first is second}")
print(f"first is third: {first is third}")

second.append(30)

print(f"first: {first}")
print(f"second: {second}")
print(f"third: {third}")
```

### Kotlin

```kotlin
fun main() {
    val first = mutableListOf(10, 20)
    val second = first
    val third = first.toMutableList()

    println("Equal contents: ${first == third}")
    println("first === second: ${first === second}")
    println("first === third: ${first === third}")

    second.add(30)

    println("first: $first")
    println("second: $second")
    println("third: $third")
}
```

Record your answers:

1. Which variables are aliases?
2. Which lists initially have equal contents?
3. Why does modifying `second` also affect `first`?
4. Why does `third` remain unchanged?
5. How do Python `is` and Kotlin `===` differ from `==`?

## Exercise 4: Kotlin Values and References

Kotlin does not provide a portable numeric object ID equivalent to Python's
`id()`. For numeric values, compare the type and value. For reference objects,
use `===` to determine whether two variables refer to the same object.

### Part A: Numeric value

```kotlin
fun numericValueDemo() {
    var number = 12.5
    val originalValue = number

    println("Before type: ${number::class.simpleName}")
    println("Before value: $number")

    number += 20

    println("After type: ${number::class.simpleName}")
    println("After value: $number")
    println("Same value: ${number == originalValue}")
}
```

### Part B: Mutable reference object

```kotlin
fun mutableReferenceDemo() {
    val numbers = mutableListOf<Int>()
    val originalReference = numbers

    println("Before value: $numbers")
    println("Same object before: ${numbers === originalReference}")

    numbers.add(300)

    println("After value: $numbers")
    println("Same object after: ${numbers === originalReference}")
}

fun main() {
    numericValueDemo()
    mutableReferenceDemo()
}
```

Record your answers:

1. What type did Kotlin infer for `number`?
2. Why can `number` receive `32.5` but not `"32.5"`?
3. Why is `numbers.add(300)` allowed even though `numbers` uses `val`?
4. Did the list reference change after `add(300)`?
5. Explain the difference between reassignment and mutation.

## Exercise 5: Scope in Python and Kotlin

Predict whether each program runs successfully. If it runs, predict its output.

### Python

```python
def scope_test():
    if True:
        message = "Inside the block"

    print(message)


scope_test()
```

### Kotlin

```kotlin
fun scopeTest() {
    if (true) {
        val message = "Inside the block"
    }

    println(message)
}

fun main() {
    scopeTest()
}
```

Complete the following tasks:

1. Run the Python program and record its output.
2. Compile the Kotlin program and record the compiler message.
3. Explain why Python can use `message` after the `if` block.
4. Explain why Kotlin cannot use `message` after the braced block.
5. Correct the Kotlin program by using an `if` expression:

```kotlin
fun scopeTest() {
    val message = if (true) {
        "Inside the block"
    } else {
        "Outside the block"
    }

    println(message)
}
```

## Exercise 6: Conditional Expressions

Rewrite each statement-based solution as a conditional expression.

### Python

```python
score = 72

if score >= 60:
    result = "Pass"
else:
    result = "Retry"

print(result)
```

Replace the `if` statement with one assignment:

```python
result = "TODO"
```

### Kotlin

```kotlin
fun main() {
    val score = 72
    var result: String

    if (score >= 60) {
        result = "Pass"
    } else {
        result = "Retry"
    }

    println(result)
}
```

Replace the statement-style version with one `val` declaration:

```kotlin
val result = TODO()
```

Test both programs with scores of `59`, `60`, and `85`.

Record your answers:

1. What value does each program produce for each test score?
2. Which part of each expression is the condition?
3. Why does the Kotlin expression require an `else` branch?
4. How does the order of the Python syntax differ from Kotlin's syntax?

## Exercise 7: Object Lifetime and Reachability

Garbage collectors reclaim unreachable objects, not variable names. Do not try
to predict the exact time at which garbage collection will run.

### Python

```python
numbers = [100, 200]
alias = numbers

del numbers

print(alias)

del alias
```

### Kotlin/JVM

```kotlin
fun main() {
    var numbers: MutableList<Int>? = mutableListOf(100, 200)
    val alias = numbers

    numbers = null

    println(alias)
}
```

Record your answers:

1. Does removing the first reference immediately remove the list?
2. Which variable keeps the list reachable in each program?
3. When does the list become eligible for garbage collection?
4. Does either language guarantee exactly when the memory will be reclaimed?
5. Explain why assigning `null` or using `del` is not the same as directly
   deleting an object.

## Exit Ticket

Answer each question in one or two sentences.

1. What does assignment do in Python?
2. What is the difference between Kotlin `val` and `var`?
3. What is the difference between value equality and object identity?
4. Why does a Python name created inside an `if` remain available in the
   surrounding function?
5. When does an object become eligible for garbage collection?

## Submission Checklist

- [ ] I recorded a prediction before running each exercise.
- [ ] My Python code runs without unaddressed errors.
- [ ] My final Kotlin code compiles and runs.
- [ ] I added screenshots showing my Python and Kotlin programs running with
      their output visible.
- [ ] I recorded the intentional Kotlin scope error before correcting it.
- [ ] I answered every analysis question and the exit ticket.
- [ ] I explained results using terms such as binding, object, reference,
      mutation, alias, scope, reachability, and garbage collection.
- [ ] I renamed my notebook using the format `your_name_LabB03.ipynb`.

## Suggested Grading

This laboratory is worth **20 points**.

- Python identity, type, and mutability exercises: 4 points
- Aliasing and copying comparison: 4 points
- Kotlin values and references: 4 points
- Python and Kotlin scope comparison: 4 points
- Conditional expressions, lifetime, and exit ticket: 4 points
