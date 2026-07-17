# Section 16: Counting Processes

> MATH2702 Stochastic Processes - 自学教材
> 生成时间: 2026-07-17 14:54
> 来源页: 79-82

---

# MATH2702 Study Guide / 学习指南
## Section 16: Counting Processes / 计数过程

---

### 📋 Section Overview / 章节概览

This section extends our understanding of counting processes beyond the Poisson process. We explore two important generalizations:

1. **Birth Processes (生灭过程)** - where the rate of events changes as the population grows
2. **Time Inhomogeneous Poisson Process (时间非齐次泊松过程)** - where the rate changes over time

**Why this matters / 为什么重要**: Real-world systems rarely have constant rates. Birth processes model population growth (biology, epidemiology), while time-inhomogeneous processes model systems with varying demand (call centers, traffic, insurance claims). Understanding these gives you tools to model more realistic scenarios.

---

### 🎯 Learning Objectives / 学习目标

After completing this section, you will be able to:

1. **Define** and **distinguish** between birth processes, simple birth processes, and time-inhomogeneous Poisson processes
2. **Derive** the forward equations (Kolmogorov forward equations) for birth processes
3. **Calculate** probabilities for time-inhomogeneous Poisson processes using integration of rate functions
4. **Solve** the forward equations for the simple birth process to find the probability distribution
5. **Compute** expected values for both birth processes and time-inhomogeneous Poisson processes
6. **Apply** these models to real-world scenarios (call centers, cell division, immigration)

---

### 📚 Prerequisites / 前置知识

Before studying this section, you should be comfortable with:

| Concept | Details |
|---------|---------|
| **Poisson Process (泊松过程)** | Definition, properties, exponential holding times |
| **Exponential Distribution (指数分布)** | PDF: $f(t) = \lambda e^{-\lambda t}$, mean $1/\lambda$, memoryless property |
| **Minimum of Exponentials (指数最小值)** | $\min(\text{Exp}(\lambda_1),...,\text{Exp}(\lambda_n)) \sim \text{Exp}(\lambda_1+...+\lambda_n)$ |
| **Poisson Distribution (泊松分布)** | $P(X=k) = e^{-\lambda}\lambda^k/k!$, mean $\lambda$ |
| **Integration (积分)** | Basic definite integrals, especially $\int t\,dt = t^2/2$ |
| **Differential Equations (微分方程)** | First-order linear ODEs: $y' + ay = 0$ solution $y = Ce^{-at}$ |
| **Geometric Distribution (几何分布)** | $P(X=k) = (1-p)^{k-1}p$, mean $1/p$ |

---

### 📖 Core Content / 核心内容

---

#### Topic 1: Birth Processes / 生灭过程

##### Intuition / 直觉理解

**Why counting processes? / 为什么是计数过程?**

The Poisson process was easier to understand because it's a **counting process (计数过程)** - it counts arrivals. We always knew the next change would be an increase by 1; the only question was **when** that increase would happen.

**The key insight / 关键洞察**: In a counting process, transitions are always from state $i$ to state $i+1$ (increase by 1). The difference between processes lies in the **holding times (停留时间)** - how long we wait between events.

**Simple Birth Process (简单生灭过程)** - Example: Cell Division

Imagine starting with 1 cell. After an exponential time with rate $\lambda$, the cell divides into 2 cells. Now we have 2 cells, each of which will divide after an exponential time with rate $\lambda$. The next division happens when the **first** of these 2 cells divides - this is the **minimum** of two exponential random variables.

**Key property**: When you have $n$ individuals, each waiting an Exp($\lambda$) time to produce offspring, the time until the **next** offspring is Exp($n\lambda$). This is because:
- Each individual has "memoryless" remaining time
- The minimum of $n$ i.i.d. Exp($\lambda$) variables is Exp($n\lambda$)
- The mean holding time decreases as population grows: $\mathbb{E}[T_n] = 1/(n\lambda)$

