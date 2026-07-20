# Section 21: Queues

> MATH2702 - 自学教材 / Self-Study Guide
> 生成时间: 2026-07-20 15:59
> 来源页: 99-102

---

# Chapter 21: Queues / 第21章：排队论

## 📋 Section Overview / 章节概览

**中文解释：** 本章介绍排队论（Queueing Theory）中的两个基本模型：M/M/∞无限服务器系统和M/M/1单服务器队列。排队论是研究等待队列行为的数学理论，广泛应用于通信网络、计算机系统、客户服务等领域。我们将学习如何分析这些系统的长期行为，包括平均队列长度、服务器空闲时间比例等关键性能指标。

**English explanation:** This chapter introduces two fundamental models in Queueing Theory: the M/M/∞ infinite server system and the M/M/1 single server queue. Queueing theory is the mathematical study of waiting lines, widely applied in telecommunications, computer systems, customer service, and many other fields. We will learn how to analyze the long-term behavior of these systems, including key performance metrics such as average queue length and server idle time proportion.

**Real-world applications / 实际应用：**
- Website livestream viewers / 网站直播观众数量
- University library occupancy / 大学图书馆人数
- Insurance contracts held by a broker / 保险经纪人持有的保单数
- Lecturer's office hours / 教授的办公时间
- Shop with a single till / 单收银台商店
- Phone calls to a receptionist / 电话接线员服务

## 🎯 Learning Objectives / 学习目标

After completing this section, you should be able to / 完成本节后，你应该能够：

1. **Describe** the M/M/∞ and M/M/1 queue models and their key characteristics / **描述** M/M/∞和M/M/1排队模型及其关键特征
2. **Derive** the stationary distribution for both models / **推导**两个模型的平稳分布
3. **Calculate** long-run average number of individuals in the system / **计算**系统中个体的长期平均数量
4. **Determine** the long-run proportion of time the server is idle / **确定**服务器空闲的长期时间比例
5. **Identify** conditions for stability (positive recurrence) of the M/M/1 queue / **识别**M/M/1队列的稳定性条件
6. **Apply** these models to real-world scenarios / **应用**这些模型到实际场景

## 📚 Prerequisites / 前置知识

Before studying this section, you should be familiar with / 在学习本节之前，你应该熟悉：

- **Poisson process (泊松过程)**: Understanding of arrival processes with rate λ
- **Exponential distribution (指数分布)**: Memoryless property, rate parameter μ
- **Markov jump processes (马尔可夫跳跃过程)**: Generator matrix Q, stationary distribution π
- **Stationary distribution (平稳分布)**: Solving πQ = 0
- **Discrete-time Markov chains (离散时间马尔可夫链)**: Transience, null recurrence, positive recurrence
- **Geometric and Poisson distributions (几何分布和泊松分布)**: Basic properties

## 📖 Core Content / 核心内容

### Topic 1: M/M/∞ Infinite Server Process / M/M/∞无限服务器过程

#### Intuition / 直觉理解

**中文解释：** M/M/∞模型描述的是一个"无限服务器"系统。想象一个直播网站：观众以泊松过程到达（平均到达率λ），每个人观看直播的时间服从指数分布（平均服务时间1/μ），然后离开。因为有无穷多个"服务器"（即每个观众都可以立即开始观看，不需要排队），所以实际上不存在等待队列。每个人到达后立即开始服务。

**English explanation:** The M/M/∞ model describes a system with "infinite servers." Imagine a livestreaming website: viewers arrive according to a Poisson process (average arrival rate λ), each person watches the livestream for an exponentially distributed time (average service time 1/μ), then leaves. Because there are infinitely many "servers" (i.e., every viewer can start watching immediately without waiting), there is actually no queue. Everyone starts service immediately upon arrival.

**Key insight / 关键洞察：** The "∞" means there is no limit on how many individuals can be serviced simultaneously. This is different from real queues where people wait.

#### Formal Definition / 形式化定义

**Definition 21.1: M/M/∞ Process / M/M/∞过程定义**

