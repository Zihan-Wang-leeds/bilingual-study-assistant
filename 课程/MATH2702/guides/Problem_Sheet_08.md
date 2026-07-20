# Problem Sheet 8 - 详细解答 / Detailed Solutions

> MATH2702 Stochastic Processes
> 生成时间 / Generated: 2026-07-17 15:14
> 来源页 / Source Pages: 82-82

---

好的，作为大学数学导师，我将为MATH2702: 随机过程 的问题单8提供完整、详细的逐步解答。

---

### Question 1 / 第1题

**Problem / 题目原文:**
Let (𝑋(𝑡)) be a Poisson process with rate 𝜆.
(a) Fix 𝑛. What is the expected time between the 𝑛th arrival and the (𝑛+1)th arrival?
(b) Fix 𝑡. What is the expected time between the previous arrival before 𝑡 and the next arrival after 𝑡?
(c) Your answers to the previous two questions should be different. Explain why one should expect the second answer to be bigger than the first.

**中文翻译:**
设 (𝑋(𝑡)) 是一个速率为 𝜆 的泊松过程。
(a) 固定 𝑛。求第 𝑛 次到达和第 (𝑛+1) 次到达之间的期望时间。
(b) 固定 𝑡。求在时间 𝑡 之前最后一次到达和在时间 𝑡 之后第一次到达之间的期望时间。
(c) 你对前两个问题的答案应该是不同的。解释为什么第二个答案应该比第一个大。

**Knowledge Points / 考查知识点:**
- Poisson process properties (stationary and independent increments)
- Inter-arrival times (exponential distribution)
- Memoryless property of exponential distribution
- Inspection paradox / waiting time paradox

**Step-by-Step Solution / 逐步解答:**

**(a) Expected time between the nth and (n+1)th arrival**

*Step 1: Identify the distribution of inter-arrival times.*
For a Poisson process with rate λ, the inter-arrival times, i.e., the time between successive arrivals, are independent and identically distributed (i.i.d.) exponential random variables with mean 1/λ.
Let $T_n$ be the time between the $(n-1)$th and $n$th arrival. Then $T_n \sim \text{Exp}(\lambda)$.

*Step 2: Apply this to the specific interval.*
The time between the $n$th arrival and the $(n+1)$th arrival is exactly the inter-arrival time $T_{n+1}$.

*Step 3: Calculate the expectation.*
The expected value of an exponential random variable with rate λ is $1/\lambda$.
Therefore, $\mathbb{E}[T_{n+1}] = 1/\lambda$.

**Intermediate Result:** The expected time is $1/\lambda$.

**(b) Expected time between the previous arrival before t and the next arrival after t**

*Step 1: Define the relevant random variables.*
Let $A_t$ be the time of the last arrival before or at time $t$ (the "previous arrival").
Let $B_t$ be the time of the first arrival after time $t$ (the "next arrival").
We want to find $\mathbb{E}[B_t - A_t]$.

*Step 2: Decompose the interval.*
The interval $[A_t, B_t]$ can be split into two parts:
1.  The time since the last arrival: $S_t = t - A_t$ (the "age" or "backward recurrence time").
2.  The time until the next arrival: $R_t = B_t - t$ (the "residual life" or "forward recurrence time").
So, $B_t - A_t = S_t + R_t$.

*Step 3: Determine the distribution of $R_t$.*
Due to the memoryless property of the exponential distribution and the stationary increments of the Poisson process, the time until the next arrival $R_t$ is exponentially distributed with rate λ, regardless of $t$.
Thus, $\mathbb{E}[R_t] = 1/\lambda$.

*Step 4: Determine the distribution of $S_t$.*
For a Poisson process, the time since the last arrival $S_t$ also follows an exponential distribution with rate λ. This is a known property: the backward recurrence time has the same distribution as the forward recurrence time.
Thus, $\mathbb{E}[S_t] = 1/\lambda$.

*Step 5: Combine the expectations.*
Since $S_t$ and $R_t$ are independent (a property of the Poisson process), the expected total length is the sum of the expectations:
$\mathbb{E}[B_t - A_t] = \mathbb{E}[S_t] + \mathbb{E}[R_t] = 1/\lambda + 1/\lambda = 2/\lambda$.

