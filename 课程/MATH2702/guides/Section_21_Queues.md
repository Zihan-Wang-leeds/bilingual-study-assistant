# Section 21: Queues

> MATH2702 Stochastic Processes - 自学教材
> 生成时间: 2026-07-17 14:57
> 来源页: 99-102

---

# 📋 Section Overview / 章节概览

This section introduces **Queueing Theory (排队论)** , specifically two fundamental queueing models: the **M/M/∞ infinite server process (无限服务台过程)** and the **M/M/1 single server queue (单服务台排队系统)** . These models are essential for understanding how systems handle arrivals, service, and waiting times. Queueing theory has wide applications in computer networks, telecommunications, customer service, healthcare, and manufacturing. Understanding these models helps predict system performance, such as average queue length and server utilization, which is crucial for designing efficient systems.

# 🎯 Learning Objectives / 学习目标

By the end of this section, you will be able to:

1. **Define** the M/M/∞ and M/M/1 queueing models, explaining the meaning of each "M" and the number.
2. **Derive** the stationary distribution for the M/M/∞ process and prove it follows a Poisson distribution.
3. **Derive** the stationary distribution for the M/M/1 queue and prove it follows a geometric distribution.
4. **Calculate** key performance measures: average number in system, proportion of idle time, and server utilization.
5. **Determine** the conditions for stability (positive recurrence) of the M/M/1 queue.
6. **Apply** these models to real-world scenarios and interpret the results.

# 📚 Prerequisites / 前置知识

Before studying this section, you should be familiar with:

- **Poisson Process (泊松过程)** : Understanding of arrival processes with rate λ
- **Exponential Distribution (指数分布)** : Memoryless property, rate parameter μ
- **Markov Jump Processes (马尔可夫跳跃过程)** : Generator matrix Q, stationary distribution π satisfying πQ = 0
- **Stationary Distribution (平稳分布)** : Long-run behavior of Markov processes
- **Geometric Series (几何级数)** : Sum formula ∑_{i=0}^∞ r^i = 1/(1-r) for |r|<1
- **Basic Probability Distributions (基本概率分布)** : Poisson, Geometric, Exponential

# 📖 Core Content / 核心内容

## Topic 1: M/M/∞ Infinite Server Process (无限服务台过程)

### Intuition / 直觉理解

Imagine a **livestream (直播)** where viewers arrive at random times (like a Poisson process) and watch for a random amount of time (exponentially distributed). Since there's no limit on how many can watch simultaneously, everyone gets service immediately - there's no waiting! This is like a library where students come and go, or a download server where files are being downloaded. The key idea is that **everyone is served immediately** because there are "infinite servers" available.

### Formal Definition / 形式化定义

**Definition 21.1: M/M/∞ Process**
- **M (Memoryless arrivals)**: Arrivals follow a Poisson process with rate λ (λ > 0)
- **M (Memoryless service)**: Service times are independent and identically distributed as Exp(μ) (μ > 0)
- **∞ (Infinite servers)**: No limit on simultaneous service

Let **X(t)** = number of individuals in the system (receiving service) at time t.

The process is a Markov jump process with:
- **Arrival rate**: q_{i,i+1} = λ (when i individuals are in system, new arrivals occur at rate λ)
- **Departure rate**: q_{i,i-1} = iμ (when i individuals are being served, the first to finish is the minimum of i independent Exp(μ) times, which is Exp(iμ))
- **Total rate out of state i**: q_i = -q_{ii} = λ + iμ

**Generator Matrix Q** (where blank entries are 0):

Q = 
⎛⎜⎜⎜⎜⎜⎜
⎝
-λ      λ       0       0       ...
μ      -(λ+μ)   λ       0       ...
0      2μ      -(λ+2μ) λ       ...
0      0       3μ      -(λ+3μ) λ
⋱      ⋱       ⋱       ⋱       ⋱
⎞⎟⎟⎟⎟⎟⎟
⎠