**English:** The M/M/∞ process is a Markov jump process (X(t)) where:
- Individuals arrive as a Poisson process with rate λ
- Each individual receives service for an Exp(μ) time, independent of everything else
- There are infinitely many servers, so no queue forms
- The number of individuals receiving service at time t is X(t)

**中文解释：** M/M/∞过程是一个马尔可夫跳跃过程(X(t))，其中：
- 个体以速率λ的泊松过程到达
- 每个个体接受服务的时间服从Exp(μ)分布，且相互独立
- 有无穷多个服务器，因此不会形成队列
- X(t)表示在时间t正在接受服务的个体数量

**Notation explanation / 符号说明：**

| Symbol | Meaning (English) | 含义 (中文) |
|--------|-------------------|-------------|
| λ | Arrival rate | 到达率 |
| μ | Service rate per server | 每个服务器的服务率 |
| X(t) | Number in system at time t | t时刻系统中的数量 |
| ρ = λ/μ | Traffic intensity | 交通强度 |

**The three M's explained / 三个M的解释：**

1. **First M (第一个M)**: Memoryless arrivals - arrival process is Poisson with exponential interarrival times / 无记忆到达 - 到达过程是泊松过程，间隔时间服从指数分布
2. **Second M (第二个M)**: Memoryless service - service times are exponential / 无记忆服务 - 服务时间服从指数分布
3. **∞ (无穷大)**: Infinite servers - no limit on simultaneous service / 无限服务器 - 同时服务人数无限制

#### Generator Matrix / 生成矩阵

**English:** The generator matrix Q for the M/M/∞ process has the following structure:

**中文解释：** M/M/∞过程的生成矩阵Q具有以下结构：

$$Q = $$
\begin{pmatrix}
-\lambda & \lambda & & & \\
\mu & -(\lambda + \mu) & \lambda & & \\
& 2\mu & -(\lambda + 2\mu) & \lambda & \\
& & 3\mu & -(\lambda + 3\mu) & \lambda \\
& & & \ddots & \ddots & \ddots
\end{pmatrix}
$$$$

**Explanation of entries / 矩阵元素解释：**

| Entry | Value | Meaning (English) | 含义 (中文) |
|-------|-------|-------------------|-------------|
| q_{i,i+1} | λ | Arrival rate when i in system | 系统中有i人时的到达率 |
| q_{i,i-1} | iμ | Departure rate when i in system | 系统中有i人时的离开率 |
| q_{ii} | -(λ + iμ) | Diagonal entries (negative sum of row) | 对角线元素（行和的负值） |

**Why is q_{i,i-1} = iμ? / 为什么离开率是iμ？**

**中文解释：** 当有i个人正在接受服务时，每个人都有一个独立的Exp(μ)服务时间。第一个完成的服务时间是最小值，即i个独立指数分布的最小值。由于指数分布的无记忆性，这个最小值也服从指数分布，且速率为iμ。

**English explanation:** When i individuals are being served, each has an independent Exp(μ) service time. The first service to finish is the minimum of i independent exponential random variables. Due to the memoryless property of exponential distribution, this minimum is also exponential with rate iμ.

#### Stationary Distribution / 平稳分布

**Theorem 21.1: Stationary Distribution of M/M/∞ / M/M/∞的平稳分布**

**English:** Let (X(t)) be an M/M/∞ process with arrival rate λ and service rate μ. The process has the stationary distribution:

$$\pi_i = e^{-\rho} \frac{\rho^i}{i!}, \quad \text{where } \rho = \frac{\lambda}{\mu}$$

This corresponds to X(t) ~ Po(ρ), a Poisson distribution with mean ρ.

**中文解释：** 设(X(t))是到达率为λ、服务率为μ的M/M/∞过程。该过程的平稳分布为：

$$\pi_i = e^{-\rho} \frac{\rho^i}{i!}, \quad \text{其中 } \rho = \frac{\lambda}{\mu}$$

这对应于X(t)服从参数为ρ的泊松分布，即X(t) ~ Po(ρ)。

**Proof / 证明：**

**Step 1: Set up the balance equations / 建立平衡方程**

**English:** The stationary distribution satisfies πQ = 0. From the generator matrix, we get:

