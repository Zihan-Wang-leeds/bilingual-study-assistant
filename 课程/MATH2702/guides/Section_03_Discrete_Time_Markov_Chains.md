# Section 3: Discrete Time Markov Chains

> MATH2702 Stochastic Processes - 自学教材
> 生成时间: 2026-07-17 14:45
> 来源页: 19-21

---

Here is the comprehensive, bilingual self-study guide for the section on Discrete Time Markov Chains, created from the provided raw course material.

---

### 📋 Section Overview / 章节概览

This section introduces **Discrete Time Markov Chains (离散时间马尔可夫链)**. These are a fundamental class of stochastic processes (随机过程) used to model systems that change randomly over time, where the future depends only on the present state, not the past. This is known as the **Markov property (马尔可夫性)**.

We will learn how to formally define a Markov chain, how to calculate the probabilities of moving between states over multiple time steps, and the powerful **Chapman–Kolmogorov equations (查普曼-科尔莫戈罗夫方程)** that govern these calculations. This is the core theoretical foundation for many models in finance, engineering, computer science, and physics.

### 🎯 Learning Objectives / 学习目标

By the end of this section, you will be able to:

1.  **Define** a time-homogeneous discrete-time Markov chain using its initial distribution and transition probabilities.
2.  **Construct** and interpret a transition matrix **P** and a transition diagram.
3.  **Calculate** multi-step transition probabilities by conditioning on the first step and using matrix multiplication.
4.  **State and apply** the Chapman–Kolmogorov equations.
5.  **Compute** the distribution of the chain after `n` steps using the initial distribution and `Pⁿ`.

### 📚 Prerequisites / 前置知识

Before starting this section, you should be comfortable with:

- **Basic Probability (基础概率论)**: Conditional probability (条件概率) `ℙ(A|B)`, the law of total probability (全概率公式), and probability distributions (概率分布).
- **Matrix Algebra (矩阵代数)**: Matrix multiplication (矩阵乘法), and the concept of a row vector (行向量).
- **Summation Notation (求和符号)**: Understanding `∑` notation.

### 📖 Core Content / 核心内容

---

#### Topic 1: Definition of a Time-Homogeneous Markov Chain (时间齐次马尔可夫链的定义)

**Intuition / 直觉理解**

Imagine a frog jumping between lily pads in a pond. The frog's position at each second is a random process. The **Markov property (马尔可夫性)** means that the frog's next jump depends *only* on which lily pad it is sitting on *right now*. It doesn't matter how it got there—whether it came from the left or the right, or if it was tired from a long jump. The future is independent of the past, given the present.

A **time-homogeneous (时间齐次)** chain means the frog's jumping rules don't change over time. The probability of jumping from pad `i` to pad `j` is the same on Monday, Tuesday, and every other day.

**Formal Definition / 形式化定义**

A **time-homogeneous discrete-time Markov chain (时间齐次离散时间马尔可夫链)** is a sequence of random variables `(Xₙ)`, where `n = 0, 1, 2, ...`, defined by two components:

1.  **Initial Distribution (初始分布)**: A probability distribution `(λᵢ)` over the state space `𝒮`.
    - `λᵢ = ℙ(X₀ = i)` is the probability that the chain starts in state `i`.
    - `λᵢ ≥ 0` for all `i`, and `∑ᵢ λᵢ = 1`.

2.  **Transition Probabilities (转移概率)**: A set of numbers `pᵢⱼ`, where `i, j ∈ 𝒮`.
    - `pᵢⱼ = ℙ(Xₙ₊₁ = j | Xₙ = i)` is the probability of moving from state `i` to state `j` in one step.
    - **Key Property (关键性质)**: This probability does **not** depend on `n` (this is the "time-homogeneous" part).
    - **Constraints (约束条件)**:
        - `pᵢⱼ ≥ 0` for all `i, j`.
        - `∑ⱼ pᵢⱼ = 1` for every state `i`. This means from any state `i`, you must go to *some* state (including possibly itself) with probability 1.

The Markov property is formally stated as:
`ℙ(Xₙ₊₁ = j | Xₙ = i, Xₙ₋₁ = xₙ₋₁, ..., X₀ = x₀) = ℙ(Xₙ₊₁ = j | Xₙ = i) = pᵢⱼ`

**Notation (符号)**: Sometimes `p(i, j)` is written instead of `pᵢⱼ` for readability, especially when the state indices are complex.

**Transition Matrix (转移矩阵) P**

When the state space `𝒮` is finite, we can arrange the transition probabilities into a matrix **P**.
- The entry in row `i`, column `j` is `pᵢⱼ`.
- **P** is a **stochastic matrix (随机矩阵)** because every row sums to 1.

