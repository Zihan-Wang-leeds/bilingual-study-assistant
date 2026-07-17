# Section 14: Poisson Process with Exponential Holding Times

> MATH2702 Stochastic Processes - 自学教材
> 生成时间: 2026-07-17 14:53
> 来源页: 72-75

---

# 📘 MATH2702 Study Guide: Poisson Process with Exponential Holding Times

## 📋 Section Overview / 章节概览

This section explores the **Poisson process (泊松过程)** from a new perspective: instead of counting arrivals in a fixed time interval, we examine the **waiting times (等待时间)** between arrivals. We discover that these waiting times follow an **exponential distribution (指数分布)**, and this property gives us a powerful alternative definition of the Poisson process. We also introduce the **Markov property (马尔可夫性)** in continuous time.

**Why this matters**: Understanding the exponential holding time structure allows us to:
- Model real-world waiting phenomena (bus arrivals, customer service times, equipment failures)
- Compute probabilities and expectations for arrival times
- Connect discrete-time Markov chains to continuous-time processes
- Lay the foundation for more complex continuous-time Markov processes

---

## 🎯 Learning Objectives / 学习目标

By the end of this section, you will be able to:

1. **Define** the exponential distribution and recall its key properties (PDF, CDF, mean, variance, memoryless property)
2. **Prove** that the Poisson process has exponentially distributed holding times
3. **Apply** the exponential holding time structure to compute probabilities and expectations
4. **State and verify** the Markov property for continuous-time processes
5. **Solve** problems involving the minimum of independent exponential random variables
6. **Use** both the Poisson increment definition and the exponential holding time definition interchangeably

---

## 📚 Prerequisites / 前置知识

Before studying this section, you should be familiar with:

| Concept | Details |
|---------|---------|
| **Poisson distribution (泊松分布)** | \(X \sim \text{Po}(\lambda)\), PMF: \(\mathbb{P}(X = k) = e^{-\lambda} \lambda^k / k!\) |
| **Poisson process definition** | Independent increments, \(X(t) - X(s) \sim \text{Po}(\lambda(t-s))\) |
| **Conditional probability (条件概率)** | \(\mathbb{P}(A \mid B) = \mathbb{P}(A \cap B) / \mathbb{P}(B)\) |
| **Independence (独立性)** | \(\mathbb{P}(A \cap B) = \mathbb{P}(A)\mathbb{P}(B)\) for independent events |
| **Expectation and variance (期望与方差)** | Basic properties: \(\mathbb{E}[aX+b] = a\mathbb{E}[X]+b\), \(\text{Var}(aX) = a^2\text{Var}(X)\) |
| **Normal approximation (正态近似)** | Using CLT to approximate sums of random variables |

---

## 📖 Core Content / 核心内容

---

### Topic 1: The Exponential Distribution / 指数分布

#### Intuition / 直觉理解

The **exponential distribution (指数分布)** is the continuous-time analogue of the geometric distribution. It models the **waiting time (等待时间)** until an event occurs, assuming the event happens at a constant average rate.

**Real-world examples**:
- Time until a light bulb burns out
- Time between bus arrivals at a stop
- Time between withdrawals from a bank account
- Time until a radioactive particle decays

**Key intuition**: If events occur randomly at a constant average rate \(\lambda\) per unit time, then the time between consecutive events follows an exponential distribution with rate \(\lambda\).

#### Formal Definition / 形式化定义

**Definition**: A continuous random variable \(T\) has the **exponential distribution (指数分布)** with **rate (速率)** \(\lambda > 0\), written as:

\[
T \sim \text{Exp}(\lambda)
\]

if it has the **probability density function (PDF, 概率密度函数)**:

\[
f(t) = \lambda e^{-\lambda t} \quad \text{for } t \geq 0
\]

where:
- \(f(t)\) = probability density at time \(t\)
- \(\lambda\) = rate parameter (average number of events per unit time)
- \(e^{-\lambda t}\) = exponential decay factor
- \(t \geq 0\) = time is non-negative

#### Key Properties / 关键性质

**1. Cumulative Distribution Function (CDF, 累积分布函数)**:

\[
F(t) = \mathbb{P}(T \leq t) = 1 - e^{-\lambda t} \quad \text{for } t \geq 0
\]

**2. Tail Probability (尾部概率)**:

\[
\mathbb{P}(T > t) = 1 - F(t) = e^{-\lambda t} \quad \text{for } t \geq 0
\]

This is often more convenient to work with than the CDF.

**3. Mean (期望) and Variance (方差)**:

\[
\mathbb{E}[T] = \frac{1}{\lambda}, \quad \text{Var}(T) = \frac{1}{\lambda^2}
\]

where:
- \(\mathbb{E}[T]\) = expected waiting time
- \(\text{Var}(T)\) = variance of waiting time
- Note: mean = standard deviation = \(1/\lambda\)

**4. Memoryless Property (无记忆性)** - Theorem 14.1:

\[
\mathbb{P}(T > t + s \mid T > t) = \mathbb{P}(T > s) \quad \text{for all } s, t \geq 0
\]

**Interpretation**: If you've already waited \(t\) units of time without the event occurring, the remaining waiting time is still exponentially distributed with the same rate \(\lambda\). The process "forgets" how long you've already waited.

#### Proof of Memoryless Property / 无记忆性证明

**Theorem 14.1**: Let \(T \sim \text{Exp}(\lambda)\). Then for any \(s, t \geq 0\):

\[
\mathbb{P}(T > t + s \mid T > t) = \mathbb{P}(T > s)
\]

**Proof**:

**Step 1**: Write the conditional probability using the definition:

\[
\mathbb{P}(T > t + s \mid T > t) = \frac{\mathbb{P}(T > t + s \text{ and } T > t)}{\mathbb{P}(T > t)}
\]

**Step 2**: Note that the event \(\{T > t + s\}\) is a subset of \(\{T > t\}\) (if \(T > t+s\), then certainly \(T > t\)). So:

\[
\mathbb{P}(T > t + s \text{ and } T > t) = \mathbb{P}(T > t + s)
\]

**Step 3**: Substitute the tail probabilities:

\[
\frac{\mathbb{P}(T > t + s)}{\mathbb{P}(T > t)} = \frac{e^{-\lambda(t+s)}}{e^{-\lambda t}}
\]

**Step 4**: Simplify using exponent rules:

\[
\frac{e^{-\lambda(t+s)}}{e^{-\lambda t}} = e^{-\lambda(t+s - t)} = e^{-\lambda s}
\]

**Step 5**: Recognize that \(e^{-\lambda s} = \mathbb{P}(T > s)\), completing the proof.

\[
\boxed{\mathbb{P}(T > t + s \mid T > t) = e^{-\lambda s} = \mathbb{P}(T > s)}
\]

**Commentary**: This proof is elegant because it uses only the tail probability formula and basic algebra. The key insight is that the exponential function's multiplicative property (\(e^{a+b} = e^a e^b\)) directly gives the memoryless property.

---

### Topic 2: Minimum of Independent Exponentials / 独立指数分布的最小值

#### Intuition / 直觉理解

Suppose you have multiple independent "alarms" that each ring after an exponentially distributed time. The **minimum (最小值)** of these times represents the time until the **first** alarm rings. Intuitively, if you have more alarms, the first one rings sooner - the rate of the minimum is the sum of the individual rates.

#### Theorem 14.2 / 定理14.2

**Statement**: Let \(T_1 \sim \text{Exp}(\lambda_1), T_2 \sim \text{Exp}(\lambda_2), \ldots, T_n \sim \text{Exp}(\lambda_n)\) be independent exponential random variables. Define:

\[
T = \min\{T_1, T_2, \ldots, T_n\}
\]

Then:

1. **Distribution of the minimum**:
   \[
   T \sim \text{Exp}(\lambda_1 + \lambda_2 + \cdots + \lambda_n)
   \]

2. **Probability that a specific variable is the minimum**:
   \[
   \mathbb{P}(T = T_j) = \frac{\lambda_j}{\lambda_1 + \lambda_2 + \cdots + \lambda_n}
   \]

