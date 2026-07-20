# Section 16: Counting processes

> MATH2702 - 自学教材 / Self-Study Guide
> 生成时间: 2026-07-20 15:45
> 来源页: 79-82

---

# 📖 Chapter 16: Counting Processes / 计数过程

## 📋 Section Overview / 章节概览

**中文解释：** 本章我们将深入探讨计数过程（Counting Processes）的两种重要变体：生灭过程（Birth Processes）和时间非齐次泊松过程（Time Inhomogeneous Poisson Process）。计数过程是随机过程理论中的核心概念，它描述了随时间推移，事件发生的次数如何累积。在标准泊松过程中，事件发生的速率是恒定的，但在实际应用中，速率可能会随时间变化或依赖于当前状态。本章将帮助您理解这些更复杂的计数模型，并掌握它们的数学定义、性质和应用。

**English explanation:** In this chapter, we will explore two important variants of counting processes: Birth Processes and Time Inhomogeneous Poisson Processes. Counting processes are core concepts in stochastic process theory that describe how the number of events accumulates over time. In the standard Poisson process, the rate of events is constant, but in real-world applications, the rate may change over time or depend on the current state. This chapter will help you understand these more complex counting models and master their mathematical definitions, properties, and applications.

**Why this matters / 为什么重要：**
- Birth processes model population growth, cell division, and other exponential growth phenomena / 生灭过程模拟人口增长、细胞分裂和其他指数增长现象
- Time inhomogeneous Poisson processes model real-world arrival processes where rates vary (e.g., call centers, traffic flow) / 时间非齐次泊松过程模拟速率变化的现实到达过程（如呼叫中心、交通流量）

## 🎯 Learning Objectives / 学习目标

By the end of this section, you should be able to / 完成本节学习后，你应该能够：

1. **Define** and **distinguish** between simple birth processes, general birth processes, and time inhomogeneous Poisson processes / **定义**并**区分**简单生灭过程、一般生灭过程和时间非齐次泊松过程
2. **Derive** the forward equations for birth processes / **推导**生灭过程的前向方程
3. **Solve** the forward equations for the simple birth process / **求解**简单生灭过程的前向方程
4. **Calculate** probabilities and expectations for time inhomogeneous Poisson processes / **计算**时间非齐次泊松过程的概率和期望
5. **Apply** these models to real-world problems / **应用**这些模型解决实际问题
6. **Understand** the relationship between holding times and rates in birth processes / **理解**生灭过程中停留时间和速率之间的关系

## 📚 Prerequisites / 前置知识

Before starting this section, you should be familiar with / 开始本节学习前，你应该熟悉：

- **Poisson process basics / 泊松过程基础**: Definition, properties, inter-arrival times / 定义、性质、到达间隔时间
- **Exponential distribution / 指数分布**: PDF, CDF, memoryless property / 概率密度函数、累积分布函数、无记忆性
- **Minimum of exponential random variables / 指数随机变量的最小值**: Distribution of min of i.i.d. exponentials / 独立同分布指数随机变量最小值的分布
- **Basic differential equations / 基础微分方程**: Solving simple ODEs / 求解简单常微分方程
- **Poisson distribution / 泊松分布**: PMF, mean, variance / 概率质量函数、均值、方差

## 📖 Core Content / 核心内容

### Topic 16.1: Birth Processes / 生灭过程

#### Intuition / 直觉理解

**中文解释：** 想象一个生物实验，我们从单个细胞开始。这个细胞经过一段随机时间后分裂成两个细胞。然后，这两个细胞各自独立地经过随机时间后分裂，以此类推。这就是简单生灭过程（Simple Birth Process）的基本思想。与泊松过程不同，这里的"事件发生率"不是常数，而是随着种群规模的增加而增加——因为每个个体都在独立地产生后代。

**English explanation:** Imagine a biological experiment starting with a single cell. After a random amount of time, this cell divides into two cells. Then, each of these two cells independently divides after a random amount of time, and so on. This is the basic idea of the Simple Birth Process. Unlike the Poisson process, the "event rate" here is not constant but increases with the population size—because each individual is independently producing offspring.