For i = 0: $-\lambda \pi_0 + \mu \pi_1 = 0$ (Equation 13)

For i ≥ 1: $\lambda \pi_{i-1} - (\lambda + i\mu)\pi_i + (i+1)\mu \pi_{i+1} = 0$ (Equation 12)

**中文解释：** 平稳分布满足πQ = 0。从生成矩阵得到：

对于i = 0：$-\lambda \pi_0 + \mu \pi_1 = 0$ (方程13)

对于i ≥ 1：$\lambda \pi_{i-1} - (\lambda + i\mu)\pi_i + (i+1)\mu \pi_{i+1} = 0$ (方程12)

**Step 2: Solve recursively / 递归求解**

**English:** From Equation 13:
$$\pi_1 = \frac{\lambda}{\mu} \pi_0 = \rho \pi_0$$

For i = 1 in Equation 12:
$$\lambda \pi_0 - (\lambda + \mu)\pi_1 + 2\mu \pi_2 = 0$$
$$\lambda \pi_0 - (\lambda + \mu)\rho \pi_0 + 2\mu \pi_2 = 0$$
$$\lambda \pi_0 - \lambda \pi_0 - \mu\rho \pi_0 + 2\mu \pi_2 = 0$$
$$2\mu \pi_2 = \mu\rho \pi_0$$
$$\pi_2 = \frac{\rho}{2} \pi_0 = \pi_0 \frac{\rho^2}{2}$$

For i = 2:
$$\lambda \pi_1 - (\lambda + 2\mu)\pi_2 + 3\mu \pi_3 = 0$$
$$\lambda \rho \pi_0 - (\lambda + 2\mu)\frac{\rho^2}{2}\pi_0 + 3\mu \pi_3 = 0$$
$$3\mu \pi_3 = \frac{\lambda \rho^2}{2} \pi_0 + \frac{2\mu \rho^2}{2} \pi_0 - \lambda \rho \pi_0$$
$$3\mu \pi_3 = \frac{\rho^2}{2}(\lambda + 2\mu)\pi_0 - \lambda \rho \pi_0$$
$$\pi_3 = \pi_0 \frac{\rho^3}{6}$$

**中文解释：** 从方程13得到π₁ = ρπ₀。然后依次代入方程12，得到π₂ = π₀ρ²/2，π₃ = π₀ρ³/6。这暗示平稳分布可能是参数为ρ的泊松分布。

**Step 3: Verify the Poisson distribution / 验证泊松分布**

**English:** We conjecture $\pi_i = e^{-\rho} \rho^i / i!$ and verify it satisfies the balance equations.

For i = 0: $-\lambda \pi_0 + \mu \pi_1 = -\lambda e^{-\rho} + \mu e^{-\rho} \rho = e^{-\rho}(-\lambda + \mu\rho) = e^{-\rho}(-\lambda + \lambda) = 0$ ✓

For i ≥ 1, substitute into Equation 12:
$$\lambda \pi_{i-1} - (\lambda + i\mu)\pi_i + (i+1)\mu \pi_{i+1}$$
$$= \lambda e^{-\rho} \frac{\rho^{i-1}}{(i-1)!} - (\lambda + i\mu) e^{-\rho} \frac{\rho^i}{i!} + (i+1)\mu e^{-\rho} \frac{\rho^{i+1}}{(i+1)!}$$
$$= \lambda e^{-\rho} \frac{i}{\rho} \frac{\rho^i}{i!} - (\lambda + i\mu) e^{-\rho} \frac{\rho^i}{i!} + \mu e^{-\rho} \rho \frac{\rho^i}{i!}$$
$$= e^{-\rho} \frac{\rho^i}{i!} (i\mu - (\lambda + i\mu) + \lambda)$$
$$= e^{-\rho} \frac{\rho^i}{i!} (i\mu - \lambda - i\mu + \lambda) = 0$$ ✓

**中文解释：** 我们猜想πᵢ = e⁻ᵖ ρⁱ / i!并验证它满足平衡方程。通过代入计算，所有方程都成立，因此这确实是平稳分布。

