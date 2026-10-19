# Lab A9: Generics

**Total: 10 points**

In this lab, you will write a generic Kotlin function and investigate how variance affects generic classes. Complete each exercise and explain how its type parameters are used.

## Lab A9.1: Replace the First Element of a List

The **head** of a list is its first element. Implement a generic function named `setHead` that returns a new list with its first element replaced by a supplied value.

For example, replacing the head of `[1, 2, 3]` with `9` produces `[9, 2, 3]`.

**Assume that `xs` contains at least one element.** Handling an empty list is an optional extension below.

### Starter Code

Replace `TODO(...)` with your implementation. You may use a block body if needed, but keep the same parameter and return types.

```kotlin
fun <A> setHead(xs: List<A>, x: A): List<A> =
    TODO("Replace the first element and return a new list")

fun main() {
    val numbers = listOf(1, 2, 3)
    val updatedNumbers = setHead(numbers, 9)

    println(updatedNumbers)
    println(numbers)

    val animals = listOf("Cat", "Dog", "Fish")
    println(setHead(animals, "Bird"))

    val singleItem = listOf(true)
    println(setHead(singleItem, false))
}
```

`TODO(...)` is a placeholder that throws an error when executed. Complete the function before running the program.

### Expected Output

```text
[9, 2, 3]
[1, 2, 3]
[Bird, Dog, Fish]
[false]
```

The second line confirms that the original `numbers` list has not changed.

### Test Your Function

In addition to the starter examples, create one example using a list of `Double` values. Show the original list, the replacement value, the returned list, and the original list again after the call.

Check that the returned list has the same number of elements as the original, and that every element after the first remains in its original position.

### Reflection

Predict whether the following call compiles, then check your prediction. Explain the effect of explicitly specifying `<Int>`.

   ```kotlin
   setHead<Int>(listOf(1, 2, 3), "nine")
   ```

### Optional Extension: Empty Lists

Extend your function so that an empty input list causes an `IllegalArgumentException` with a clear message. You may use Kotlin's `require` function. Test this behavior with `setHead(emptyList<Int>(), 9)` separately from the successful examples.


## Lab A9.2: Be the Compiler

Here are four classes that use generics. Your job is to act as the Kotlin compiler and determine whether each class will compile. If a class does not compile, identify the declaration that causes the error and explain why.

### Instructions

1. Predict the result for each class before compiling it.
2. Compile each class separately so an error in one does not prevent you from checking the others.
3. Record the compiler's result and explain any difference from your prediction.
4. Treat warnings about unused parameters separately from compilation errors.

These examples are for compilation checks; you do not need to create objects or call the methods. In class C, `TODO(...)` provides a valid placeholder body for a function returning `T`. It throws if called, but your task is to determine whether the declaration compiles.

### Class A

```kotlin
class A<in T>(t: T) {
    fun myFunction(t: T) { }
}
```

### Class B

```kotlin
class B<in T>(t: T) {
    val x = t

    fun myFunction(t: T) { }
}
```

### Class C

```kotlin
abstract class C<in T> {
    fun myFunction(): T = TODO("Not implemented")
}
```

### Class E

```kotlin
class E<in T>(t: T) {
    var y = t

    fun myFunction(t: T) { }
}
```

### Record Your Findings

For every rejected class, name the offending declaration and explain how its use of `T` conflicts with `in T`. For a class that compiles, explain why its uses of `T` are allowed.

| Class | Your prediction: compiles? | Compiler result | Explanation |
|---|---|---|---|
| A | | | |
| B | | | |
| C | | | |
| E | | | |


### Follow-Up: Repair the Rejected Classes

For each class that fails to compile, propose and test one correction. Briefly explain what you changed and whether your change preserves contravariance.

### What to Include

- Your completed prediction and results table.
- The relevant compiler error message for each rejected class.
- Your explanations of the compilation results.
- Your corrected code and explanation for each rejected class.

## Lab A9.3: Sharpen Your Pencil

Below is a complete Kotlin file listing. The code, however, will not compile. Which lines will not compile? What changes do you need to make to the class and interface definitions to make them compile?