**Example: Simple Random Walk (简单随机游走)**
- State space `𝒮 = {..., -2, -1, 0, 1, 2, ...}` (all integers).
- Initial distribution: `λ₀ = 1`, and `λᵢ = 0` for all `i ≠ 0`. (Starts at 0 with certainty).
- Transition probabilities:
    - `pᵢ,ᵢ₊₁ = p` (probability to move right)
    - `pᵢ,ᵢ₋₁ = q` (probability to move left), where `p + q = 1`.
    - `pᵢⱼ = 0` for all other `j`.

---

#### Topic 2: Calculating Joint and Conditional Probabilities (计算联合与条件概率)

**Intuition / 直觉理解**

We can use the Markov property and the chain rule of probability to calculate the probability of a specific sequence of states. The probability of a path is just the product of the probabilities of each step along the path.

**Formal Definition / 形式化定义**

**Example 3.1 (from text):**
1.  **What is `ℙ(X₀ = i and X₁ = j)`?**
    This is the probability of starting at `i` and then moving to `j`.
    `ℙ(X₀ = i and X₁ = j) = ℙ(X₀ = i) * ℙ(X₁ = j | X₀ = i) = λᵢ * pᵢⱼ`

2.  **What is `ℙ(Xₙ₊₂ = j and Xₙ₊₁ = k | Xₙ = i)`?**
    This is the probability of being at `i` now, moving to `k` next, and then to `j` the step after.
    `ℙ(Xₙ₊₂ = j and Xₙ₊₁ = k | Xₙ = i)`
    `= ℙ(Xₙ₊₁ = k | Xₙ = i) * ℙ(Xₙ₊₂ = j | Xₙ₊₁ = k, Xₙ = i)`
    `= ℙ(Xₙ₊₁ = k | Xₙ = i) * ℙ(Xₙ₊₂ = j | Xₙ₊₁ = k)` (by Markov property)
    `= pᵢₖ * pₖⱼ`

---

#### Topic 3: A Two-State Example (两状态例子)

**Intuition / 直觉理解**

This is the simplest possible Markov chain. It models a system that can be in one of two states, like a printer that is either "Broken (0)" or "Working (1)". The probabilities of switching between states are constant.

**Formal Definition / 形式化定义**

- **State Space**: `𝒮 = {0, 1}`
- **Transition Matrix**:
    `P = ( p₀₀  p₀₁ ) = ( 1-α   α  )`
    `    ( p₁₀  p₁₁ )   (  β   1-β )`
    where `0 < α, β < 1`.
    - `α = ℙ(Xₙ₊₁ = 1 | Xₙ = 0)`: Probability a broken printer is fixed by tomorrow.
    - `β = ℙ(Xₙ₊₁ = 0 | Xₙ = 1)`: Probability a working printer breaks by tomorrow.

- **Transition Diagram (转移图)**:
    ```
        0 <--------> 1
        |  α         |  β
        | 1-α        | 1-β
    ```
    (Arrows from 0 to 0 with `1-α`, 0 to 1 with `α`, 1 to 0 with `β`, 1 to 1 with `1-β`)

**Worked Example / 例题**

**Example 3.2 (from text): The Broken Printer**
If the printer is working on Monday, what is the probability it is also working on Wednesday?

- **Step 1: Define the problem.**
    Let Monday be time `n`. Wednesday is time `n+2`. We want the **two-step transition probability** `p₁₁(2) = ℙ(Xₙ₊₂ = 1 | Xₙ = 1)`.

- **Step 2: Condition on the first step (Tuesday).**
    The key is to think about the state of the printer on Tuesday (`Xₙ₊₁`). It can be either 0 (broken) or 1 (working). We use the Law of Total Probability:
    `p₁₁(2) = ℙ(Xₙ₊₂ = 1 | Xₙ = 1)`
    `= ℙ(Xₙ₊₁ = 0 | Xₙ = 1) * ℙ(Xₙ₊₂ = 1 | Xₙ₊₁ = 0, Xₙ = 1)`
    `+ ℙ(Xₙ₊₁ = 1 | Xₙ = 1) * ℙ(Xₙ₊₂ = 1 | Xₙ₊₁ = 1, Xₙ = 1)`

- **Step 3: Apply the Markov property.**
    The Markov property says the future (`Xₙ₊₂`) depends only on the present (`Xₙ₊₁`), not the past (`Xₙ`). So:
    `ℙ(Xₙ₊₂ = 1 | Xₙ₊₁ = 0, Xₙ = 1) = ℙ(Xₙ₊₂ = 1 | Xₙ₊₁ = 0) = p₀₁ = α`
    `ℙ(Xₙ₊₂ = 1 | Xₙ₊₁ = 1, Xₙ = 1) = ℙ(Xₙ₊₂ = 1 | Xₙ₊₁ = 1) = p₁₁ = 1-β`