**Key insight / 关键洞察：** The Poisson process is a special case of a birth process where the rate is constant (λₙ = λ). In a general birth process, the rate depends on the current state (population size). / 泊松过程是生灭过程的一个特例，其中速率是常数（λₙ = λ）。在一般生灭过程中，速率取决于当前状态（种群规模）。

#### Formal Definition / 形式化定义

**Definition 16.1 (Birth Process / 生灭过程):**

A birth process (Xₙ) with rates (λₙ) is defined by its starting population X(0) = x₀ and that the holding times are Tₙ ~ Exp(λₙ). So we have / 一个具有速率 (λₙ) 的生灭过程 (Xₙ) 由初始种群 X(0) = x₀ 和停留时间 Tₙ ~ Exp(λₙ) 定义。因此我们有：

$$X(t) = \begin{cases} 
x_0 & 0 \leq t < J_1 \\
x_0 + n & J_n \leq t < J_{n+1}, \text{ for } n = 1, 2, \ldots
\end{cases}$$

where / 其中：
- Jₙ = T₁ + T₂ + ... + Tₙ are the jump times / 跳跃时间
- Tₙ is the holding time in state x₀ + (n-1) / 在状态 x₀ + (n-1) 的停留时间
- λₙ is the rate when the population is n / 当种群规模为 n 时的速率

**Symbol Table / 符号表：**

| Symbol | Meaning (English) | 含义 (中文) |
|--------|-------------------|-------------|
| X(t) | Population size at time t | t时刻的种群规模 |
| λₙ | Birth rate when population is n | 种群规模为n时的出生率 |
| Tₙ | Holding time in state n-1 | 在状态n-1的停留时间 |
| Jₙ | Time of nth jump | 第n次跳跃的时间 |
| x₀ | Initial population | 初始种群规模 |

**Examples / 示例 (Example 16.1):**

1. **Simple Birth Process / 简单生灭过程**: x₀ = 1, λₙ = nλ
   - Each individual gives birth at rate λ / 每个个体以速率λ生育
   - Total rate = number of individuals × individual rate / 总速率 = 个体数 × 个体速率

2. **Poisson Process / 泊松过程**: x₀ = 0, λₙ = λ (constant)
   - Rate is constant regardless of state / 速率与状态无关，保持常数

3. **Birth Process with Immigration / 带移民的生灭过程**: x₀ = 1, λₙ = nλ + μ
   - Internal births at rate nλ / 内部出生速率为 nλ
   - Immigration from outside at rate μ / 外部移民速率为 μ

#### Key Properties / 关键性质

**Property 1: Holding Times / 停留时间性质**

For the simple birth process starting from X(0) = 1 / 对于从 X(0) = 1 开始的简单生灭过程：

- First holding time: T₁ ~ Exp(λ) (one individual) / 第一个停留时间：T₁ ~ Exp(λ)（一个个体）
- Second holding time: T₂ ~ Exp(2λ) (two individuals) / 第二个停留时间：T₂ ~ Exp(2λ)（两个个体）
- nth holding time: Tₙ ~ Exp(nλ) (n individuals) / 第n个停留时间：Tₙ ~ Exp(nλ)（n个个体）

**Why? / 为什么？** 
When there are n individuals, each has an Exp(λ) time until producing offspring. The time until the next offspring is the minimum of these n independent exponential random variables, which is Exp(nλ). / 当有n个个体时，每个个体产生后代的时间服从Exp(λ)。下一个后代出现的时间是这n个独立指数随机变量的最小值，服从Exp(nλ)。

**Property 2: Expected Population Size / 期望种群规模**

For the simple birth process / 对于简单生灭过程：
$$\mathbb{E}[X(t)] = e^{\lambda t}$$

This shows exponential growth on average / 这表明平均而言呈指数增长。

**Property 3: Forward Equations / 前向方程**

For j ≥ 2 / 对于 j ≥ 2:
$$p'_j(t) = -\lambda_j p_j(t) + \lambda_{j-1} p_{j-1}(t)$$

