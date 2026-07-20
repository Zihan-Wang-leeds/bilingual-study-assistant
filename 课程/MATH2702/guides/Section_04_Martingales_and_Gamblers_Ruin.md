# Section 4: Martingales and Gambler's Ruin

> MATH2702 Stochastic Processes - 自学教材
> 生成时间: 2026-07-17 14:45
> 来源页: 22-29

---

当然可以。作为一名大学教授，我将为您将这份关于“鞅与赌徒破产”的原始课程材料，转化为一份详尽、自包含的中英双语自学指南。这份指南将确保您即使在没有讲座的情况下，也能独立、深入地掌握所有内容。

---

### 📋 Section Overview / 章节概览

This section introduces **Martingales (鞅)** , a fundamental class of stochastic processes that model "fair games" where the expected future value equals the current value. We then apply this powerful concept to analyze the classic **Gambler's Ruin (赌徒破产)** problem, a Markov chain that models a simple gambling game. Using martingales and the **Optional Stopping Theorem (可选停止定理)** , we will derive elegant formulas for two key questions: the probability that a gambler goes bankrupt, and the expected duration of the game.

**Why it matters (为什么重要):** Martingales are a cornerstone of modern probability theory and have profound applications in finance (option pricing), statistics (sequential analysis), and physics. The Gambler's Ruin problem provides a clear, intuitive example of how martingales can be used to solve practical problems, illustrating the power of this theoretical framework. The insights about "certain ruin" even against a fair casino are both surprising and profound.

### 🎯 Learning Objectives / 学习目标

By the end of this section, you will be able to:

1.  **Define (定义)** a discrete-time martingale and verify if a given stochastic process is a martingale with respect to another process.
2.  **Identify (识别)** the Gambler's Ruin Markov chain, its state space, and transition probabilities.
3.  **Derive (推导)** the probability of ruin for Alice using a cleverly chosen martingale and the Optional Stopping Theorem.
4.  **Derive (推导)** the expected duration of the Gambler's Ruin game using another martingale.
5.  **Define (定义)** a stopping time and determine whether a given random time is a stopping time.
6.  **State (陈述)** the conditions of the Optional Stopping Theorem and explain why they are necessary.

### 📚 Prerequisites / 前置知识

Before starting this section, you should be comfortable with the following concepts:

*   **Probability Theory (概率论):** Conditional expectation `𝔼(X | Y)`, random variables, expectation `𝔼[X]`.
*   **Stochastic Processes (随机过程):** Basic understanding of a stochastic process as a collection of random variables indexed by time.
*   **Markov Chains (马尔可夫链):** The Markov property, state space, transition probabilities.
*   **Simple Random Walk (简单随机游走):** A process where `X_n = X_0 + Z_1 + ... + Z_n`, and `Z_i` are independent increments (e.g., +1 or -1).
*   **Geometric Distribution (几何分布):** The distribution of the number of trials until the first success.

### 📖 Core Content / 核心内容

---

#### Topic 1: Martingales (鞅)

**Intuition / 直觉理解**

Imagine you are playing a fair game. Your total winnings after each round form a sequence. A **martingale** is a mathematical model for such a "fair game". The key idea is that, given all the information up to the current round (your current winnings and the history of the game), your *expected* winnings in the *next* round are exactly equal to your current winnings. You don't expect to gain or lose money on average. The name "martingale" comes from a French gambling strategy, but the mathematical concept is much broader.

**Formal Definition / 形式化定义**

**Definition 4.1 (Martingale / 鞅).** A discrete-time stochastic process `(M_n)_{n≥0}` on a state space `𝒮` (not necessarily discrete) is a **martingale** with respect to another discrete-time stochastic process `(X_n)_{n≥0}` if, for all `n ≥ 0`:

1.  **Integrability (可积性):** `𝔼|M_n| < ∞`. (The expected absolute value of `M_n` is finite. This is a technical condition ensuring the expectation exists.)
2.  **Martingale Property (鞅性质):** `𝔼(M_{n+1} | X_0, X_1, ..., X_n) = M_n`. (The conditional expectation of the next value, given the entire history of the `X` process up to time `n`, is equal to the current value `M_n`.)

**Explanation of Symbols (符号解释):**
*   `(M_n)`: The process we are checking to see if it's a martingale.
*   `(X_n)`: The process that provides the "information" or "history". Often, `M_n` is a function of `X_n`.
*   `𝔼(·|·)`: Conditional expectation.
*   `M_n`: The value of the martingale at time `n`.
*   `M_{n+1}`: The value of the martingale at the next time step.
*   `X_0, X_1, ..., X_n`: The history of the `X` process up to time `n`.