**Symbol Explanation**:
- λ (lambda): arrival rate (average number of arrivals per unit time)
- μ (mu): service rate per server (average number of services completed per unit time per server)
- i: number of individuals currently in the system
- q_{ij}: transition rate from state i to state j
- q_{ii}: negative of total rate out of state i

### Key Properties / 关键性质

**Theorem 21.1: Stationary Distribution of M/M/∞**

Let (X(t)) be an M/M/∞ process with arrival rate λ and service rate μ. The process has stationary distribution:

π_i = e^{-ρ} ρ^i / i!   for i = 0, 1, 2, ...

where ρ = λ/μ (traffic intensity/流量强度).

This means X(t) ~ Po(ρ) in stationarity (follows Poisson distribution with mean ρ).

**Properties**:
1. The process is **irreducible** (all states communicate)
2. It is **positive recurrent** (has a stationary distribution)
3. By the limit theorem, π is also the **equilibrium distribution** (平衡分布)
4. By the ergodic theorem, long-run proportion of time in each state is governed by π

**Key Performance Measures**:
1. **Average number in system**: E[Po(ρ)] = ρ = λ/μ
2. **Proportion of time empty**: π_0 = e^{-ρ} = e^{-λ/μ}

### Proof / 证明

**Proof of Theorem 21.1**:

We need to verify that π satisfies the global balance equations πQ = 0.

**Step 1: Verify equation for i = 0 (from first column of Q)**

Equation (13): -λπ_0 + μπ_1 = 0

Substitute π_1 = ρπ_0 (from rearranging):
-λπ_0 + μ(ρπ_0) = -λπ_0 + μ(λ/μ)π_0 = -λπ_0 + λπ_0 = 0 ✓

**Step 2: Verify equation for i ≥ 1 (from general equation (12))**

Equation (12): λπ_{i-1} - (λ + iμ)π_i + (i+1)μπ_{i+1} = 0

Substitute π_i = e^{-ρ}ρ^i/i!:

λπ_{i-1} = λ · e^{-ρ}ρ^{i-1}/(i-1)!
(λ + iμ)π_i = (λ + iμ) · e^{-ρ}ρ^i/i!
(i+1)μπ_{i+1} = (i+1)μ · e^{-ρ}ρ^{i+1}/(i+1)! = μ · e^{-ρ}ρ^{i+1}/i!

Now compute the sum:

= λe^{-ρ}ρ^{i-1}/(i-1)! - (λ + iμ)e^{-ρ}ρ^i/i! + μe^{-ρ}ρ^{i+1}/i!

**Step 3: Rewrite first term with common denominator i!**

λe^{-ρ}ρ^{i-1}/(i-1)! = λe^{-ρ}ρ^{i-1} · i / i! = λe^{-ρ}ρ^i · i / (ρ · i!) = (iλ/ρ)e^{-ρ}ρ^i/i! = iμe^{-ρ}ρ^i/i!

(since λ/ρ = μ)

**Step 4: Combine all terms**

= iμe^{-ρ}ρ^i/i! - (λ + iμ)e^{-ρ}ρ^i/i! + μe^{-ρ}ρ^{i+1}/i!

= e^{-ρ}ρ^i/i! [iμ - (λ + iμ) + μρ]

= e^{-ρ}ρ^i/i! [iμ - λ - iμ + λ]   (since μρ = μ·λ/μ = λ)

= e^{-ρ}ρ^i/i! [0] = 0 ✓

Thus πQ = 0 is satisfied, confirming π is the stationary distribution.

### Worked Examples / 例题

**Example 1: Livestream Viewers**

A livestream has viewers arriving at rate λ = 10 per hour. Each viewer watches for an average of 30 minutes (so μ = 2 per hour since 1/μ = 0.5 hours).

**Question**: In the long run, what is the average number of viewers? What proportion of time is the stream empty?

**Solution**:
1. Calculate ρ = λ/μ = 10/2 = 5
2. Average number of viewers = ρ = 5 viewers
3. Proportion of time empty = e^{-ρ} = e^{-5} ≈ 0.0067 (about 0.67% of the time)