#### Proof Sketch / 证明思路

The full proof is assigned as a problem sheet question. Here's the key idea:

**Part 1 (Distribution of minimum)**:

\[
\mathbb{P}(T > t) = \mathbb{P}(\min\{T_1, \ldots, T_n\} > t)
\]

Since the minimum is greater than \(t\) if and only if **all** \(T_i > t\):

\[
\mathbb{P}(T > t) = \mathbb{P}(T_1 > t, T_2 > t, \ldots, T_n > t)
\]

By independence:

\[
\mathbb{P}(T > t) = \mathbb{P}(T_1 > t) \cdot \mathbb{P}(T_2 > t) \cdots \mathbb{P}(T_n > t)
\]

Using tail probabilities:

\[
\mathbb{P}(T > t) = e^{-\lambda_1 t} \cdot e^{-\lambda_2 t} \cdots e^{-\lambda_n t} = e^{-(\lambda_1 + \lambda_2 + \cdots + \lambda_n)t}
\]

This is the tail probability of \(\text{Exp}(\lambda_1 + \cdots + \lambda_n)\), so \(T \sim \text{Exp}(\lambda_1 + \cdots + \lambda_n)\).

**Part 2 (Probability of being minimum)**: The probability that \(T_j\) is the minimum equals the probability that \(T_j\) is smaller than all others. This can be computed by conditioning on \(T_j = t\) and integrating.

#### Worked Example / 例题

**Example**: Three independent exponential random variables:
- \(T_1 \sim \text{Exp}(2)\) (rate 2)
- \(T_2 \sim \text{Exp}(3)\) (rate 3)
- \(T_3 \sim \text{Exp}(5)\) (rate 5)

**Question**: What is the distribution of \(T = \min\{T_1, T_2, T_3\}\)?

**Solution**:
\[
T \sim \text{Exp}(2 + 3 + 5) = \text{Exp}(10)
\]

So the expected time until the first event is \(\mathbb{E}[T] = 1/10 = 0.1\) time units.

**Question**: What is the probability that \(T_2\) is the smallest?

**Solution**:
\[
\mathbb{P}(T = T_2) = \frac{\lambda_2}{\lambda_1 + \lambda_2 + \lambda_3} = \frac{3}{2 + 3 + 5} = \frac{3}{10} = 0.3
\]

---

### Topic 3: Definition 2 - Exponential Holding Times / 定义2：指数停留时间

#### Intuition / 直觉理解

Instead of counting arrivals in a fixed time interval, we can define the Poisson process by describing the **waiting times (停留时间)** between arrivals:

- Start at time 0 with 0 arrivals
- Wait an exponential amount of time for the first arrival
- After the first arrival, wait another independent exponential amount of time for the second arrival
- Continue this process indefinitely

This is like a **conveyor belt (传送带)** where items arrive at random intervals, and the time between items follows an exponential distribution.

#### Formal Definition / 形式化定义

**Definition (Exponential Holding Time Structure)**: A process \((X(t))\) with the following properties:

1. **Initial condition**: \(X(0) = 0\)

2. **Holding times**: Let \(T_1, T_2, T_3, \ldots \sim \text{Exp}(\lambda)\) be independent and identically distributed exponential random variables.

3. **Process definition**:
   \[
   X(t) = 
   \begin{cases}
   0 & \text{for } 0 \leq t < T_1 \\
   1 & \text{for } T_1 \leq t < T_1 + T_2 \\
   2 & \text{for } T_1 + T_2 \leq t < T_1 + T_2 + T_3 \\
   \vdots & \vdots
   \end{cases}
   \]

where:
- \(X(t)\) = number of arrivals by time \(t\)
- \(T_i\) = holding time between \((i-1)\)-th and \(i\)-th arrival
- \(\lambda\) = rate parameter

#### Theorem 14.3: Equivalence of Definitions / 定理14.3：定义的等价性

**Statement**: A Poisson process with rate \(\lambda\) (defined by independent Poisson increments) has the exponential holding time structure described above.

**Proof**:

**Part 1: Distribution of first holding time \(T_1\)**

