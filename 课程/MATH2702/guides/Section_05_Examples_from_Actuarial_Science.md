# Section 5: Examples from Actuarial Science

> MATH2702 Stochastic Processes - 自学教材
> 生成时间: 2026-07-17 14:46
> 来源页: 30-34

---

# 📋 Section Overview / 章节概览

This section (Section 5) explores **practical applications of Markov chains** in various fields, particularly **actuarial science (精算科学)** and **physics (物理学)**. We will examine five distinct examples:

1. **Simple no-claims discount model** - A direct Markov chain for insurance
2. **Monkey typing "ABRACADABRA"** - A martingale (鞅) example using gambling strategies
3. **Accident model with memory** - Converting a non-Markov process into a Markov chain
4. **Ising model from physics** - A Markov chain model of magnetism
5. **No-claims discount model with memory** - Expanding state space to preserve Markov property

**Why this matters**: These examples demonstrate how Markov chains can model real-world phenomena, from insurance pricing to physical systems. They also show techniques for handling situations where the obvious process is NOT Markovian, by cleverly redefining the state space or considering related processes.

---

# 🎯 Learning Objectives / 学习目标

By the end of this section, you will be able to:

1. **Construct** a transition probability matrix and transition diagram for a simple insurance no-claims discount model
2. **Calculate** multi-step transition probabilities using both path summation and matrix multiplication methods
3. **Apply** optional stopping theorem (可选停止定理) to compute expected waiting times in martingale problems
4. **Identify** when a stochastic process is NOT a Markov chain and **transform** it into one by redefining the state space
5. **Verify** the Markov property for a given probability distribution (e.g., the Ising model)
6. **Interpret** the conditions on functions \( f \) and \( g \) in accident models with memory

---

# 📚 Prerequisites / 前置知识

Before studying this section, you should be familiar with:

- **Basic probability theory**: Conditional probability (条件概率), expectation (期望), independence
- **Markov chain fundamentals**: State space (状态空间), transition probabilities (转移概率), Markov property (马尔可夫性质), time homogeneity (时间齐次性)
- **Matrix multiplication**: For computing multi-step transition probabilities
- **Martingale theory** (for Section 5.2): Definition of martingale, optional stopping theorem
- **Basic physics concepts** (for Section 5.4): Energy, temperature (optional - not required for mathematical understanding)

---

# 📖 Core Content / 核心内容

## Topic 1: Simple No-Claims Discount Model / 简单无索赔折扣模型

### Intuition / 直觉理解

Imagine a car insurance company that rewards safe drivers with discounts. Each year, if you have no accidents, you move up one discount level. If you have at least one accident, you move down one level. This creates a simple "ladder" system where your future discount depends only on your current discount and whether you had an accident this year - NOT on your entire driving history. This is exactly the Markov property!

**Analogy**: Think of a board game where you move forward one space if you roll a certain number, and backward one space otherwise. Your position next turn depends only on where you are now, not on how you got there.

### Formal Definition / 形式化定义

**State Space (状态空间)**: \( \mathcal{S} = \{1, 2, 3\} \)
- State 1: No discount (无折扣)
- State 2: 25% discount (25%折扣)
- State 3: 50% discount (50%折扣)

**Transition Rules (转移规则)**:
- New policyholders start in state 1
- If no claim in a year: move up one level (1→2, 2→3, 3→3)
- If at least one claim in a year: move down one level (1→1, 2→1, 3→2)
- Probability of a claim-free year: \( \frac{3}{4} \)

**Transition Probability Matrix (转移概率矩阵)**:

\[
P = \begin{pmatrix}
\frac{1}{4} & \frac{3}{4} & 0 \\
\frac{1}{4} & 0 & \frac{3}{4} \\
0 & \frac{1}{4} & \frac{3}{4}
\end{pmatrix}
\]

Where:
- \( P_{ij} = \mathbb{P}(X_{n+1} = j \mid X_n = i) \)
- Row 1 (state 1): \( P_{11} = \frac{1}{4} \) (claim, stay in 1), \( P_{12} = \frac{3}{4} \) (no claim, go to 2), \( P_{13} = 0 \) (cannot jump to 3 directly)
- Row 2 (state 2): \( P_{21} = \frac{1}{4} \) (claim, go to 1), \( P_{22} = 0 \) (cannot stay in 2), \( P_{23} = \frac{3}{4} \) (no claim, go to 3)
- Row 3 (state 3): \( P_{31} = 0 \) (cannot go to 1 directly), \( P_{32} = \frac{1}{4} \) (claim, go to 2), \( P_{33} = \frac{3}{4} \) (no claim, stay in 3)