**Key properties / 关键性质：**

1. **Irreducibility (不可约性)**: The process can reach any state from any other state
2. **Positive recurrence (正常返)**: Since a stationary distribution exists, the process is positive recurrent
3. **Equilibrium distribution (平衡分布)**: By the limit theorem, π is also the equilibrium distribution
4. **Ergodic theorem (遍历定理)**: Long-run time proportions are governed by π

#### Answers to Key Questions / 关键问题解答

**Question 1: Long-run average number in system / 长期平均系统人数**

**English:** The average number of individuals being serviced in the long run is:
$$\mathbb{E}[X(\infty)] = \rho = \frac{\lambda}{\mu}$$

**中文解释：** 长期平均接受服务的人数为ρ = λ/μ。这是泊松分布的均值。

**Question 2: Proportion of time system is empty / 系统空闲的时间比例**

**English:** The long-run proportion of time the process is empty (no one being serviced) is:
$$\pi_0 = e^{-\rho} = e^{-\lambda/\mu}$$

**中文解释：** 系统长期空闲（无人接受服务）的时间比例为π₀ = e⁻ᵖ = e⁻ˡ/ᵐ。

---

### Topic 2: M/M/1 Single Server Queue / M/M/1单服务器队列

#### Intuition / 直觉理解

**中文解释：** M/M/1模型描述的是只有一个服务器的排队系统。想象教授的办公时间：学生以泊松过程到达（速率λ）。如果教授空闲，学生立即开始咨询（服务时间Exp(μ)）。如果教授正在忙，学生必须排队等待。当教授完成一个学生的咨询后，如果队列非空，立即开始服务等待时间最长的学生。

**English explanation:** The M/M/1 model describes a queueing system with only one server. Imagine a professor's office hours: students arrive as a Poisson process (rate λ). If the professor is free, the student immediately starts consulting (service time Exp(μ)). If the professor is busy, the student must join a queue and wait. When the professor finishes with one student, if the queue is non-empty, they immediately start serving the student who has been waiting the longest.

**Real-world examples / 实际应用：**
- Lecturer's office hours / 教授的办公时间
- Shop with a single till / 单收银台商店
- Phone calls to a receptionist / 电话接线员服务
- Self-employed person's tasks / 自由职业者的任务

#### Formal Definition / 形式化定义

**Definition 21.2: M/M/1 Queue / M/M/1队列定义**

**English:** The M/M/1 queue is a Markov jump process (X(t)) where:
- X(t) = number of individuals in the system at time t
- X(t) = 0: server is free
- X(t) = 1: one individual being served, no one waiting
- X(t) = x > 1: one being served, x-1 waiting in queue
- Arrivals occur at rate λ (q_{i,i+1} = λ)
- When i ≥ 1, departures occur at rate μ (q_{i,i-1} = μ)

**中文解释：** M/M/1队列是一个马尔可夫跳跃过程(X(t))，其中：
- X(t) = t时刻系统中的个体数量
- X(t) = 0：服务器空闲
- X(t) = 1：一个个体正在接受服务，无人等待
- X(t) = x > 1：一个正在接受服务，x-1人在队列中等待
- 到达速率为λ (q_{i,i+1} = λ)
- 当i ≥ 1时，离开速率为μ (q_{i,i-1} = μ)

#### Generator Matrix / 生成矩阵

**English:** The generator matrix Q for the M/M/1 queue is:

**中文解释：** M/M/1队列的生成矩阵Q为：

$$Q = $$
\begin{pmatrix}
-\lambda & \lambda & & & \\
\mu & -(\lambda + \mu) & \lambda & & \\
& \mu & -(\lambda + \mu) & \lambda & \\
& & \mu & -(\lambda + \mu) & \lambda \\
& & & \ddots & \ddots & \ddots
\end{pmatrix}
$$$$

**Key difference from M/M/∞ / 与M/M/∞的关键区别：**

| Feature | M/M/∞ | M/M/1 |
|---------|-------|-------|
| Departure rate when i in system | iμ | μ (constant) |
| Queue forms? | No (infinite servers) | Yes (single server) |
| Number of servers | ∞ | 1 |

