# Lab A9 Solutions

## Lab A9.1: Replace the First Element of a List

### Solution

```kotlin
fun <T> setHead(xs: List<T>, x: T): List<T> =
    listOf(x) + xs.drop(1)

fun main() {
    val numbers = listOf(1, 2, 3)
    val updatedNumbers = setHead(numbers, 9)
    println(updatedNumbers)
    println(numbers)

    val animals = listOf("Cat", "Dog", "Fish")
    println(setHead(animals, "Bird"))

    val singleItem = listOf(true)
    println(setHead(singleItem, false))

    // Confirm that these original lists also remain unchanged.
    println("Animals after call: $animals")
    println("Single item after call: $singleItem")

    // Additional Double example.
    val doubles = listOf(1.5, 2.5, 3.5)
    val replacement = 9.5
    println("Original: $doubles")
    println("Replacement: $replacement")

    val updatedDoubles = setHead(doubles, replacement)
    println("Returned: $updatedDoubles")
    println("Original after call: $doubles")

    check(updatedDoubles.first() == replacement)
    check(updatedDoubles.size == doubles.size)
    check(updatedDoubles.drop(1) == doubles.drop(1))
    check(doubles == listOf(1.5, 2.5, 3.5))
}
```

### Expected Output

```text
[9, 2, 3]
[1, 2, 3]
[Bird, Dog, Fish]
[false]
Animals after call: [Cat, Dog, Fish]
Single item after call: [true]
Original: [1.5, 2.5, 3.5]
Replacement: 9.5
Returned: [9.5, 2.5, 3.5]
Original after call: [1.5, 2.5, 3.5]
```

The `check` calls produce no output when their conditions are true.

### Explanation

`T` is a type parameter. It plays the same role as `A` in the starter code; changing its name does not change the function's behavior or parameter structure. `xs` has type `List<T>`, `x` has type `T`, and the function returns `List<T>`.

`listOf(x)` creates a list containing the replacement value. `xs.drop(1)` returns the original list's elements after the first, in their original order. The `+` operator combines these into a new list without changing `xs`.

For a nonempty list of size `n`, the result contains one replacement element and `n - 1` remaining elements, so its size is still `n`. For a singleton list, the tail is empty and the result contains only the replacement.

### Reflection

Prediction: this call does **not compile**. Check it separately from the successful examples.

```kotlin
setHead<Int>(listOf(1, 2, 3), "nine")
```

Expected compiler result: an argument type mismatch because the replacement is a `String`, but an `Int` is required.

Explicitly specifying `<Int>` fixes `T` as `Int`, so the function requires `xs: List<Int>` and `x: Int`, and returns `List<Int>`. This corrected call is valid:

```kotlin
setHead<Int>(listOf(1, 2, 3), 9)
```

Without an explicit type argument, Kotlin can infer a common supertype for mixed arguments; explicitly choosing `<Int>` prevents that broader inference.

*The output and compiler result above are expected results, not captured compiler output; this solution has not been run in a Kotlin environment.*

## Lab A9.2: Be the Compiler

### Prediction and Compiler Results

Each original class and each correction below was compiled separately using **Kotlin/JVM 2.3.20**. All predictions matched the compiler results. Successful compilations produced no output or warnings.

| Class | Prediction: compiles? | Actual compiler result | Explanation |
|---|---|---|---|
| A | Yes | Compiles | `T` is used as a plain constructor parameter and a function parameter. These uses are allowed with `in T`. |
| B | No | Compilation error | `val x = t` exposes a public getter returning `T`, an output position that conflicts with `in T`. |
| C | No | Compilation error | `fun myFunction(): T` returns `T`, an output position that conflicts with `in T`. |
| E | No | Compilation error | `var y = t` exposes both a getter and a setter, placing `T` in an invariant position. Its getter conflicts with `in T`. |

`in T` declares **contravariance**: the class can accept values of type `T` through its public API, but cannot expose values of type `T` as outputs. A public `val` has a getter, and a public `var` has both a getter and a setter. The getter returns a value, even when it is not written explicitly in the source code.

### Class A: Compiles

```kotlin
class A<in T>(t: T) {
    fun myFunction(t: T) { }
}
```

The constructor accepts `t: T`, and `myFunction` also accepts `t: T`. Neither exposes `T` as a return type or public property. No correction is needed. Unused parameters do not make the code invalid.

### Class B: Does Not Compile

The offending declaration is `val x = t`. Kotlin infers the property's type as `T`, and its public getter returns `T`.

Actual compiler diagnostic excerpt:

```text
B.kt:2:5: error: type parameter 'T' is declared as 'in' but occurs in 'out' position in type 'T (of class B<in T>)'.
    val x = t
    ^^^^^
```

Correction:

```kotlin
class B<T>(t: T) {
    val x = t

    fun myFunction(t: T) { }
}
```

Removing `in` makes `T` **invariant**, allowing the class to accept `T` in a method and return `T` through the property getter. This correction compiles. It does **not** preserve contravariance.

### Class C: Does Not Compile

The offending declaration is `fun myFunction(): T`: its return type exposes `T` as an output.

Actual compiler diagnostic excerpt:

```text
C.kt:2:23: error: type parameter 'T' is declared as 'in' but occurs in 'out' position in type 'T (of class C<in T>)'.
    fun myFunction(): T = TODO("Not implemented")
                      ^
```

