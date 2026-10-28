# Lab B10: Writing Loops Functionally

**Total: 20 points**

In this lab, you will express repetition using local tail-recursive functions. Instead of reassigning loop variables, pass the next state as arguments to a recursive call.

## Lab B10.1: A Recursive Sum

**Points: 3**

Complete the function `sumTo` so that it returns the sum of the integers from `1` through `i`.

For example, `sumTo(4)` returns `10` because `1 + 2 + 3 + 4 = 10`. Define `sumTo(0)` to return `0`.

**Assume that `0 <= i <= 1000`.** You do not need to handle inputs outside this range.

### Starter Code

Replace each `____` with the appropriate Kotlin expression. These blanks are not valid Kotlin expressions; complete them before compiling or running the code.

```kotlin
fun sumTo(i: Int): Int {
    tailrec fun go(n: Int, acc: Int): Int =
        if (n <= 0) ____
        else go(n - 1, ____)

    return go(i, ____)
}
```

### Requirements

- Keep the `sumTo(i: Int): Int` signature and the local `tailrec` helper `go`.
- Use `n` to track the remaining work and `acc` to carry the accumulated sum.
- Do not use loops, mutable variables (`var`), or changes to external state inside your implementation.
- Make progress toward the base case on every recursive call.

### Test Your Function

Run this test code after completing the function:

```kotlin
fun main() {
    println(sumTo(0))
    println(sumTo(1))
    println(sumTo(4))
    println(sumTo(10))
    println(sumTo(1000))
}
```

Expected output:

```text
0
1
10
55
500500
```

### Explain Your Solution

1. Identify the base case and explain what it returns.
2. Explain your choice of initial accumulator value.
3. Trace `sumTo(4)` by listing every call to `go` and its `(n, acc)` arguments.
4. Explain why the recursive call is in tail position. What work, if any, remains after that call returns?

## Lab B10.2: Tail-Recursive Fibonacci

**Points: 5**