#### Stability Condition / 稳定性条件

**English:** The first question we need to answer is whether the queue will keep growing indefinitely or eventually clear. This depends on the relationship between λ and μ.

**中文解释：** 我们需要回答的第一个问题是队列是否会无限增长还是最终清空。这取决于λ和μ的关系。

**Discrete-time jump chain analysis / 离散时间跳跃链分析：**

**English:** The discrete-time jump chain (Yₙ) of the M/M/1 queue is a simple random walk with:
- Up probability: $p = \frac{\lambda}{\lambda + \mu}$
- Down probability: $q = \frac{\mu}{\lambda + \mu}$
- Reflecting barrier at 0

**中文解释：** M/M/1队列的离散时间跳跃链(Yₙ)是一个简单随机游走，具有：
- 向上概率：p = λ/(λ + μ)
- 向下概率：q = μ/(λ + μ)
- 在0处有反射壁

**Stability classification / 稳定性分类：**

| Condition | Type | Behavior | 行为 |
|-----------|------|----------|------|
| λ > μ | Transient (p > q) | Queue grows indefinitely | 队列无限增长 |
| λ = μ | Null recurrent (p = q) | Queue clears eventually, but expected time is infinite | 队列最终清空，但期望时间无穷大 |
| λ < μ | Positive recurrent (p < q) | Queue clears regularly | 队列定期清空 |

**中文解释：** 
- 当λ > μ时，队列是瞬时的，长度会无限增长，永远不会清空。这是非常不理想的。
- 当λ = μ时，队列是零常返的，虽然最终会清空，但期望清空时间是无穷大，队列会变得非常长。
- 当λ < μ时，队列是正常返的，虽然有时需要等待，但队列会定期清空。这是我们想要的情况。

**Important note / 重要说明：** In what follows, we only consider the "good" case λ < μ.

#### Stationary Distribution / 平稳分布

**Theorem 21.2: Stationary Distribution of M/M/1 / M/M/1的平稳分布**

**English:** Let (X(t)) be an M/M/1 queue with arrival rate λ and service rate μ > λ. The queue has the stationary distribution:

$$\pi_i = (1 - \rho) \rho^i, \quad \text{where } \rho = \frac{\lambda}{\mu} < 1$$

This corresponds to X(t) ~ Geom(ρ), a geometric distribution starting from i = 0.

**中文解释：** 设(X(t))是到达率为λ、服务率为μ > λ的M/M/1队列。该队列的平稳分布为：

$$\pi_i = (1 - \rho) \rho^i, \quad \text{其中 } \rho = \frac{\lambda}{\mu} < 1$$

这对应于X(t)服从参数为ρ的几何分布（从i = 0开始）。

**Proof / 证明：**

**Step 1: Set up the balance equations / 建立平衡方程**

**English:** The equation πQ = 0 gives:

For i ≥ 1: $\mu \pi_{i+1} - (\lambda + \mu)\pi_i + \lambda \pi_{i-1} = 0$

Initial condition (from first column of Q): $\mu \pi_1 - \lambda \pi_0 = 0$

Normalizing condition: $\sum_{i=0}^\infty \pi_i = 1$

**中文解释：** 方程πQ = 0给出：

对于i ≥ 1：μ π_{i+1} - (λ + μ)π_i + λ π_{i-1} = 0

初始条件（来自Q的第一列）：μ π₁ - λ π₀ = 0

归一化条件：∑_{i=0}^∞ π_i = 1

**Step 2: Solve the linear difference equation / 解线性差分方程**

**English:** The equation $\mu \pi_{i+1} - (\lambda + \mu)\pi_i + \lambda \pi_{i-1} = 0$ is a linear difference equation.

The characteristic equation is: $\mu r^2 - (\lambda + \mu)r + \lambda = 0$

Factoring: $(r-1)(\mu r - \lambda) = 0$

So the roots are: $r_1 = 1$, $r_2 = \frac{\lambda}{\mu} = \rho$

The general solution is: $\pi_i = A \cdot 1^i + B \cdot \rho^i = A + B\rho^i$