Correction:

```kotlin
abstract class C<out T> {
    fun myFunction(): T = TODO("Not implemented")
}
```

Changing `in` to `out` makes `T` **covariant**, allowing the method to return `T`. This correction compiles. It does **not** preserve contravariance; it changes the class to covariance.

The lab's `TODO(...)` is a valid placeholder body for this compilation exercise, but it throws if the method is called. An empty body `{ }`, as shown in the reference image, would also need a return value; retaining the lab's `TODO(...)` avoids that separate error.

### Class E: Does Not Compile

The offending declaration is `var y = t`. Its getter returns `T`, while its setter accepts `T`. The setter is compatible with `in T`, but the getter is not, so the public mutable property conflicts with contravariance.

Actual compiler diagnostic excerpt:

```text
E.kt:2:5: error: type parameter 'T' is declared as 'in' but occurs in 'invariant' position in type 'T (of class E<in T>)'.
    var y = t
    ^^^^^
```

Correction:

```kotlin
class E<T>(t: T) {
    var y = t

    fun myFunction(t: T) { }
}
```

Removing `in` makes `T` **invariant**, allowing both the getter and setter. This correction compiles. It does **not** preserve contravariance.

The diagnostics above retain the compiler's wording; temporary directory prefixes have been omitted from the filenames.

## Lab A9.3: Sharpen Your Pencil

### Prediction and Compiler Results

In the original code, `Seller<T>` and `Consumer<T>` are **invariant**. Although `VeganFood` is a subtype of `Food`, this does not automatically create a subtype relationship between their invariant generic interfaces.

| Assignment | Prediction: compiles? | Actual compiler result | Explanation |
|---|---|---|---|
| `foodSeller = FoodSeller()` | Yes | Accepted | `FoodSeller` implements the required `Seller<Food>`. |
| `foodSeller = VeganFoodSeller()` | No | Compilation error | `VeganFoodSeller` implements `Seller<VeganFood>`, which is not a subtype of `Seller<Food>` when `Seller` is invariant. |
| `veganFoodConsumer = Vegan()` | Yes | Accepted | `Vegan` implements the required `Consumer<VeganFood>`. |
| `veganFoodConsumer = Person()` | No | Compilation error | `Person` implements `Consumer<Food>`, which is not a subtype of `Consumer<VeganFood>` when `Consumer` is invariant. |

The original file was compiled using **Kotlin/JVM 2.3.20**. Compilation failed with these two errors; the results matched the predictions.

### Original Compiler Errors

Actual diagnostic excerpts, with temporary directory prefixes omitted:

```text
Original.kt:23:16: error: assignment type mismatch: actual type is 'VeganFoodSeller', but 'Seller<Food>' was expected.
    foodSeller = VeganFoodSeller()
               ^
Original.kt:27:23: error: assignment type mismatch: actual type is 'Person', but 'Consumer<VeganFood>' was expected.
    veganFoodConsumer = Person()
                      ^
```

### Corrected Complete Code

Only two definitions need to change:

```kotlin
interface Seller<out T>
interface Consumer<in T>
```

The complete corrected listing is below. The `main` function, food inheritance relationship, and implementing classes' type arguments are unchanged.

```kotlin
// Food types
open class Food

class VeganFood : Food()

// Sellers
interface Seller<out T>

class FoodSeller : Seller<Food>

class VeganFoodSeller : Seller<VeganFood>

// Consumers
interface Consumer<in T>

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

**Verification:** The corrected file compiled successfully with Kotlin/JVM 2.3.20, exit code 0, with no compiler output or warnings. The program has no print statements, so it has no console output. Unused-variable or unused-parameter warnings, if reported by another compiler or IDE, are separate from type errors.

### Explanation of the Changes

**1. Rejected assignments and required types**

`VeganFoodSeller()` has type `VeganFoodSeller` and implements `Seller<VeganFood>`. The variable `foodSeller` requires `Seller<Food>`. The original invariant `Seller<T>` does not permit this assignment.

`Person()` has type `Person` and implements `Consumer<Food>`. The variable `veganFoodConsumer` requires `Consumer<VeganFood>`. The original invariant `Consumer<T>` does not permit this assignment.

**2. Variance and subtype relationships**

`Seller<out T>` is **covariant**. It preserves the subtype direction: because `VeganFood` is a subtype of `Food`, `Seller<VeganFood>` is a subtype of `Seller<Food>`. A seller that provides vegan food can satisfy a request for a seller of food, because vegan food is food. This makes `foodSeller = VeganFoodSeller()` valid.

`Consumer<in T>` is **contravariant**. It reverses the subtype direction: because `VeganFood` is a subtype of `Food`, `Consumer<Food>` is a subtype of `Consumer<VeganFood>`. A consumer that accepts any food can also accept vegan food. This makes `veganFoodConsumer = Person()` valid.

**3. Possible future interface methods**

A method such as `fun sell(): T` fits `Seller<out T>` because it returns `T`, placing the type parameter in an output position.

A method such as `fun consume(food: T)` fits `Consumer<in T>` because it accepts `T`, placing the type parameter in an input position.

These method signatures agree with the chosen variance. If added as abstract interface methods, they would also require implementations in the corresponding seller and consumer classes.