**Intermediate Result:** The expected time is $2/\lambda$.

**(c) Explanation for the difference**

*Step 1: State the results.*
From (a), the expected time between two *specific consecutive* arrivals (the nth and (n+1)th) is $1/\lambda$.
From (b), the expected time between the arrival before a *fixed time* t and the arrival after t is $2/\lambda$.

*Step 2: Explain the "Inspection Paradox".*
The reason the second answer is larger is due to the **inspection paradox** (or waiting time paradox). When we fix a time $t$, we are more likely to "land" in a longer inter-arrival interval than a shorter one. This is because longer intervals occupy more time on the timeline, so a randomly chosen point $t$ has a higher probability of falling within them.

*Step 3: Elaborate on the bias.*
- In part (a), we are looking at a *specific* inter-arrival interval (the one between the nth and (n+1)th arrival). This is a "typical" interval with an expected length of $1/\lambda$.
- In part (b), we are looking at the *interval that contains the fixed time t*. This interval is not a "typical" one; it is "length-biased". The probability of an interval being selected is proportional to its length. Therefore, the expected length of the selected interval is longer than the expected length of a typical interval. In fact, for a Poisson process, the expected length of the interval containing a fixed point is $2/\lambda$, which is the sum of the expected forward and backward recurrence times.

**Final Answer / 最终答案:**
(a) $\boxed{1/\lambda}$
(b) $\boxed{2/\lambda}$
(c) The second answer is larger due to the inspection paradox. A fixed time $t$ is more likely to fall within a longer inter-arrival interval, biasing the expected length of the interval containing $t$ upwards.

**Key Insight / 解题要点:**
The memoryless property of the exponential distribution is key, but the inspection paradox shows that conditioning on a fixed time $t$ introduces a length bias, making the expected interval containing $t$ twice as long as a typical inter-arrival interval.

---

### Question 2 / 第2题

**Problem / 题目原文:**
Let 𝑋(𝑡) be a Poisson process with rate 𝜆, and mark each arrival independently with probability 𝑝.
Use the infinitesimals definition to show that the marked process is a Poisson process with rate 𝑝𝜆.

**中文翻译:**
设 𝑋(𝑡) 是一个速率为 𝜆 的泊松过程，并且独立地以概率 𝑝 标记每次到达。使用无穷小定义来证明标记过程是一个速率为 𝑝𝜆 的泊松过程。

**Knowledge Points / 考查知识点:**
- Definition of a Poisson process via infinitesimal probabilities
- Thinning of a Poisson process
- Independence of increments

**Step-by-Step Solution / 逐步解答:**

*Step 1: State the infinitesimal definition of a Poisson process.*
A counting process $N(t)$ is a Poisson process with rate $\lambda$ if:
1.  $N(0) = 0$.
2.  It has independent increments.
3.  For a small time interval $\Delta t$:
    - $\mathbb{P}(N(t+\Delta t) - N(t) = 0) = 1 - \lambda \Delta t + o(\Delta t)$
    - $\mathbb{P}(N(t+\Delta t) - N(t) = 1) = \lambda \Delta t + o(\Delta t)$
    - $\mathbb{P}(N(t+\Delta t) - N(t) \ge 2) = o(\Delta t)$

*Step 2: Define the marked process.*
Let $Y(t)$ be the number of marked arrivals up to time $t$. We want to show $Y(t)$ is a Poisson process with rate $p\lambda$.

*Step 3: Verify condition 1 (Initial condition).*
Since $X(0) = 0$, there are no arrivals at time 0, and therefore no marked arrivals. So $Y(0) = 0$. Condition 1 is satisfied.

*Step 4: Verify condition 2 (Independent increments).*
The original process $X(t)$ has independent increments. The marking of each arrival is independent of everything else. Therefore, the number of marked arrivals in disjoint time intervals depends only on the number of original arrivals in those intervals, which are independent. Since the marking is independent, the increments of $Y(t)$ are also independent. Condition 2 is satisfied.

*Step 5: Verify condition 3 (Infinitesimal probabilities).*
Consider a small time interval $[t, t+\Delta t)$. Let $\Delta X = X(t+\Delta t) - X(t)$ and $\Delta Y = Y(t+\Delta t) - Y(t)$.