**中文解释：** 方程μ π_{i+1} - (λ + μ)π_i + λ π_{i-1} = 0是一个线性差分方程。

特征方程为：μ r² - (λ + μ)r + λ = 0

因式分解得：(r-1)(μ r - λ) = 0

根为：r₁ = 1，r₂ = λ/μ = ρ

通解为：πᵢ = A·1ⁱ + B·ρⁱ = A + Bρⁱ

**Step 3: Apply the initial condition / 应用初始条件**

**English:** From μπ₁ - λπ₀ = 0:
$$\mu(A + B\rho) - \lambda(A + B) = A\mu + B\lambda - A\lambda - B\lambda = A(\mu - \lambda) = 0$$

Since λ < μ, we have μ - λ ≠ 0, so A = 0.

Thus $\pi_i = B\rho^i$.

**中文解释：** 从μπ₁ - λπ₀ = 0：
μ(A + Bρ) - λ(A + B) = Aμ + Bλ - Aλ - Bλ = A(μ - λ) = 0

由于λ < μ，所以μ - λ ≠ 0，因此A = 0。

所以πᵢ = Bρⁱ。

**Step 4: Apply the normalizing condition / 应用归一化条件**

**English:** 
$$\sum_{i=0}^\infty \pi_i = \sum_{i=0}^\infty B\rho^i = B \sum_{i=0}^\infty \rho^i = B \cdot \frac{1}{1-\rho} = 1$$

Since ρ < 1, the geometric series converges, giving $B = 1 - \rho$.

Therefore: $\pi_i = (1 - \rho)\rho^i$

**中文解释：**
∑_{i=0}^∞ πᵢ = ∑_{i=0}^∞ Bρⁱ = B ∑_{i=0}^∞ ρⁱ = B · 1/(1-ρ) = 1

由于ρ < 1，几何级数收敛，得到B = 1 - ρ。

因此：πᵢ = (1 - ρ)ρⁱ

#### Answers to Key Questions / 关键问题解答

**Question 1: Long-run average number in system / 长期平均系统人数**

**English:** The long-run average number of individuals in the system is:
$$\mathbb{E}[X(\infty)] = \frac{\rho}{1-\rho} = \frac{\lambda}{\mu - \lambda}$$

**中文解释：** 长期平均系统人数为ρ/(1-ρ) = λ/(μ - λ)。如果λ只比μ略小，这个数会非常大。

**Question 2: Server idle and busy time / 服务器空闲和忙碌时间**

**English:** In the long run:
- Server free proportion: $\pi_0 = 1 - \rho = 1 - \frac{\lambda}{\mu}$
- Server busy proportion: $1 - \pi_0 = \frac{\lambda}{\mu}$

**中文解释：** 长期来看：
- 服务器空闲比例：π₀ = 1 - ρ = 1 - λ/μ
- 服务器忙碌比例：1 - π₀ = λ/μ

如果λ只比μ略小，服务器大部分时间都在忙碌。

## 🔗 Connections / 知识关联

**Connections to previous topics / 与之前主题的联系：**

1. **Poisson process (泊松过程)**: Both models use Poisson arrivals, which we studied earlier
2. **Exponential distribution (指数分布)**: Memoryless property is crucial for both models
3. **Markov jump processes (马尔可夫跳跃过程)**: Both are examples of continuous-time Markov chains
4. **Discrete-time Markov chains (离散时间马尔可夫链)**: The jump chain analysis for M/M/1 uses concepts of transience and recurrence

**Connections to future topics / 与未来主题的联系：**

1. **More complex queueing models**: M/M/c (multiple servers), M/G/1 (general service times)
2. **Queueing networks**: Systems of interconnected queues
3. **Performance analysis**: Response time, waiting time distributions

## ⚠️ Common Mistakes / 常见误区

1. **Confusing M/M/∞ and M/M/1 departure rates / 混淆M/M/∞和M/M/1的离开率**
   - M/M/∞: departure rate = iμ (depends on number in system)
   - M/M/1: departure rate = μ (constant when i ≥ 1)
   - **Tip**: Remember that in M/M/