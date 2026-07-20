# Section 2: Random walk

> MATH2702 - 自学教材 / Self-Study Guide
> 生成时间: 2026-07-20 15:35
> 来源页: 14-18

---

# MATH2702: Random Walk / 随机游走

## 📋 Section Overview / 章节概览

**中文解释：** 本章介绍随机游走（Random Walk）这一重要的随机过程模型。随机游走是最基本的随机过程之一，广泛应用于金融、物理、生物学等领域。我们将从最简单的简单随机游走开始，逐步扩展到一般随机游走，并学习如何计算其期望、方差以及精确分布。

**English explanation:** This chapter introduces the random walk, an important stochastic process model. Random walks are among the most fundamental stochastic processes, with applications in finance, physics, biology, and many other fields. We will start with the simplest case—the simple random walk—then extend to general random walks, and learn how to calculate their expectation, variance, and exact distribution.

**Real-world applications / 实际应用：**
- Stock price modeling / 股票价格建模
- Population dynamics / 种群动态
- Gas particle diffusion / 气体粒子扩散
- Gambling / 赌博问题

---

## 🎯 Learning Objectives / 学习目标

完成本章学习后，你应该能够：

1. **定义**简单随机游走和一般随机游走，并解释其马尔可夫性质
2. **计算**简单随机游走的概率分布（精确二项分布）
3. **推导**随机游走的期望和方差公式
4. **应用**正态近似对大 n 时的随机游走进行近似
5. **解决**涉及随机游走的实际问题

By the end of this chapter, you should be able to:

1. **Define** simple and general random walks and explain their Markov property
2. **Calculate** the probability distribution of a simple random walk (exact binomial distribution)
3. **Derive** expectation and variance formulas for random walks
4. **Apply** normal approximation for large n random walks
5. **Solve** practical problems involving random walks

---

## 📚 Prerequisites / 前置知识

在开始本章之前，你需要熟悉以下概念：

**中文解释：**
- 概率论基础：概率空间、随机变量、概率分布
- 期望和方差的计算
- 二项分布及其概率质量函数
- 独立同分布（IID）随机变量
- 条件概率和条件期望（将在问题中用到）

**English explanation:**
- Basic probability theory: probability spaces, random variables, probability distributions
- Calculation of expectation and variance
- Binomial distribution and its probability mass function
- Independent and identically distributed (IID) random variables
- Conditional probability and conditional expectation (will be used in problems)

---

## 📖 Core Content / 核心内容

---

### Topic 1: Simple Random Walk / 简单随机游走

#### Intuition / 直觉理解

**中文解释：** 想象一个醉汉在一条直线上行走。他从原点（0）出发，每一步随机地向上（+1）或向下（-1）移动一个单位。经过 n 步后，他的位置就是这 n 次随机移动的累计结果。这就是"简单随机游走"的基本思想。当向上和向下的概率相等时（各为 1/2），我们称之为"简单对称随机游走"。

**English explanation:** Imagine a drunkard walking on a straight line. Starting from the origin (0), at each step they randomly move up (+1) or down (-1) by one unit. After n steps, their position is the cumulative result of these n random moves. This is the basic idea of a "simple random walk." When the probabilities of moving up and down are equal (both 1/2), we call it a "simple symmetric random walk."

**Real-world applications / 实际应用：**
- Stock prices / 股票价格
- Population sizes / 种群规模
- Gas particle positions / 气体粒子位置
- "Drunkard's walk" model / "醉汉行走"模型

#### Formal Definition / 形式化定义

**English definition:** Consider the following simple random walk on the integers ℤ: We start at 0, then at each time step, we go up by one with probability p and down by one with probability q = 1 - p. When p = q = 1/2, we are equally likely to go up as down, and we call this the simple symmetric random walk.

**中文定义：** 考虑整数集 ℤ 上的简单随机游走：我们从 0 出发，每一步以概率 p 向上移动 1，以概率 q = 1 - p 向下移动 1。当 p = q = 1/2 时，向上和向下的概率相等，我们称之为简单对称随机游走。

**Mathematical representation / 数学表示：**

