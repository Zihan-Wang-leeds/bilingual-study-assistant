# Section 4: Martingales and Gambler’s ruin

> MATH2702 - 自学教材 / Self-Study Guide
> 生成时间: 2026-07-20 15:37
> 来源页: 22-29

---

# MATH2702: Stochastic Processes / 随机过程

## Section 4: Martingales and Gambler's Ruin / 鞅与赌徒破产问题

---

### 📋 Section Overview / 章节概览

**中文解释：** 本章节将介绍两个重要的随机过程概念：鞅（Martingale）和赌徒破产问题（Gambler's Ruin）。鞅是一种特殊的随机过程，其核心性质是"公平游戏"——给定当前信息，未来一步的期望值等于当前值。赌徒破产问题则是一个经典的马尔可夫链模型，研究两个赌徒之间的赌博游戏，直到一方输光所有资金为止。我们将使用鞅理论来优雅地解决赌徒破产问题中的两个关键问题：破产概率和游戏期望持续时间。

**English explanation:** This section introduces two important concepts in stochastic processes: martingales and the gambler's ruin problem. A martingale is a special type of stochastic process with the key property of a "fair game" — given current information, the expected value of the next step equals the current value. The gambler's ruin problem is a classic Markov chain model that studies a gambling game between two players until one loses all their money. We will use martingale theory to elegantly solve two key questions in the gambler's ruin problem: the probability of ruin and the expected duration of the game.

---

### 🎯 Learning Objectives / 学习目标

完成本章学习后，你应该能够：

1. **定义鞅**并理解其作为"公平游戏"模型的直观含义
2. **识别**一个随机过程是否为鞅，并能够构造鞅
3. **理解**赌徒破产马尔可夫链的转移概率和状态空间
4. **计算**赌徒破产问题中的破产概率，使用鞅方法和差分方程方法
5. **计算**赌徒破产问题的期望持续时间
6. **理解**停时（stopping time）的概念和可选停时定理（Optional Stopping Theorem）

After completing this section, you should be able to:

1. **Define a martingale** and understand its intuitive meaning as a "fair game" model
2. **Identify** whether a stochastic process is a martingale, and be able to construct martingales
3. **Understand** the transition probabilities and state space of the gambler's ruin Markov chain
4. **Calculate** the probability of ruin in the gambler's ruin problem, using martingale methods and difference equation methods
5. **Calculate** the expected duration of the gambler's ruin game
6. **Understand** the concept of stopping time and the Optional Stopping Theorem

---

### 📚 Prerequisites / 前置知识

在开始本章之前，你应该熟悉以下概念：

**中文解释：**
- **条件期望（Conditional Expectation）：** 理解 𝔼(𝑋|𝑌) 的含义，即给定随机变量 𝑌 时 𝑋 的期望值。条件期望本身是一个随机变量。
- **马尔可夫链（Markov Chain）：** 理解马尔可夫性质——给定当前状态，未来与过去独立。
- **简单随机游走（Simple Random Walk）：** 理解 𝑋ₙ = 𝑋₀ + ∑ᵢ₌₁ⁿ 𝑍ᵢ，其中 𝑍ᵢ 是独立同分布的 ±1 随机变量。
- **概率论基础：** 期望值、方差、条件概率。

**English explanation:**
- **Conditional Expectation:** Understand the meaning of 𝔼(𝑋|𝑌), the expected value of 𝑋 given the random variable 𝑌. Conditional expectation is itself a random variable.
- **Markov Chain:** Understand the Markov property — given the current state, the future is independent of the past.
- **Simple Random Walk:** Understand that 𝑋ₙ = 𝑋₀ + ∑ᵢ₌₁ⁿ 𝑍ᵢ, where 𝑍ᵢ are i.i.d. ±1 random variables.
- **Probability Basics:** Expectation, variance, conditional probability.

---

## 4.1 Martingales / 鞅

### Intuition / 直觉理解

**中文解释：**

想象你在玩一个"公平"的赌博游戏。假设你现在有 100 元。在公平游戏中，下一轮结束后，你期望拥有的钱数仍然是 100 元——你不期望赢钱，也不期望输钱。这就是鞅的核心思想：**给定当前的信息，未来一步的期望值等于当前值**。

鞅（Martingale）这个词与马具无关（不是"马鞅"）。它来自法语，最初指一种赌博策略，其中赌徒在输钱后加倍赌注。但在概率论中，鞅代表一种"公平游戏"的数学模型。