**You may not change the `main` function.** Preserve the `Food` and `VeganFood` inheritance relationship and the type arguments used by `FoodSeller`, `VeganFoodSeller`, `Person`, and `Vegan` when they implement their interfaces.

### Code to Investigate

```kotlin
// Food types
open class Food

class VeganFood : Food()

// Sellers
interface Seller<T>

class FoodSeller : Seller<Food>

class VeganFoodSeller : Seller<VeganFood>

// Consumers
interface Consumer<T>

class Person : Consumer<Food>

class Vegan : Consumer<VeganFood>

fun main(args: Array<String>) {
    var foodSeller: Seller<Food>
    foodSeller = FoodSeller()
    foodSeller = VeganFoodSeller()

    var veganFoodConsumer: Consumer<VeganFood>
    veganFoodConsumer = Vegan()
    veganFoodConsumer = Person()
}
```

### Predict and Check

Before compiling, predict whether each assignment is allowed. Then compile the file and record the results. Distinguish unused-variable or unused-parameter warnings from errors.

| Assignment | Your prediction: compiles? | Compiler result | Explanation |
|---|---|---|---|
| `foodSeller = FoodSeller()` | | | |
| `foodSeller = VeganFoodSeller()` | | | |
| `veganFoodConsumer = Vegan()` | | | |
| `veganFoodConsumer = Person()` | | | |

### Repair the Definitions

1. Identify the definitions that need to change.
2. Make the smallest changes needed to allow all assignments while keeping `main` unchanged.
3. Compile the corrected file and confirm that the type errors are resolved.

This program has no print statements, so it produces no console output. Successful compilation is the result to verify.

### Explain Your Changes

1. For each rejected assignment, identify the type being assigned and the type required by the variable.
2. Which kind of variance does each corrected interface use? Explain how the resulting subtype relationship makes the corresponding assignment valid.
3. The interfaces in this example are empty. If `Seller` later had a method returning `T`, and `Consumer` later had a method accepting `T`, would those methods fit your variance choices? Explain.

## Submission

Submit **one Jupyter notebook named `notebook.ipynb`** containing your work for all three exercises. Label each section **Lab A9.1**, **Lab A9.2**, and **Lab A9.3**.

Include the following:

| Exercise | Required contents |
|---|---|
| **Lab A9.1** | Your completed `setHead` function; output for the integer, string, Boolean, and additional `Double` examples; evidence that the original lists remain unchanged; and your prediction, compiler result, and explanation for the explicit `<Int>` call in the reflection question. |
| **Lab A9.2** | Your completed prediction and results table; relevant compiler errors for the rejected classes; explanations of why each class compiles or fails; and corrected code with an explanation and confirmation that each correction compiles. |
| **Lab A9.3** | Your completed prediction and results table; the original compiler errors; the corrected complete Kotlin listing with `main`, the food hierarchy, and the implementing classes' type arguments unchanged; confirmation that it compiles; and answers to the questions under “Explain Your Changes.” |

Use Markdown cells for explanations and tables. Keep intentionally failing examples separate from corrected code and label the expected failures clearly. Include the actual compiler messages from your checks.

If your notebook can execute Kotlin, include your code and its output in the notebook. If it cannot, place the Kotlin code in fenced Markdown code blocks, run it in a Kotlin environment such as IntelliJ IDEA, and include the resulting output or compiler messages in the notebook. For code that compiles without printing anything, state that compilation succeeded; do not invent console output.

The empty-list extension in Lab A9.1 is optional and is not required for full credit. Include its code and observed behavior if you complete it.

## Grading: 10 Points

| Exercise | Criteria | Points |
|---|---|---:|
| **Lab A9.1** | Correct generic implementation that replaces only the first element and leaves the input unchanged (2); complete examples and testing evidence (1); correct reflection prediction, compiler result, and explanation (1). | **4** |
| **Lab A9.2** | Completed prediction table with accurate verified results and relevant error messages (1); explanations of the variance issues (1); valid corrections with explanations and compilation confirmation (1). | **3** |
| **Lab A9.3** | Correct identification and explanation of the rejected assignments (1); corrected definitions that compile with `main` and the required type relationships unchanged (1); answers explaining the variance choices and proposed methods (1). | **3** |
| **Total** | | **10** |