**Transition Diagram (转移图)**:

```
    1/4         1/4         1/4
   ┌───┐       ┌───┐       ┌───┐
   │ 1 │──3/4→│ 2 │──3/4→│ 3 │
   └───┘       └───┘       └───┘
     ↑           ↑           ↑
    1/4         3/4         3/4
```

(Arrows show transitions with probabilities; self-loops at states 1 and 3)

### Key Properties / 关键性质

1. **Time homogeneity (时间齐次性)**: Transition probabilities do not depend on time \( n \)
2. **Discrete state space**: \( \mathcal{S} = \{1, 2, 3\} \)
3. **Discrete time**: One step per year
4. **Markov property holds**: Future depends only on present state

### Worked Example / 例题

**Example 5.1**: What is the probability of having a 50% reduction to your premium three years from now, given that you currently have no reduction on the premium?

**Solution**:

We want \( p_{13}(3) = \mathbb{P}(X_3 = 3 \mid X_0 = 1) \)

**Method 1: Path Summation (路径求和法)**

We need all paths of length 3 from state 1 to state 3:
- Path 1: \( 1 \rightarrow 1 \rightarrow 2 \rightarrow 3 \)
- Path 2: \( 1 \rightarrow 2 \rightarrow 3 \rightarrow 3 \)

Calculate each path probability:
- Path 1: \( p_{11} \cdot p_{12} \cdot p_{23} = \frac{1}{4} \cdot \frac{3}{4} \cdot \frac{3}{4} = \frac{9}{64} \)
- Path 2: \( p_{12} \cdot p_{23} \cdot p_{33} = \frac{3}{4} \cdot \frac{3}{4} \cdot \frac{3}{4} = \frac{27}{64} \)

Sum: \( \frac{9}{64} + \frac{27}{64} = \frac{36}{64} = \frac{9}{16} \)

**Method 2: Matrix Multiplication (矩阵乘法)**

Compute \( P^{(3)} = P^3 = P \cdot P \cdot P \):

\[
P^2 = \begin{pmatrix}
\frac{1}{4} & \frac{3}{4} & 0 \\
\frac{1}{4} & 0 & \frac{3}{4} \\
0 & \frac{1}{4} & \frac{3}{4}
\end{pmatrix}
\cdot
\begin{pmatrix}
\frac{1}{4} & \frac{3}{4} & 0 \\
\frac{1}{4} & 0 & \frac{3}{4} \\
0 & \frac{1}{4} & \frac{3}{4}
\end{pmatrix}
\]

First row of \( P^2 \):
- \( P^2_{11} = \frac{1}{4} \cdot \frac{1}{4} + \frac{3}{4} \cdot \frac{1}{4} + 0 \cdot 0 = \frac{1}{16} + \frac{3}{16} = \frac{4}{16} = \frac{1}{4} \)
- \( P^2_{12} = \frac{1}{4} \cdot \frac{3}{4} + \frac{3}{4} \cdot 0 + 0 \cdot \frac{1}{4} = \frac{3}{16} \)
- \( P^2_{13} = \frac{1}{4} \cdot 0 + \frac{3}{4} \cdot \frac{3}{4} + 0 \cdot \frac{3}{4} = \frac{9}{16} \)

Continuing this calculation (you can verify), we get:

\[
P^3 = \frac{1}{64} \begin{pmatrix}
7 & 21 & 36 \\
7 & 12 & 45 \\
4 & 15 & 45
\end{pmatrix}
\]

The desired \( p_{13}(3) \) is the top-right entry: \( \frac{36}{64} = \frac{9}{16} \)

**Answer**: \( \frac{9}{16} \) or 0.5625

---

## Topic 2: Monkey Typing "ABRACADABRA" / 猴子打字"ABRACADABRA"

### Intuition / 直觉理解

A monkey randomly types letters (each of 26 letters equally likely). We want to know the expected number of letters typed until the word "ABRACADABRA" first appears. This seems like a difficult problem, but we can solve it using a clever gambling strategy and martingale theory.

**The Gambling Strategy**: Before each new letter is typed, a new gambler arrives and bets £1 on "A". If correct, they win £26 and bet all on "B", and so on. They continue until they either lose or the full word appears. The total wealth of all gamblers forms a martingale.

### Formal Definition / 形式化定义

**Setup**:
- Letters typed independently with probability \( \frac{1}{26} \) each
- \( T \) = total number of letters typed when "ABRACADABRA" first appears
- We want \( \mathbb{E}(T) \)