**English explanation:**

Imagine you're playing a "fair" gambling game. Suppose you currently have 100 yuan. In a fair game, after the next round, your expected amount of money is still 100 yuan — you don't expect to win or lose. This is the core idea of a martingale: **given current information, the expected value of the next step equals the current value**.

The word "martingale" has nothing to do with horse tack. It comes from French and originally referred to a gambling strategy where the gambler doubles their bet after losing. But in probability theory, a martingale represents a mathematical model of a "fair game".

**Key intuition / 关键直觉：**
- 鞅 = 公平游戏 (fair game)
- 你不能期望在鞅中获利或亏损
- 鞅的"未来最佳预测"就是"现在"

---

### Formal Definition / 形式化定义

**Definition 4.1 (Martingale / 鞅的定义).** A discrete time stochastic process (𝑀ₙ)ₙ≥₀ on a state space 𝒮 (not necessarily discrete) is a **martingale** with respect to another discrete time stochastic process (𝑋ₙ)ₙ≥₀ if, for all 𝑛 ≥ 0:

1. 𝔼|𝑀ₙ| < ∞ (可积性条件)
2. 𝔼(𝑀ₙ₊₁ | 𝑋₀, 𝑋₁, …, 𝑋ₙ) = 𝑀ₙ (鞅性质)

**中文解释：**

定义中的两个条件：
1. **可积性条件：** 𝑀ₙ 的绝对值的期望是有限的。这确保我们能够计算条件期望。
2. **鞅性质：** 给定直到时间 𝑛 的所有信息（即 𝑋₀, 𝑋₁, …, 𝑋ₙ），下一时刻 𝑀ₙ₊₁ 的条件期望等于当前值 𝑀ₙ。

注意：如果我们定义 𝑍ₙ = (𝑋₀, …, 𝑋ₙ)，那么 𝔼(𝑀ₙ₊₁ | 𝑋₀, 𝑋₁, …, 𝑋ₙ) = 𝔼(𝑀ₙ₊₁ | 𝑍ₙ)，这符合我们条件期望的定义。

**重要提醒：** 条件期望是随机变量，所以像 𝔼(𝐴|𝐵) = 𝐶 这样的等式只需要几乎必然成立（即概率为 1 地成立）。

**English explanation:**

The two conditions in the definition:
1. **Integrability condition:** The expected absolute value of 𝑀ₙ is finite. This ensures we can compute conditional expectations.
2. **Martingale property:** Given all information up to time 𝑛 (i.e., 𝑋₀, 𝑋₁, …, 𝑋ₙ), the conditional expectation of the next value 𝑀ₙ₊₁ equals the current value 𝑀ₙ.

Note: If we define 𝑍ₙ = (𝑋₀, …, 𝑋ₙ), then 𝔼(𝑀ₙ₊₁ | 𝑋₀, 𝑋₁, …, 𝑋ₙ) = 𝔼(𝑀ₙ₊₁ | 𝑍ₙ), which fits our definition of conditional expectation.

**Important reminder:** Conditional expectations are random variables, so equalities like 𝔼(𝐴|𝐵) = 𝐶 need only hold almost surely (i.e., with probability 1).

---

### Symbol Table / 符号表

| Symbol | Meaning (English) | 含义（中文） |
|--------|-------------------|--------------|
| 𝑀ₙ | The martingale process at time n | 鞅过程在时间 n 的值 |
| 𝑋ₙ | Another stochastic process (the "information" process) | 另一个随机过程（"信息"过程） |
| 𝒮 | State space | 状态空间 |
| 𝔼(·) | Expectation operator | 期望算子 |
| 𝔼(·|·) | Conditional expectation | 条件期望 |
| ℤ⁺ | Non-negative integers {0, 1, 2, ...} | 非负整数集合 |

---

### Example 4.1: Simple Random Walk as a Martingale / 简单随机游走作为鞅

**Question / 问题：** Is the simple random walk a martingale? If so, with respect to what process?

**中文解释：**

考虑简单随机游走：𝑋ₙ = 𝑋₀ + ∑ᵢ₌₁ⁿ 𝑍ᵢ，其中 𝑍ᵢ 是独立同分布的随机变量：
- ℙ(𝑍ᵢ = +1) = 𝑝
- ℙ(𝑍ᵢ = -1) = 𝑞 = 1 - 𝑝

