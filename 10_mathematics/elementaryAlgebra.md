# Elementary Algebra - Complete Notes

## Table of Contents
1. [Core Concepts](#core-concepts)
2. [Basic Operations](#basic-operations)
3. [Simplifying Expressions](#simplifying-expressions)
4. [Solving Equations](#solving-equations)
5. [Inequalities](#inequalities)
6. [Functions and Graphs](#functions-and-graphs)
7. [Systems of Equations](#systems-of-equations)
8. [Applications in Data Science](#applications-in-data-science)
9. [Practice Exercises](#practice-exercises)

---

## Core Concepts

### Variables
- **Definition**: A symbol (usually a letter like x, y, z) that represents an unknown number
- **Example**: In `x + 5 = 10`, 'x' is a variable
- **Data Science Connection**: Variables represent features in datasets (age, income, temperature, etc.)

### Constants
- **Definition**: Fixed values that don't change
- **Examples**: Numbers like 3, -7, 15.5
- **In expressions**: In `7y + 4`, the number 4 is a constant

### Coefficients
- **Definition**: The numerical factor of a term containing a variable
- **Example**: In `3x`, the coefficient is 3
- **Special cases**: 
  - In `x`, the coefficient is 1 (implied)
  - In `-x`, the coefficient is -1

### Terms
- **Definition**: Single numbers, variables, or products of numbers and variables
- **Examples**: 
  - `5x` (one term)
  - `3x + 2y - 7` (three terms: 3x, 2y, -7)

### Expressions vs Equations
- **Expression**: Mathematical phrase without equals sign
  - Example: `2x + 5`
- **Equation**: Two expressions connected by equals sign
  - Example: `2x + 5 = 11`

### Fractions in Algebra
- **Numerator**: Top part of fraction
- **Denominator**: Bottom part of fraction
- **Example**: In `3/4`, numerator = 3, denominator = 4

---

## Basic Operations

### Addition
```
3x + 2x = 5x
x + 7 = x + 7
```

### Subtraction
```
5x - 2x = 3x
10 - y = 10 - y
```

### Multiplication
```
3 × x = 3x
2(x + 3) = 2x + 6
```

### Division
```
6x ÷ 2 = 3x
x/4 = x ÷ 4
```

---

## Simplifying Expressions

### Combining Like Terms
**Rule**: Only combine terms with the same variable and same power

**Examples**:
- `3x + 2x = 5x` ✅
- `3x + 2y` cannot be simplified ❌
- `4x² + 2x²= 6x²` ✅
- `4x² + 2x` cannot be simplified ❌

### Distributive Property
**Formula**: `a(b + c) = ab + ac`

**Examples**:
- `2(x + 3) = 2x + 6`
- `3(2y - 4) = 6y - 12`
- `-(x + 5) = -x - 5`

### Order of Operations (PEMDAS/BODMAS)
1. **P**arentheses/(**B**rackets)
2. **E**xponents/(**O**rders)
3. **M**ultiplication and **D**ivision (left to right)
4. **A**ddition and **S**ubtraction (left to right)

---

## Solving Equations

### Linear Equations (One Variable)
**Goal**: Isolate the variable on one side

**Steps**:
1. Simplify both sides
2. Move variable terms to one side
3. Move constants to other side
4. Divide by coefficient of variable

**Example**: Solve `3x + 7 = 22`
```
3x + 7 = 22
3x = 22 - 7    (subtract 7 from both sides)
3x = 15
x = 15/3       (divide both sides by 3)
x = 5
```

**Check**: `3(5) + 7 = 15 + 7 = 22` ✅

### More Complex Examples
**Example 1**: Solve `2(x - 3) = 4x + 2`
```
2(x - 3) = 4x + 2
2x - 6 = 4x + 2      (distribute)
2x - 4x = 2 + 6      (collect like terms)
-2x = 8
x = -4
```

**Example 2**: Solve `(x + 5)/3 = 7`
```
(x + 5)/3 = 7
x + 5 = 21           (multiply both sides by 3)
x = 21 - 5
x = 16
```

---

## Inequalities

### Basic Inequality Symbols
- `>` : greater than
- `<` : less than  
- `≥` : greater than or equal to
- `≤` : less than or equal to

### Solving Inequalities
**Same rules as equations, BUT**: When multiplying or dividing by a negative number, flip the inequality sign!

**Example 1**: Solve `2x + 3 > 11`
```
2x + 3 > 11
2x > 11 - 3
2x > 8
x > 4
```

**Example 2**: Solve `-3x + 5 ≤ 14`
```
-3x + 5 ≤ 14
-3x ≤ 14 - 5
-3x ≤ 9
x ≥ -3           (flip the sign when dividing by -3)
```

---

## Functions and Graphs

### Function Notation
- `f(x)` reads as "f of x"
- `f(x) = 2x + 3` means "function f takes input x and outputs 2x + 3"

### Evaluating Functions
If `f(x) = 2x + 3`, find `f(4)`:
```
f(4) = 2(4) + 3 = 8 + 3 = 11
```

### Linear Functions
**Standard Form**: `y = mx + b`
- `m` = slope (rate of change)
- `b` = y-intercept (where line crosses y-axis)

**Example**: `y = 2x + 3`
- Slope = 2 (line rises 2 units for every 1 unit right)
- Y-intercept = 3 (line crosses y-axis at point (0,3))

### Finding Intercepts
**Y-intercept**: Set x = 0
- For `y = 2x + 3`: y-intercept = 3

**X-intercept**: Set y = 0
- For `y = 2x + 3`: `0 = 2x + 3`, so `x = -3/2`

---

## Systems of Equations

### What is a System?
A set of equations with the same variables that must be solved together.

**Example**:
```
x + y = 7
x - y = 1
```

### Solution Methods

#### 1. Substitution Method
**Steps**:
1. Solve one equation for one variable
2. Substitute into the other equation
3. Solve for remaining variable
4. Find the other variable

**Example**:
```
x + y = 7    ... (1)
x - y = 1    ... (2)

From (2): x = y + 1
Substitute into (1): (y + 1) + y = 7
                     2y + 1 = 7
                     2y = 6
                     y = 3

Substitute back: x = 3 + 1 = 4
Solution: (4, 3)
```

#### 2. Elimination Method
**Steps**:
1. Make coefficients of one variable the same (multiply if needed)
2. Add or subtract equations to eliminate one variable
3. Solve for remaining variable
4. Substitute back to find other variable

**Example**:
```
x + y = 7    ... (1)
x - y = 1    ... (2)

Add equations: (x + y) + (x - y) = 7 + 1
               2x = 8
               x = 4

Substitute: 4 + y = 7
           y = 3
Solution: (4, 3)
```

#### 3. Graphical Method
- Plot both equations on same graph
- Solution is where lines intersect
- Can have: one solution, no solution, or infinite solutions

---

## Applications in Data Science

### Linear Regression
Uses the equation `y = mx + b` to predict outcomes:
- `x` = input feature (age, experience, etc.)
- `y` = predicted output (salary, price, etc.)
- `m` = how much y changes per unit change in x
- `b` = baseline value when x = 0

### Data Modeling Examples
1. **Sales Prediction**: `Sales = 1000 + 50 × Advertising_Budget`
2. **Temperature Conversion**: `F = (9/5)C + 32`
3. **Cost Analysis**: `Total_Cost = Fixed_Cost + Variable_Cost × Units`

---

## Practice Exercises

### Level 1: Basic Operations
1. Simplify: `5x + 3x`
2. Simplify: `8y - 3y`
3. Simplify: `2(x + 4)`
4. Simplify: `3(2y - 1)`
5. Combine like terms: `4x + 2y + 3x - y`

### Level 2: Solving Equations
1. Solve: `x + 8 = 15`
2. Solve: `3x = 21`
3. Solve: `2x + 5 = 13`
4. Solve: `4x - 7 = 9`
5. Solve: `2(x + 3) = 14`

### Level 3: Inequalities
1. Solve: `x + 4 > 10`
2. Solve: `2x ≤ 12`
3. Solve: `3x - 5 < 7`
4. Solve: `-2x + 3 ≥ 9`
5. Solve: `5 - x > 2`

### Level 4: Functions
Given `f(x) = 3x - 2`, find:
1. `f(0)`
2. `f(4)`
3. `f(-1)`
4. The value of x when `f(x) = 10`

Given `g(x) = x² + 2x`, find:
5. `g(2)`
6. `g(-3)`

### Level 5: Systems of Equations
Solve using substitution method:
1. ```
   x + y = 9
   x - y = 3
   ```

2. ```
   2x + y = 8
   x - y = 1
   ```

Solve using elimination method:
3. ```
   3x + 2y = 12
   x + 2y = 8
   ```

4. ```
   2x + 3y = 7
   4x - 3y = 5
   ```

### Level 6: Word Problems
1. **Age Problem**: Sarah is 3 years older than Tom. The sum of their ages is 27. How old is each person?

2. **Cost Problem**: A company's total cost is $500 plus $20 per item produced. Write an equation and find the cost for producing 15 items.

3. **Distance Problem**: Two cars start from the same point. One travels at 60 mph, the other at 80 mph in the opposite direction. After how many hours will they be 350 miles apart?

---

## Answer Key

### Level 1 Answers:
1. `8x`
2. `5y`
3. `2x + 8`
4. `6y - 3`
5. `7x + y`

### Level 2 Answers:
1. `x = 7`
2. `x = 7`
3. `x = 4`
4. `x = 4`
5. `x = 4`

### Level 3 Answers:
1. `x > 6`
2. `x ≤ 6`
3. `x < 4`
4. `x ≤ -3`
5. `x < 3`

### Level 4 Answers:
1. `f(0) = -2`
2. `f(4) = 10`
3. `f(-1) = -5`
4. `x = 4`
5. `g(2) = 8`
6. `g(-3) = 3`

### Level 5 Answers:
1. `x = 6, y = 3`
2. `x = 3, y = 2`
3. `x = 2, y = 3`
4. `x = 2, y = 1`

### Level 6 Answers:
1. Tom = 12 years, Sarah = 15 years
2. Equation: `C = 500 + 20n`; Cost for 15 items = $800
3. After 2.5 hours

---

## Key Formulas Reference

### Linear Equation: `y = mx + b`
- `m` = slope
- `b` = y-intercept

### Slope Formula: `m = (y₂ - y₁)/(x₂ - x₁)`

### Distance Formula: `d = √[(x₂-x₁)² + (y₂-y₁)²]`

### Quadratic Formula: `x = (-b ± √(b²-4ac))/2a`

---

## Common Mistakes to Avoid

1. **Sign Errors**: Be careful with negative signs
   - Wrong: `-(x + 3) = -x + 3`
   - Right: `-(x + 3) = -x - 3`

2. **Inequality Direction**: Flip sign when multiplying/dividing by negative
   - Wrong: `-2x > 6` → `x > -3`
   - Right: `-2x > 6` → `x < -3`

3. **Like Terms**: Only combine terms with same variables and powers
   - Wrong: `3x + 2y = 5xy`
   - Right: `3x + 2y` cannot be simplified

4. **Order of Operations**: Follow PEMDAS/BODMAS
   - Wrong: `2 + 3 × 4 = 20`
   - Right: `2 + 3 × 4 = 14`

---

## Study Tips

### For Mastery:
1. **Practice Daily**: 15-20 minutes of problem solving
2. **Check Your Work**: Always substitute answers back
3. **Understand, Don't Memorize**: Focus on why methods work
4. **Use Real Examples**: Connect algebra to everyday situations
5. **Visual Learning**: Draw graphs and diagrams when possible

### Common Study Sequence:
1. Master basic operations first
2. Move to simple equations
3. Practice with inequalities
4. Learn function notation
5. Tackle systems of equations
6. Apply to word problems

---

## Quick Reference

### Solving Equations Checklist:
- [ ] Simplify both sides
- [ ] Collect like terms
- [ ] Isolate variable term
- [ ] Divide by coefficient
- [ ] Check solution

### Function Evaluation Steps:
- [ ] Identify the function rule
- [ ] Substitute given value for variable
- [ ] Follow order of operations
- [ ] Simplify to get answer

### Systems Strategy:
- [ ] Choose substitution or elimination
- [ ] Solve for one variable
- [ ] Substitute to find other variable
- [ ] Check solution in both original equations

---

*Remember: Algebra is the foundation of data science. Master these basics and you'll be ready for advanced topics like linear regression, optimization, and machine learning algorithms!*