**Population growth / 种群增长**: The expected population size at time $t$ is $\mathbb{E}[X(t)] = e^{\lambda t}$ - exponential growth!

---

##### Formal Definition / 形式化定义

**Definition 16.1: Birth Process (生灭过程)**

A **birth process** $(X_n)$ with **rates** $(\lambda_n)$ is defined by:

- **Starting population**: $X(0) = x_0$ (初始种群数量)
- **Holding times**: $T_n \sim \text{Exp}(\lambda_n)$ (停留时间服从指数分布)

The process is:
$$X(t) = \begin{cases}
x_0 & 0 \leq t < J_1 \\
x_0 + n & J_n \leq t < J_{n+1}, \text{ for } n = 1, 2, \ldots
\end{cases}$$

Where:
- $X(t)$ = population size at time $t$ (t时刻的种群数量)
- $x_0$ = initial population (初始数量)
- $T_n$ = $n$th holding time, the time spent in state $x_0 + n - 1$ (第n个停留时间)
- $J_n = T_1 + T_2 + \cdots + T_n$ = **jump times (跳跃时间)** - the time of the $n$th birth
- $\lambda_n$ = rate parameter when population is $n$ (当种群数量为n时的速率参数)
- $\text{Exp}(\lambda_n)$ = exponential distribution with rate $\lambda_n$, mean $1/\lambda_n$

**Important**: The notation $T_n \sim \text{Exp}(\lambda_n)$ means:
- $T_n$ has PDF $f(t) = \lambda_n e^{-\lambda_n t}$ for $t \geq 0$
- $\mathbb{E}[T_n] = 1/\lambda_n$
- $\text{Var}(T_n) = 1/\lambda_n^2$

---

**Examples of Birth Processes / 生灭过程的例子**

| Process | $x_0$ | $\lambda_n$ | Description |
|---------|-------|-------------|-------------|
| **Simple Birth Process (简单生灭过程)** | 1 | $\lambda_n = n\lambda$ | Each individual reproduces at rate $\lambda$ |
| **Poisson Process (泊松过程)** | 0 | $\lambda_n = \lambda$ (constant) | Constant arrival rate regardless of state |
| **Birth with Immigration (带移民的生灭过程)** | 1 | $\lambda_n = n\lambda + \mu$ | Internal births at rate $n\lambda$, external immigration at rate $\mu$ |

---

**Infinitesimal Definition (无穷小定义)**

For a birth process starting from $X(0) = 1$, for small $\tau > 0$:

$$\mathbb{P}(X(t+\tau) = j \mid X(t) = j) = 1 - \lambda_j \tau + o(\tau)$$
$$\mathbb{P}(X(t+\tau) = j+1 \mid X(t) = j) = \lambda_j \tau + o(\tau)$$
$$\mathbb{P}(X(t+\tau) \geq j+2 \mid X(t) = j) = o(\tau)$$

Where:
- $\mathbb{P}(A \mid B)$ = probability of A given B (条件概率)
- $\lambda_j$ = rate when population is $j$ (当种群数量为j时的速率)
- $\tau$ = small time increment (微小时间增量)
- $o(\tau)$ = "little-o of tau" - a term that goes to 0 faster than $\tau$ as $\tau \to 0$ (比τ更快趋于0的量)
  - Formally: $\lim_{\tau \to 0} o(\tau)/\tau = 0$

**Interpretation / 解释**:
- Probability of **no change** in $(t, t+\tau)$: $1 - \lambda_j\tau$ (plus negligible term)
- Probability of **one birth** in $(t, t+\tau)$: $\lambda_j\tau$ (plus negligible term)
- Probability of **two or more births** in $(t, t+\tau)$: negligible ($o(\tau)$)

This is exactly the same as the Poisson process, except with $\lambda$ replaced by $\lambda_j$ (the rate depends on the current state).

---

##### Key Properties / 关键性质

**Property 1: Forward Equations (Kolmogorov Forward Equations)**