**Interpretation**: On average, there are 5 viewers watching simultaneously. The stream is empty less than 1% of the time.

**Example 2: Library Occupancy**

Students arrive at a library at rate λ = 20 per hour. Average study time is 2 hours (μ = 0.5 per hour).

**Question**: What is the probability that exactly 10 students are in the library in the long run?

**Solution**:
1. ρ = λ/μ = 20/0.5 = 40
2. π_{10} = e^{-40} · 40^{10} / 10!
3. This is very small (e^{-40} ≈ 4.2 × 10^{-18}), so probability is essentially 0.

**Interpretation**: With such high traffic, the library is almost always very full.

---

## Topic 2: M/M/1 Single Server Queue (单服务台排队系统)

### Intuition / 直觉理解

Now imagine a **single server** (like a shop with one cashier). Customers arrive randomly, but if the server is busy, they must **wait in a queue (排队)** . This is like a lecturer's office hours: students arrive; if the lecturer is free, they get immediate help; otherwise, they wait in line. The key difference from M/M/∞ is that **only one person can be served at a time**, so queues form when arrival rate exceeds service capacity.

### Formal Definition / 形式化定义

**Definition 21.2: M/M/1 Queue**
- **M**: Memoryless arrivals (Poisson process with rate λ)
- **M**: Memoryless service times (Exp(μ))
- **1**: Single server

Let **X(t)** = number of individuals in the system at time t (including the one being served).
- X(t) = 0: server is free
- X(t) = 1: one being served, no one waiting
- X(t) = x > 1: one being served, x-1 waiting in queue

**Transition Rates**:
- q_{i,i+1} = λ (arrivals occur at rate λ regardless of state)
- q_{i,i-1} = μ for i ≥ 1 (departures occur at rate μ when someone is being served)
- q_0 = -q_{00} = λ (only arrivals possible from state 0)
- q_i = -q_{ii} = λ + μ for i ≥ 1

**Generator Matrix Q**:

Q = 
⎛⎜⎜⎜⎜⎜⎜
⎝
-λ      λ       0       0       ...
μ      -(λ+μ)   λ       0       ...
0      μ       -(λ+μ)  λ       ...
0      0       μ       -(λ+μ)  λ
⋱      ⋱       ⋱       ⋱       ⋱
⎞⎟⎟⎟⎟⎟⎟
⎠

### Key Properties / 关键性质

**Stability Condition (稳定性条件)** :

The discrete-time jump chain (Y_n) is a simple random walk with:
- Up probability: p = λ/(λ+μ)
- Down probability: q = μ/(λ+μ)
- Reflecting barrier at 0

**Three Cases**:
1. **λ > μ** (p > q): **Transient (瞬态)** - queue grows indefinitely, never clears
2. **λ = μ** (p = q): **Null recurrent (零常返)** - queue clears eventually but expected time is infinite
3. **λ < μ** (p < q): **Positive recurrent (正常返)** - queue clears regularly, stable system

**Theorem 21.2: Stationary Distribution of M/M/1**

For λ < μ (stable case), the stationary distribution is:

π_i = (1 - ρ)ρ^i   for i = 0, 1, 2, ...

where ρ = λ/μ < 1.

This is a **Geometric distribution (几何分布)** starting from i = 0: X(t) ~ Geom(ρ) in stationarity.

**Key Performance Measures**:
1. **Average number in system**: E[Geom(ρ)] = ρ/(1-ρ) = λ/(μ-λ)
2. **Proportion of time server idle**: π_0 = 1 - ρ = 1 - λ/μ
3. **Proportion of time server busy**: 1 - π_0 = λ/μ

### Proof / 证明

**Proof of Theorem 21.2**:

We need to solve πQ = 0 with normalizing condition ∑π_i = 1.

**Step 1: Global balance equations**

From πQ = 0, for i ≥ 1:
μπ_{i+1} - (λ+μ)π_i + λπ_{i-1} = 0   (Equation for column i)

From first column (i=0):
μπ_1 - λπ_0 = 0   (Initial condition)