We can write this as a stochastic process (Xₙ) with:
- Discrete time: n ∈ {0, 1, 2, ...} = ℤ₊
- Discrete state space: 𝒮 = ℤ
- Initial condition: X₀ = 0
- Transition rule: For n ≥ 0,
  Xₙ₊₁ = { Xₙ + 1 with probability p
           Xₙ - 1 with probability q }

**Symbol explanation table / 符号说明表：**

| Symbol | Meaning | 含义 |
|--------|---------|------|
| Xₙ | Position at time n | 第 n 时刻的位置 |
| n | Time step | 时间步 |
| p | Probability of moving up | 向上移动的概率 |
| q | Probability of moving down (q = 1-p) | 向下移动的概率 |
| ℤ | Set of all integers | 整数集 |
| 𝒮 | State space | 状态空间 |

#### Markov Property / 马尔可夫性质

**中文解释：** 从定义可以清楚地看到，Xₙ₊₁（未来）依赖于 Xₙ（现在），但在给定 Xₙ 的条件下，不依赖于 Xₙ₋₁, ..., X₁, X₀（过去）。这就是马尔可夫性质（Markov property）。因此，简单随机游走是一个离散时间马尔可夫过程（Markov chain）。

**English explanation:** It is clear from the definition that Xₙ₊₁ (the future) depends on Xₙ (the present), but, given Xₙ, does not depend on Xₙ₋₁, ..., X₁, X₀ (the past). Thus the Markov property holds, and the simple random walk is a discrete time Markov process or Markov chain.

**Key insight / 关键理解：** 随机游走的"记忆"只有一步——未来的位置只取决于当前位置，而不取决于过去的历史。

#### Worked Examples / 例题

**Example 2.1 / 例 2.1**

**Problem / 问题：** What is the probability that after two steps a simple random walk has reached X₂ = 2?

**中文解释：** 要到达 X₂ = 2，必须在两个时间步都向上移动。所以概率为 p × p = p²。

**Solution / 解答：**
To achieve X₂ = 2, the walk must go upwards in both time steps.
ℙ(X₂ = 2) = p × p = p²

**Example 2.2 / 例 2.2**

**Problem / 问题：** What is the probability that after three steps a simple random walk has reached X₃ = -1?

**中文解释：** 要到达 -1，需要三步中有两步向下、一步向上。有三种可能的路径：
1. 上-下-下 (up-down-down)
2. 下-上-下 (down-up-down)
3. 下-下-上 (down-down-up)

每种路径的概率都是 p × q × q = pq²，所以总概率为 3pq²。

**Solution / 解答：**
There are three ways to reach -1 after three steps:
- up-down-down: probability p × q × q = pq²
- down-up-down: probability q × p × q = pq²
- down-down-up: probability q × q × p = pq²

ℙ(X₃ = -1) = pq² + pq² + pq² = 3pq²

**General pattern / 一般规律：** 这实际上就是二项分布的应用——在 n 步中恰好有 k 次向上的概率。

---

### Topic 2: General Random Walks / 一般随机游走

#### Alternative Representation / 另一种表示方式

**中文解释：** 简单随机游走可以用另一种方式表示：将每一步的移动看作一个独立的随机变量 Zᵢ，其中 Zᵢ = +1（概率 p）或 Zᵢ = -1（概率 q）。那么 n 步后的位置就是初始位置加上所有步长之和。

**English explanation:** An alternative way to write the simple random walk is to express it as the sum of independent increments. Let Zᵢ be the step at time i, where Zᵢ = +1 (with probability p) or Zᵢ = -1 (with probability q). Then the position after n steps is the initial position plus the sum of all steps.

**Formal definition / 形式化定义：**

Xₙ = X₀ + Σᵢ₌₁ⁿ Zᵢ

where:
- X₀ = 0 (starting point / 起点)
- Z₁, Z₂, ... are independent and identically distributed (IID) random variables
- ℙ(Zᵢ = 1) = p and ℙ(Zᵢ = -1) = q

**Symbol explanation table / 符号说明表：**

| Symbol | Meaning | 含义 |
|--------|---------|------|
| Xₙ | Position at time n | 第 n 时刻的位置 |
| X₀ | Initial position | 初始位置 |
| Zᵢ | Step at time i (increment) | 第 i 步的步长（增量） |
| Σᵢ₌₁ⁿ | Sum from i=1 to n | 从 i=1 到 n 的求和 |