For j = 1 / 对于 j = 1:
$$p'_1(t) = -\lambda_1 p_1(t)$$

with initial conditions / 初始条件为：
- p₁(0) = 1 (starting from 1 individual / 从1个个体开始)
- pⱼ(0) = 0 for j ≥ 2

#### Derivation of Forward Equations / 前向方程的推导

**中文解释：** 让我们详细推导前向方程。这个推导过程与泊松过程的推导非常相似，关键区别在于速率λ被替换为依赖于状态的λⱼ。

**English explanation:** Let's derive the forward equations in detail. This derivation is very similar to that for the Poisson process, with the key difference being that the rate λ is replaced by the state-dependent λⱼ.

**Step 1: Consider the infinitesimal time period [t, t+τ] / 考虑无穷小时段 [t, t+τ]**

For j ≥ 2 / 对于 j ≥ 2:

$$p_j(t+\tau) = (1 - \lambda_j\tau + o(\tau))p_j(t) + (\lambda_{j-1}\tau + o(\tau))p_{j-1}(t) + o(\tau)$$

**Explanation / 解释：**
- First term / 第一项: We are already at state j and no birth occurs in (t, t+τ) / 我们已经在状态j，且在(t, t+τ)内没有出生事件
- Second term / 第二项: We are at state j-1 and a birth occurs in (t, t+τ) / 我们在状态j-1，且在(t, t+τ)内发生出生事件
- Third term / 第三项: All other possibilities (probability o(τ)) / 所有其他可能性（概率为o(τ)）

**Step 2: Rearrange / 重新整理**

$$p_j(t+\tau) - p_j(t) = -\lambda_j\tau p_j(t) + \lambda_{j-1}\tau p_{j-1}(t) + o(\tau)$$

**Step 3: Divide by τ and take limit τ → 0 / 除以τ并取极限τ → 0**

$$\frac{p_j(t+\tau) - p_j(t)}{\tau} = -\lambda_j p_j(t) + \lambda_{j-1} p_{j-1}(t) + \frac{o(\tau)}{\tau}$$

As τ → 0, the left side becomes p'_j(t) and o(τ)/τ → 0 / 当τ → 0时，左边变为p'_j(t)，且o(τ)/τ → 0。

**Result / 结果：**
$$p'_j(t) = -\lambda_j p_j(t) + \lambda_{j-1} p_{j-1}(t)$$

**For j = 1 / 对于 j = 1:**

$$p_1(t+\tau) = (1 - \lambda_1\tau + o(\tau))p_1(t) + o(\tau)$$

Following the same steps / 按照相同步骤：
$$p'_1(t) = -\lambda_1 p_1(t)$$

#### Worked Example: Simple Birth Process / 例题：简单生灭过程

**Problem / 问题：** For the simple birth process with rates λⱼ = λj starting from X(0) = 1, show that X(t) follows a geometric distribution / 对于从X(0)=1开始、速率为λⱼ=λj的简单生灭过程，证明X(t)服从几何分布：
$$p_j(t) = (1 - e^{-\lambda t})^{j-1} e^{-\lambda t}$$

**Solution / 解答：**

**Step 1: Verify for j = 1 / 验证 j = 1 的情况**

The forward equation for j = 1 is / j = 1 的前向方程为：
$$p'_1(t) = -\lambda_1 p_1(t) = -\lambda p_1(t)$$

With initial condition p₁(0) = 1 / 初始条件 p₁(0) = 1。

This is a simple ODE / 这是一个简单的常微分方程：
$$\frac{dp_1}{dt} = -\lambda p_1$$

Solution / 解：
$$p_1(t) = e^{-\lambda t}$$

This matches our formula with j = 1 / 这与我们的公式在 j = 1 时一致。

**Step 2: Verify for j ≥ 2 / 验证 j ≥ 2 的情况**

Assume the formula holds for j-1 / 假设公式对 j-1 成立：
$$p_{j-1}(t) = (1 - e^{-\lambda t})^{j-2} e^{-\lambda t}$$

The forward equation for j is / j 的前向方程为：
$$p'_j(t) = -\lambda j p_j(t) + \lambda(j-1) p_{j-1}(t)$$

