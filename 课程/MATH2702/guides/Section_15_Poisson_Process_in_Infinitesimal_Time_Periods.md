# Section 15: Poisson Process in Infinitesimal Time Periods

> MATH2702 Stochastic Processes - 自学教材
> 生成时间: 2026-07-17 14:53
> 来源页: 76-78

---

# 📋 Section Overview / 章节概览

This section introduces the **third definition** of the Poisson process, focusing on what happens in **infinitesimally small time periods** (无穷小时间段). This approach is more "natural" because it doesn't require direct assumptions about distributions—it only assumes what seems intuitively obvious about arrivals in very short time intervals. We'll also derive the **Kolmogorov forward equations** (科尔莫戈罗夫前向方程), which connect Markov processes to differential equations. This is crucial for understanding how stochastic processes evolve over time.

**Why this matters**: This definition provides a powerful tool for proving properties of Poisson processes (like the sum of two processes) and establishes a deep link between probability theory and differential equations, which is foundational for advanced topics in stochastic processes.

---

# 🎯 Learning Objectives / 学习目标

By the end of this section, you will be able to:

1. **Understand** the "little-o" notation (小o记号) and use it to describe probabilities in infinitesimal time periods.
2. **State** the third definition of the Poisson process in terms of infinitesimal increments (无穷小增量).
3. **Prove** that the sum of two independent Poisson processes is a Poisson process using the infinitesimal definition.
4. **Derive** the Kolmogorov forward equations from the infinitesimal definition.
5. **Verify** that the Poisson distribution satisfies these forward equations.
6. **Connect** the three definitions of the Poisson process (Poisson increments, exponential holding times, infinitesimal increments).

---

# 📚 Prerequisites / 前置知识

Before studying this section, you should be familiar with:

- **Basic probability**: Random variables, probability distributions, independence (独立性)
- **Poisson distribution**: Definition, probability mass function \( P(X = k) = e^{-\lambda} \lambda^k / k! \)
- **Exponential distribution**: Definition, memoryless property (无记忆性)
- **Calculus**: Derivatives (导数), limits (极限), especially limits as \( \tau \to 0 \)
- **Previous definitions of Poisson process**: 
  - Definition 1: Increments have Poisson distribution (增量服从泊松分布)
  - Definition 2: Holding times are exponential (等待时间服从指数分布)
- **Markov processes**: Basic concept of memoryless property

---

# 📖 Core Content / 核心内容

## Topic 1: Little-o Notation / 小o记号

### Intuition / 直觉理解

When we study very small time periods, some terms become so tiny that we can "ignore" them. For example, if \( \tau = 0.001 \), then \( \tau^2 = 0.000001 \) is much smaller. The "little-o" notation \( o(\tau) \) captures this idea: it represents any term that is **negligible** compared to \( \tau \) as \( \tau \) approaches 0.

Think of it like this: If you're measuring the length of a room and your measurement error is 1 mm, you don't worry about errors of 0.001 mm. Similarly, when \( \tau \) is very small, terms like \( \tau^2 \) or \( \tau^3 \) are so tiny that they don't affect our calculations.

### Formal Definition / 形式化定义

**Definition (Little-o Notation)**:
A function \( f(\tau) \) is said to be \( o(\tau) \) (read as "little-o of tau") if:
\[
\frac{f(\tau)}{\tau} \to 0 \quad \text{as} \quad \tau \to 0
\]

**Symbol explanation**:
- \( f(\tau) \): any function of \( \tau \)
- \( \tau \): a small time increment (时间增量)
- \( o(\tau) \): pronounced "little-o of tau", represents terms of lower order than \( \tau \)
- The arrow \( \to \) means "approaches" or "tends to"

**Examples of \( o(\tau) \) terms**:
- \( \tau^2 \) is \( o(\tau) \) because \( \tau^2 / \tau = \tau \to 0 \)
- \( \tau^3 \) is \( o(\tau) \) because \( \tau^3 / \tau = \tau^2 \to 0 \)
- \( 5\tau^2 \) is \( o(\tau) \) because \( 5\tau^2 / \tau = 5\tau \to 0 \)