**Step 1: Check integrability / 检查可积性**
𝔼|𝑋ₙ| ≤ |𝑋₀| + 𝑛 < ∞ ✓

**Step 2: Check martingale property / 检查鞅性质**
𝔼(𝑋ₙ₊₁ | 𝑋₀, 𝑍₁, …, 𝑍ₙ) = 𝔼(𝑋ₙ + 𝑍ₙ₊₁ | 𝑋₀, 𝑍₁, …, 𝑍ₙ)
= 𝑋ₙ + 𝔼(𝑍ₙ₊₁)  (因为 𝑍ₙ₊₁ 与过去独立)
= 𝑋ₙ + (𝑝 - 𝑞)

**Conclusion / 结论：**
- 如果 𝑝 = 𝑞（对称随机游走），则 𝔼(𝑋ₙ₊₁ | ·) = 𝑋ₙ，所以 (𝑋ₙ) 是关于 (𝑍ₙ) 的鞅。
- 如果 𝑝 ≠ 𝑞，则 (𝑋ₙ) 不是鞅。

**Generalization / 推广：**
更一般地，𝑀ₙ = 𝑋ₙ - 𝑛(𝑝 - 𝑞) 是关于 (𝑍ₙ) 的鞅，对任意 𝑝 ∈ [0, 1] 都成立。

验证：𝔼(𝑀ₙ₊₁ | ·) = 𝔼(𝑋ₙ₊₁ - (𝑛+1)(𝑝-𝑞) | ·)
= 𝔼(𝑋ₙ + 𝑍ₙ₊₁ - 𝑛(𝑝-𝑞) - (𝑝-𝑞) | ·)
= 𝑋ₙ - 𝑛(𝑝-𝑞) + 𝔼(𝑍ₙ₊₁) - (𝑝-𝑞)
= 𝑀ₙ + (𝑝-𝑞) - (𝑝-𝑞) = 𝑀ₙ ✓

**English explanation:**

Consider the simple random walk: 𝑋ₙ = 𝑋₀ + ∑ᵢ₌₁ⁿ 𝑍ᵢ, where 𝑍ᵢ are i.i.d. random variables:
- ℙ(𝑍ᵢ = +1) = 𝑝
- ℙ(𝑍ᵢ = -1) = 𝑞 = 1 - 𝑝

**Step 1: Check integrability**
𝔼|𝑋ₙ| ≤ |𝑋₀| + 𝑛 < ∞ ✓

**Step 2: Check martingale property**
𝔼(𝑋ₙ₊₁ | 𝑋₀, 𝑍₁, …, 𝑍ₙ) = 𝔼(𝑋ₙ + 𝑍ₙ₊₁ | 𝑋₀, 𝑍₁, …, 𝑍ₙ)
= 𝑋ₙ + 𝔼(𝑍ₙ₊₁)  (since 𝑍ₙ₊₁ is independent of the past)
= 𝑋ₙ + (𝑝 - 𝑞)

**Conclusion:**
- If 𝑝 = 𝑞 (symmetric random walk), then 𝔼(𝑋ₙ₊₁ | ·) = 𝑋ₙ, so (𝑋ₙ) is a martingale with respect to (𝑍ₙ).
- If 𝑝 ≠ 𝑞, then (𝑋ₙ) is not a martingale.

**Generalization:**
More generally, 𝑀ₙ = 𝑋ₙ - 𝑛(𝑝 - 𝑞) is a martingale with respect to (𝑍ₙ) for any 𝑝 ∈ [0, 1].

Verification: 𝔼(𝑀ₙ₊₁ | ·) = 𝔼(𝑋ₙ₊₁ - (𝑛+1)(𝑝-𝑞) | ·)
= 𝔼(𝑋ₙ + 𝑍ₙ₊₁ - 𝑛(𝑝-𝑞) - (𝑝-𝑞) | ·)
= 𝑋ₙ - 𝑛(𝑝-𝑞) + 𝔼(𝑍ₙ₊₁) - (𝑝-𝑞)
= 𝑀ₙ + (𝑝-𝑞) - (𝑝-𝑞) = 𝑀ₙ ✓

---

### Important Observation / 重要观察

**中文解释：**