*Step 5a: Calculate $\mathbb{P}(\Delta Y = 0)$.*
$\Delta Y = 0$ if either there are no arrivals in the interval ($\Delta X = 0$), or there are arrivals but none of them are marked.
$\mathbb{P}(\Delta Y = 0) = \mathbb{P}(\Delta X = 0) + \mathbb{P}(\Delta X = 1 \text{ and it is not marked}) + \mathbb{P}(\Delta X \ge 2 \text{ and none are marked})$.
Using the infinitesimal properties of $X(t)$:
$\mathbb{P}(\Delta X = 0) = 1 - \lambda \Delta t + o(\Delta t)$.
$\mathbb{P}(\Delta X = 1) = \lambda \Delta t + o(\Delta t)$. The probability this single arrival is not marked is $1-p$. So $\mathbb{P}(\Delta X = 1 \text{ and not marked}) = (1-p)\lambda \Delta t + o(\Delta t)$.
The probability of $\Delta X \ge 2$ is $o(\Delta t)$. Even if all are unmarked, the probability is at most $o(\Delta t)$.
Therefore,
$\mathbb{P}(\Delta Y = 0) = (1 - \lambda \Delta t) + (1-p)\lambda \Delta t + o(\Delta t) = 1 - p\lambda \Delta t + o(\Delta t)$.

*Step 5b: Calculate $\mathbb{P}(\Delta Y = 1)$.*
$\Delta Y = 1$ if there is exactly one arrival in the interval AND it is marked, OR there are two or more arrivals and exactly one of them is marked.
$\mathbb{P}(\Delta Y = 1) = \mathbb{P}(\Delta X = 1 \text{ and it is marked}) + \mathbb{P}(\Delta X \ge 2 \text{ and exactly one is marked})$.
$\mathbb{P}(\Delta X = 1 \text{ and marked}) = p \cdot \mathbb{P}(\Delta X = 1) = p(\lambda \Delta t + o(\Delta t)) = p\lambda \Delta t + o(\Delta t)$.
The probability of $\Delta X \ge 2$ is $o(\Delta t)$. The probability that exactly one of these is marked is at most the probability of $\Delta X \ge 2$, which is $o(\Delta t)$.
Therefore,
$\mathbb{P}(\Delta Y = 1) = p\lambda \Delta t + o(\Delta t)$.