**Martingale Construction**:
- Let \( X_n \) = total wealth of all gamblers after \( n \)th letter typed
- Define \( M_n = X_n - n \)
- Claim: \( M_n \) is a martingale

**Verification of Martingale Property**:
- Each gambler still in play: loses with probability \( \frac{25}{26} \), multiplies by 26 with probability \( \frac{1}{26} \)
- Gamblers who lost remain at 0
- New gambler brings £1
- Therefore: \( \mathbb{E}(M_{n+1} \mid X_1, \ldots, X_n) = X_n + 1 - (n+1) = X_n - n = M_n \)
- Also \( \mathbb{E}|M_n| < \infty \) (bounded by maximum of \( n \) and finite sum of powers of 26 up to \( 26^{11} \))

**Optional Stopping**:
- Stopped martingale \( M_{T \wedge n} \) is bounded (by \( 1 + 26 + 26^2 + \ldots + 26^{11} \))
- \( \mathbb{P}(T < \infty) = 1 \) (dominated by geometric random variable)
- Therefore: \( 0 = \mathbb{E}(M_0) = \mathbb{E}(M_T) = \mathbb{E}(X_T) - \mathbb{E}(T) \)

### Key Observation / 关键观察

At time \( T \) (when "ABRACADABRA" appears), only 3 gamblers are still in play:

1. **Gambler who arrived at \( T-11 \)**: Successfully bet on all 11 letters → won \( 26^{11} \)
2. **Gambler who arrived at \( T-4 \)**: Successfully bet on "ABRA" (first 4 letters) → won \( 26^4 \)
3. **Gambler who arrived at \( T \)**: Successfully bet on "A" (first letter) → won \( 26 \)

**Why these three?** Because "ABRACADABRA" has overlapping patterns:
- The full word "ABRACADABRA" (11 letters)
- The prefix "ABRA" (4 letters) appears at the beginning AND at positions 8-11
- The single letter "A" appears at the beginning, position 5, and position 8

### Calculation / 计算

\[
\mathbb{E}(T) = \mathbb{E}(X_T) = 26^{11} + 26^4 + 26
\]

\[
26^{11} \approx 3.67 \times 10^{15}, \quad 26^4 = 456,976, \quad 26 = 26
\]

\[
\mathbb{E}(T) \approx 3.7 \times 10^{15} \text{ letters}
\]

**Interpretation**: If the monkey types one letter per second, this is about 100 million years!

### Important Note / 重要说明

The repetitions in "ABRACADABRA" (the overlapping patterns "ABRA" and "A") led to the extra terms \( 26^4 \) and \( 26 \) being included in \( \mathbb{E}(T) \), increasing the expected waiting time.

---

## Topic 3: Accident Model with Memory / 带记忆的事故模型

### Intuition / 直觉理解