**Check / 验证：** You can check that Xₙ₊₁ = Xₙ + Zₙ₊₁, and that this property defines the simple random walk.

#### General Random Walk Definition / 一般随机游走定义

**中文解释：** 任何具有形式 Xₙ = X₀ + Σᵢ₌₁ⁿ Zᵢ 的随机过程，其中 Zᵢ 是独立同分布的随机变量（不一定是 ±1），都称为随机游走（不带有"简单"二字）。

**English explanation:** Any stochastic process with the form Xₙ = X₀ + Σᵢ₌₁ⁿ Zᵢ for some X₀ and some distribution for the IID Zᵢ's is called a random walk (without the word "simple").

**Extensions / 扩展：**
- State space can be ℤ (like simple random walk) or other spaces
- Higher dimensional: e.g., in ℤ², step up, down, left, or right each with probability 1/4
- Continuous state space: e.g., ℝ if Zᵢ have a normal distribution

#### Expectation of a Random Walk / 随机游走的期望

**中文解释：** 利用期望的线性性质，我们可以计算任意随机游走的期望。由于 Zᵢ 是同分布的，每个 Zᵢ 的期望都等于 Z₁ 的期望。

**English explanation:** Using the linearity of expectation, we can calculate the expectation of any random walk. Since the Zᵢ are identically distributed, each Zᵢ has the same expectation as Z₁.

**Derivation / 推导：**

𝔼[Xₙ] = 𝔼[X₀ + Σᵢ₌₁ⁿ Zᵢ]
       = 𝔼[X₀] + Σᵢ₌₁ⁿ 𝔼[Zᵢ]
       = 𝔼[X₀] + n𝔼[Z₁]

**For the simple random walk / 对于简单随机游走：**
- 𝔼[X₀] = 0 (since we start from 0 with certainty / 因为我们确定从 0 出发)
- 𝔼[Z₁] = Σ_{z∈ℤ} z ℙ(Z₁ = z) = 1 × p + (-1) × q = p - q

**Therefore / 因此：**
𝔼[Xₙ] = n(p - q)

**Interpretation / 解释：**
- If p > 1/2, then p > q, so 𝔼[Xₙ] grows ever bigger over time (向上趋势)
- If p < 1/2, then 𝔼[Xₙ] grows ever smaller (negative with larger absolute value) over time (向下趋势)
- If p = 1/2 = q (symmetric case), then 𝔼[Xₙ] = 0 for all time (无趋势)

#### Variance of a Random Walk / 随机游走的方差

**中文解释：** 计算方差时，关键条件是 X₀ 和所有 Zᵢ 是独立的，因此没有协方差项。利用方差的可加性（对独立随机变量），我们可以得到简洁的公式。

**English explanation:** When calculating variance, the crucial condition is that X₀ and all Zᵢ are independent, so there are no covariance terms. Using the additivity of variance for independent random variables, we get a clean formula.

**Derivation / 推导：**

Var(Xₙ) = Var(X₀ + Σᵢ₌₁ⁿ Zᵢ)
         = Var(X₀) + Σᵢ₌₁ⁿ Var(Zᵢ)
         = Var(X₀) + n Var(Z₁)

**For the simple random walk / 对于简单随机游走：**
- Var(X₀) = 0 (since we always start from 0 with certainty / 因为我们确定从 0 出发)

**Calculate Var(Z₁) / 计算 Var(Z₁)：**

Var(Z₁) = 𝔼[(Z₁ - 𝔼[Z₁])²]

First, 𝔼[Z₁] = p - q (as calculated above)

Var(Z₁) = p(1 - (p-q))² + q(-1 - (p-q))²

Let's simplify step by step / 逐步简化：

1 - (p-q) = 1 - p + q = q + q = 2q (since 1-p = q)
-1 - (p-q) = -1 - p + q = -(1+p-q) = -(p+q+p-q) = -2p (since 1 = p+q)

So:
Var(Z₁) = p(2q)² + q(-2p)²
         = p(4q²) + q(4p²)
         = 4pq² + 4p²q
         = 4pq(q + p)
         = 4pq(1)  (since p+q=1)
         = 4pq