**Step 3: Compute p'_j(t) from the proposed formula / 从假设的公式计算 p'_j(t)**

Let's write / 令：
$$p_j(t) = (1 - e^{-\lambda t})^{j-1} e^{-\lambda t}$$

Using the product rule / 使用乘积法则：
$$p'_j(t) = (j-1)(1 - e^{-\lambda t})^{j-2} \cdot \lambda e^{-\lambda t} \cdot e^{-\lambda t} + (1 - e^{-\lambda t})^{j-1} \cdot (-\lambda e^{-\lambda t})$$

Simplify / 简化：
$$p'_j(t) = \lambda(j-1)(1 - e^{-\lambda t})^{j-2} e^{-2\lambda t} - \lambda(1 - e^{-\lambda t})^{j-1} e^{-\lambda t}$$

**Step 4: Compute the right side of the forward equation / 计算前向方程的右边**

$$-\lambda j p_j(t) + \lambda(j-1) p_{j-1}(t)$$
$$= -\lambda j (1 - e^{-\lambda t})^{j-1} e^{-\lambda t} + \lambda(j-1) (1 - e^{-\lambda t})^{j-2} e^{-\lambda t}$$

**Step 5: Show equality / 证明相等**

We need to show / 我们需要证明：
$$\lambda(j-1)(1 - e^{-\lambda t})^{j-2} e^{-2\lambda t} - \lambda(1 - e^{-\lambda t})^{j-1} e^{-\lambda t} = -\lambda j (1 - e^{-\lambda t})^{j-1} e^{-\lambda t} + \lambda(j-1) (1 - e^{-\lambda t})^{j-2} e^{-\lambda t}$$

Factor out λ(1 - e^{-λt})^{j-2} e^{-λt} / 提取公因子 λ(1 - e^{-λt})^{j-2} e^{-λt}:

Left side / 左边：
$$\lambda(1 - e^{-\lambda t})^{j-2} e^{-\lambda t}[(j-1)e^{-\lambda t} - (1 - e^{-\lambda t})]$$
$$= \lambda(1 - e^{-\lambda t})^{j-2} e^{-\lambda t}[(j-1)e^{-\lambda t} - 1 + e^{-\lambda t}]$$
$$= \lambda(1 - e^{-\lambda t})^{j-2} e^{-\lambda t}[je^{-\lambda t} - 1]$$

Right side / 右边：
$$\lambda(1 - e^{-\lambda t})^{j-2} e^{-\lambda t}[-j(1 - e^{-\lambda t}) + (j-1)]$$
$$= \lambda(1 - e^{-\lambda t})^{j-2} e^{-\lambda t}[-j + je^{-\lambda t} + j - 1]$$
$$= \lambda(1 - e^{-\lambda t})^{j-2} e^{-\lambda t}[je^{-\lambda t} - 1]$$

Both sides are equal / 两边相等。✓

**Step 6: Calculate expected value / 计算期望值**

For a geometric distribution with parameter p = e^{-λt} / 对于参数 p = e^{-λt} 的几何分布：
$$\mathbb{E}[X(t)] = \frac{1}{p} = \frac{1}{e^{-\lambda t}} = e^{\lambda t}$$

This confirms the exponential growth mentioned earlier / 这证实了前面提到的指数增长。

### Topic 16.2: Time Inhomogeneous Poisson Process / 时间非齐次泊松过程

#### Intuition / 直觉理解

**中文解释：** 在标准的泊松过程中，事件发生的速率λ是常数，这意味着在任何时刻，事件发生的概率密度都是相同的。但在现实世界中，速率往往会随时间变化。例如，呼叫中心在早上刚开门时电话较少，随后逐渐增多；保险公司在特定季节收到的索赔更多。时间非齐次泊松过程（Time Inhomogeneous Poisson Process）允许速率λ(t)随时间变化，从而更真实地模拟这些现象。