We want to find \(\mathbb{P}(T_1 > t_1)\), the probability that the first arrival occurs after time \(t_1\).

**Step 1**: The first arrival occurs after \(t_1\) if and only if there are **zero arrivals** in the interval \([0, t_1]\).

\[
\mathbb{P}(T_1 > t_1) = \mathbb{P}(X(t_1) - X(0) = 0)
\]

**Step 2**: By the Poisson increment property, \(X(t_1) - X(0) \sim \text{Po}(\lambda t_1)\).

\[
\mathbb{P}(X(t_1) - X(0) = 0) = \frac{e^{-\lambda t_1} (\lambda t_1)^0}{0!} = e^{-\lambda t_1}
\]

**Step 3**: Recognize \(e^{-\lambda t_1}\) as the tail probability of \(\text{Exp}(\lambda)\).

\[
\mathbb{P}(T_1 > t_1) = e^{-\lambda t_1} \implies T_1 \sim \text{Exp}(\lambda)
\]

**Part 2: Distribution of second holding time \(T_2\) given \(T_1 = t_1\)**

**Step 1**: Condition on the first arrival time being exactly \(t_1\).

\[
\mathbb{P}(T_2 > t_2 \mid T_1 = t_1) = \mathbb{P}(X(t_1 + t_2) - X(t_1) = 0)
\]

**Step 2**: By the independent increments property, \(X(t_1 + t_2) - X(t_1) \sim \text{Po}(\lambda t_2)\).

\[
\mathbb{P}(X(t_1 + t_2) - X(t_1) = 0) = e^{-\lambda t_2}
\]

**Step 3**: This is the tail probability of \(\text{Exp}(\lambda)\), independent of \(t_1\).

\[
\mathbb{P}(T_2 > t_2 \mid T_1 = t_1) = e^{-\lambda t_2} \implies T_2 \sim \text{Exp}(\lambda) \text{ independent of } T_1
\]

**Part 3: General case**

Repeating this argument for all \(n\) gives the desired exponential holding time structure.

**Technical Note on Conditioning**: The proof conditions on \(\{T_1 = t_1\}\), which has probability 0 (continuous random variable). To make this rigorous:

\[
\mathbb{P}(T_2 > t_2 \mid T_1 = t_1) = \lim_{\varepsilon \to 0} \mathbb{P}(T_2 > t_2 \mid T_1 \in (t_1 - \varepsilon, t_1 + \varepsilon))
\]

Using the Poisson increment property:

\[
\lim_{\varepsilon \to 0} \mathbb{P}(X(t_1 + t_2 + \varepsilon) - X(t_1 - \varepsilon) = 0) = \lim_{\varepsilon \to 0} e^{-\lambda(t_2 + 2\varepsilon)} = e^{-\lambda t_2}
\]

A similar lower bound gives the same result, justifying the conditioning.

---

### Topic 4: Worked Example - Bookshop / 例题：书店

#### Example 14.1 / 例题14.1

**Problem**: Customers visit a second-hand bookshop at a rate of \(\lambda = 5\) per hour. Each customer buys a book with probability \(p = 0.4\).

**Questions**:
1. What is the expected time to make ten sales?
2. What is the standard deviation of this time?
3. What is the probability it takes more than an hour to sell the first book?

**Solution**:

**Step 1: Identify the process**

The number of books sold is a **marked Poisson process (标记泊松过程)**. Each customer independently buys a book with probability \(p = 0.4\). The sales process is itself a Poisson process with rate:

\[
\lambda_{\text{sales}} = p \cdot \lambda = 0.4 \times 5 = 2 \text{ sales per hour}
\]

**Step 2: Expected time for 10 sales**

Let \(T_1, T_2, \ldots, T_{10}\) be the holding times between sales. Each \(T_i \sim \text{Exp}(2)\).

The time of the 10th sale is \(J_{10} = T_1 + T_2 + \cdots + T_{10}\).

\[
\mathbb{E}[J_{10}] = \mathbb{E}[T_1 + T_2 + \cdots + T_{10}] = 10 \cdot \mathbb{E}[T_1]
\]