**Examples of terms that are NOT \( o(\tau) \)**:
- \( 2\tau \) is NOT \( o(\tau) \) because \( 2\tau / \tau = 2 \not\to 0 \)
- \( \tau \) itself is NOT \( o(\tau) \) because \( \tau / \tau = 1 \not\to 0 \)

### Key Properties / 关键性质

1. **Sum of \( o(\tau) \) terms**: If \( f(\tau) = o(\tau) \) and \( g(\tau) = o(\tau) \), then \( f(\tau) + g(\tau) = o(\tau) \)
2. **Constant times \( o(\tau) \)**: If \( c \) is a constant and \( f(\tau) = o(\tau) \), then \( c \cdot f(\tau) = o(\tau) \)
3. **Product with bounded function**: If \( f(\tau) = o(\tau) \) and \( g(\tau) \) is bounded, then \( f(\tau)g(\tau) = o(\tau) \)

---

## Topic 2: Definition 3 - Infinitesimal Increments / 定义三：无穷小增量

### Intuition / 直觉理解

Imagine watching a bus stop for a very short time—say, one second. What's likely to happen?

1. **Most likely**: No bus arrives (概率最大：没有公交车到达)
2. **Possible but unlikely**: Exactly one bus arrives (可能但不常见：恰好一辆公交车到达)
3. **Extremely unlikely**: Two or more buses arrive (极不可能：两辆或更多公交车到达)

The probability of exactly one arrival should be roughly proportional to the length of time we watch. If we watch for 2 seconds instead of 1 second, the chance of seeing one bus roughly doubles.

This intuitive idea is formalized in the third definition of the Poisson process.

### Formal Definition / 形式化定义

**Definition 3 (Poisson Process via Infinitesimal Increments)**:
Let \( (X(t)) \) be a stochastic process counting arrivals over time. For a very small time period of length \( \tau \), the number of arrivals is \( X(t+\tau) - X(t) \). The process satisfies:

\[
\mathbb{P}(X(t+\tau) - X(t) = j) = 
\begin{cases}
1 - \lambda\tau + o(\tau) & \text{if } j = 0 \\
\lambda\tau + o(\tau) & \text{if } j = 1 \\
o(\tau) & \text{if } j \geq 2
\end{cases}
\quad \text{as } \tau \to 0
\]

**Symbol explanation**:
- \( X(t) \): the number of arrivals up to time \( t \) (到时间t为止的到达数)
- \( X(t+\tau) - X(t) \): the number of arrivals in the interval \( (t, t+\tau] \) (在区间(t, t+τ]内的到达数)
- \( \mathbb{P}(\cdot) \): probability of an event (事件的概率)
- \( j \): the number of arrivals (到达数)
- \( \lambda \): the rate parameter (速率参数), average arrivals per unit time
- \( \tau \): a small time increment (时间增量)
- \( o(\tau) \): terms of lower order than \( \tau \) (比τ更低阶的项)
- The notation "as \( \tau \to 0 \)" means this holds when \( \tau \) is very small

**Interpretation of the three cases**:
- **j = 0**: Probability of no arrivals ≈ \( 1 - \lambda\tau \) (close to 1 for small τ)
- **j = 1**: Probability of exactly one arrival ≈ \( \lambda\tau \) (proportional to τ)
- **j ≥ 2**: Probability of two or more arrivals is negligible (negligible compared to τ)

### Theorem 15.1: Equivalence to Poisson Process

**Theorem 15.1**: Let \( (X(t)) \) be a stochastic process with the following properties:

1. **Initial condition**: \( X(0) = 0 \) (starts at zero)
2. **Infinitesimal increments**: \( X(t+\tau) - X(t) \) has the structure in equation (11) above, as \( \tau \to 0 \)
3. **Independent increments**: \( X(t_2) - X(t_1) \) and \( X(t_4) - X(t_3) \) are independent for all \( t_1 \leq t_2 \leq t_3 \leq t_4 \)

Then \( (X(t)) \) is a Poisson process with rate \( \lambda \).