**Therefore / 因此：**
Var(Xₙ) = 4pqn

**For the symmetric case / 对称情况：**
When p = q = 1/2:
Var(Xₙ) = 4 × (1/2) × (1/2) × n = n

**Interpretation / 解释：**
- Unless p is 0 or 1, the variance grows over time (方差随时间增长)
- It becomes harder and harder to predict where the random walk will be (预测越来越困难)

#### Normal Approximation / 正态近似

**中文解释：** 对于大 n，我们可以用正态分布来近似随机游走。假设增量 Zₙ 的均值为 μ，方差为 σ²，且从 X₀ = 0 出发，则 Xₙ 近似服从 N(μn, σ²n)。

**English explanation:** For large n, we can use a normal approximation for a random walk. Suppose the increments Zₙ have mean μ and variance σ², and the walk starts from X₀ = 0. Then Xₙ is approximately N(μn, σ²n).

**Formal statement / 正式表述：**

As n → ∞:
(Xₙ - nμ) / (σ√n) → N(0, 1)

This is the Central Limit Theorem (中心极限定理) applied to the sum of IID random variables.

**Important note / 重要说明：** Remember that the Xₙ are not independent (Xₙ 之间不是独立的).

---

### Topic 3: Exact Distribution of the Simple Random Walk / 简单随机游走的精确分布

#### Binomial Distribution Connection / 与二项分布的联系

**中文解释：** 对于简单随机游走，我们可以给出精确的分布公式。关键在于：在 n 步中，每一步独立地以概率 p 向上、以概率 q 向下。设 Yₙ 为前 n 步中向上步数的总数，则 Yₙ 服从二项分布 Bin(n, p)。

**English explanation:** For the simple random walk, we can give the exact distribution. The key insight: in n steps, each step independently goes up with probability p or down with probability q. Let Yₙ be the total number of upward steps in the first n steps. Then Yₙ follows a binomial distribution Bin(n, p).

**Binomial distribution / 二项分布：**

ℙ(Yₙ = k) = (n choose k) pᵏ qⁿ⁻ᵏ

where (n choose k) = n! / (k!(n-k)!)

for k = 0, 1, ..., n.

#### Derivation of Exact Distribution / 精确分布的推导

**中文解释：** 如果 Yₙ = k，意味着有 k 步向上，n-k 步向下。最终位置为：
Xₙ = k - (n-k) = 2k - n

因此：
ℙ(Xₙ = 2k - n) = ℙ(Yₙ = k) = (n choose k) pᵏ qⁿ⁻ᵏ

**English explanation:** If Yₙ = k, that means we've taken k upward steps and n-k downward steps, leaving us at position:
Xₙ = k - (n-k) = 2k - n

Thus:
ℙ(Xₙ = 2k - n) = ℙ(Yₙ = k) = (n choose k) pᵏ qⁿ⁻ᵏ

**Parity observation / 奇偶性观察：**
- After an odd number of steps n, we are always at an odd-numbered state (奇数步后位置为奇数)
- After an even number of steps n, we are always at an even-numbered state (偶数步后位置为偶数)

#### Alternative Form / 另一种形式

**中文解释：** 设 i = 2k - n，则 k = (n+i)/2，n-k = (n-i)/2。代入公式得到：

**English explanation:** Let i = 2k - n, then k = (n+i)/2 and n-k = (n-i)/2. Substituting into the formula:

ℙ(Xₙ = i) = (n choose (n+i)/2) p^{(n+i)/2} q^{(n-i)/2}

when n and i have the same parity (奇偶性相同) and -n ≤ i ≤ n, and is 0 otherwise.

#### Symmetric Case / 对称情况

**中文解释：** 对于简单对称随机游走 (p = q = 1/2)：

**English explanation:** For the simple symmetric random walk (p = q = 1/2):

ℙ(Xₙ = i) = (n choose (n+i)/2) (1/2)^{(n+i)/2} (1/2)^{(n-i)/2}
           = (n choose (n+i)/2) 2^{-n}

---

## 🔗 Connections / 知识关联