**Step 2: Recognize as linear difference equation**

The equation μπ_{i+1} - (λ+μ)π_i + λπ_{i-1} = 0 is a second-order linear homogeneous difference equation.

Assume solution of form π_i = A + Bρ^i (where ρ = λ/μ).

**Step 3: Apply initial condition**

μπ_1 - λπ_0 = 0
μ(A + Bρ) - λ(A + B) = 0
Aμ + Bμρ - Aλ - Bλ = 0
A(μ - λ) + B(μρ - λ) = 0

Since ρ = λ/μ, we have μρ = λ, so B(λ - λ) = 0.
Thus A(μ - λ) = 0.

Since λ < μ (stable case), μ - λ ≠ 0, so A = 0.

Therefore π_i = Bρ^i.

**Step 4: Normalize**

∑_{i=0}^∞ π_i = ∑_{i=0}^∞ Bρ^i = B · 1/(1-ρ) = 1

Therefore B = 1 - ρ.

**Step 5: Final stationary distribution**

π_i = (1 - ρ)ρ^i   for i = 0, 1, 2, ...

This is a geometric distribution with parameter (1-ρ).

### Worked Examples / 例题

**Example 1: Coffee Shop**

A coffee shop has one barista. Customers arrive at rate λ = 3 per hour. Service time averages 15 minutes (μ = 4 per hour).

**Question 1**: Is the queue stable? What is the average number of customers in the shop?

**Solution**:
1. ρ = λ/μ = 3/4 = 0.75 < 1, so queue is stable (positive recurrent)
2. Average number = ρ/(1-ρ) = 0.75/0.25 = 3 customers

**Question 2**: What proportion of time is the barista idle?

**Solution**:
π_0 = 1 - ρ = 1 - 0.75 = 0.25 (25% of the time idle)

**Question 3**: What is the probability that exactly 2 customers are in the shop?

**Solution**:
π_2 = (1-ρ)ρ^2 = 0.25 × 0.75^2 = 0.25 × 0.5625 = 0.1406 (about 14%)

**Example 2: Lecture Office Hours**

A lecturer has office hours. Students arrive at rate λ = 5 per hour. Average consultation time is 10 minutes (μ = 6 per hour).

**Question**: What is the probability that more than 3 students are waiting (i.e., total in system > 4)?

**Solution**:
1. ρ = 5/6 ≈ 0.833
2. P(X > 4) = 1 - P(X ≤ 4) = 1 - ∑_{i=0}^4 (1-ρ)ρ^i
3. ∑_{i=0}^4 (1-ρ)ρ^i = (1-ρ)(1 + ρ + ρ^2 + ρ^3 + ρ^4) = (1-ρ)(1-ρ^5)/(1-ρ) = 1 - ρ^5
4. P(X > 4) = ρ^5 = (5/6)^5 ≈ 0.4019 (about 40%)

**Interpretation**: There's a 40% chance that more than 3 students are waiting, which might be problematic.

# 🔗 Connections / 知识关联

## Previous Topics
- **Poisson Process**: Both models use Poisson arrivals, connecting to earlier material on counting processes
- **Exponential Distribution**: Memoryless property is crucial for both models' analysis
- **Markov Jump Processes**: Both are specific examples of continuous-time Markov chains
- **Stationary Distribution**: The πQ = 0 equation is applied directly here

## Future Topics
- **M/M/c Queues**: Multiple servers (c servers) generalize M/M/1
- **M/G/1 Queues**: General service time distributions
- **Queueing Networks**: Interconnected queues
- **Performance Analysis**: Real-world applications in computer systems, telecommunications

## Comparison of M/M/∞ vs M/M/1

| Feature | M/M/∞ | M/M/1 |
|---------|-------|-------|
| Servers | Infinite | 1 |
| Queue | No queue | FIFO queue |
| Stationary Distribution | Poisson(ρ) | Geometric(ρ) |
| Mean number | ρ | ρ/(1-ρ) |
| Stability | Always stable | Only if λ < μ |
| Idle proportion | e^{-ρ} | 1-ρ |