**Important Note (重要说明):** The equality `𝔼(M_{n+1} | X_0, X_1, ..., X_n) = M_n` holds **almost surely (几乎必然地)** , meaning with probability 1. Conditional expectations are random variables, and the equality is a statement about their distributions.

**Key Properties / 关键性质**

*   **Fair Game Interpretation (公平游戏解释):** A martingale models a game where, given your current fortune, the expected change in your fortune in the next round is zero: `𝔼(M_{n+1} - M_n | history) = 0`.
*   **Not Necessarily Markov (不一定是马尔可夫链):** A martingale does not have to be a Markov chain. The example in the text describes a random walk that "remembers" the previous two steps to decide if it must stay put. This process is a martingale but not a Markov chain, because its future depends on more than just the current state.
*   **Construction from Other Processes (从其他过程构造):** A common theme is to find a function `f` such that `M_n = f(X_n, n)` is a martingale. For example, for a simple random walk `X_n` with step probabilities `p` and `q`, the process `M_n = X_n - n(p-q)` is a martingale.

**Worked Examples / 例题**

**Example 4.1: Is the Simple Random Walk a Martingale? (简单随机游走是鞅吗？)**

Let `X_n` be a simple random walk starting at `X_0`. It is defined as `X_n = X_0 + Σ_{i=1}^n Z_i`, where `Z_i` are independent increments with `ℙ(Z_i = +1) = p` and `ℙ(Z_i = -1) = q = 1-p`.

**Step 1: Check Integrability (检查可积性).**
`𝔼|X_n| ≤ 𝔼|X_0| + Σ_{i=1}^n 𝔼|Z_i| = |X_0| + n * 1 = |X_0| + n < ∞`. This condition is satisfied.

**Step 2: Check the Martingale Property (检查鞅性质).**
We need to compute `𝔼(X_{n+1} | X_0, Z_1, ..., Z_n)`.
We know `X_{n+1} = X_n + Z_{n+1}`.
So, `𝔼(X_{n+1} | X_0, Z_1, ..., Z_n) = 𝔼(X_n + Z_{n+1} | X_0, Z_1, ..., Z_n)`.
Since `X_n` is known given the history, `𝔼(X_n | ...) = X_n`.
Since `Z_{n+1}` is independent of the history, `𝔼(Z_{n+1} | ...) = 𝔼(Z_{n+1}) = p*(+1) + q*(-1) = p - q`.
Therefore, `𝔼(X_{n+1} | X_0, Z_1, ..., Z_n) = X_n + (p - q)`.

**Conclusion (结论):**
*   If `p = q = 1/2`, then `p - q = 0`, so `𝔼(X_{n+1} | ...) = X_n`. The simple symmetric random walk **is** a martingale with respect to its increments `(Z_n)`.
*   If `p ≠ q`, then `𝔼(X_{n+1} | ...) = X_n + (p-q) ≠ X_n`. The simple random walk **is not** a martingale.

**A More General Martingale (一个更一般的鞅):**
The process `M_n = X_n - n(p - q)` **is** a martingale for any `p ∈ [0,1]`. Let's check:
`𝔼(M_{n+1} | ...) = 𝔼(X_{n+1} - (n+1)(p-q) | ...) = 𝔼(X_n + Z_{n+1} - n(p-q) - (p-q) | ...)`
`= X_n - n(p-q) + 𝔼(Z_{n+1}) - (p-q) = M_n + (p-q) - (p-q) = M_n`.

---

#### Topic 2: Gambler's Ruin Markov Chain (赌徒破产马尔可夫链)

**Intuition / 直觉理解**

Alice and Bob are gambling. Alice starts with £`a`, Bob with £`b`. The total money is `m = a + b`. Each round, they bet £1. Alice wins with probability `p`, Bob wins with probability `q = 1-p`. The game ends when one player has all the money (the other is "ruined"). The amount of money Alice has after `n` rounds, `X_n`, is a stochastic process.

**Formal Definition / 形式化定义**