- **Step 4: Substitute the known probabilities.**
    `ℙ(Xₙ₊₁ = 0 | Xₙ = 1) = p₁₀ = β`
    `ℙ(Xₙ₊₁ = 1 | Xₙ = 1) = p₁₁ = 1-β`
    Therefore:
    `p₁₁(2) = (β) * (α) + (1-β) * (1-β)`
    `p₁₁(2) = βα + (1-β)²`

- **Step 5: Interpret the result.**
    The probability is the sum of probabilities of all length-2 paths from state 1 to state 1:
    - Path `1 → 0 → 1`: probability `β * α`
    - Path `1 → 1 → 1`: probability `(1-β) * (1-β)`

---

#### Topic 4: n-Step Transition Probabilities and Chapman–Kolmogorov Equations (n步转移概率与查普曼-科尔莫戈罗夫方程)

**Intuition / 直觉理解**

The idea of "conditioning on the first step" can be extended to any number of steps. To find the probability of going from `i` to `j` in `n` steps, you sum over all possible intermediate states. This process is exactly the same as matrix multiplication.

**Formal Definition / 形式化定义**

- **n-step transition probability (n步转移概率)**: `pᵢⱼ(n) = ℙ(Xₙ = j | X₀ = i)`. This is the probability of being in state `j` exactly `n` steps after starting in state `i`.

**Theorem 3.1 (Theorem 3.1)**
Let `(Xₙ)` be a Markov chain with state space `𝒮` and transition matrix `P = (pᵢⱼ)`. Then:
`pᵢⱼ(n) = ∑_{k₁, k₂, ..., kₙ₋₁ ∈ 𝒮} p_{i,k₁} * p_{k₁,k₂} * ... * p_{kₙ₋₂,kₙ₋₁} * p_{kₙ₋₁,j}`

**In particular, `pᵢⱼ(n)` is the `(i, j)`-th element of the matrix `Pⁿ`.** The matrix of n-step transition probabilities is `P(n) = Pⁿ`.

**Proof / 证明 (Conceptual)**
This is proven by induction. We already showed it's true for `n=2`:
`pᵢⱼ(2) = ∑ₖ pᵢₖ * pₖⱼ`, which is the `(i,j)` entry of `P²`.
For `n=3`, we condition on the state after the first step (`k`), and then use the `n=2` result for the remaining two steps:
`pᵢⱼ(3) = ∑ₖ pᵢₖ * pₖⱼ(2) = ∑ₖ pᵢₖ * (P²)ₖⱼ = (P³)ᵢⱼ`.
This logic continues for any `n`.

**Theorem 3.2: Chapman–Kolmogorov Equations (查普曼-科尔莫戈罗夫方程)**
Let `(Xₙ)` be a Markov chain with state space `𝒮` and transition matrix `P = (pᵢⱼ)`. Then, for non-negative integers `n, m`:
`pᵢⱼ(n+m) = ∑_{k ∈ 𝒮} pᵢₖ(n) * pₖⱼ(m)`

In matrix notation: `P(n+m) = P(n) * P(m)`

**Proof / 证明**
Since `P(n) = Pⁿ` and `P(m) = Pᵐ`, we have:
`P(n+m) = Pⁿ⁺ᵐ = Pⁿ * Pᵐ = P(n) * P(m)`.
The equation `pᵢⱼ(n+m) = ∑ₖ pᵢₖ(n) * pₖⱼ(m)` is simply the formula for the `(i,j)` entry of the matrix product `Pⁿ * Pᵐ`.

**Interpretation (解释)**: A journey of `n+m` steps from `i` to `j` can be thought of as a journey of `n` steps from `i` to some intermediate state `k`, followed by a journey of `m` steps from `k` to `j`. We sum over all possible intermediate states `k`.

**Worked Example / 例题**

**Example 3.3 (from text): Two-State Chain Matrix Power**
For our two-state printer example, the matrix of two-step transition probabilities is:
`P(2) = P² = ( 1-α   α  ) * ( 1-α   α  )`
`           (  β   1-β )   (  β   1-β )`

`P(2) = ( (1-α)² + αβ      (1-α)α + α(1-β) )`
`       ( β(1-α) + (1-β)β    βα + (1-β)²   )`

Notice the bottom-right entry is `βα + (1-β)²`, which is exactly the `p₁₁(2)` we calculated in Example 3.2.

**Distribution after n steps (n步后的分布)**
If we represent the initial distribution as a row vector `λ = (λᵢ)`, then the distribution of the chain after 1 step is:
`ℙ(X₁ = j) = ∑ᵢ λᵢ * pᵢⱼ`
This is the `j`-th element of the vector-matrix product `λP`.
More generally, the row vector of probabilities after `n` steps is given by `λPⁿ`.

---

### 🔗 Connections / 知识关联