**English explanation:** In the standard Poisson process, the rate λ is constant, meaning the probability density of an event occurring is the same at all times. However, in the real world, rates often change over time. For example, a call center receives fewer calls when it first opens in the morning, then gradually more; an insurance company receives more claims during certain seasons. The Time Inhomogeneous Poisson Process allows the rate λ(t) to vary with time, providing more realistic models for these phenomena.

**Key difference / 关键区别：**
- Homogeneous processes: Transition probabilities depend only on the state and time interval length / 齐次过程：转移概率仅取决于状态和时间间隔长度
- Inhomogeneous processes: Transition probabilities also depend on the current time / 非齐次过程：转移概率还取决于当前时间

#### Formal Definition / 形式化定义

**Definition 16.2 (Time Inhomogeneous Poisson Process / 时间非齐次泊松过程):**

A time inhomogeneous Poisson process with rate function λ = λ(t) ≥ 0 is a stochastic process (X(t)) with continuous time t ∈ [0, ∞) and state space S = ℤ₊ with the following properties / 具有速率函数 λ = λ(t) ≥ 0 的时间非齐次泊松过程是一个连续时间 t ∈ [0, ∞)、状态空间 S = ℤ₊ 的随机过程 (X(t))，具有以下性质：

1. **Initial condition / 初始条件**: X(0) = 0
2. **Poisson increments / 泊松增量**: 
   $$X(t+s) - X(t) \sim \text{Po}\left(\int_t^{t+s} \lambda(u) du\right) \text{ for all } s, t > 0$$
3. **Independent increments / 独立增量**: X(t₂) - X(t₁) and X(t₄) - X(t₃) are independent for all t₁ ≤ t₂ ≤ t₃ ≤ t₄

**Symbol Table / 符号表：**

| Symbol | Meaning (English) | 含义 (中文) |
|--------|-------------------|-------------|
| λ(t) | Rate function at time t | t时刻的速率函数 |
| ∫ₜ^{t+s} λ(u)du | Integrated rate over interval [t, t+s] | 区间[t, t+s]上的积分速率 |
| Po(μ) | Poisson distribution with mean μ | 均值为μ的泊松分布 |

**Special case / 特殊情况：**
If λ(t) = λ is constant, then ∫ₜ^{t+s} λ(u)du = λs, and we recover the standard Poisson process / 如果λ(t)=λ是常数，则∫ₜ^{t+s} λ(u)du = λs，我们得到标准泊松过程。

#### Key Properties / 关键性质

**Property 1: Infinitesimal Definition / 无穷小定义**

For small τ / 对于小的 τ：
$$\mathbb{P}(X(t+\tau) - X(t) = j) = \begin{cases}
1 - \lambda(t)\tau + o(\tau) & \text{if } j = 0 \\
\lambda(t)\tau + o(\tau) & \text{if } j = 1 \\
o(\tau) & \text{if } j \geq 2
\end{cases}$$

**Property 2: Mean and Variance / 均值和方差**

$$\mathbb{E}[X(t+s) - X(t)] = \text{Var}[X(t+s) - X(t)] = \int_t^{t+s} \lambda(u) du$$

This follows from the Poisson distribution property that mean = variance / 这源于泊松分布均值等于方差的性质。

#### Worked Example / 例题 (Example 16.2)

**Problem / 问题：** A call centre models incoming calls as a time inhomogeneous Poisson process with rate function / 一个呼叫中心将来电建模为时间非齐次泊松过程，速率函数为：
$$\lambda(t) = \begin{cases}
20t & 0 \leq t < 1 \\
20 & t \geq 1
\end{cases}$$
calls per hour / 每小时通话数。

**(a) Probability of no calls in first 10 minutes / 前10分钟没有电话的概率**

**Solution / 解答：**

**Step 1: Convert time to hours / 将时间转换为小时**
10 minutes = 1/6 hour / 10分钟 = 1/6小时

**Step 2: Calculate the integrated rate / 计算积分速率**
$$\int_0^{1/6} \lambda(t) dt = \int_0^{1/6} 20t \, dt = [10t^2]_0^{1/6} = 10 \cdot \frac{1}{36} = \frac{10}{36} = 0.278$$