Write a recursive function named `fib` that returns the *n*th [Fibonacci number](https://www.britannica.com/science/Fibonacci-number). Use **zero-based indexing**: `fib(0)` is `0` and `fib(1)` is `1`. For each index `n >= 2`, the value is the sum of the previous two values:

```text
F(0) = 0
F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n >= 2
```

The sequence begins:

```text
Index:  0  1  2  3  4  5  6   7   8
Value:  0  1  1  2  3  5  8  13  21
```

Your implementation must use a **local tail-recursive function**.

**Assume that `0 <= i <= 45`.** This range keeps both the requested result and the next Fibonacci value within Kotlin's `Int` range. You do not need to handle inputs outside this range.

### Starter Code

Replace `TODO(...)` with your implementation. You may change the expression body to a block body so that you can define a local helper, but keep the same parameter and return types.

```kotlin
fun fib(i: Int): Int =
    TODO("Implement Fibonacci using a local tail-recursive function")
```

`TODO(...)` is a built-in Kotlin placeholder. The starter declaration compiles, but calling it throws a `NotImplementedError` until you replace the placeholder. Some textbook examples use `SOLUTION_HERE()` as an alias; no such alias is needed here.

### Requirements

- Keep the public signature `fib(i: Int): Int`.
- Define a helper function inside `fib` and mark it `tailrec`.
- Pass the state needed for the next step through the helper's parameters.
- Use a single recursive call per step, in tail position.
- Do not use loops, mutable variables (`var`), mutable collections, or changes to external state inside your implementation.

**Hint:** Think about carrying two consecutive Fibonacci values. What should the next pair be, and how many steps remain?

The direct expression `fib(n - 1) + fib(n - 2)` follows the mathematical definition, but it does not meet the tail-recursive requirement: addition remains after the recursive calls return.

### Test Your Function

Run this test code separately from the `main` function in Lab B10.1, or combine both sets of test calls into one `main` function.

```kotlin
fun main() {
    println(fib(0))
    println(fib(1))
    println(fib(2))
    println(fib(5))
    println(fib(8))
    println(fib(10))
    println(fib(45))
}
```

Expected output:

```text
0
1
1
5
21
55
1134903170
```

### Explain Your Solution

1. Explain the meaning of each helper parameter and its initial value.
2. Identify the base case and explain why it returns the correct Fibonacci value.
3. Trace `fib(5)` by listing the helper's arguments at every call.
4. Explain why the recursive call is in tail position and how Kotlin uses the `tailrec` modifier.

## Lab B10.3: Shopping-Cart Total

**Points: 5**

An online store needs to calculate the total cost of the items in a shopping cart. Each item has a name, a unit price, and a quantity.

Write a pure function named `cartTotal` that returns the total cost using a **local tail-recursive helper**. For each item, multiply its unit price by its quantity, then include that amount in the total.

For example:

```text
2 notebooks at $3.50 each = $7.00
3 pens at $1.25 each     = $3.75
Cart total              = $10.75
```

Use `Double` prices, such as `3.50`, for this exercise. Assume prices and quantities are nonnegative. Calculate only the item total; no taxes, discounts, or delivery charges are required.

### Starter Code

Replace `TODO(...)` with your implementation. You may change the expression body to a block body so that you can define a local helper, but keep the same parameter and return types.

```kotlin
data class CartItem(
    val name: String,
    val unitPrice: Double,
    val quantity: Int
)

fun cartTotal(items: List<CartItem>): Double =
    TODO("Calculate the cart total using a local tail-recursive helper")
```

### Requirements

- Keep the public signature `cartTotal(items: List<CartItem>): Double`.
- Define a local helper marked `tailrec` that carries the current index and accumulated total as parameters.
- Process one item per recursive call, advancing toward the end of the list.
- Return `0.0` for an empty cart. An item with quantity zero contributes `0.0`.
- Do not use loops, mutable variables (`var`), mutable collections, or aggregation functions such as `sumOf`, `fold`, or `reduce` inside your implementation.
- Leave the input list and its items unchanged. Do not read or modify external state.
- Keep printing and price formatting in `main`, outside `cartTotal`.

**Hint:** The recursive helper needs to know which item comes next and the total calculated so far. What condition means that every item has been processed?

### Test Your Function

Run this test code separately from the earlier `main` functions, or combine all test calls into one `main` function.

```kotlin
fun main() {
    val cart = listOf(
        CartItem("Notebook", 3.50, 2),
        CartItem("Pen", 1.25, 3)
    )
    val originalCart = cart.toList()
    val emptyCart = emptyList<CartItem>()
    val singleItem = listOf(CartItem("Notebook", 3.50, 1))
    val zeroQuantity = listOf(CartItem("Notebook", 3.50, 0))

    println("$%.2f".format(java.util.Locale.US, cartTotal(cart)))
    println("$%.2f".format(java.util.Locale.US, cartTotal(emptyCart)))
    println("$%.2f".format(java.util.Locale.US, cartTotal(singleItem)))
    println("$%.2f".format(java.util.Locale.US, cartTotal(zeroQuantity)))

    check(cart == originalCart)
}
```

Expected output:

```text
$10.75
$0.00
$3.50
$0.00
```

`%.2f` displays a number with two decimal places. `java.util.Locale.US` makes the decimal separator a period. Formatting affects the displayed text, not the numeric value returned by `cartTotal`. The `check` call confirms that the original cart remains unchanged and produces no output when successful.

### Explain Your Solution

1. Explain the meaning of each helper parameter and its initial value.
2. Identify the base case. How does it also handle an empty cart?
3. Trace the two-item example by listing the helper's arguments at every call.
4. Explain why the recursive call is in tail position and why `cartTotal` is pure.

## Lab B10.4: Greatest Common Divisor (Hard)

**Points: 7**

The **greatest common divisor (GCD)** of two integers, not both zero, is the largest positive integer that divides both without a remainder. For example, `gcd(48, 18)` is `6`.

Read the definition, the fraction-reduction application, and the remainder-based Euclidean algorithm in [Greatest common divisor](https://en.wikipedia.org/wiki/Greatest_common_divisor).

This challenge has two parts: implement a local tail-recursive GCD function, then reuse it to simplify fractions. You will design the helper's parameters and stopping condition yourself.

### Part A: Calculate the GCD

Implement `gcd(a, b)` using the **remainder-based Euclidean algorithm**. Instead of checking every possible divisor, repeatedly replace the current pair of numbers with a smaller equivalent problem.

**Assume that `a >= 0` and `b >= 0`, and that at least one is positive.** Either input may be zero, and either input may be larger. You do not need to handle negative inputs or `gcd(0, 0)`.

```kotlin
fun gcd(a: Int, b: Int): Int =
    TODO("Implement Euclid's algorithm using a local tail-recursive helper")
```

You may change the expression body to a block body, but keep the public signature.

**Hint:** For a nonzero second argument, `gcd(a, b)` has the same value as `gcd(b, a % b)`. Kotlin's `%` operator calculates the remainder. Think about when this process must stop and which value is the answer at that point. Check the stopping condition before calculating a remainder with a zero divisor.

### Part B: Simplify a Fraction

Use your `gcd` function to implement `simplifyFraction`. Return a new `Fraction` whose numerator and denominator have no common divisor greater than `1`.

For example:

```text
48/18 = (48 / 6)/(18 / 6) = 8/3
```

**Assume the numerator is nonnegative and the denominator is positive.** Represent a zero-valued fraction as `0/1`. Keep the result as an integer numerator and denominator, rather than converting it to a decimal or mixed number.

```kotlin
data class Fraction(
    val numerator: Int,
    val denominator: Int
)

fun simplifyFraction(numerator: Int, denominator: Int): Fraction =
    TODO("Use your gcd function to return a simplified fraction")
```

### Requirements

- Keep both public function signatures and the supplied `Fraction` data class.
- Define a local helper inside `gcd` and mark it `tailrec`.
- Use one recursive call per step, in tail position. Pass the next pair of values as arguments.
- Use the remainder-based Euclidean algorithm; do not enumerate possible divisors or call a library GCD function.
- Do not use loops, mutable variables (`var`), mutable collections, or external state in either implementation.
- Make `simplifyFraction` call your `gcd` function. It does not need its own recursive helper.
- Keep printing in `main`. Both calculation functions should return values without performing I/O.

### Test Your Functions

Run this code separately from the earlier `main` functions, or combine all test calls into one `main` function.

```kotlin
fun main() {
    println(gcd(48, 18))
    println(gcd(18, 48))
    println(gcd(60, 24))
    println(gcd(17, 13))
    println(gcd(42, 42))
    println(gcd(0, 9))
    println(gcd(9, 0))

    val first = simplifyFraction(48, 18)
    val second = simplifyFraction(42, 56)
    val third = simplifyFraction(17, 13)
    val zero = simplifyFraction(0, 9)

    println("${first.numerator}/${first.denominator}")
    println("${second.numerator}/${second.denominator}")
    println("${third.numerator}/${third.denominator}")
    println("${zero.numerator}/${zero.denominator}")
}
```

Expected output:

```text
6
6
12
1
42
9
9
8/3
3/4
17/13
0/1
```

Add two tests of your own: one pair where one number divides the other, and one fraction that reduces to an integer. Express the integer result as a fraction with denominator `1`.

### Explain Your Solution

1. Identify the recursive state and the base case. Unlike the sum exercise, does this algorithm need a separate accumulator? Explain.
2. Trace `gcd(270, 192)` by listing every pair of helper arguments and the final result.
3. Explain why replacing `(a, b)` with `(b, a % b)` preserves the common divisors. Use `a = q * b + r` to support your explanation, where `q` is the quotient and `r` is the remainder.
4. Explain why the recursion terminates for the allowed inputs, including when the first input is smaller than the second.
5. Explain why the recursive call is in tail position and what `tailrec` allows Kotlin to do.
6. Explain why dividing both parts of a fraction by their GCD produces an equivalent fraction in lowest terms, including the `0/9` case.

## Submission

Submit **one Kotlin Jupyter notebook named `labb10.ipynb`** containing your work for all four exercises. Use the `.ipynb` extension.

Organize the notebook with Markdown section headings labeled **Lab B10.1**, **Lab B10.2**, **Lab B10.3**, and **Lab B10.4**.

For each section, include:

- **Kotlin code cells** containing the completed functions and any required data classes.
- **Executed test cells with visible output** for every provided test. For Lab B10.4, also include the two additional tests requested in the exercise.
- **Markdown cells** containing the requested recursive trace and answers to every question under “Explain Your Solution.”

Use a Kotlin kernel to execute the notebook. The supplied test programs use `main`; in a notebook, you may place the test statements directly in code cells. If you keep a `main` function, explicitly call it to produce its output. Keep test definitions organized so the notebook runs from top to bottom without conflicting declarations.

Before submitting, restart the kernel, run all cells in order, and save the notebook with its actual outputs visible. Replace all `____` and `TODO(...)` placeholders in your submitted solutions.

## Grading: 20 Points

Implementation points include following each exercise's required functional style and local `tailrec` helper requirements. Testing points require actual notebook output, not copied expected output.

| Exercise | Criteria | Points |
|---|---|---:|
| **Lab B10.1: A Recursive Sum** | Correct completed tail-recursive implementation (1); all provided tests with actual output (1); recursive trace and complete explanations (1). | **3** |
| **Lab B10.2: Tail-Recursive Fibonacci** | Correct local tail-recursive implementation, including initial state, base case, and state updates (3); all provided tests with actual output (1); recursive trace and complete explanations (1). | **5** |
| **Lab B10.3: Shopping-Cart Total** | Correct pure, local tail-recursive implementation that handles all required cart cases and leaves the input unchanged (3); all provided tests with actual output and the unchanged-cart check (1); recursive trace and complete explanations (1). | **5** |
| **Lab B10.4: Greatest Common Divisor (Hard)** | Correct local tail-recursive Euclidean algorithm for all allowed inputs (3); correct fraction simplification using `gcd`, including zero numerators (2); all provided and two additional tests with actual output (1); recursive trace and complete explanations of correctness, termination, and tail position (1). | **7** |
| **Total** | | **20** |
