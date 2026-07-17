# Section 6: Class Structure

> MATH2702 Stochastic Processes - 自学教材
> 生成时间: 2026-07-17 14:47
> 来源页: 35-39

---

Of course. As a university professor, I will create a comprehensive, bilingual self-study guide for the provided course material. This guide is designed to be a complete replacement for a lecture, ensuring you can master the concepts independently.

---

### 📋 Section Overview / 章节概览

This section, "Class Structure," is about understanding the **anatomy** of a Markov chain. Imagine a large, complex network of states. Instead of trying to understand the whole thing at once, we can break it down into smaller, more manageable pieces. This section introduces two fundamental tools for doing this:

1.  **Communicating Classes (通信类)**: This helps us group states that can "talk" to each other, meaning you can travel from one state to another and back again. This reveals the chain's fundamental building blocks.
2.  **Periodicity (周期性)**: This helps us understand the "rhythm" of a chain. Does it only visit certain states at specific times (like every 2 steps), or can it visit them at any time?

Understanding these concepts is crucial for analyzing the long-term behavior of a Markov chain, such as whether it will settle into a steady state or cycle forever.

### 🎯 Learning Objectives / 学习目标

By the end of this section, you will be able to:

1.  **Define** the concepts of accessibility (可达性) and communication (通信) between states in a Markov chain.
2.  **Prove** that the "communicates with" relation is an equivalence relation (等价关系).
3.  **Identify** the communicating classes (通信类) of a given Markov chain from its transition matrix or diagram.
4.  **Define** and **calculate** the period (周期) of a state.
5.  **Prove** that all states in the same communicating class have the same period.
6.  **Classify** a Markov chain as irreducible (不可约的) or not, and states as periodic (周期的) or aperiodic (非周期的).

### 📚 Prerequisites / 前置知识

Before starting this section, you should be comfortable with:

- **Basic Probability (基础概率论)**: Understanding of probability, conditional probability, and random variables.
- **Markov Chain Basics (马尔可夫链基础)**: You should know what a Markov chain is, its state space (状态空间) `𝒮`, and its transition matrix (转移矩阵) `P`. You should understand the notation `p_{ij}(n)` for the n-step transition probability.
- **Chapman-Kolmogorov Equations (查普曼-科尔莫戈罗夫方程)**: The fundamental equation for calculating multi-step transition probabilities.
- **Set Theory & Relations (集合论与关系)**: Basic understanding of sets, partitions, and equivalence relations (reflexive, symmetric, transitive).
- **Number Theory (数论)**: Understanding of the greatest common divisor (GCD, 最大公约数).

### 📖 Core Content / 核心内容

---

#### Topic 1: Communicating Classes (通信类)

**Intuition / 直觉理解**

Imagine a Markov chain as a map of cities connected by one-way roads. We want to group cities into "countries." A good rule is: two cities should be in the same country if you can drive from one to the other *and* drive back again. This is the core idea of a **communicating class (通信类)**. If you can get from city A to city B, we say B is **accessible (可达的)** from A. If you can also get back from B to A, then A and B **communicate (通信)**.

**Formal Definition / 形式化定义**

**Definition 6.1 (Accessibility and Communication / 可达性与通信的定义)**

Consider a Markov chain on a state space `𝒮` with transition matrix `P`.

- **Accessibility (可达性)**: We say that state `j ∈ 𝒮` is **accessible from (从...可达)** state `i ∈ 𝒮`, and write `i → j`, if, for some integer `n ≥ 0`, the n-step transition probability `p_{ij}(n) > 0`.
    - **Symbol Explanation**:
        - `i, j`: Specific states in the state space `𝒮`.
        - `n`: A number of steps.
        - `p_{ij}(n)`: The probability of being in state `j` after exactly `n` steps, starting from state `i`.
        - `p_{ij}(n) > 0`: Means there is a positive probability (greater than zero) of making this transition in `n` steps.

- **Communication (通信)**: If `i → j` and `j → i`, we say that `i` **communicates with (与...通信)** `j` and write `i ↔ j`.

**Key Properties / 关键性质**

**Theorem 6.1 (Communication is an Equivalence Relation / 通信关系是等价关系)**

The "communicates with" relation `↔` is an **equivalence relation (等价关系)**. This means it has three properties:

1.  **Reflexive (自反性)**: `i ↔ i` for all `i ∈ 𝒮`.
    - *Intuition*: You can always "stay put" in zero steps.
2.  **Symmetric (对称性)**: If `i ↔ j`, then `j ↔ i`.
    - *Intuition*: The definition is symmetric by its very nature.
3.  **Transitive (传递性)**: If `i ↔ j` and `j ↔ k`, then `i ↔ k`.
    - *Intuition*: You can travel from `i` to `k` by going through `j`.

**Proof / 证明**

*Proof of Theorem 6.1:*

1.  **Reflexivity (自反性)**: We need to show `i ↔ i`.
    - By definition, `p_{ii}(0) = 1`. This is the probability of being in state `i` after 0 steps, which is always 1 (we start there and haven't moved).
    - Since `p_{ii}(0) = 1 > 0`, we have `i → i`. The condition `i → i` and `i → i` is trivially true, so `i ↔ i`. ✅

2.  **Symmetry (对称性)**: The definition `i ↔ j` requires both `i → j` and `j → i`. Swapping `i` and `j` gives `j → i` and `i → j`, which is the same condition. Therefore, if `i ↔ j`, then `j ↔ i`. ✅

3.  **Transitivity (传递性)**: We need to show that if `i ↔ j` and `j ↔ k`, then `i ↔ k`. We will show `i → k` and `k → i`. The proof for `k → i` is identical by swapping roles.
    - Since `i → j`, there exists some `n` such that `p_{ij}(n) > 0`.
    - Since `j → k`, there exists some `m` such that `p_{jk}(m) > 0`.
    - Now, consider the probability of going from `i` to `k` in `n + m` steps. We use the **Chapman-Kolmogorov equations (查普曼-科尔莫戈罗夫方程)**:
        `p_{ik}(n+m) = Σ_{l∈𝒮} p_{il}(n) * p_{lk}(m)`
        This equation says: to go from `i` to `k` in `n+m` steps, you first go from `i` to some intermediate state `l` in `n` steps, and then from `l` to `k` in `m` steps. You sum this over all possible intermediate states `l`.
    - The sum over all `l` is greater than or equal to any single term in the sum. Let's pick the term where `l = j`:
        `p_{ik}(n+m) ≥ p_{ij}(n) * p_{jk}(m)`
    - Since `p_{ij}(n) > 0` and `p_{jk}(m) > 0`, their product is also positive: `p_{ij}(n) * p_{jk}(m) > 0`.
    - Therefore, `p_{ik}(n+m) > 0`, which means `i → k`.
    - By a symmetric argument (using `k → j` and `j → i`), we can show `k → i`.
    - Since `i → k` and `k → i`, we conclude `i ↔ k`. ✅

**Consequence (推论)**: Because `↔` is an equivalence relation, it **partitions (划分)** the state space `𝒮` into disjoint **equivalence classes (等价类)**. In the context of Markov chains, these classes are called **communicating classes (通信类)**. Each state belongs to exactly one communicating class. The class containing state `i` is the set of all states `j` such that `i ↔ j`.

**Worked Examples / 例题**

**Example 6.1 (Simple Random Walk / 简单随机游走)**
Consider a simple random walk on `𝒮 = ℤ` (all integers). The walk moves up (+1) with probability `p` and down (-1) with probability `q = 1-p`, where `0 < p < 1`.
- **Analysis**: From any state `i`, you can reach any other state `j > i` by taking `(j-i)` steps to the right. You can also return from `j` to `i` by taking `(j-i)` steps to the left. The same logic applies for `j < i`. Therefore, every state communicates with every other state.
- **Conclusion**: The entire state space `𝒮 = ℤ` is **one single communicating class**.

**Example 6.2 (Gambler's Ruin / 赌徒破产问题)**
Consider the gambler's ruin chain on `𝒮 = {0, 1, 2, ..., m}`. The gambler wins or loses $1 each round until they reach 0 (ruin) or `m` (success).
- **Analysis**:
    - State `0`: From state 0, you can only stay at 0 (it's absorbing). You cannot reach any other state. So `0` does not communicate with any other state. It forms its own class: `{0}`.
    - State `m`: Similarly, from state `m`, you can only stay at `m`. It forms its own class: `{m}`.
    - States `{1, 2, ..., m-1}`: From any of these states, you can move up and down, similar to a simple random walk (until you hit 0 or `m`). Crucially, you can reach any other state in this set and return. For example, from 1 you can go to 2, and from 2 you can go back to 1. So all these states communicate with each other.
- **Conclusion**: There are **three communicating classes**: `{0}`, `{m}`, and `{1, 2, ..., m-1}`.

**Example 6.3 (Healthy-Sick-Dead Model / 健康-生病-死亡模型)**
Consider a model with states `H` (Healthy), `S` (Sick), and `D` (Dead). The transition matrix is:
```
P = | p_HH  p_HS   0 |
    | p_SH  p_SS  p_SD |
    | 0     0      1 |
```
- **Analysis**:
    - From `H`, you can go to `S` (get sick) and back from `S` to `H` (recover). So `H ↔ S`.
    - From `D`, you can only stay at `D`. You cannot go to `H` or `S`. So `D` does not communicate with them.
- **Conclusion**: There are **two communicating classes**: `{H, S}` and `{D}`.

**Further Definitions / 更多定义**

**Definition 6.2 (Irreducible, Closed, Open, Absorbing / 不可约的, 封闭的, 开放的, 吸收的)**

- **Irreducible Markov Chain (不可约马尔可夫链)**: If the entire state space `𝒮` is one single communicating class, we say the Markov chain is **irreducible (不可约的)**.
    - *Intuition*: The chain cannot be broken down into smaller, independent pieces. You can get from any state to any other state.

- **Closed Class (封闭类)**: A communicating class `C ⊂ 𝒮` is **closed (封闭的)** if no state outside the class is accessible from any state within the class. Formally: if there exists `i ∈ C` and `j ∈ 𝒮` such that `i → j`, then `j ∈ C` must also hold.
    - *Intuition*: "Once you enter, you can never leave." The chain is trapped inside the class forever.

- **Open Class (开放类)**: A communicating class that is not closed is called **open (开放的)**.
    - *Intuition*: You can leave this class and never come back.

- **Absorbing State (吸收态)**: If a state `i` is in a communicating class `{i}` by itself, and that class is closed, then state `i` is called **absorbing (吸收的)**.
    - *Intuition*: "Once you enter, you are stuck forever." It's a closed class of size 1.

**Worked Examples (Revisited) / 例题回顾**

- **Simple Random Walk (Example 6.4)**: The whole state space is one class, so it is **closed** and the chain is **irreducible**. There are no absorbing states.
- **Gambler's Ruin (Example 6.4)**: Classes `{0}` and `{m}` are **closed** (you can't leave). Since they are single-state closed classes, states `0` and `m` are **absorbing states**. The class `{1, 2, ..., m-1}` is **open** (you can leave to 0 or `m`). The chain is **not irreducible**.
- **Healthy-Sick-Dead (Example 6.4)**: Class `{D}` is **closed**, so `D` is an **absorbing state**. Class `{H, S}` is **open** (you can leave by dying). The chain is **not irreducible**.

---

#### Topic 2: Periodicity (周期性)

**Intuition / 直觉理解**

Some Markov chains have a "rhythm." For example, in a simple random walk, you always switch between even and odd states. If you start on an even number, you can only be on an even number after an even number of steps. This is **periodic (周期的)** behavior. The **period (周期)** is the "beat" of this rhythm. It's the greatest common divisor (GCD) of all the step counts at which you can return to your starting state.

**Formal Definition / 形式化定义**

**Definition 6.3 (Period of a State / 状态的周期)**

Consider a Markov chain with transition matrix `P`. We say that a state `i ∈ 𝒮` has **period (周期)** `d_i`, where:
```
d_i = gcd{ n ∈ {1, 2, 3, ...} : p_{ii}(n) > 0 }
```
- **Symbol Explanation**:
    - `d_i`: The period of state `i`.
    - `gcd`: The **greatest common divisor (最大公约数)**. For example, `gcd{2, 4, 6} = 2`.
    - `{ n ∈ {1, 2, 3, ...} : p_{ii}(n) > 0 }`: The set of all positive integers `n` for which there is a positive probability of returning to state `i` in exactly `n` steps.
- **Interpretation**:
    - If `d_i > 1`, the state `i` is called **periodic (周期的)**.
    - If `d_i = 1`, the state `i` is called **aperiodic (非周期的)**.

**Worked Examples / 例题**

**Example 6.5 (Simple Random Walk / 简单随机游走)**
For the simple random walk with `p ≠ 0, 1`.
- `p_{ii}(n) = 0` for all odd `n`. You can never return to the same state in an odd number of steps because you always change parity.
- `p_{ii}(2) = 2pq > 0`. You can return in 2 steps (up then down, or down then up).
- `p_{ii}(4) > 0`, `p_{ii}(6) > 0`, etc.
- The set of `n` with `p_{ii}(n) > 0` is `{2, 4, 6, 8, ...}`.
- `gcd{2, 4, 6, ...} = 2`.
- **Conclusion**: All states have period `d_i = 2`. They are **periodic**.

**Example 6.6 (Gambler's Ruin / 赌徒破产问题)**
- States `0` and `m` are absorbing. `p_{00}(1) = 1 > 0` and `p_{mm}(1) = 1 > 0`. The set of `n` includes `1`. `gcd{1, 2, 3, ...} = 1`. So states `0` and `m` are **aperiodic**.
- States `{1, 2, ..., m-1}` behave like a simple random walk (until absorption). They have period `2`. They are **periodic**.

**Example 6.7 (A Complex Chain / 一个复杂链)**
Consider the chain in Figure 8 of the original text (reproduced conceptually here):
- There are two communicating classes: `{1, 2, 3, 4}` (open) and `{5, 6, 7}` (closed).
- **Class `{1, 2, 3, 4}`**: The transitions cause a swap between odd and even states (1↔2, 2↔3, etc.) until possibly exiting to state 5. The return times to any state in this class are even numbers. Therefore, states `1, 2, 3, 4` have period `2`.
- **Class `{5, 6, 7}`**: The transitions are deterministic: `5 → 6 → 7 → 5`. To return to state 5, you need 3 steps (5→6→7→5). To return in 6 steps, you go around twice. The set of return times is `{3, 6, 9, ...}`. `gcd{3, 6, 9, ...} = 3`. Therefore, states `5, 6, 7` have period `3`.

**Key Properties / 关键性质**

**Theorem 6.2 (States in a Communicating Class Have the Same Period / 同一通信类中的状态具有相同周期)**

All states in a communicating class have the same period. Formally: If `i, j ∈ 𝒮` are such that `i ↔ j`, then `d_i = d_j`.

**Corollary (推论)**: In an **irreducible** Markov chain, all states have the same period `d`. We say the chain is **periodic** if `d > 1` and **aperiodic** if `d = 1`.

**Proof / 证明**

*Proof of Theorem 6.2:*

We want to show `d_i = d_j`. The strategy is to show `d_i ≤ d_j` and `d_j ≤ d_i`, which implies equality.

**Step 1: Show `d_i ≤ d_j`.**

1.  Since `i ↔ j`, there exist integers `n` and `m` such that:
    - `p_{ij}(n) > 0` (can go from `i` to `j` in `n` steps).
    - `p_{ji}(m) > 0` (can go from `j` to `i` in `m` steps).

2.  Consider returning from `i` to `i` in `n + m` steps by going `i → j → i`.
    - By Chapman-Kolmogorov: `p_{ii}(n+m) ≥ p_{ij}(n) * p_{ji}(m) > 0`.
    - This means `(n+m)` is in the set of return times for state `i`. Therefore, `d_i` must divide `(n+m)`. (Because `d_i` is the GCD of all return times, it must divide every return time).

3.  Now, let `r` be any positive integer such that `p_{jj}(r) > 0`. (This means `r` is a return time for state `j`).

4.  Consider returning from `i` to `i` in `n + m + r` steps by going `i → j → j → i`.
    - By Chapman-Kolmogorov: `p_{ii}(n+m+r) ≥ p_{ij}(n) * p_{jj}(r) * p_{ji}(m) > 0`.
    - This means `(n+m+r)` is also a return time for state `i`. Therefore, `d_i` must divide `(n+m+r)`.

5.  We have established that `d_i` divides both `(n+m)` and `(n+m+r)`.
    - If a number divides two numbers, it must also divide their difference: `(n+m+r) - (n+m) = r`.
    - Therefore, `d_i` divides `r`.

6.  The argument in step 5 holds for **every** `r` such that `p_{jj}(r) > 0`. This means `d_i` is a **common divisor** of all the return times for state `j`.

7.  The **greatest** common divisor of all return times for state `j` is, by definition, `d_j`. Since `d_i` is a common divisor, it cannot be larger than the greatest common divisor.
    - Therefore, `d_i ≤ d_j`. ✅

**Step 2: Show `d_j ≤ d_i`.**

- This is a completely symmetric argument. We simply swap the roles of `i` and `j` in the proof above. Since `j ↔ i`, the same logic applies.
- Therefore, `d_j ≤ d_i`. ✅

**Conclusion**: Since `d_i ≤ d_j` and `d_j ≤ d_i`, we must have `d_i = d_j`. ✅

### 🔗 Connections / 知识关联

- **Previous Topics**: This section builds directly on the definition of a Markov chain, transition probabilities, and the Chapman-Kolmogorov equations. The concept of a closed class is a more formal way of thinking about absorbing states, which you may have encountered before.
- **Future Topics**: The next section (Section 6.3 in the original text) deals with **hitting times (首达时间)**. The concepts of communicating classes and periodicity are essential for analyzing hitting times. For example, if a state is in a closed class, the probability of ever hitting a state outside that class is zero. Periodicity affects the probability of being in a state at a specific future time. These concepts are also fundamental for understanding the **stationary distribution (平稳分布)** and **long-run behavior (长期行为)** of a Markov chain, which is a major goal of the course.

### ⚠️ Common Mistakes / 常见误区

1.  **Confusing Accessibility with Communication (混淆可达性与通信)**: `i → j` only means you can get from `i` to `j`. `i ↔ j` requires you can get back. A state can be accessible from another without them communicating. For example, in the gambler's ruin, state `0` is accessible from state `1`, but state `1` is *not* accessible from state `0`. So they do not communicate.

2.  **Thinking Period is about the "Best" Path (认为周期是关于"最佳"路径的)**: The period is the GCD of *all* possible return times, not just the shortest one. For example, if you can return in 4, 6, and 8 steps, the period is `gcd(4,6,8) = 2`, not 4.

3.  **Forgetting the "Zero-Step" Return (忘记"零步"返回)**: In the proof of reflexivity, we use `p_{ii}(0) = 1`. This is a valid mathematical trick, but it's important to remember that the definition of period explicitly considers only `n ∈ {1, 2, 3, ...}`. The 0-step return is not used to calculate the period.

4.  **Assuming All States in a Chain Have the Same Period (假设链中所有状态具有相同周期)**: This is only true if the chain is **irreducible**. If the chain has multiple communicating classes, states in different classes can have different periods (as seen in Example 6.7).

5.  **Misinterpreting "Closed Class" (误解"封闭类")**: A closed class means you cannot leave it. It does *not* mean you cannot enter it. In the gambler's ruin, `{0}` is closed. Once you are in it, you stay there. But you can enter it from state `1`.

### ✍️ Practice / 练习

Here are some self-test questions to check your understanding.

**Question 1:**
Consider a Markov chain with state space `𝒮 = {1, 2, 3, 4}` and transition matrix:
```
P = | 0   1   0   0 |
    | 0.5 0   0.5 0 |
    | 0   0.5 0   0.5|
    | 0   0   1   0 |
```
- (a) Draw the transition diagram.
- (b) Find all communicating classes.
- (c) Is the chain irreducible?
- (d) Find the period of each state.
- (e) Are there any absorbing states? Any closed classes?
    - **Hint**: Start by drawing the diagram. Look for states that can reach each other and return. For period, list the possible return times for each state.

**Question 2:**
True or False? Justify your answer.
- (a) If a state is absorbing, it is aperiodic.
- (b) If a Markov chain is irreducible, all states must be aperiodic.
- (c) In an irreducible Markov chain, every state is accessible from every other state.
    - **Hint**: Review the definitions of "absorbing," "aperiodic," "irreducible," and "accessible."

**Question 3:**
Consider a Markov chain on `𝒮 = {a, b, c}` where `a → b`, `b → a`, `b → c`, `c → b`, but `a` cannot reach `c` and `c` cannot reach `a`.
- (a) What are the communicating classes?
- (b) Which classes are closed?
- (c) What is the period of each state? (Assume all allowed transitions have positive probability