- **Previous Topics (先前主题)**: This section formalizes the intuition from earlier examples of stochastic processes like the simple random walk. The Markov property is the key concept that makes these processes tractable.
- **Future Topics (未来主题)**: This theory is the foundation for the next section on the **Gambler's Ruin (赌徒破产)** problem, which is a specific application of a Markov chain. Later, you will study **long-run behavior (长期行为)** and **stationary distributions (平稳分布)**, which rely heavily on the n-step transition probabilities and the Chapman–Kolmogorov equations.

### ⚠️ Common Mistakes / 常见误区

1.  **Forgetting the Markov Property (忘记马尔可夫性)**: When calculating `ℙ(Xₙ₊₂ = j | Xₙ₊₁ = k, Xₙ = i)`, students often keep the condition on `Xₙ = i`. Remember, given the present (`Xₙ₊₁ = k`), the future is independent of the past (`Xₙ = i`).
2.  **Confusing `pᵢⱼ` and `pᵢⱼ(n)` (混淆一步与n步概率)**: `pᵢⱼ` is a one-step transition probability. `pᵢⱼ(n)` is the probability of being in `j` after *exactly* `n` steps. They are not the same thing.
3.  **Incorrect Matrix Multiplication (矩阵乘法错误)**: When calculating `P²`, remember that the entry `(i,j)` is the dot product of the **i-th row** of `P` and the **j-th column** of `P`. A common mistake is to multiply rows by rows.
4.  **Misunderstanding the Row Sum Condition (误解行和为1)**: The condition `∑ⱼ pᵢⱼ = 1` applies to **each row** of the transition matrix. It means from any state `i`, you must go somewhere. It does *not* mean the columns sum to 1.
5.  **Forgetting the Initial Distribution (忘记初始分布)**: The probability of a specific path, like `ℙ(X₀=i, X₁=j)`, always starts with the initial distribution `λᵢ`. You cannot just multiply transition probabilities.

### ✍️ Practice / 练习

1.  **Weather Model (天气模型)**: A simple weather model has two states: Sunny (S) and Rainy (R). The transition matrix is:
    `P = ( 0.8  0.2 )`
    `    ( 0.4  0.6 )`
    If it is Sunny today, what is the probability it will be Rainy in two days?
    - **Hint (提示)**: You need to find `p_{S,R}(2)`. Use matrix multiplication or condition on the weather tomorrow.

2.  **Three-State Chain (三状态链)**: Consider a Markov chain with states {A, B, C} and a transition matrix **P** where `p_{A,B} = 0.5`, `p_{A,C} = 0.5`, `p_{B,A} = 1`, `p_{C,C} = 1`. All other entries are 0. Write down the matrix **P** and calculate `P²`.
    - **Hint (提示)**: Draw the transition diagram first. It will help you understand the process.

3.  **Applying Chapman-Kolmogorov (应用查普曼-科尔莫戈罗夫方程)**: You know that `p_{1,2}(3) = 0.2` and `p_{2,3}(4) = 0.5`. What is `p_{1,3}(7)`? Can you calculate it from this information alone? Why or why not?
    - **Hint (提示)**: Look at the Chapman-Kolmogorov equation: `p_{1,3}(7) = ∑ₖ p_{1,k}(3) * p_{k,3}(4)`. You only know one term in the sum.

4.  **Initial Distribution (初始分布)**: A Markov chain has initial distribution `λ = (0.2, 0.8)` for states {1, 2} and transition matrix `P = (0.5, 0.5; 0.1, 0.9)`. Find the probability that `X₁ = 1`.
    - **Hint (提示)**: Calculate the vector `λP`. The first element of this vector is `ℙ(X₁ = 1)`.

5.  **Path Probability (路径概率)**: For the two-state printer example with `α=0.3` and `β=0.1`, what is the probability of the specific path `X₀=1, X₁=1, X₂=0, X₃=1`?
    - **Hint (提示)**: Multiply the initial probability `ℙ(X₀=1)` by the transition probabilities for each step.

### 📌 Key Takeaways / 要点总结

1.  A **time-homogeneous Markov chain (时间齐次马尔可夫链)** is defined by its initial distribution `(λᵢ)` and transition probabilities `(pᵢⱼ)`.
2.  The **Markov property (马尔可夫性)** states that the future is independent of the past, given the present.
3.  The **transition matrix (转移矩阵) P** is a stochastic matrix where each row sums to 1.
4.  **Conditioning on the first step (对第一步进行条件化)** is the most crucial technique for calculating multi-step probabilities.
5.  The **n-step transition probabilities (n步转移概率)** are given by the matrix power `Pⁿ`.
6.  The **Chapman–Kolmogorov equations (查普曼-科尔莫戈罗夫方程)** (`P(n+m) = P(n)P(m)`) are a fundamental property that follows directly from matrix multiplication.
7.  The distribution of the chain after `n` steps is given by the row vector `λPⁿ`.