**Symbol explanation**:
- \( t_1, t_2, t_3, t_4 \): time points satisfying \( t_1 \leq t_2 \leq t_3 \leq t_4 \)
- Independent increments means arrivals in non-overlapping time intervals are independent

**Why this is important**: This theorem shows that the seemingly "weak" assumptions about what happens in tiny time periods are actually equivalent to the full Poisson process definition.

---

## Topic 3: Example - Sum of Two Poisson Processes / 例题：两个泊松过程之和

### Intuition / 直觉理解

If you have two independent sources of arrivals (e.g., red buses and blue buses), and each follows a Poisson process, then the total number of arrivals (any color bus) also follows a Poisson process. The rates simply add.

This is intuitive: if red buses arrive at rate \( \lambda \) per hour and blue buses at rate \( \mu \) per hour, then total buses arrive at rate \( \lambda + \mu \) per hour.

### Worked Example / 例题

**Problem**: Let \( (X(t)) \) be a Poisson process with rate \( \lambda \) and \( (Y(t)) \) be an independent Poisson process with rate \( \mu \). Define \( Z(t) = X(t) + Y(t) \). Show that \( (Z(t)) \) is a Poisson process with rate \( \lambda + \mu \).

**Solution**:

We need to verify the three properties from Theorem 15.1 for \( Z(t) \).

**Step 1: Initial condition**
\[
Z(0) = X(0) + Y(0) = 0 + 0 = 0
\]
✓ Property 1 is satisfied.

**Step 2: Independent increments**
Since \( X \) and \( Y \) both have independent increments, and they are independent of each other, \( Z \) also has independent increments. ✓ Property 3 is satisfied.

**Step 3: Infinitesimal increments** - This is the main calculation.

**Case j = 0**: Probability of no arrivals in \( Z \)
\[
\mathbb{P}(Z(t+\tau) - Z(t) = 0) = \mathbb{P}(X(t+\tau)-X(t)=0) \cdot \mathbb{P}(Y(t+\tau)-Y(t)=0)
\]

**Explanation**: \( Z \) doesn't increase only if **neither** \( X \) nor \( Y \) increases.

Using the infinitesimal definition:
\[
= (1 - \lambda\tau + o(\tau))(1 - \mu\tau + o(\tau))
\]

**Multiply out**:
\[
= 1 - \lambda\tau - \mu\tau + \lambda\mu\tau^2 + \text{terms with } o(\tau)
\]

**Simplify**: The term \( \lambda\mu\tau^2 \) is \( o(\tau) \) (since \( \tau^2/\tau = \tau \to 0 \)). Also, products of \( o(\tau) \) terms are \( o(\tau) \).

\[
= 1 - (\lambda + \mu)\tau + o(\tau)
\]

✓ This matches the form for j = 0 with rate \( \lambda + \mu \).

**Case j = 1**: Probability of exactly one arrival in \( Z \)

There are two ways this can happen:
1. \( X \) increases by 1 and \( Y \) stays at 0
2. \( X \) stays at 0 and \( Y \) increases by 1

\[
\mathbb{P}(Z(t+\tau) - Z(t) = 1) = 
\mathbb{P}(X(t+\tau)-X(t)=1) \cdot \mathbb{P}(Y(t+\tau)-Y(t)=0)
+ \mathbb{P}(X(t+\tau)-X(t)=0) \cdot \mathbb{P}(Y(t+\tau)-Y(t)=1)
\]

Using the infinitesimal definition:
\[
= (\lambda\tau + o(\tau))(1 - \mu\tau + o(\tau)) + (1 - \lambda\tau + o(\tau))(\mu\tau + o(\tau))
\]

**Multiply out**:
\[
= \lambda\tau - \lambda\mu\tau^2 + o(\tau) + \mu\tau - \lambda\mu\tau^2 + o(\tau)
\]

**Simplify**: The \( \lambda\mu\tau^2 \) terms are \( o(\tau) \). So:
\[
= (\lambda + \mu)\tau + o(\tau)
\]

✓ This matches the form for j = 1 with rate \( \lambda + \mu \).

**Case j ≥ 2**: Probability of two or more arrivals