# ⚠️ Common Mistakes / 常见误区

1. **Confusing ρ = λ/μ with probability**: ρ is the traffic intensity, not a probability. For M/M/1, ρ must be < 1 for stability, but ρ can be > 1 for M/M/∞.

2. **Forgetting the stability condition**: For M/M/1, always check λ < μ before using the stationary distribution. If λ ≥ μ, the queue is not stable.

3. **Misinterpreting π_0**: π_0 is the proportion of time the system is empty, not the proportion of time the server is idle (though they're the same for M/M/1).

4. **Confusing M/M/∞ and M/M/1 formulas**: The stationary distributions are very different (Poisson vs Geometric). Don't mix them up!

5. **Forgetting the normalizing condition**: When deriving stationary distributions, always verify ∑π_i = 1.

6. **Misunderstanding "number in system"**: For M/M/1, X(t) includes the one being served. So X(t) = 1 means one being served, zero waiting.

# ✍️ Practice / 练习

**Question 1**: A call center has infinite phone lines. Calls arrive at rate λ = 100 per hour, and average call duration is 3 minutes. Find:
a) The average number of calls in progress
b) The probability that exactly 5 calls are in progress
c) The proportion of time the system is empty

**Hint**: This is M/M/∞. First convert everything to same time unit (hours). μ = 20 per hour (since 60/3 = 20).

**Question 2**: A single-server repair shop receives broken machines at rate λ = 2 per day. Average repair time is 0.4 days. Find:
a) Is the queue stable?
b) Average number of machines in the shop
c) Probability that at most 2 machines are in the shop
d) Proportion of time the repair person is busy

**Hint**: Check λ < μ first. μ = 1/0.4 = 2.5 per day.

**Question 3**: For an M/M/1 queue with λ = 4 and μ = 5, find the probability that the queue length (excluding the one being served) exceeds 3.

**Hint**: Queue length = X(t) - 1 when X(t) ≥ 1. P(queue > 3) = P(X > 4) = 1 - ∑_{i=0}^4 π_i.

**Question 4**: Compare the average number in system for M/M/∞ and M/M/1 when λ = 10 and μ = 12. Which is larger? Why?

**Hint**: For M/M/∞: ρ = 10/12 ≈ 0.833, average = 0.833. For M/M/1: average = 0.833/(1-0.833) = 5. The M/M/1 has much larger average because of queueing.

**Question 5**: Derive the stationary distribution for M/M/1 by solving the global balance equations directly (without using the difference equation approach).

**Hint**: From μπ_1 = λπ_0, get π_1 = ρπ_0. Then from μπ_2 - (λ+μ)π_1 + λπ_0 = 0, substitute and solve for π_2. Continue pattern to guess π_i = ρ^iπ_0, then normalize.

# 📌 Key Takeaways / 要点总结

1. **M/M/∞ Process**: Infinite servers, no queueing. Stationary distribution is **Poisson(ρ)** where ρ = λ/μ. Always stable.

2. **M/M/1 Queue**: Single server with FIFO queue. Stationary distribution is **Geometric(ρ)** where ρ = λ/μ < 1 for stability.

3. **Stability Condition**: M/M/1 requires λ < μ (arrival rate < service rate). If λ ≥ μ, queue grows without bound.

4. **Generator Matrix**: Both models have tridiagonal generator matrices with specific patterns. M/M/∞ has state-dependent departure rates (iμ), M/M/1 has constant departure rate (μ).

5. **Key Performance Measures**:
   - M/M/∞: Average number = ρ, idle proportion = e^{-ρ}
   - M/M/1: Average number = ρ/(1-ρ), idle proportion = 1-ρ

6. **Proof Technique**: Both stationary distributions are verified by checking πQ = 0. The M/M/1 solution uses linear difference equations.

7. **Real-World Applications**: These models apply to many systems including customer service, computer networks, healthcare, and manufacturing.

8. **Limitation**: These are simplified models. Real systems may have non-Poisson arrivals, non-exponential service times, or more complex queueing disciplines.