*   **State Space (状态空间):** `𝒮 = {0, 1, 2, ..., m}`. This represents how much money Alice has.
*   **Initial State (初始状态):** `X_0 = a`.
*   **Transition Probabilities (转移概率):** For `n ≥ 0`:
    *   If `1 ≤ X_n ≤ m-1` (game is ongoing):
        *   `X_{n+1} = X_n + 1` with probability `p` (Alice wins).
        *   `X_{n+1} = X_n - 1` with probability `q` (Bob wins).
    *   If `X_n = 0` (Alice is ruined):
        *   `X_{n+1} = 0` with probability 1 (absorbing state).
    *   If `X_n = m` (Bob is ruined):
        *   `X_{n+1} = m` with probability 1 (absorbing state).

**Key Properties / 关键性质**

*   **Markov Property (马尔可夫性质):** The next state `X_{n+1}` depends only on the current state `X_n`, not on the history. This is a Markov chain.
*   **Absorbing Barriers (吸收壁):** States 0 and `m` are absorbing. Once the process enters one of these states, it stays there forever. This models the end of the game.
*   **Analogy to Random Walk (与随机游走的类比):** The process is like a simple random walk started at `a`, but with absorbing barriers at 0 and `m`.

**Two Key Questions (两个关键问题):**
1.  What is the probability that Alice is ruined (the process hits 0)?
2.  What is the expected duration of the game (expected time to hit 0 or `m`)?

---

#### Topic 3: Probability of Ruin (破产概率)

**Intuition / 直觉理解**

Let `r_i` be the probability that Alice ends up ruined if she currently has £`i`. We know `r_0 = 1` (already ruined) and `r_m = 0` (Bob is ruined). For `1 ≤ i ≤ m-1`, we can find a relationship for `r_i` by conditioning on the first step from state `i`. If she wins (to `i+1`), her ruin probability becomes `r_{i+1}`. If she loses (to `i-1`), it becomes `r_{i-1}`. This gives `r_i = p * r_{i+1} + q * r_{i-1}`. Solving this recurrence with the boundary conditions gives the formula below. The course material uses a more elegant method with martingales.

**Formal Definition / 形式化定义**

**Theorem 4.1 (Ruin Probability / 破产概率).** Let `ρ = q/p`. The probability that Alice is ruined, starting with £`a`, is:

`r_a = { (ρ^a - ρ^m) / (1 - ρ^m) , if ρ ≠ 1
       { 1 - a/m , if ρ = 1`

**Explanation of Symbols (符号解释):**
*   `r_a`: The probability of Alice's ruin, starting from state `a`.
*   `a`: Alice's initial fortune.
*   `m`: Total money in the game (`a + b`).
*   `p`: Probability Alice wins a round.
*   `q`: Probability Bob wins a round (`= 1-p`).
*   `ρ = q/p`: The odds ratio. If `ρ > 1`, the game is in Bob's favor. If `ρ = 1`, the game is fair. If `ρ < 1`, the game is in Alice's favor.

**Proof / 证明 (Using Martingales)**

This proof is a beautiful application of martingales and the Optional Stopping Theorem.

**Case 1: `p ≠ q` (i.e., `ρ ≠ 1`)**

1.  **Construct a Martingale (构造一个鞅):** Define the process `M_n = (q/p)^{X_n} = ρ^{X_n}`.
    *   **Check Integrability:** `𝔼|M_n| ≤ max{1, ρ^m} < ∞`. This is fine because `X_n` is bounded between 0 and `m`.
    *   **Check Martingale Property:** We need to show `𝔼(M_{n+1} | Z_1, ..., Z_n) = M_n`.
        *   If `X_n = 0` or `X_n = m` (game over), then `M_{n+1} = M_n`, so the property holds trivially.
        *   If `0 < X_n < m` (game ongoing), then `X_{n+1} = X_n + Z_{n+1}`, where `Z_{n+1}` is +1 with prob `p` and -1 with prob `q`.
        `𝔼(M_{n+1} | Z_1, ..., Z_n) = 𝔼(ρ^{X_n + Z_{n+1}} | ...) = ρ^{X_n} * 𝔼(ρ^{Z_{n+1}} | ...)`.
        Since `Z_{n+1}` is independent of the past, `𝔼(ρ^{Z_{n+1}}) = p * ρ^{+1} + q * ρ^{-1} = p*(q/p) + q*(p/q) = q + p = 1`.
        Therefore, `𝔼(M_{n+1} | ...) = ρ^{X_n} * 1 = M_n`. So `(M_n)` is a martingale.

2.  **Define a Stopping Time (定义一个停止时间):** Let `T` be the first time the process hits either 0 or `m`. This is a stopping time because at any time `n`, we know if `T=n` by looking at `X_0, ..., X_n`.