**Step 3: Apply Poisson probability / 应用泊松概率**
Number of calls in first 10 minutes ~ Po(0.278) / 前10分钟的通话数 ~ Po(0.278)

$$\mathbb{P}(\text{no calls}) = e^{-0.278} \cdot \frac{0.278^0}{0!} = e^{-0.278} = 0.757$$

**(b) Expected number of calls in first 2 hours / 前2小时的期望通话数**

**Solution / 解答：**

**Step 1: Split the integral at t = 1 / 在 t = 1 处分割积分**
$$\int_0^2 \lambda(t) dt = \int_0^1 20t \, dt + \int_1^2 20 \, dt$$

**Step 2: Compute each part / 计算各部分**
$$\int_0^1 20t \, dt = [10t^2]_0^1 = 10$$
$$\int_1^2 20 \, dt = [20t]_1^2 = 40 - 20 = 20$$

**Step 3: Sum / 求和**
Total integrated rate = 10 + 20 = 30 / 总积分速率 = 10 + 20 = 30

**Step 4: Expected value / 期望值**
Since the number of calls ~ Po(30), the expected number is 30 / 由于通话数 ~ Po(30)，期望值为30。

#### Comparison: Homogeneous vs Inhomogeneous / 齐次与非齐次对比

| Property | Homogeneous Poisson | Inhomogeneous Poisson |
|----------|-------------------|----------------------|
| Rate | λ (constant) | λ(t) (time-dependent) |
| Increment distribution | Po(λs) | Po(∫ₜ^{t+s} λ(u)du) |
| Mean of increment | λs | ∫ₜ^{t+s} λ(u)du |
| Stationarity | Yes | No |
| Example | Radioactive decay | Call center traffic |

## 🔗 Connections / 知识关联

### Connection to Previous Topics / 与前面主题的联系

1. **Poisson Process (Chapter 14) / 泊松过程（第14章）**: 
   - The Poisson process is a special case of both birth processes (with λₙ = λ) and time inhomogeneous Poisson processes (with λ(t) = λ) / 泊松过程既是生灭过程（λₙ = λ）的特例，也是时间非齐次泊松过程（λ(t) = λ）的特例
   - The forward equation derivation follows the same pattern / 前向方程的推导遵循相同模式

2. **Exponential Distribution (Chapter 14) / 指数分布（第14章）**:
   - Holding times in birth processes are exponential / 生灭过程中的停留时间服从指数分布
   - Memoryless property is crucial for the derivation / 无记忆性对推导至关重要

### Connection to Future Topics / 与后续主题的联系

1. **Continuous Time Markov Chains (Chapter 17) / 连续时间马尔可夫链（第17章）**:
   - Birth processes are examples of continuous time Markov chains / 生灭过程是连续时间马尔可夫链的例子
   - The forward equations generalize to the Kolmogorov equations / 前向方程推广为柯尔莫哥洛夫方程

2. **Queueing Theory / 排队论**:
   - Birth processes model queue lengths / 生灭过程模拟队列长度
   - Time inhomogeneous Poisson processes model time-varying arrival rates / 时间非齐次泊松过程模拟时变的到达率

## ⚠️ Common Mistakes / 常见误区

### Mistake 1: Confusing λₙ with λ(t) / 混淆 λₙ 和 λ(t)

**Wrong / 错误：** Thinking λₙ in birth processes is the same as λ(t) in time inhomogeneous Poisson processes / 认为生灭过程中的 λₙ 与时间非齐次泊松过程中的 λ(t) 相同。

**Correct / 正确：** 
- λₙ depends on the state (population size) / λₙ 依赖于状态（种群规模）
- λ(t) depends on time / λ(t) 依赖于时间
- They are fundamentally different concepts / 它们本质上是不同的概念

### Mistake 2: Forgetting the initial conditions / 忘记初始条件

**Wrong / 错误：** Solving forward equations without specifying pⱼ(0) / 求解前向方程时未指定 pⱼ(0)。

**Correct / 正确：** Always include initial conditions / 始终包含初始条件：
- For simple birth process: p₁(0) = 1, pⱼ(0) = 0 for j ≥ 2 / 