Sometimes the obvious stochastic process is NOT a Markov chain. For example, if the probability of an accident next year depends on the TOTAL number of past accidents (not just last year's result), then the accident indicator process \( Y_n \) is not Markovian. However, we can define a new process \( X_n \) = total accidents up to year \( n \), which IS a Markov chain.

**Analogy**: Your driving record doesn't just depend on whether you had an accident last year, but on your entire history. However, the cumulative number of accidents evolves in a Markovian way.

### Formal Definition / 形式化定义

**Original Process (原始过程)**:
- \( Y_n \) = accident indicator for year \( n \)
- \( Y_n = \begin{cases} 0 & \text{if no accident in year } n \\ 1 & \text{if one accident in year } n \end{cases} \)
- State space: \( \mathcal{S} = \{0, 1\} \)
- Probability of accident in year \( n+1 \):
  \[
  \mathbb{P}(Y_{n+1} = 1 \mid Y_n = y_n, \ldots, Y_1 = y_1) = \frac{f(y_1 + y_2 + \cdots + y_n)}{g(n)}
  \]
  where \( f \) and \( g \) are non-negative increasing functions with \( 0 \leq f(m) \leq g(m) \) for all \( m \)

**Problem**: \( (Y_n) \) is NOT a Markov chain because \( Y_{n+1} \) depends on the entire history \( Y_1, \ldots, Y_n \), not just \( Y_n \).

**Clever Work-around (巧妙方法)**:
- Define \( X_n = \sum_{i=1}^n Y_i \) = total number of accidents up to year \( n \)
- Then \( (X_n) \) IS a Markov chain

**Verification of Markov Property**:

\[
\begin{aligned}
&\mathbb{P}(X_{n+1} = x_{n+1} \mid X_n = x_n, \ldots, X_1 = x_1) \\
&= \mathbb{P}(Y_{n+1} = 1 \mid Y_n = x_n - x_{n-1}, \ldots, Y_2 = x_2 - x_1, Y_1 = x_1) \\
&= \frac{f((x_n - x_{n-1}) + \cdots + (x_2 - x_1) + x_1)}{g(n)} \\
&= \frac{f(x_n)}{g(n)}
\end{aligned}
\]

The last step uses telescoping: \( (x_n - x_{n-1}) + \cdots + (x_2 - x_1) + x_1 = x_n \)

This depends only on \( x_n \), so the Markov property holds!

**Note**: This is a **time inhomogeneous** Markov chain because the transition probability depends on \( n \) (through \( g(n) \)).

### Conditions on f and g / 对f和g的条件

1. **\( f \) is increasing**: Among drivers who have been driving the same number of years, those with more past accidents are more likely to have an accident in the future
2. **\( g \) is increasing**: Among drivers with the same number of past accidents, those who spread accidents over a longer period are less likely to have accidents in the future
3. **\( 0 \leq f(m) \leq g(m) \)**: Ensures transition probabilities are in [0,1] (since \( \sum_{i=1}^m y_i \leq m \))

---

## Topic 4: Ising Model from Physics / 物理中的Ising模型

### Intuition / 直觉理解

The Ising model is a simple model of magnetism. Imagine a line of atoms, each with a "spin" that can be either up (+1) or down (-1). Neighboring spins prefer to align (both up or both down) because this gives lower energy. The temperature controls how strong this preference is - at high temperatures, spins are random; at low temperatures, they tend to align.

**Key Question**: Can we extract a Markov chain from this model?

### Formal Definition / 形式化定义

**State Space**: \( \mathcal{S} = \{1, -1\} \) (spins: up and down)

**Configuration**: \( (\sigma_1, \sigma_2, \ldots, \sigma_N) \) where each \( \sigma_i \in \{1, -1\} \)

**Probability Distribution**:

\[
\mu_N(\sigma_1, \sigma_2, \ldots, \sigma_N) = \frac{1}{Z_N} e^{\beta \sum_{i=1}^{N-1} \sigma_i \sigma_{i+1}}
\]

Where:
- \( \beta \geq 0 \) = inverse temperature (逆温度)
- \( Z_N = \sum_{(a_1, \ldots, a_N) \in \mathcal{S}^N} e^{\beta \sum_{i=1}^{N-1} a_i a_{i+1}} \) = partition function (配分函数)
- \( H(\sigma_1, \ldots, \sigma_N) = -\sum_{i=1}^{N-1} \sigma_i \sigma_{i+1} \) = Hamiltonian (哈密顿量) = energy of configuration
- So \( \mu_N \propto \exp(-\beta H) \)

**Physics Interpretation**:
- Spins agreeing (\( \sigma_i = \sigma_{i+1} \)) gives \( \sigma_i \sigma_{i+1} = 1 \), contributing \( e^\beta \) to probability
- Spins disagreeing (\( \sigma_i \neq \sigma_{i+1} \)) gives \( \sigma_i \sigma_{i+1} = -1 \), contributing \( e^{-\beta} \) to probability
- Lower energy (more agreement) is more probable
- \( \beta = 1/(k_B T) \) where \( T \) = temperature, \( k_B = 1.38 \times 10^{-23} \) J/K = Boltzmann's constant

### Verification of Markov Property / 验证马尔可夫性质

We want to check if \( (\sigma_i)_{i \geq 1} \) is a Markov chain.

**Step 1**: Compute conditional probability given full history

\[
\begin{aligned}
&\mu_N(\sigma_N = x_N \mid \sigma_1 = x_1, \ldots, \sigma_{N-1} = x_{N-1}) \\
&= \frac{\mu_N(\sigma_1 = x_1, \ldots, \sigma_N = x_N)}{\mu_N(\sigma_1 = x_1, \ldots, \sigma_{N-1} = x_{N-1})} \\
&= \frac{\frac{1}{Z_N} e^{\beta \sum_{i=1}^{N-2} x_i x_{i+1}} e^{\beta x_{N-1} x_N}}{\frac{1}{Z_N} e^{\beta \sum_{i=1}^{N-2} x_i x_{i+1}} \sum_{y \in \{-1,1\}} e^{\beta x_{N-1} y}} \\
&= \frac{e^{\beta x_{N-1} x_N}}{e^{\beta x_{N-1}} + e^{-\beta x_{N-1}}}
\end{aligned}
\]

**Step 2**: Compute conditional probability given only the last state

\[
\begin{aligned}
&\mu_N(\sigma_N = x_N \mid \sigma_{N-1} = x_{N-1}) \\
&= \frac{\sum_{x_1, \ldots, x_{N-2}} \frac{1}{Z_N} e^{\beta \sum_{i=1}^{N-2} x_i x_{i+1}} e^{\beta x_{N-1} x_N}}{\sum_{x_1, \ldots, x_{N-2}} \frac{1}{Z_N} e^{\beta \sum_{i=1}^{N-2} x_i x_{i+1}} \sum_{x_N \in \{-1,1\}} e^{\beta x_{N-1} x_N}} \\
&= \frac{e^{\beta x_{N-1} x_N}}{e^{\beta x_{N-1}} + e^{-\beta x_{N-1}}}
\end{aligned}
\]

**Conclusion**: The two conditional probabilities are equal, so \( (\sigma_i) \) is a Markov chain!

### Discussion / 讨论

**As \( N \to \infty \)**: What happens to the Markov chain? We cannot take the limit naively because \( H(\sigma_1, \ldots) = \pm \infty \) for almost every configuration - this is not physical (infinite energy).

**Magnetization (磁化强度)**:
\[
m = \frac{1}{N} \sum_{i=1}^N \sigma_i
\]
If \( m \to m^* \neq 0 \) as \( N \to \infty \), the system is said to have **spontaneous magnetization (自发磁化)**. This is a key concept in statistical mechanics.

---

## Topic 5: No-Claims Discount Model with Memory / 带记忆的无索赔折扣模型

### Intuition / 直觉理解

Now we have a more complex insurance model with 4 discount levels. The rule for moving down after an accident depends on whether the previous year also had an accident. This means the simple state space (just discount levels) is NOT Markovian - we need to remember the previous year's accident status.

**Solution**: Split the 40% discount level into two states: one for those who had no accident last year, and one for those who did. This carries the memory forward.

### Formal Definition / 形式化定义

**Original Model**:
- 4 discount levels: 0%, 20%, 40%, 60%
- If accident-free: move up one level (max 60%)
- If accident: 
  - If previous year was accident-free: move down one level
  - If previous year had accident: move down two levels
  - Minimum: no discount
- Probability of claim-free year: \( \frac{3}{4} \)

**Problem**: State space \( \mathcal{S} = \{1, 2, 3, 4\} \) is NOT Markovian because from state 3 (40% discount), an accident could lead to either state 2 or state 1, depending on whether the previous year had an accident.

**Expanded State Space (扩展状态空间)**:

| State | Description |
|-------|-------------|
| 1 | No discount (无折扣) |
| 2 | 20% discount (20%折扣) |
| 3a | 40% discount, no claim in previous year (40%折扣, 上一年无索赔) |
| 3b | 40% discount, claim in previous year (40%折扣, 上一年有索赔) |
| 4 | 60% discount (60%折扣) |

**Transition Matrix**:

\[
P = \begin{pmatrix}
0.25 & 0.75 & 0 & 0 & 0 \\
0.25 & 0 & 0.75 & 0 & 0 \\
0 & 0.25 & 0 & 0 & 0.75 \\
0.25 & 0 & 0 & 0 & 0.75 \\
0 & 0 & 0 & 0.25 & 0.75
\end{pmatrix}
\]

**Transition Diagram**:

```
    0.25        0.25        0.25        0.25
   ┌───┐       ┌───┐       ┌───┐       ┌───┐
   │ 1 │──0.75→│ 2 │──0.75→│3a │──0.75→│ 4 │
   └───┘       └───┘       └───┘       └───┘
     ↑           ↑           ↑           ↑
    0.25        0.25        0.25        0.25
                              │
                              │0.25
                              ↓
                             ┌───┐
                             │3b │
                             └───┘
                               ↑
                              0.25
```

**Key Transitions**:
- From state 2 (20% discount), moving up goes to 3a (no accident in previous year)
- From state 4 (60% discount), moving down goes to 3b (accident in previous year)
- From state 3a (40%, no previous accident), accident leads to state 2 (down one level)
- From state 3b (40%, previous accident), accident leads to state 1 (down two levels)

---

# 🔗 Connections / 知识关联

## Connections to Previous Topics / 与之前主题的联系

1. **Markov Chain Fundamentals**: This section builds directly on the definition of Markov chains, transition matrices, and multi-step probabilities from earlier lectures
2. **Martingale Theory**: The monkey typing