3.  **Apply the Optional Stopping Theorem (应用可选停止定理):** The theorem states that under certain conditions, `𝔼(M_T) = 𝔼(M_0)`. We will justify this later. Assuming it holds:
    *   `𝔼(M_0) = 𝔼(ρ^{X_0}) = ρ^a`.
    *   `M_T` is the value of the martingale at the stopping time. It can only be one of two values:
        *   If Alice is ruined (hits 0), `M_T = ρ^0 = 1`. This happens with probability `r_a`.
        *   If Bob is ruined (hits `m`), `M_T = ρ^m`. This happens with probability `1 - r_a`.
    *   So, `𝔼(M_T) = 1 * r_a + ρ^m * (1 - r_a)`.

4.  **Solve for `r_a` (解出 `r_a`):**
    `ρ^a = r_a + ρ^m * (1 - r_a)`
    `ρ^a = r_a + ρ^m - ρ^m * r_a`
    `ρ^a - ρ^m = r_a * (1 - ρ^m)`
    `r_a = (ρ^a - ρ^m) / (1 - ρ^m)`

**Case 2: `p = q = 1/2` (i.e., `ρ = 1`)**

1.  **Construct a Martingale (构造一个鞅):** In this case, `(X_n)` itself is a martingale (as shown in Example 4.1).

2.  **Apply the Optional Stopping Theorem (应用可选停止定理):** Assuming `𝔼(X_T) = 𝔼(X_0)`:
    *   `𝔼(X_0) = a`.
    *   `X_T` is either 0 (with prob `r_a`) or `m` (with prob `1 - r_a`).
    *   So, `𝔼(X_T) = 0 * r_a + m * (1 - r_a) = m * (1 - r_a)`.

3.  **Solve for `r_a` (解出 `r_a`):**
    `a = m * (1 - r_a)`
    `1 - r_a = a/m`
    `r_a = 1 - a/m`

**Important Insight (重要见解): Playing Against a Casino (与赌场对赌)**

Imagine Alice plays against a large casino, so `m` is very large. We take the limit as `m → ∞`.

*   **Unfair Game (不公平游戏, `q > p`, `ρ > 1`):**
    `lim_{m→∞} r_a = lim_{m→∞} (ρ^a - ρ^m) / (1 - ρ^m) = 1`. Alice is ruined with certainty.
*   **Fair Game (公平游戏, `p = q = 1/2`, `ρ = 1`):**
    `lim_{m→∞} r_a = lim_{m→∞} (1 - a/m) = 1`. Alice is still ruined with certainty!

This leads to the quote: “Millionaires should always gamble, poor men never” - J.M. Keynes. The rich can withstand the inevitable losing streaks, while the poor will eventually be wiped out.

---

#### Topic 4: Expected Duration of the Game (游戏期望时长)

**Intuition / 直觉理解**

Let `d_i` be the expected number of steps remaining in the game when Alice has £`i`. We know `d_0 = d_m = 0`. The formula for `d_a` can be derived using another cleverly chosen martingale.

**Formal Definition / 形式化定义**

**Theorem 4.2 (Expected Duration / 期望时长).** The expected duration of the game, `d_a`, is given by:

`d_a = { (1/(q-p)) * (a - m * (1 - ρ^a) / (1 - ρ^m)) , if ρ ≠ 1
       { a * (m - a) , if ρ = 1`

**Proof / 证明 (Outline, as it is an exercise)**

The proof uses the Optional Stopping Theorem with different martingales.

*   **Case `p ≠ q`:** Find a constant `c` such that `M_n = X_n + n*c` is a martingale.
    *   `𝔼(M_{n+1} | ...) = 𝔼(X_n + Z_{n+1} + (n+1)*c | ...) = X_n + (p-q) + n*c + c = M_n + (p-q) + c`.
    *   For this to be `M_n`, we need `c = -(p-q) = q-p`.
    *   So, `M_n = X_n + n*(q-p)` is a martingale.
    *   Apply OST: `𝔼(M_T) = 𝔼(M_0)`. `𝔼(M_0) = a`. `𝔼(M_T) = 𝔼(X_T) + 𝔼(T)*(q-p) = [0*r_a + m*(1-r_a)] + d_a*(q-p)`.
    *   Solve for `d_a` using the expression for `r_a` from Theorem 4.1 to get the formula.