Let $p_j(t) = \mathbb{P}(X(t) = j)$ be the probability that the population is exactly $j$ at time $t$.

**For $j \geq 2$**:
$$p'_j(t) = -\lambda_j p_j(t) + \lambda_{j-1} p_{j-1}(t)$$

**For $j = 1$**:
$$p'_1(t) = -\lambda_1 p_1(t)$$

**Initial conditions** (starting from $X(0) = 1$):
- $p_1(0) = 1$ (we start with 1 individual)
- $p_j(0) = 0$ for all $j \geq 2$ (we don't start with more than 1)

**Derivation / 推导** (for $j \geq 2$):

Step 1: Consider $p_j(t+\tau)$ - the probability of being in state $j$ at time $t+\tau$.

There are two ways to be in state $j$ at time $t+\tau$:
1. **Already at $j$ at time $t$** AND **no birth occurs** in $(t, t+\tau)$
2. **At $j-1$ at time $t$** AND **one birth occurs** in $(t, t+\tau)$

All other possibilities (e.g., being at $j-2$ and having two births) have probability $o(\tau)$.

Step 2: Write the equation:
$$p_j(t+\tau) = (1 - \lambda_j\tau + o(\tau))p_j(t) + (\lambda_{j-1}\tau + o(\tau))p_{j-1}(t) + o(\tau)$$

Step 3: Rearrange:
$$p_j(t+\tau) - p_j(t) = -\lambda_j\tau p_j(t) + \lambda_{j-1}\tau p_{j-1}(t) + o(\tau)$$

Step 4: Divide by $\tau$:
$$\frac{p_j(t+\tau) - p_j(t)}{\tau} = -\lambda_j p_j(t) + \lambda_{j-1} p_{j-1}(t) + \frac{o(\tau)}{\tau}$$

Step 5: Take limit as $\tau \to 0$:
- Left side becomes $p'_j(t)$ (derivative)
- Right side: $o(\tau)/\tau \to 0$
- Result: $p'_j(t) = -\lambda_j p_j(t) + \lambda_{j-1} p_{j-1}(t)$

**For $j=1$**: Similar derivation, but there's no state 0 to come from (since we start at 1 and only increase), so:
$$p'_1(t) = -\lambda_1 p_1(t)$$

---

**Property 2: Simple Birth Process Solution**

For the simple birth process with $\lambda_n = n\lambda$ and $X(0) = 1$:

$$p_j(t) = (1 - e^{-\lambda t})^{j-1} e^{-\lambda t}$$

This is a **Geometric distribution (几何分布)**:
$$X(t) \sim \text{Geom}(e^{-\lambda t})$$

Where:
- $p = e^{-\lambda t}$ is the "success probability" (probability of no birth in time $t$)
- $j$ starts at 1 (minimum population)
- $\mathbb{P}(X(t) = j) = (1-p)^{j-1}p$

**Expected population size / 期望种群数量**:
$$\mathbb{E}[X(t)] = \frac{1}{p} = \frac{1}{e^{-\lambda t}} = e^{\lambda t}$$

---

##### Proof / 证明: Simple Birth Process Solution

**Goal**: Show that $p_j(t) = (1 - e^{-\lambda t})^{j-1} e^{-\lambda t}$ satisfies the forward equations.

**Step 1: Write the forward equations for simple birth process**

For $\lambda_n = n\lambda$:
- For $j = 1$: $p'_1(t) = -\lambda \cdot 1 \cdot p_1(t) = -\lambda p_1(t)$
- For $j \geq 2$: $p'_j(t) = -j\lambda p_j(t) + (j-1)\lambda p_{j-1}(t)$

Initial conditions: $p_1(0) = 1$, $p_j(0) = 0$ for $j \geq 2$.

**Step 2: Check $j = 1$**

Proposed solution: $p_1(t) = (1 - e^{-\lambda t})^{0} e^{-\lambda t} = e^{-\lambda t}$

Left side: $p'_1(t) = -\lambda e^{-\lambda t}$

Right side: $-\lambda p_1(t) = -\lambda e^{-\lambda t}$

✓ They match! And $p_1(0) = e^0 = 1$ ✓

**Step 3: Check $j \geq 2$**

Proposed solution: $p_j(t) = (1 - e^{-\lambda t})^{j-1} e^{-\lambda t}$

Let $u = e^{-\lambda t}$. Then $1 - e^{-\lambda t} = 1 - u$.

So $p_j(t) = (1-u)^{j-1} u$

**Step 3a: Compute derivative $p'_j(t)$**

Using chain rule: $\frac{d}{dt} = \frac{du}{dt} \cdot \frac{d}{du} = (-\lambda e^{-\lambda t}) \frac{d}{du} = -\lambda u \frac{d}{du}$

$p'_j(t) = -\lambda u \cdot \frac{d}{du}[(1-u)^{j-1} u]$

$= -\lambda u \cdot [-(j-1)(1-u)^{j-2} \cdot u + (1-u)^{j-1} \cdot 1]$

$= -\lambda u \cdot [-(j-1)(1-u)^{j-2}u + (1-u)^{j-1}]$

$= \lambda u (j-1)(1-u)^{j-2}u - \lambda u (1-u)^{j-1}$

$= \lambda (j-1)(1-u)^{j-2}u^2 - \lambda u (1-u)^{j-1}$

**Step 3b: Compute right side of forward equation**

Right side: $-j\lambda p_j(t) + (j-1)\lambda p_{j-1}(t)$

First term: $-j\lambda (1-u)^{j-1}u$

Second term: $(j-1)\lambda (1-u)^{j-2}u$

So right side $= -j\lambda (1-u)^{j-1}u + (j-1)\lambda (1-u)^{j-2}u$

**Step 3c: Compare left and right sides**

Left side: $\lambda (j-1)(1-u)^{j-2}u^2 - \lambda u (1-u)^{j-1}$

Right side: $-j\lambda (1-u)^{j-1}u + (j-1)\lambda (1-u)^{j-2}u$

Factor left side: $\lambda u (1-u)^{j-2}[(j-1)u - (1-u)] = \lambda u (1-u)^{j-2}[(j-1)u - 1 + u] = \lambda u (1-u)^{j-2}[ju - 1]$

Factor right side: $\lambda u (1-u)^{j-2}[-(j)(1-u) + (j-1)] = \lambda u (1-u)^{j-2}[-j + ju + j - 1] = \lambda u (1-u)^{j-2}[ju - 1]$

✓ They match!

**Step 4: Verify initial condition**

$p_j(0) = (1 - e^{0})^{j-1} e^{0} = (1-1)^{j-1} \cdot 1 = 0^{j-1}$

For $j=1$: $0^0 = 1$ ✓
For $j \geq 2$: $0^{j-1} = 0$ ✓

**Conclusion**: The proposed solution satisfies the forward equations and initial conditions, so it is correct.

---

##### Worked Examples / 例题

**Example 16.1: Simple Birth Process - Expected Population**

**Problem**: For a simple birth process with $\lambda = 0.5$ per hour, starting with 1 individual, what is the expected population after 3 hours?

**Solution**:

Step 1: Recall the formula for expected population
$$\mathbb{E}[X(t)] = e^{\lambda t}$$

Step 2: Substitute values
- $\lambda = 0.5$
- $t = 3$

$$\mathbb{E}[X(3)] = e^{0.5 \times 3} = e^{1.5}$$

Step 3: Calculate
$$e^{1.5} \approx 4.48$$

**Answer**: The expected population after 3 hours is approximately 4.48 individuals.

---

**Example 16.2: Birth Process with Immigration**

**Problem**: Consider a birth process with immigration: $\lambda_n = n\lambda + \mu$, starting from $X(0) = 1$. If $\lambda = 0.1$ and $\mu = 0.5$, what is the rate of the first birth? What about the second birth?

**Solution**:

Step 1: First holding time $T_1$ has rate $\lambda_1$
$$\lambda_1 = 1 \times 0.1 + 0.5 = 0.6$$

So $T_1 \sim \text{Exp}(0.6)$, mean $1/0.6 \approx 1.67$ time units.

Step 2: Second holding time $T_2$ has rate $\lambda_2$
$$\lambda_2 = 2 \times 0.1 + 0.5 = 0.7$$

So $T_2 \sim \text{Exp}(0.7)$, mean $1/0.7 \approx 1.43$ time units.

**Interpretation**: The immigration adds a constant rate $\mu = 0.5$ regardless of population size, while the birth rate increases with population.

---

#### Topic 2: Time Inhomogeneous Poisson Process / 时间非齐次泊松过程

##### Intuition / 直觉理解

**The Problem with Constant Rate / 恒定速率的问题**

In the standard Poisson process, the arrival rate $\lambda$ is constant - calls arrive at the same rate at 2 AM as at 2 PM. But real life is different:
- Call centers: busy in morning, quiet at lunch, busy again in afternoon
- Traffic: rush hour vs. midnight
- Insurance claims: more after natural disasters

**The Solution / 解决方案**: Let the rate depend on time: $\lambda = \lambda(t)$

This creates a **time inhomogeneous (时间非齐次)** process - the transition probabilities depend on the current time $t$, not just on the length of the time interval.

**Key difference from homogeneous processes / 与齐次过程的关键区别**:
- **Homogeneous (齐次)**: $\mathbb{P}(X(t+s) = j \mid X(t) = i)$ depends only on $i$, $j$, and $s$ (the length of time), not on $t$ (the current time)
- **Inhomogeneous (非齐次)**: The probability depends on $t$ as well, because the rate changes over time

**The Key Formula / 关键公式**: Instead of $\lambda s$ for the mean number of arrivals in interval of length $s$, we use:
$$\int_t^{t+s} \lambda(u) \, du$$

This is the **integrated rate (积分速率)** over the interval.

---

##### Formal Definition / 形式化定义

**Definition 16.2: Time Inhomogeneous Poisson Process (时间非齐次泊松过程)**

A stochastic process $(X(t))$ with:
- **Time**: $t \in [0, \infty)$ (continuous time)
- **State space**: $\mathcal{S} = \mathbb{Z}_+ = \{0, 1, 2, \ldots\}$ (non-negative integers)
- **Rate function**: $\lambda(t) \geq 0$ (a function of time)

**Properties**:

1. **Initial condition**: $X(0) = 0$

2. **Poisson increments**: For all $s, t > 0$:
   $$X(t+s) - X(t) \sim \text{Po}\left(\int_t^{t+s} \lambda(u) \, du\right)$$
   
   Where:
   - $X(t+s) - X(t)$ = number of arrivals in $(t, t+s]$ (在区间(t, t+s]内的到达数)
   - $\text{Po}(m)$ = Poisson distribution with mean $m$ (均值为m的泊松分布)
   - $\int_t^{t+s} \lambda(u) \, du$ = integrated rate over the interval (区间上的积分速率)

3. **Independent increments**: For any $t_1 \leq t_2 \leq t_3 \leq t_4$:
   $$X(t_2) - X(t_1) \text{ and } X(t_4) - X(t_3) \text{ are independent}$$

**Special case**: If $\lambda(t) = \lambda$ (constant), then:
$$\int_t^{t+s} \lambda(u) \, du = \lambda s$$
And we recover the standard Poisson process definition.

---

**Infinitesimal Definition (无穷小定义)**

For small $\tau > 0$:

$$\mathbb{P}(X(t+\tau) - X(t) = j) = \begin{cases}
1 - \lambda(t)\tau + o(\tau) & \text{if } j = 0 \\
\lambda(t)\tau + o(\tau) & \text{if } j = 1 \\
o(\tau) & \text{if } j \geq 2
\end{cases}$$

The only difference from the standard Poisson process: $\lambda$ is replaced by $\lambda(t)$ - the "current rate" at time $t$.

---

##### Key Properties / 关键性质

**Property 1: Mean and Variance**

For a time inhomogeneous Poisson process:
$$\mathbb{E}[X(t+s) - X(t)] = \int_t^{t+s} \lambda(u) \, du$$
$$\text{Var}[X(t+s) - X(t)] = \int_t^{t+s} \lambda(u) \, du$$

Since the increment follows a Poisson distribution, mean equals variance.

**Property 2: Probability of $k$ arrivals**

$$\mathbb{P}(X(t+s) - X(t) = k) = \frac{e^{-\Lambda(t,s)} \Lambda(t,s)^k}{k!}$$

Where $\Lambda(t,s) = \int_t^{t+s} \lambda(u) \, du$ is the cumulative rate.

---

##### Worked Examples / 例题

**Example 16.3: Call Center - First 10 Minutes**

**Problem**: A call center models calls with rate function:
$$\lambda(t) = \begin{cases}
20t & 0 \leq t < 1 \\
20 & t \geq 1
\end{cases}$$
(calls per hour)

What is the probability of **no calls** in the first 10 minutes?

**Solution**:

Step 1: Convert 10 minutes to hours
$$10 \text{ minutes} = \frac{10}{60} = \frac{1}{6} \text{ hour}$$

Step 2: Calculate the integrated rate for $[0, 1/6]$
Since $1/6 < 1$, we use $\lambda(t) = 20t$:
$$\int_0^{1/6} \lambda(t) \, dt = \int_0^{1/6} 20t \, dt$$

Step 3: Evaluate the integral
$$\int_0^{1/6} 20t \, dt = [10t^2]_0^{1/6} = 10 \times \left(\frac{1}{6}\right)^2 - 10 \times 0^2 = \frac{10}{36} = 0.278$$

Step 4: Calculate probability of 0 calls
Number of calls in first 10 minutes $\sim \text{Po}(0.278)$

$$\mathbb{P}(\text{no calls}) = \frac{e^{-0.278} \times 0.278^0}{0!} = e^{-0.278}$$

Step 5: Compute
$$e^{-0.278} \approx 0.757$$

**Answer**: The probability of no calls in the first 10 minutes is approximately 0.757 (75.7%).

---

**Example 16.4: Call Center - First 2 Hours**

**Problem**: For the same call center, what is the **expected number** of calls in the first 2 hours?

**Solution**:

Step 1: The number of calls in $[0, 2]$ is Poisson with rate:
$$\int_0^2 \lambda(t) \, dt$$

Step 2: Split the integral at $t=1$ (where the rate function changes)
$$\int_0^2 \lambda(t) \, dt = \int_0^1 20t \, dt + \int_1^2 20 \, dt$$

Step 3: Evaluate each part
$$\int_0^1 20t \, dt = [10t^2]_0^1 = 10(1)^2 - 10(0)^2 = 10$$

$$\int_1^2 20 \, dt = [20t]_1^2 = 20(2) - 20(1) = 40 - 20 = 20$$

Step 4: Sum
$$\int_0^2 \lambda(t) \, dt = 10 + 20 = 30$$

**Answer**: The expected number of calls in the first 2 hours is 30.

---

**Example 16.5: Call Center - Probability of Exactly 1 Call in First Hour**

**Problem**: For the same call center, what is the probability of exactly 1 call in the first hour?

**Solution**:

Step 1: Calculate integrated rate for $[0, 1]$
$$\int_0^1 \lambda(t) \, dt = \int_0^1 20t \, dt = [10t^2]_0^1 = 10$$

Step 2: Number of calls in first hour $\sim \text{Po}(10)$

Step 3: Calculate probability
$$\mathbb{P}(\text{exactly 1 call}) = \frac{e^{-10} \times 10^1}{1!} = 10e^{-10}$$

Step 4: Compute
$$10e^{-10} \approx 10 \times