Since \(\mathbb{E}[T_1] = 1/\lambda = 1/2 = 0.5\) hours:

\[
\mathbb{E}[J_{10}] = 10 \times 0.5 = 5 \text{ hours}
\]

**Step 3: Variance and standard deviation**

By independence of holding times:

\[
\text{Var}(J_{10}) = \text{Var}(T_1 + T_2 + \cdots + T_{10}) = 10 \cdot \text{Var}(T_1)
\]

Since \(\text{Var}(T_1) = 1/\lambda^2 = 1/2^2 = 1/4 = 0.25\):

\[
\text{Var}(J_{10}) = 10 \times 0.25 = 2.5
\]

Standard deviation:

\[
\text{SD}(J_{10}) = \sqrt{2.5} \approx 1.58 \text{ hours}
\]

**Step 4: Probability of waiting more than an hour for first sale**

**Method 1: Using exponential distribution**

The first sale occurs at time \(T_1 \sim \text{Exp}(2)\).

\[
\mathbb{P}(T_1 > 1) = e^{-\lambda \times 1} = e^{-2 \times 1} = e^{-2} \approx 0.135
\]

**Method 2: Using Poisson process**

The first sale occurs after 1 hour if and only if \(X(1) = 0\) (zero sales in the first hour).

\[
\mathbb{P}(X(1) = 0) = \frac{e^{-2 \times 1} (2 \times 1)^0}{0!} = e^{-2} \approx 0.135
\]

Both methods give the same answer, confirming the equivalence of the two definitions.

---

### Topic 5: Markov Property in Continuous Time / 连续时间马尔可夫性

#### Intuition / 直觉理解

The **Markov property (马尔可夫性)** says that the future depends on the present but not on the past. In continuous time, this means:

- To predict the state at time \(t_{n+1}\), you only need to know the state at time \(t_n\)
- The entire history before \(t_n\) gives no additional information

This is the continuous-time analogue of the discrete-time Markov property we studied earlier.

#### Formal Definition / 形式化定义

**Definition 14.1**: Let \((X(t))\) be a stochastic process on a **discrete state space (离散状态空间)** \(\mathcal{S}\) and **continuous time (连续时间)** \(t \in [0, \infty)\). We say that \((X(t))\) has the **Markov property (马尔可夫性)** if:

\[
\mathbb{P}(X(t_{n+1}) = x_{n+1} \mid X(t_n) = x_n, \ldots, X(t_1) = x_1, X(t_0) = x_0)
\]
\[
= \mathbb{P}(X(t_{n+1}) = x_{n+1} \mid X(t_n) = x_n)
\]

for all times \(t_0 < t_1 < \cdots < t_n < t_{n+1}\) and all states \(x_0, x_1, \ldots, x_n, x_{n+1} \in \mathcal{S}\).

**Symbol explanation**:
- \(t_0, t_1, \ldots, t_n, t_{n+1}\) = increasing sequence of times
- \(x_0, x_1, \ldots, x_n, x_{n+1}\) = states at those times
- \(\mathcal{S}\) = state space (e.g., \(\{0, 1, 2, \ldots\}\) for Poisson process)
- The left side conditions on the entire history
- The right side conditions only on the most recent time

#### Verification for Poisson Process / 泊松过程的验证

The Poisson process satisfies the Markov property. Two ways to see this:

**Method 1: Using independent increments**

\[
\mathbb{P}(X(t_{n+1}) = x_{n+1} \mid X(t_n) = x_n, \ldots, X(t_0) = x_0)
\]

Let \(x = x_{n+1} - x_n\) be the number of arrivals between \(t_n\) and \(t_{n+1}\).

By the independent increments property:

\[
= \mathbb{P}(X(t_{n+1}) - X(t_n) = x)
\]

Since \(X(t_{n+1}) - X(t_n) \sim \text{Po}(\lambda(t_{n+1} - t_n))\):

\[
= \frac{e^{-\lambda(t_{n+1} - t_n)} (\lambda(t_{n+1} - t_n))^x}{x!}
\]

This depends only on \(t_n\) and \(t_{n+1}\), not on earlier times.