*Step 5c: Calculate $\mathbb{P}(\Delta Y \ge 2)$.*
$\Delta Y \ge 2$ implies that $\Delta X \ge 2$ (you can't have more marked arrivals than total arrivals).
$\mathbb{P}(\Delta Y \ge 2) \le \mathbb{P}(\Delta X \ge 2) = o(\Delta t)$.
Therefore, $\mathbb{P}(\Delta Y \ge 2) = o(\Delta t)$.

*Step 6: Conclusion.*
The process $Y(t)$ satisfies all three conditions of the infinitesimal definition of a Poisson process with rate $p\lambda$. Therefore, the marked process is a Poisson process with rate $p\lambda$.

**Final Answer / 最终答案:**
The marked process $Y(t)$ satisfies the infinitesimal definition of a Poisson process with rate $p\lambda$, as shown by verifying the initial condition, independent increments, and the infinitesimal probabilities $\mathbb{P}(\Delta Y = 0) = 1 - p\lambda \Delta t + o(\Delta t)$, $\mathbb{P}(\Delta Y = 1) = p\lambda \Delta t + o(\Delta t)$, and $\mathbb{P}(\Delta Y \ge 2) = o(\Delta t)$. $\boxed{\text{The marked process is a Poisson process with rate } p\lambda.}$

**Key Insight / 解题要点:**
The proof relies on the "thinning" property: independently selecting events from a Poisson process results in another Poisson process whose rate is the original rate multiplied by the selection probability.

---

### Question 3 / 第3题

**Problem / 题目原文:**
Let (𝑋(𝑡)) be a simple birth process with rates 𝜆𝑗 = 𝜆𝑗 starting from 𝑋(0) = 1. Let 𝑝𝑗(𝑡) = ℙ(𝑋(𝑡) = 𝑗).
(a) Write down the Kolmogorov forward equations for 𝑝𝑗(𝑡). You should have separate equations for 𝑗 = 1 and 𝑗 ≥ 2. Remember to include the initial conditions 𝑝𝑗(0).
(b) Show that 𝑋(𝑡) follows a geometric distribution 𝑋(𝑡) ∼ Geom(𝑒^{−𝜆𝑡}). That is, show that
𝑝𝑗(𝑡) = (1−𝑒^{−𝜆𝑡})^{𝑗−1}𝑒^{−𝜆𝑡}
satisfies the forward equation.
(c) Hence, calculate 𝔼𝑋(𝑡), the expected population size at time 𝑡.

**中文翻译:**
设 (𝑋(𝑡)) 是一个简单生灭过程，其出生率为 𝜆𝑗 = 𝜆𝑗，从 𝑋(0) = 1 开始。设 𝑝𝑗(𝑡) = ℙ(𝑋(𝑡) = 𝑗)。
(a) 写出 𝑝𝑗(𝑡) 的 Kolmogorov 向前方程。你应该为 𝑗 = 1 和 𝑗 ≥ 2 分别写出方程。记得包括初始条件 𝑝𝑗(0)。
(b) 证明 𝑋(𝑡) 服从几何分布 𝑋(𝑡) ∼ Geom(𝑒^{−𝜆𝑡})。即，证明
𝑝𝑗(𝑡) = (1−𝑒^{−𝜆𝑡})^{𝑗−1}𝑒^{−𝜆𝑡}
满足向前方程。
(c) 由此计算 𝔼𝑋(𝑡)，即时间 𝑡 时的期望种群大小。

**Knowledge Points / 考查知识点:**
- Simple birth process (Yule process)
- Kolmogorov forward equations
- Solving differential-difference equations
- Geometric distribution and its expectation

**Step-by-Step Solution / 逐步解答:**

**(a) Kolmogorov Forward Equations**

*Step 1: General form of forward equations for a birth process.*
For a birth process with birth rates $\lambda_n$, the forward equation for $p_j(t)$ is:
$p_j'(t) = -\lambda_j p_j(t) + \lambda_{j-1} p_{j-1}(t)$ for $j \ge 1$, with the convention that $\lambda_0 = 0$ and $p_0(t) = 0$.

*Step 2: Apply the specific birth rates.*
Here, $\lambda_j = \lambda j$ for $j \ge 1$.

*Step 3: Write the equation for $j = 1$.*
For $j=1$, the term $\lambda_{j-1} p_{j-1}(t) = \lambda_0 p_0(t) = 0$.
So, $p_1'(t) = -\lambda_1 p_1(t) = -\lambda \cdot 1 \cdot p_1(t) = -\lambda p_1(t)$.

*Step 4: Write the equation for $j \ge 2$.*
For $j \ge 2$, both terms are present:
$p_j'(t) = -\lambda_j p_j(t) + \lambda_{j-1} p_{j-1}(t) = -\lambda j p_j(t) + \lambda (j-1) p_{j-1}(t)$.

*Step 5: State the initial conditions.*
The process starts from $X(0) = 1$. Therefore:
$p_1(0) = \mathbb{P}(X(0) = 1) = 1$.
$p_j(0) = \mathbb{P}(X(0) = j) = 0$ for all $j \ge 2$.

**Intermediate Result:**
The forward equations are:
$p_1'(t) = -\lambda p_1(t)$, with $p_1(0) = 1$.
$p_j'(t) = -\lambda j p_j(t) + \lambda (j-1) p_{j-1}(t)$, for $j \ge 2$, with $p_j(0) = 0$.

**(b) Verification of the Geometric Distribution Solution**

*Step 1: State the proposed solution.*
We want to show that $p_j(t) = (1 - e^{-\lambda t})^{j-1} e^{-\lambda t}$ satisfies the forward equations.

*Step 2: Verify the initial condition.*
At $t=0$, $e^{-\lambda \cdot 0} = 1$, so $1 - e^{-\lambda \cdot 0} = 0$.
For $j=1$: $p_1(0) = (1-1)^{0} \cdot 1 = 1$. Correct.
For $j \ge 2$: $p_j(0) = (1-1)^{j-1} \cdot 1 = 0$. Correct.

*Step 3: Verify the equation for $j=1$.*
First, find the derivative of $p_1(t) = e^{-\lambda t}$.
$p_1'(t) = -\lambda e^{-\lambda t}$.
The right-hand side of the forward equation for $j=1$ is $-\lambda p_1(t) = -\lambda e^{-\lambda t}$.
Since $p_1'(t) = -\lambda e^{-\lambda t}$, the equation holds.

*Step 4: Verify the equation for a general $j \ge 2$.*
Let $q(t) = 1 - e^{-\lambda t}$. Then $p_j(t) = q(t)^{j-1} e^{-\lambda t}$.
First, find the derivative $p_j'(t)$.
$q'(t) = \lambda e^{-\lambda t}$.
Using the product rule:
$p_j'(t) = (j-1) q(t)^{j-2} q'(t) e^{-\lambda t} + q(t)^{j-1} (-\lambda e^{-\lambda t})$
$p_j'(t) = (j-1) q(t)^{j-2} (\lambda e^{-\lambda t}) e^{-\lambda t} - \lambda q(t)^{j-1} e^{-\lambda t}$
$p_j'(t) = \lambda (j-1) q(t)^{j-2} e^{-2\lambda t} - \lambda q(t)^{j-1} e^{-\lambda t}$.

*Step 5: Compute the right-hand side (RHS) of the forward equation.*
RHS $= -\lambda j p_j(t) + \lambda (j-1) p_{j-1}(t)$.
First term: $-\lambda j p_j(t) = -\lambda j q(t)^{j-1} e^{-\lambda t}$.
Second term: $\lambda (j-1) p_{j-1}(t) = \lambda (j-1) q(t)^{j-2} e^{-\lambda t}$.

*Step 6: Show LHS = RHS.*
We need to show:
$\lambda (j-1) q(t)^{j-2} e^{-2\lambda t} - \lambda q(t)^{j-1} e^{-\lambda t} = -\lambda j q(t)^{j-1} e^{-\lambda t} + \lambda (j-1) q(t)^{j-2} e^{-\lambda t}$.

Let's rearrange the RHS to match the LHS. Factor out $\lambda (j-1) q(t)^{j-2} e^{-\lambda t}$ from the RHS where possible.
RHS $= \lambda (j-1) q(t)^{j-2} e^{-\lambda t} - \lambda j q(t)^{j-1} e^{-\lambda t}$.

Now, look at the LHS. The first term is $\lambda (j-1) q(t)^{j-2} e^{-2\lambda t} = \lambda (j-1) q(t)^{j-2} e^{-\lambda t} \cdot e^{-\lambda t}$.
The second term is $-\lambda q(t)^{j-1} e^{-\lambda t}$.

Let's try to manipulate the RHS to see if it equals the LHS.
RHS $= \lambda (j-1) q(t)^{j-2} e^{-\lambda t} - \lambda j q(t)^{j-1} e^{-\lambda t}$
$= \lambda (j-1) q(t)^{j-2} e^{-\lambda t} - \lambda (j-1+1) q(t)^{j-1} e^{-\lambda t}$
$= \lambda (j-1) q(t)^{j-2} e^{-\lambda t} - \lambda (j-1) q(t)^{j-1} e^{-\lambda t} - \lambda q(t)^{j-1} e^{-\lambda t}$
$= \lambda (j-1) q(t)^{j-2} e^{-\lambda t} (1 - q(t)) - \lambda q(t)^{j-1} e^{-\lambda t}$.

Since $q(t) = 1 - e^{-\lambda t}$, we have $1 - q(t) = e^{-\lambda t}$.
Substitute this into the expression:
RHS $= \lambda (j-1) q(t)^{j-2} e^{-\lambda t} \cdot e^{-\lambda t} - \lambda q(t)^{j-1} e^{-\lambda t}$
RHS $= \lambda (j-1) q(t)^{j-2} e^{-2\lambda t} - \lambda q(t)^{j-1} e^{-\lambda t}$.

This is exactly the LHS we calculated. Therefore, the proposed solution satisfies the forward equation.

**(c) Expected Population Size**

*Step 1: Identify the distribution.*
We have shown that $X(t) \sim \text{Geom}(e^{-\lambda t})$, where the geometric distribution is defined as the number of trials until the first success. In this parameterization, $p_j(t) = \mathbb{P}(X(t) = j) = (1-p)^{j-1} p$, where $p = e^{-\lambda t}$ is the "success" probability.

*Step 2: Recall the expectation of a geometric distribution.*
For a geometric random variable $Y$ with success probability $p$ (i.e., $\mathbb{P}(Y=k) = (1-p)^{k-1}p$ for $k=1,2,\dots$), the expectation is $\mathbb{E}[Y] = 1/p$.

*Step 3: Apply to our process.*
Here, $p = e^{-\lambda t}$. Therefore,
$\mathbb{E}[X(t)] = \frac{1}{e^{-\lambda t}} = e^{\lambda t}$.

**Final Answer / 最终答案:**
(a) $p_1'(t) = -\lambda p_1(t), p_1(0)=1$; $p_j'(t) = -\lambda j p_j(t) + \lambda (j-1) p_{j-1}(t), p_j(0)=0$ for $j \ge 2$.
(b) The proposed $p_j(t)$ satisfies the initial conditions and the forward equations, as shown by direct substitution and algebraic manipulation.
(c) $\boxed{\mathbb{E}[X(t)] = e^{\lambda t}}$

**Key Insight / 解题要点:**
The simple birth process (Yule process) leads to a geometric distribution at each time $t$, and its expectation grows exponentially, reflecting the multiplicative nature of the birth rates $\lambda_n = \lambda n$.

---

### Question 4 / 第4题

**Problem / 题目原文:**
Let (𝑋(𝑡)) be a simple birth process with rates 𝜆𝑛 = 𝜆𝑛 starting from 𝑋(0) = 1. Let 𝑇𝑛 ∼ Exp(𝜆𝑛) be the 𝑛th holding time, and let 𝐽𝑛 = 𝑇1 + 𝑇2 + ⋯ + 𝑇𝑛 be the time of the 𝑛th birth.
(a) Write down 𝔼𝑇𝑛 and Var(𝑇𝑛).
(b) Show that, as 𝑛 → ∞, the expectation 𝔼𝐽𝑛 tends to infinity, but the variance Var(𝐽𝑛) is bounded.

**中文翻译:**
设 (𝑋(𝑡)) 是一个简单生灭过程，其出生率为 𝜆𝑛 = 𝜆𝑛，从 𝑋(0) = 1 开始。设 𝑇𝑛 ∼ Exp(𝜆𝑛) 是第 𝑛 次停留时间，并设 𝐽𝑛 = 𝑇1 + 𝑇2 + ⋯ + 𝑇𝑛 是第 𝑛 次出生的时间。
(a) 写出 𝔼𝑇𝑛 和 Var(𝑇𝑛)。
(b) 证明，当 𝑛 → ∞ 时，期望 𝔼𝐽𝑛 趋于无穷大，但方差 Var(𝐽𝑛) 是有界的。

**Knowledge Points / 考查知识点:**
- Holding times in a birth process
- Expectation and variance of exponential distribution
- Expectation and variance of sum of independent random variables
- Harmonic series and its divergence
- Basel problem (sum of reciprocals of squares)

**Step-by-Step Solution / 逐步解答:**

**(a) Expectation and Variance of the nth Holding Time**

*Step 1: State the distribution of $T_n$.*
$T_n \sim \text{Exp}(\lambda_n)$, where $\lambda_n = \lambda n$.

*Step 2: Recall the expectation of an exponential random variable.*
If $X \sim \text{Exp}(\mu)$, then $\mathbb{E}[X] = 1/\mu$.
Therefore, $\mathbb{E}[T_n] = 1/\lambda_n = 1/(\lambda n)$.

*Step 3: Recall the variance of an exponential random variable.*
If $X \sim \text{Exp}(\mu)$, then $\text{Var}(X) = 1/\mu^2$.
Therefore, $\text{Var}(T_n) = 1/\lambda_n^2 = 1/(\lambda^2 n^2)$.

**Intermediate Result:**
$\mathbb{E}[T_n] = \frac{1}{\lambda n}$, $\text{Var}(T_n) = \frac{1}{\lambda^2 n^2