鞅不一定是马尔可夫链。考虑一个例子：对称随机游走，以 1/2 概率向上或向下移动，但如果连续两次向上或向下移动，则下一步必须停留在原地。你可以验证这是一个鞅，但不是马尔可夫链（其转移依赖于前两步，而不仅仅是前一步）。

**常见主题：** 我们可以通过对随机过程应用适当的函数来找到/构造鞅。例如，上面的例子中函数是 𝑓(𝑥) = 𝑥 - 𝑛(𝑝-𝑞)。

**English explanation:**

Martingales are not necessarily Markov chains. Consider an example: a symmetric random walk that moves up/down with probability 1/2, except that if it moves upwards or downwards twice in a row, then on the next step it has to stay where it is. You can check this is a martingale but not a Markov chain (its transitions depend on the previous two steps, not just on the previous step).

**Common theme:** We can find/construct a martingale from a stochastic process by applying the right function to it. For example, in the above case the function was 𝑓(𝑥) = 𝑥 - 𝑛(𝑝-𝑞).

---

## 4.2 Gambler's Ruin Markov Chain / 赌徒破产马尔可夫链

### Problem Setup / 问题设定

**中文解释：**

Alice 和 Bob 在赌博。游戏规则如下：
- Alice 初始有 £𝑎，Bob 初始有 £𝑏
- 总金额 𝑚 = 𝑎 + 𝑏，所以 Bob 有 £(𝑚 - 𝑎)
- 每轮游戏，两人各下注 £1
- Alice 以概率 𝑝 赢得 Bob 的 £1
- Bob 以概率 𝑞 赢得 Alice 的 £1（其中 𝑝 + 𝑞 = 1）
- 游戏持续到一方输光所有钱（即"破产"）

**English explanation:**

Alice is gambling against Bob. The game rules are as follows:
- Alice starts with £𝑎, Bob starts with £𝑏
- Total amount 𝑚 = 𝑎 + 𝑏, so Bob has £(𝑚 - 𝑎)
- At each step, both players bet £1
- Alice wins £1 from Bob with probability 𝑝
- Bob wins £1 from Alice with probability 𝑞 (where 𝑝 + 𝑞 = 1)
- The game continues until one player is out of money (i.e., "ruined")

---

### Mathematical Formulation / 数学表述

**中文解释：**

令 𝑋ₙ 表示 Alice 在 n 步后的钱数。这是一个离散时间随机过程，时间 𝑛 ∈ {0, 1, 2, ...} = ℤ⁺，状态空间 𝒮 = {0, 1, ..., 𝑚}。

初始条件：𝑋₀ = 𝑎

转移规则：
- 当 1 ≤ 𝑋ₙ ≤ 𝑚-1 时（游戏进行中）：
  - 𝑋ₙ₊₁ = 𝑋ₙ + 1 以概率 𝑝
  - 𝑋ₙ₊₁ = 𝑋ₙ - 1 以概率 𝑞
- 当 𝑋ₙ = 0 时（Alice 已破产）：𝑋ₙ₊₁ = 0
- 当 𝑋ₙ = 𝑚 时（Bob 已破产）：𝑋ₙ₊₁ = 𝑚

**English explanation:**

Let 𝑋ₙ denote how much money Alice has after n steps. This is a discrete-time stochastic process with time 𝑛 ∈ {0, 1, 2, ...} = ℤ⁺ and discrete state space 𝒮 = {0, 1, ..., 𝑚}.

Initial condition: 𝑋₀ = 𝑎

Transition rules:
- When 1 ≤ 𝑋ₙ ≤ 𝑚-1 (game in progress):
  - 𝑋ₙ₊₁ = 𝑋ₙ + 1 with probability 𝑝
  - 𝑋ₙ₊₁ = 𝑋ₙ - 1 with probability 𝑞
- When 𝑋ₙ = 0 (Alice is ruined): 𝑋ₙ₊₁ = 0
- When 𝑋ₙ = 𝑚 (Bob is ruined): 𝑋ₙ₊₁ = 𝑚

---

### Markov Property / 马尔可夫性质

**中文解释：**

赌徒破产过程 (𝑋ₙ) 显然满足马尔可夫性质：下一步 𝑋ₙ₊₁ 只依赖于当前位置 𝑋ₙ，给定当前位置后，不依赖于过去的历史。

赌徒破产过程就像一个从 𝑋₀ = 𝑎 开始的简单随机游走，但在 0 和 𝑚 处有吸收壁（absorbing barriers），随机游走在此停止，因为一方已经破产。