**Method 2: Using memoryless property of exponential**

At time \(t_n\), the process has been in its current state for some time. By the memoryless property of the exponential distribution, the remaining holding time is still exponentially distributed with the same rate. This means the future evolution depends only on the current state, not on how long we've been there.

---

## 🔗 Connections / 知识关联

### Previous Topics / 先前内容

| Topic | Connection |
|-------|------------|
| **Poisson distribution (Section 13)** | The Poisson increment definition is equivalent to the exponential holding time definition |
| **Discrete-time Markov chains** | The Markov property in continuous time is the natural extension |
| **Geometric distribution** | The exponential distribution is the continuous analogue of the geometric distribution |

### Future Topics / 后续内容

| Topic | Connection |
|-------|------------|
| **Continuous-time Markov chains** | The Poisson process is the simplest example; general CTMCs have exponential holding times with state-dependent rates |
| **Queueing theory** | Exponential service times and inter-arrival times are fundamental |
| **Renewal processes** | Generalize exponential holding times to arbitrary distributions |

---

## ⚠️ Common Mistakes / 常见误区

1. **Confusing rate and mean**: The rate \(\lambda\) is NOT the expected waiting time. \(\mathbb{E}[T] = 1/\lambda\). A higher rate means shorter expected waiting time.

2. **Forgetting the memoryless property**: The exponential distribution is the ONLY continuous distribution with the memoryless property. Don't assume other distributions have it.

3. **Mixing up the two definitions**: The Poisson increment definition and exponential holding time definition are equivalent. Use whichever is more convenient for the problem.

4. **Incorrectly handling the minimum of exponentials**: The minimum of independent exponentials is exponential with rate equal to the SUM of rates, not the minimum rate.

5. **Ignoring the technicality in conditioning**: When conditioning on \(\{T_1 = t_1\}\) (probability 0), remember that a limiting argument is needed for rigor.

---

## ✍️ Practice / 练习

### Question 1
Let \((X(t))\) be a Poisson process with rate \(\lambda = 3\). Calculate:
(a) \(\mathbb{P}(X(0.5) = 0)\)
(b) \(\mathbb{E}[X(2)]\)
(c) \(\mathbb{P}(X(1) = 2 \text{ and } X(2) = 3)\)

**Hint**: Use the Poisson increment definition. For (c), consider the increment from 1 to 2.

### Question 2
For the Poisson process in Question 1, let \(T_1\) be the first holding time and \(J_5 = T_1 + \cdots + T_5\) be the 5th arrival time.
(a) Find \(\mathbb{P}(T_1 > 0.5)\)
(b) Find \(\mathbb{E}[J_5]\) and \(\text{Var}(J_5)\)

**Hint**: \(T_i \sim \text{Exp}(3)\), independent.

### Question 3
Two independent Poisson processes: \((X(t))\) with rate \(\lambda_1 = 2\) and \((Y(t))\) with rate \(\lambda_2 = 3\). What is the distribution of the time until the first arrival in either process?

**Hint**: Consider the minimum of two independent exponential random variables.

### Question 4
Verify the Markov property for a Poisson process with rate \(\lambda = 1\) by computing:
\[
\mathbb{P}(X(3) = 5 \mid X(2) = 3, X(1) = 1)
\]

**Hint**: This should equal \(\mathbb{P}(X(3) - X(2) = 2)\).

### Question 5
Let \(T_1 \sim \text{Exp}(2)\) and \(T_2 \sim \text{Exp}(3)\) be independent. Find:
(a) \(\mathbb{P}(\min(T_1, T_2) > 0.5)\)
(b) \(\mathbb{P}(T_1 < T_2)\)

**Hint**: For (b), use the formula \(\mathbb{P}(T_1 < T_2) = \lambda_1 / (\lambda_1 + \lambda_2)\).

---

## 📌 Key Takeaways / 要点总结

1. **Exponential distribution (指数分布)**: \(T \sim \text{Exp}(\lambda)\) has PDF \(f(t) = \lambda e^{-\lambda t}\), mean \(1/\lambda\), variance \(1/\lambda^2\).

2. **Memory