Since probabilities must sum to 1:
\[
\mathbb{P}(Z(t+\tau) - Z(t) \geq 2) = 1 - \mathbb{P}(Z = 0) - \mathbb{P}(Z = 1)
\]
\[
= 1 - [1 - (\lambda+\mu)\tau + o(\tau)] - [(\lambda+\mu)\tau + o(\tau)]
\]
\[
= o(\tau)
\]

✓ This matches the form for j ≥ 2.

**Conclusion**: All three properties are satisfied with rate \( \lambda + \mu \), so \( (Z(t)) \) is a Poisson process with rate \( \lambda + \mu \).

---

## Topic 4: Kolmogorov Forward Equations / 科尔莫戈罗夫前向方程

### Intuition / 直觉理解

The forward equations describe how the probability distribution of the process evolves over time. Think of it like tracking the probability of being at different "states" (numbers of arrivals) as time passes.

For a Poisson process, we want to find \( p_j(t) = \mathbb{P}(X(t) = j) \), the probability that exactly \( j \) arrivals have occurred by time \( t \). The forward equations give us differential equations that \( p_j(t) \) must satisfy.

### Derivation / 推导

**Notation**: Let \( p_j(t) = \mathbb{P}(X(t) = j) \)

**Step 1: Case j ≥ 1**

Consider what happens in a small time interval \( (t, t+\tau] \):

\[
p_j(t+\tau) = \mathbb{P}(X(t+\tau) = j)
\]

To have \( j \) arrivals by time \( t+\tau \), we could:
- Have \( j \) arrivals by time \( t \) and 0 arrivals in \( (t, t+\tau] \)
- Have \( j-1 \) arrivals by time \( t \) and 1 arrival in \( (t, t+\tau] \)
- Have \( j-2 \) or fewer arrivals by time \( t \) and 2+ arrivals in \( (t, t+\tau] \) (negligible)

Using the infinitesimal definition and independence:
\[
p_j(t+\tau) = (1 - \lambda\tau + o(\tau))p_j(t) + (\lambda\tau + o(\tau))p_{j-1}(t) + o(\tau)
\]

**Rearrange** to get the increment:
\[
p_j(t+\tau) - p_j(t) = -\lambda\tau p_j(t) + \lambda\tau p_{j-1}(t) + o(\tau)
\]

**Divide by τ**:
\[
\frac{p_j(t+\tau) - p_j(t)}{\tau} = -\lambda p_j(t) + \lambda p_{j-1}(t) + \frac{o(\tau)}{\tau}
\]