**注意：** 也可以考虑反射壁（reflecting barriers），将随机游走弹回状态空间，或混合壁（mixed barriers），随机地吸收或反射。

**English explanation:**

The gambler's ruin process (𝑋ₙ) clearly satisfies the Markov property: the next step 𝑋ₙ₊₁ depends only on the current position 𝑋ₙ, and given that, does not depend on how we got here.

The gambler's ruin process is exactly like a simple random walk started from 𝑋₀ = 𝑎 except that we have absorbing barriers at 0 and 𝑚, where the random walk stops because one of the players is ruined.

**Note:** One could also consider random walks with reflecting barriers (that bounce the random walk back into the state space) or mixed barriers (that are absorbing or reflecting at random).

---

### Two Key Questions / 两个关键问题

**中文解释：**

关于赌徒破产问题，我们将回答两个问题：

1. **破产概率：** 游戏以 Alice 破产告终的概率是多少？
2. **期望持续时间：** 游戏平均持续多长时间？

**English explanation:**

There are two questions about gambler's ruin that we will answer:

1. **Probability of ruin:** What is the probability that the game ends by Alice ruining?
2. **Expected duration:** How long does the game last on average?

---

## 4.3 Probability of Ruin / 破产概率

### Setting Up the Problem / 问题设定

**中文解释：**

令 𝑟ᵢ 表示当 Alice 当前有 £𝑖 时，她最终破产的概率。那么整个游戏的破产概率就是 𝑟ₐ，因为 Alice 初始有 £𝑎。

Bob 最终破产的概率是 1 - 𝑟ₐ，因为总有一方会输。

**边界条件：**
- 𝑟₀ = 1：当 Alice 有 £0 时，她已经破产了
- 𝑟ₘ = 0：当 Alice 有 £𝑚 时，她赢了所有钱，Bob 破产了

**English explanation:**

Let 𝑟ᵢ denote the probability that Alice ends up ruined if she currently has £𝑖. Then the probability of ruin for the whole game is 𝑟ₐ, since Alice initially starts with £𝑎.

The probability Bob will end up ruined is 1 - 𝑟ₐ, since one of the players must lose.

**Boundary conditions:**
- 𝑟₀ = 1: When Alice has £0, she is already ruined
- 𝑟ₘ = 0: When Alice has £𝑚, she has won all the money, Bob is ruined

---

### Theorem 4.1: Ruin Probability / 破产概率定理

**Theorem 4.1.** Set 𝜌 = 𝑞/𝑝. Then the ruin probability is given by:

$$r_a = \begin{cases} \frac{\rho^a - \rho^m}{1 - \rho^m} & \text{if } \rho \neq 1, \\ 1 - \frac{a}{m} & \text{if } \rho = 1. \end{cases}$$

**中文解释：**

这个公式给出了 Alice 从 £𝑎 开始最终破产的概率。

- 当 𝜌 ≠ 1 时（即 𝑝 ≠ 𝑞），公式为 𝑟ₐ = (𝜌ᵃ - 𝜌ᵐ)/(1 - 𝜌ᵐ)
- 当 𝜌 = 1 时（即 𝑝 = 𝑞 = 1/2，对称情况），公式为 𝑟ₐ = 1 - 𝑎/𝑚

注意：𝜌 = 1 等同于对称条件 𝑝 = 𝑞 = 1/2。

**English explanation:**

This formula gives the probability that Alice, starting with £𝑎, will eventually be ruined.

- When 𝜌 ≠ 1 (i.e., 𝑝 ≠ 𝑞), the formula is 𝑟ₐ = (𝜌ᵃ - 𝜌ᵐ)/(1 - 𝜌ᵐ)
- When 𝜌 = 1 (i.e., 𝑝 = 𝑞 = 1/2, symmetric case), the formula is 𝑟ₐ = 1 - 𝑎/𝑚

Note that 𝜌 = 1 is the same as the symmetric condition 𝑝 = 𝑞 = 1/2.

---

### Derivation via Conditioning / 通过条件推导

**中文解释：**

我们可以通过对第一步进行条件化并使用马尔可夫性质来推导 𝑟ᵢ 满足的关系式：

$$r_i = p \cdot r_{i+1} + q \cdot r_{i-1}$$