*   **Case `p = q`:** Show that `M_n = X_n^2 - n` is a martingale.
    *   `𝔼(M_{n+1} | ...) = 𝔼((X_n + Z_{n+1})^2 - (n+1) | ...) = 𝔼(X_n^2 + 2X_n Z_{n+1} + Z_{n+1}^2 - n - 1 | ...)`.
    *   Since `Z_{n+1}` is independent and `𝔼(Z_{n+1})=0`, `𝔼(Z_{n+1}^2)=1` (because `Z = ±1`).
    *   This equals `X_n^2 + 2X_n*0 + 1 - n - 1 = X_n^2 - n = M_n`.
    *   Apply OST: `𝔼(M_T) = 𝔼(M_0)`. `𝔼(M_0) = a^2 - 0 = a^2`. `𝔼(M_T) = 𝔼(X_T^2) - 𝔼(T) = [0^2 * r_a + m^2 * (1-r_a)] - d_a`.
    *   Using `r_a = 1 - a/m`, we get `a^2 = m^2 * (a/m) - d_a = a*m - d_a`.
    *   Therefore, `d_a = a*m - a^2 = a*(m-a)`.

**Important Insight (重要见解): Playing Against a Casino (与赌场对赌)**

*   **Unfair Game (不公平游戏, `q > p`, `ρ > 1`):** As `m → ∞`, `d_a → a/(q-p)`. Alice is ruined with certainty, and it takes a finite expected time.
*   **Fair Game (公平游戏, `p = q`):** As `m → ∞`, `d_a → ∞`. Alice is ruined with certainty, but the expected time is infinite! The game can go on for a very, very long time.

---

#### Topic 5: The Optional Stopping Theorem (可选停止定理)

**Intuition / 直觉理解**

The Optional Stopping Theorem (OST) tells us when the martingale property at a fixed time `n` (`𝔼(M_n) = 𝔼(M_0)`) also holds at a random stopping time `T` (`𝔼(M_T) = 𝔼(M_0)`). This is not always true, especially if the stopping time can be very large. The theorem provides conditions under which it is safe to "stop" the martingale.

**Formal Definition / 形式化定义**

**Definition 4.2 (Stopping Time / 停止时间).** Let `(X_n)_{n≥0}` be a stochastic process. A random time `T` (taking values in `{0, 1, 2, ...} ∪ {∞}`) is a **stopping time** if for every `n`, the event `{T = n}` is completely determined by the random variables `X_0, X_1, ..., X_n`.

**Examples (例子):**
*   **Is a stopping time:** "The first visit to state `i`". You know it when you arrive.
*   **Is a stopping time:** "Three time-steps after the second visit to `j`". You can count from the second visit.
*   **Is NOT a stopping time:** "The time-step before the first visit to `i`". You need to see the future to know if the next step is the first visit.
*   **Is NOT a stopping time:** "The final visit to `j`". You need to see the entire future to know if you'll ever come back.

**Theorem 4.3 (Optional Stopping Theorem / 可选停止定理).** Let `(M_n)_{n≥0}` be a martingale with respect to `(X_n)_{n≥0}`, and let `T` be a stopping time. Then `𝔼(M_T) = 𝔼(M_0)` holds if **at least one** of the following conditions is satisfied:

1.  **Bounded Stopping Time (有界停止时间):** `T` is bounded, i.e., `ℙ(T ≤ N) = 1` for some finite `N`.
2.  **Bounded Martingale (有界鞅):** `ℙ(T < ∞) = 1` (the stopping time is almost surely finite) AND `(M_n)` is bounded, i.e., `|M_n| ≤ K` for all `n` and some constant `K`.
3.  **Finite Expected Stopping Time & Bounded Increments (有限期望停止时间与有界增量):** `𝔼(T) < ∞` AND `(M_n)` has bounded increments, i.e., `|M_{n+1} - M_n| ≤ K` for all `n` and some constant `K`.

**Justification for Gambler's Ruin (对赌徒破产问题的证明)**

In the Gambler's Ruin problem, we applied OST. Let's see how we justify it.

*   **Martingale `M_n = ρ^{X_n}`:** This martingale is not bounded (it can be as large as `ρ^m`). Condition 2 doesn't directly apply. Condition 3 requires `𝔼(T) < ∞`, which is what we are trying to find! This is circular.
*   **The "Stopped Martingale" Trick (停止鞅技巧):** To fix this, we define a **stopped martingale**:
    `M_n^T = { M_n , if n ≤ T
              { M_T , if n > T`
    This process `M_n^T` is a martingale. Crucially, for the Gambler's Ruin, `X_n` is bounded between 0 and `m` for `n ≤ T`. Therefore, `M