**Take limit as τ → 0**:
- The left side becomes the derivative: \( p'_j(t) \)
- The term \( o(\tau)/\tau \to 0 \) by definition of \( o(\tau) \)

**Result**:
\[
p'_j(t) = -\lambda p_j(t) + \lambda p_{j-1}(t) \quad \text{for } j \geq 1
\]

**Initial condition**: \( p_j(0) = 0 \) for \( j \geq 1 \) (since we start at 0)

**Step 2: Case j = 0**

To have 0 arrivals by time \( t+\tau \), we must have 0 arrivals by time \( t \) and 0 arrivals in \( (t, t+\tau] \):
\[
p_0(t+\tau) = (1 - \lambda\tau + o(\tau))p_0(t)
\]

**Rearrange**:
\[
p_0(t+\tau) - p_0(t) = -\lambda\tau p_0(t) + o(\tau)
\]

**Divide by τ and take limit**:
\[
p'_0(t) = -\lambda p_0(t)
\]

**Initial condition**: \( p_0(0) = 1 \) (we start at 0 with probability 1)

### Summary of Forward Equations

\[
\begin{cases}
p'_0(t) = -\lambda p_0(t), & p_0(0) = 1 \\
p'_j(t) = -\lambda p_j(t) + \lambda p_{j-1}(t), & p_j(0) = 0 \text{ for } j \geq 1
\end{cases}
\]

These are called the **Kolmogorov forward equations** (科尔莫戈罗夫前向方程).

### Verification that Poisson Distribution Satisfies the Equations

**Claim**: The solution is:
\[
p_j(t) = e^{-\lambda t} \frac{(\lambda t)^j}{j!}
\]

**Check for j = 0**:
\[
p_0(t) = e^{-\lambda t} \frac{(\lambda t)^0}{0!} = e^{-\lambda t}
\]
\[
p'_0(t) = -\lambda e^{-\lambda t} = -\lambda p_0(t) \quad \checkmark
\]
\[
p_0(0) = e^0 = 1 \quad \checkmark
\]

**Check for j ≥ 1**:

Left-hand side:
\[
p'_j(t) = \frac{d}{dt} \left( e^{-\lambda t} \frac{(\lambda t)^j}{j!} \right)
\]

Using the product rule:
\[
= \frac{1}{j!} \left( -\lambda e^{-\lambda t} (\lambda t)^j + e^{-\lambda t} \cdot \lambda j (\lambda t)^{j-1} \right)
\]

**Explanation**: The derivative of \( (\lambda t)^j \) is \( \lambda j (\lambda t)^{j-1} \) by the chain rule.

\[
= -\lambda \cdot \frac{e^{-\lambda t} (\lambda t)^j}{j!} + \lambda \cdot \frac{e^{-\lambda t} (\lambda t)^{j-1}}{(j-1)!}
\]

**Recognize the terms**:
\[
= -\lambda p_j(t) + \lambda p_{j-1}(t) \quad \checkmark
\]

**Initial condition**:
\[
p_j(0) = e^0 \cdot \frac{0^j}{j!} = 0 \quad \checkmark
\]

**Conclusion**: The Poisson distribution satisfies the forward equations, proving Theorem 15.1.

---

# 🔗 Connections / 知识关联

## Connections to Previous Topics

1. **Definition 1 (Poisson increments)**: The forward equations prove that the infinitesimal definition implies Poisson-distributed increments, establishing equivalence with the first definition.

2. **Definition 2 (Exponential holding times)**: The exponential distribution of inter-arrival times can also be derived from the infinitesimal definition.

3. **Markov property**: The forward equations are a key tool for analyzing Markov processes, showing the deep connection between Poisson processes and Markov chains.

## Connections to Future Topics

1. **Continuous-time Markov chains (CTMCs)**: The forward equations generalize to CTMCs, where the transition rates replace the single rate \( \lambda \).

2. **Birth-death processes**: These generalize the Poisson process by allowing both births (arrivals) and deaths (departures), with forward equations that are similar but more complex.

3. **Queueing theory**: The Poisson process is the foundation for modeling arrival processes in queues (M/M/1, M/M/c, etc.).

4. **Renewal processes**: The infinitesimal definition provides intuition for why Poisson processes are the only renewal processes with the memoryless property.

---

# ⚠️ Common Mistakes / 常见误区

1. **Misunderstanding \( o(\tau) \)**
   - ❌ Thinking \( o(\tau) \) means "approximately zero" or "small"
   - ✅ Understanding that \( o(\tau) \) specifically means the term divided by \( \tau \) goes to 0 as \( \tau \to 0 \)
   - Example: \( 0.1\tau \) is NOT \( o(\tau) \), but \( 0.1\tau^2 \) IS \( o(\tau) \)

2. **Forgetting the "as \( \tau \to 0 \)" condition**
   - ❌ Using the infinitesimal formulas for large \( \tau \)
   - ✅ Remembering these formulas only hold in the limit as \( \tau \) approaches 0

3. **Confusing \( p_j(t) \) with \( p_j(t+\tau) \)**
   - ❌ Writing \( p_j(t+\tau) = (1-\lambda\tau)p_j(t) + \lambda\tau p_{j-1}(t) \) without the \( o(\tau) \) terms
   - ✅ Including \( o(\tau) \) terms and understanding they vanish only after dividing by \( \tau \) and taking the limit

4. **Incorrect handling of the sum of Poisson processes**
   - ❌ Forgetting to consider both ways to get exactly one arrival (X increases, Y stays; X stays, Y increases)
   - ✅ Systematically enumerating all possible combinations

5. **Misapplying the forward equations**
   - ❌ Using the forward equations without the initial conditions
   - ✅ Always checking \( p_0(0) = 1 \) and \( p_j(0) = 0 \) for \( j \geq 1 \)

---

# ✍️ Practice / 练习

## Question 1
Determine whether each of the following functions is \( o(\tau) \) as \( \tau \to 0 \):
(a) \( 3\tau^2 \)
(b) \( \sqrt{\tau} \)
(c) \( \tau \sin(\tau) \)
(d) \( \tau^2 + 5\tau^3 \)

**Hint**: For each function, compute \( f(\tau)/\tau \) and see what happens as \( \tau \to 0 \).

---

## Question 2
Let \( (X(t)) \) be a Poisson process with rate \( \lambda = 2 \). Using the infinitesimal definition, write down:
(a) \( \mathbb{P}(X(t+\tau) - X(t) = 0) \) as \( \tau \to 0 \)
(b) \( \mathbb{P}(X(t+\tau) - X(t) = 1) \) as \( \tau \to 0 \)
(c) \( \mathbb{P}(X(t+\tau) - X(t) \geq 2) \) as \( \tau \to 0 \)

**Hint**: Just substitute \( \lambda = 2 \) into the formulas from equation (11).

---

## Question 3
Suppose \( (X(t)) \) is a Poisson process with rate \( \lambda \) and \( (Y(t)) \) is an independent Poisson process with rate \( \mu \). Let \( Z(t) = X(t) + Y(t) \). Calculate:
\[
\mathbb{P}(Z(t+\tau) - Z(t) = 2)
\]
as \( \tau \to 0 \). Show that this is \( o(\tau) \).

**Hint**: Consider all ways that \( X \) and \( Y \) can change so that their sum increases by 2. There are three possibilities: (2,0), (1,1), (0,2).

---

## Question 4
For a Poisson process with rate \( \lambda \), the forward equation for \( j = 1 \) is:
\[
p'_1(t) = -\lambda p_1(t) + \lambda p_0(t)
\]
Given that \( p_0(t) = e^{-\lambda t} \) and \( p_1(0) = 0 \), solve this differential equation to find \( p_1(t) \).

**Hint**: This is a first-order linear ODE. Use an integrating factor \( e^{\lambda t} \), or verify that \( p_1(t) = \lambda t e^{-\lambda t} \) satisfies the equation.

---

## Question 5
Explain in your own words why the three properties in Theorem 15.1 (initial condition, infinitesimal increments, independent increments) are sufficient to define a Poisson process. Which property ensures that the process has the memoryless property?

**Hint**: Think about which property prevents the process from "remembering" past arrivals.

---

# 📌 Key Takeaways / 要点总结

1. **Little-o notation** \( o(\tau) \) represents terms that are negligible compared to \( \tau \) as \( \tau \to 0 \), meaning \( f(\tau)/\tau \to 0 \).

2. **Third definition of Poisson process**: In an infinitesimal time interval of length \( \tau \):
   - \( \mathbb{P}(0 \text{ arrivals}) = 1 - \lambda\tau + o(\tau) \)
   - \( \mathbb{P}(1 \text{ arrival}) = \lambda\tau + o(\tau) \)
   - \( \mathbb{P}(\geq 2 \text{ arrivals}) = o(\tau) \)

3. **Sum of Poisson processes**: If \( X(t) \sim \text{Poisson}(\lambda) \) and \( Y(t) \sim \text{Poisson}(\mu) \) are independent, then \( Z(t) = X(t) + Y(t) \sim \text{Poisson}(\lambda + \mu) \). This is easily proved using the infinitesimal definition.

4. **Kolmogorov forward equations** describe how probabilities evolve over time:
   - \( p'_0(t) = -\lambda p_0(t) \), with \( p_0(0) = 1 \)
   - \( p'_j(t) = -\lambda p_j(t) + \lambda p_{j-1}(t) \), with \( p_j(0) = 0 \) for \( j \geq 1 \)

5. **Solution to forward equations** is the Poisson distribution: \( p_j(t) = e^{-\lambda t} (\lambda t)^j / j!