**中文解释：** 本章的随机游走是后续学习马尔可夫链的基础。在下一节中，我们将看到离散时间马尔可夫链的一般定义。随机游走是马尔可夫链的一个特例，理解它有助于掌握更一般的理论。

**English explanation:** The random walk in this chapter is the foundation for studying Markov chains. In the next section, we will see the general definition of discrete-time Markov chains. Random walks are a special case of Markov chains, and understanding them helps in mastering the more general theory.

**Connections to previous knowledge / 与前置知识的联系：**
- Binomial distribution (二项分布) from probability theory
- Expectation and variance (期望和方差) from statistics
- Central Limit Theorem (中心极限定理) from probability theory

---

## ⚠️ Common Mistakes / 常见误区

1. **混淆随机游走和独立同分布序列**
   - ❌ 认为 Xₙ 是独立同分布的
   - ✅ Xₙ 不是独立的，但增量 Zᵢ 是独立同分布的

2. **错误计算方差**
   - ❌ 忘记协方差项
   - ✅ 由于独立性，协方差项为零，但需要确认独立性条件

3. **奇偶性错误**
   - ❌ 认为 n 为奇数时 Xₙ 可以是偶数
   - ✅ n 为奇数时 Xₙ 必为奇数，n 为偶数时 Xₙ 必为偶数

4. **正态近似的误用**
   - ❌ 对小 n 使用正态近似
   - ✅ 正态近似只适用于大 n

5. **混淆 p 和 q**
   - ❌ 忘记 q = 1-p
   - ✅ 始终记住 q = 1-p

---

## ✍️ Practice / 练习

### Self-Test Questions / 自测题

**Question 1 / 问题 1：**
For a simple random walk with p = 0.6, calculate ℙ(X₃ = 1).

**Hint / 提示：** 需要多少步向上才能到达 X₃ = 1？列出所有可能的路径。

**Question 2 / 问题 2：**
For a simple symmetric random walk (p = q = 1/2), find ℙ(X₄ = 0).

**Hint / 提示：** 需要 2 步向上和 2 步向下。使用二项分布公式。

**Question 3 / 问题 3：**
Calculate 𝔼[X₅] and Var(X₅) for a simple random walk with p = 0.7.

**Hint / 提示：** 使用公式 𝔼[Xₙ] = n(p-q) 和 Var(Xₙ) = 4pqn。

**Question 4 / 问题 4：**
For a general random walk where Zᵢ ~ N(0, 1) and X₀ = 5, find 𝔼[X₁₀] and Var(X₁₀).

**Hint / 提示：** 使用一般随机游走的期望和方差公式。

**Question 5 / 问题 5：**
Show that for a simple symmetric random walk, ℙ(X₂ₙ = 0) = (2n choose n) 2^{-2n}.

**Hint / 提示：** 需要 n 步向上和 n 步向下。使用精确分布公式。

---

## 📌 Key Takeaways / 要点总结

1. **Simple random walk definition / 简单随机游走定义：** X₀ = 0, each step +1 with prob p, -1 with prob q = 1-p.

2. **Markov property / 马尔可夫性质：** Future depends only on present, not on past (未来只取决于现在，不取决于过去).

3. **General random walk / 一般随机游走：** Xₙ = X₀ + Σᵢ₌₁ⁿ Zᵢ, where Zᵢ are IID.

4. **Expectation / 期望：** 𝔼[Xₙ] = 𝔼[X₀] + n𝔼[Z₁]; for simple random walk: 𝔼[Xₙ] = n(p-q).

5. **Variance / 方差：** Var(Xₙ) = Var(X₀) + n Var(Z₁); for simple random walk: Var(Xₙ) = 4pqn.

6. **Exact distribution / 精确分布：** ℙ(Xₙ = i) = (n choose (n+i)/2) p^{(n+i)/2} q^{(n-i)/2}, when n and i have same parity.

7. **Normal approximation / 正态近似：** For large n, Xₙ ≈ N(μn, σ²n) by CLT.

8. **Symmetric case / 对称情况：** When p = q = 1/2, 𝔼[Xₙ] = 0 and Var(Xₙ) = n.

---

*End of Chapter 2 Study Guide / 第二章学习指南结束*