**推导过程：**
- 从状态 𝑖 开始，第一步有两种可能：
  - 以概率 𝑝 移动到 𝑖+1，然后从那里开始，破产概率为 𝑟ᵢ₊₁
  - 以概率 𝑞 移动到 𝑖-1，然后从那里开始，破产概率为 𝑟ᵢ₋₁
- 根据全概率公式：𝑟ᵢ = 𝑝·𝑟ᵢ₊₁ + 𝑞·𝑟ᵢ₋₁

**边界条件：** 𝑟₀ = 1, 𝑟ₘ = 0

这个差分方程的解就是定理 4.1 给出的公式。

**English explanation:**

We can derive a relation for 𝑟ᵢ by conditioning on the first step and using the Markov property:

$$r_i = p \cdot r_{i+1} + q \cdot r_{i-1}$$

**Derivation:**
- Starting from state 𝑖, the first step has two possibilities:
  - With probability 𝑝, move to 𝑖+1, then from there, the ruin probability is 𝑟ᵢ₊₁
  - With probability 𝑞, move to 𝑖-1, then from there, the ruin probability is 𝑟ᵢ₋₁
- By the law of total probability: 𝑟ᵢ = 𝑝·𝑟ᵢ₊₁ + 𝑞·𝑟ᵢ₋₁

**Boundary conditions:** 𝑟₀ = 1, 𝑟ₘ = 0

The solution to this difference equation is the formula given in Theorem 4.1.

---

### Martingale Approach / 鞅方法

**中文解释：**

现在我们用鞅来推导破产概率。首先考虑 𝑝 ≠ 𝑞 的情况。

定义：
$$M_n = \left(\frac{q}{p}\right)^{X_n}$$

我们声称 (𝑀ₙ) 是关于 (𝑍ₙ) 的鞅。

**验证条件 1（可积性）：**
𝔼|𝑀ₙ| ≤ max{1, (𝑞/𝑝)ᵐ} < ∞ ✓

**验证条件 2（鞅性质）：**
我们需要证明 𝔼(𝑀ₙ₊₁ | 𝑍₁, ..., 𝑍ₙ) = 𝑀ₙ 对所有 𝑛 成立。

分情况讨论：
- 如果 𝑋ₙ = 0 或 𝑋ₙ = 𝑚，游戏已经结束，所以 𝑀ₙ₊₁ = 𝑀ₙ
- 如果 0 < 𝑋ₙ < 𝑚，游戏还在进行中：

$$\mathbb{E}(M_{n+1} | Z_1, ..., Z_n) = \mathbb{E}\left(\left(\frac{q}{p}\right)^{X_n + Z_{n+1}} | Z_1, ..., Z_n\right)$$
$$= \left(\frac{q}{p}\right)^{X_n} \cdot \mathbb{E}\left(\left(\frac{q}{p}\right)^{Z_{n+1}}\right)$$
$$= \left(\frac{q}{p}\right)^{X_n} \cdot \left(p \cdot \frac{q}{p} + q \cdot \left(\frac{q}{p}\right)^{-1}\right)$$
$$= \left(\frac{q}{p}\right)^{X_n} \cdot (q + p) = \left(\frac{q}{p}\right)^{X_n} = M_n$$

所以 (𝑀ₙ) 确实是鞅。

**English explanation:**

Now we use martingales to derive the ruin probability. First consider the case 𝑝 ≠ 𝑞.

Define:
$$M_n = \left(\frac{q}{p}\right)^{X_n}$$

We claim that (𝑀ₙ) is a martingale with respect to (𝑍ₙ).

**Check condition 1 (integrability):**
𝔼|𝑀ₙ| ≤ max{1, (𝑞/𝑝)ᵐ} < ∞ ✓

**Check condition 2 (martingale property):**
We need to show 𝔼(𝑀ₙ₊₁ | 𝑍₁, ..., 𝑍ₙ) = 𝑀ₙ for all 𝑛.

Case analysis:
- If 𝑋ₙ = 0 or 𝑋ₙ = 𝑚, the game has ended, so 𝑀ₙ₊₁ = 𝑀ₙ
- If 0 < 𝑋ₙ < 𝑚, the game is still in progress:

$$\mathbb{E}(M_{n+1} | Z_1, ..., Z_n) = \mathbb{E}\left(\left(\frac{q}{p}\right)^{X_n + Z_{n+1}} | Z_1, ..., Z_n\right)$$
$$= \left(\frac{q}{p}\