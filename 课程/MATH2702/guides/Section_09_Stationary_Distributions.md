# Section 9: Stationary distributions

> MATH2702 - 自学教材 / Self-Study Guide
> 生成时间: 2026-07-20 15:40
> 来源页: 51-56

---

# 📚 Section 9: Stationary Distributions / 平稳分布

## 📋 Section Overview / 章节概览

**中文解释：** 本章节是马尔可夫链理论中最重要的部分之一。我们将学习什么是"平稳分布"——这是一种特殊的概率分布，当我们从该分布出发时，马尔可夫链在所有时间步上都保持相同的分布。这就像是一个"平衡状态"，系统一旦达到这个状态，就会一直保持下去。我们将学习如何求解平稳分布，以及判断平稳分布存在性和唯一性的条件。

**English explanation:** This section is one of the most important parts of Markov chain theory. We will learn what a "stationary distribution" is — a special probability distribution such that if we start the Markov chain from this distribution, it remains the same distribution at all time steps. This is like an "equilibrium state" — once the system reaches this state, it stays there forever. We will learn how to find stationary distributions and the conditions for their existence and uniqueness.

**Why this matters / 为什么重要：**
- Stationary distributions describe the long-term behavior of Markov chains / 平稳分布描述了马尔可夫链的长期行为
- They are used in Google's PageRank algorithm, queueing theory, and many other applications / 它们被用于谷歌的PageRank算法、排队论等众多应用中
- Understanding stationary distributions is essential for analyzing real-world stochastic systems / 理解平稳分布对于分析现实世界中的随机系统至关重要

## 🎯 Learning Objectives / 学习目标

By the end of this section, you will be able to / 学完本节后，你将能够：

1. **Define** a stationary distribution and explain its meaning / **定义**平稳分布并解释其含义
2. **Solve** for stationary distributions using the equation π = πP / **求解**平稳分布，使用方程 π = πP
3. **Apply** the three-step method to find stationary distributions / **应用**三步法求解平稳分布
4. **State** the conditions for existence and uniqueness of stationary distributions / **陈述**平稳分布存在性和唯一性的条件
5. **Determine** the number of stationary distributions for reducible chains / **确定**可约链的平稳分布数量
6. **Compute** expected return times from stationary distributions / **计算**从平稳分布得到的期望返回时间

## 📚 Prerequisites / 前置知识

Before studying this section, you should know / 在学习本节之前，你应该掌握：

- **Markov chains basics / 马尔可夫链基础**: States, transition probabilities, transition matrix P / 状态、转移概率、转移矩阵P
- **Matrix multiplication / 矩阵乘法**: How to multiply a row vector by a matrix / 如何将行向量与矩阵相乘
- **Probability distributions / 概率分布**: What a probability distribution is, ∑πᵢ = 1 / 什么是概率分布，∑πᵢ = 1
- **Irreducibility / 不可约性**: What it means for a Markov chain to be irreducible / 马尔可夫链不可约的含义
- **Recurrence and transience / 常返性和瞬时性**: Positive recurrence, null recurrence, transience / 正常返、零常返、瞬时性
- **Expected return times / 期望返回时间**: μᵢ = expected time to return to state i / 返回状态i的期望时间

## 📖 Core Content / 核心内容

### Topic 1: Definition of Stationary Distribution / 平稳分布的定义

#### Intuition / 直觉理解

**中文解释：** 让我们从一个具体的例子开始。回顾"坏打印机"马尔可夫链，它有两个状态：0（打印机正常工作）和1（打印机坏了）。转移概率如图11所示。假设我们从一个特殊的初始分布开始：
- ℙ(X₀ = 0) = β/(α+β)
- ℙ(X₀ = 1) = α/(α+β)

经过一步后，我们计算ℙ(X₁ = 0)和ℙ(X₁ = 1)。令人惊讶的是，我们得到完全相同的结果！这意味着这个分布是"平稳的"——如果我们从这个分布开始，它在所有时间步上都保持不变。

**English explanation:** Let's start with a concrete example. Consider the "broken printer" Markov chain with two states: 0 (printer working) and 1 (printer broken). The transition probabilities are shown in Figure 11. Suppose we start from a special initial distribution:
- ℙ(X₀ = 0) = β/(α+β)
- ℙ(X₀ = 1) = α/(α+β)

After one step, we compute ℙ(X₁ = 0) and ℙ(X₁ = 1). Surprisingly, we get exactly the same result! This means this distribution is "stationary" — if we start from this distribution, it stays the same at all time steps.

**Analogy / 类比：** 想象一个水池，水不断流入和流出。如果流入速率等于流出速率，水位保持不变。类似地，在马尔可夫链中，如果"概率流"在状态之间达到平衡，分布就保持不变。

Imagine a water tank with water flowing in and out. If the inflow rate equals the outflow rate, the water level stays constant. Similarly, in a Markov chain, if the "probability flow" between states reaches equilibrium, the distribution stays constant.

#### Formal Definition / 形式化定义

**Definition 9.1 (Stationary Distribution / 平稳分布).** Let (Xₙ) be a Markov chain on a state space 𝒮 with transition matrix P. Let π = (πᵢ) be a distribution on 𝒮, meaning πᵢ ≥ 0 for all i ∈ 𝒮 and ∑ᵢ∈𝒮 πᵢ = 1. We call π a **stationary distribution** if

$$ \pi_j = \sum_{i \in \mathcal{S}} \pi_i p_{ij} \quad \text{for all } j \in \mathcal{S} $$

or, equivalently, if π = πP (where π is a row vector).

**Symbol explanation / 符号说明：**

| Symbol | Meaning (English) | 含义（中文） |
|--------|-------------------|--------------|
| π | Stationary distribution vector | 平稳分布向量 |
| πᵢ | Probability of being in state i under stationary distribution | 平稳分布下处于状态i的概率 |
| pᵢⱼ | Transition probability from state i to state j | 从状态i到状态j的转移概率 |
| 𝒮 | State space | 状态空间 |
| πP | Row vector times transition matrix | 行向量乘以转移矩阵 |

**Key insight / 关键洞察：** The equation π = πP means that if we apply one step of the Markov chain starting from distribution π, we get back the same distribution π. This is a **fixed point** of the transition operator.

方程 π = πP 意味着如果我们从分布π出发，应用马尔可夫链的一步转移，我们得到相同的分布π。这是转移算子的一个**不动点**。

**Important note / 重要说明：** The Markov chain (Xₙ) itself keeps moving — individual trajectories change. But the **distribution** of where the chain is at any time remains the same. Think of it this way: if we started a thousand Markov chains, choosing each starting position to be i with probability πᵢ, then (roughly) 1000πⱼ of them would be in state j at any time in the future — but not necessarily the same ones each time.

马尔可夫链(Xₙ)本身一直在移动——单个轨迹在变化。但链在任何时刻所处位置的**分布**保持不变。可以这样理解：如果我们启动一千条马尔可夫链，每条链的起始位置以概率πᵢ选择为i，那么在未来任何时刻，大约有1000πⱼ条链处于状态j——但不一定是同一些链。

#### Verification of the Two-State Example / 验证两状态例子

Let's verify that the distribution π₀ = β/(α+β), π₁ = α/(α+β) is indeed stationary for the broken printer chain.

**Step 1: Compute ℙ(X₁ = 0) / 计算ℙ(X₁ = 0)**

$$ \mathbb{P}(X_1 = 0) = \lambda_0 p_{00} + \lambda_1 p_{10} = \frac{\beta}{\alpha+\beta}(1-\alpha) + \frac{\alpha}{\alpha+\beta}\beta = \frac{\beta}{\alpha+\beta} $$

**Step 2: Compute ℙ(X₁ = 1) / 计算ℙ(X₁ = 1)**

$$ \mathbb{P}(X_1 = 1) = \lambda_0 p_{01} + \lambda_1 p_{11} = \frac{\beta}{\alpha+\beta}\alpha + \frac{\alpha}{\alpha+\beta}(1-\beta) = \frac{\alpha}{\alpha+\beta} $$

The distribution after step 1 is exactly the same as the initial distribution. By repeating the same calculation, it stays the same forever.

---

### Topic 2: Finding a Stationary Distribution / 求解平稳分布

#### The Three-Step Method / 三步法

**中文解释：** 求解平稳分布的核心是解方程 π = πP，同时满足归一化条件 ∑πᵢ = 1。我们使用一个系统化的三步法。

**English explanation:** The core of finding a stationary distribution is solving the equation π = πP while satisfying the normalization condition ∑πᵢ = 1. We use a systematic three-step method.

**Method Summary / 方法总结：**

1. **Write out equations / 写出方程**: Write π = πP coordinate by coordinate. Discard one equation (since π = πP always gives one more equation than needed).
2. **Solve in terms of working variable / 用工作变量求解**: Select one πᵢ as a working variable (parameter). Solve the remaining equations in terms of this variable.
3. **Normalize / 归一化**: Substitute the solution into the normalization condition ∑πᵢ = 1 to find the working variable, and hence the full solution.

**Optional check / 可选检查**: Use the discarded equation to verify the solution.

#### Worked Example 1: No-Claims Discount Chain / 例题1：无索赔折扣链

Consider the no-claims discount Markov chain with state space 𝒮 = {1, 2, 3} and transition matrix:

$$ P = $$
\begin{pmatrix} \frac{1}{4} & \frac{3}{4} & 0 \\ \frac{1}{4} & 0 & \frac{3}{4} \\ 0 & \frac{1}{4} & \frac{3}{4} \end{pmatrix}
$$ $$

**Step 1: Write out equations / 写出方程**

$$ \pi = \pi P \implies (\pi_1, \pi_2, \pi_3) = (\pi_1, \pi_2, \pi_3) $$
\begin{pmatrix} \frac{1}{4} & \frac{3}{4} & 0 \\ \frac{1}{4} & 0 & \frac{3}{4} \\ 0 & \frac{1}{4} & \frac{3}{4} \end{pmatrix}
$$ $$

Coordinate-wise / 按坐标写出：

$$ \pi_1 = \frac{1}{4}\pi_1 + \frac{1}{4}\pi_2 $$
$$ \pi_2 = \frac{3}{4}\pi_1 + \frac{1}{4}\pi_3 $$
$$ \pi_3 = \frac{3}{4}\pi_2 + \frac{3}{4}\pi_3 $$

We also have the normalization condition / 还有归一化条件：
$$ \pi_1 + \pi_2 + \pi_3 = 1 $$

**Step 2: Solve in terms of working variable / 用工作变量求解**

Choose π₂ as the working variable. Discard the second equation (we have one too many).

From the first equation / 从第一个方程：
$$ \pi_1 = \frac{1}{4}\pi_1 + \frac{1}{4}\pi_2 \implies \frac{3}{4}\pi_1 = \frac{1}{4}\pi_2 \implies \pi_1 = \frac{1}{3}\pi_2 $$

From the third equation / 从第三个方程：
$$ \pi_3 = \frac{3}{4}\pi_2 + \frac{3}{4}\pi_3 \implies \frac{1}{4}\pi_3 = \frac{3}{4}\pi_2 \implies \pi_3 = 3\pi_2 $$

So we have / 所以我们得到：
$$ \pi_1 = \frac{1}{3}\pi_2, \quad \pi_3 = 3\pi_2 $$

**Step 3: Normalize / 归一化**

$$ \pi_1 + \pi_2 + \pi_3 = \frac{1}{3}\pi_2 + \pi_2 + 3\pi_2 = \frac{13}{3}\pi_2 = 1 $$

Therefore / 因此：
$$ \pi_2 = \frac{3}{13} $$

Substituting back / 代回：
$$ \pi_1 = \frac{1}{3} \cdot \frac{3}{13} = \frac{1}{13}, \quad \pi_3 = 3 \cdot \frac{3}{13} = \frac{9}{13} $$

**Solution / 解：**
$$ \pi = \left(\frac{1}{13}, \frac{3}{13}, \frac{9}{13}\right) $$

**Check / 验证：** Using the discarded second equation / 使用被丢弃的第二个方程：
$$ \pi_2 = \frac{3}{4}\pi_1 + \frac{1}{4}\pi_3 = \frac{3}{4} \cdot \frac{1}{13} + \frac{1}{4} \cdot \frac{9}{13} = \frac{3}{52} + \frac{9}{52} = \frac{12}{52} = \frac{3}{13} $$
✓ Correct / 正确！

#### Worked Example 2 (Example 9.1) / 例题2（例9.1）

Consider a Markov chain on state space 𝒮 = {1, 2, 3} with transition matrix:

$$ P = $$
\begin{pmatrix} \frac{1}{2} & \frac{1}{4} & \frac{1}{4} \\ \frac{1}{4} & \frac{1}{2} & \frac{1}{4} \\ 0 & \frac{1}{4} & \frac{3}{4} \end{pmatrix}
$$ $$

**Step 1: Write out equations / 写出方程**

$$ \pi_1 = \frac{1}{2}\pi_1 + \frac{1}{4}\pi_2 $$
$$ \pi_2 = \frac{1}{4}\pi_1 + \frac{1}{2}\pi_2 + \frac{1}{4}\pi_3 $$
$$ \pi_3 = \frac{1}{4}\pi_1 + \frac{1}{4}\pi_2 + \frac{3}{4}\pi_3 $$

We choose to discard the third equation / 我们选择丢弃第三个方程。

**Step 2: Solve in terms of working variable / 用工作变量求解**

Choose π₁ as the working variable / 选择π₁作为工作变量。

From the first equation / 从第一个方程：
$$ \pi_1 = \frac{1}{2}\pi_1 + \frac{1}{4}\pi_2 \implies \frac{1}{2}\pi_1 = \frac{1}{4}\pi_2 \implies \pi_2 = 2\pi_1 $$

From the second equation / 从第二个方程：
$$ \pi_2 = \frac{1}{4}\pi_1 + \frac{1}{2}\pi_2 + \frac{1}{4}\pi_3 $$
$$ \implies \pi_2 - \frac{1}{2}\pi_2 = \frac{1}{4}\pi_1 + \frac{1}{4}\pi_3 $$
$$ \implies \frac{1}{2}\pi_2 = \frac{1}{4}\pi_1 + \frac{1}{4}\pi_3 $$
$$ \implies 2\pi_2 = \pi_1 + \pi_3 $$
$$ \implies \pi_3 = 2\pi_2 - \pi_1 $$

Substituting π₂ = 2π₁ / 代入π₂ = 2π₁：
$$ \pi_3 = 2(2\pi_1) - \pi_1 = 4\pi_1 - \pi_1 = 3\pi_1 $$

So we have / 所以我们得到：
$$ \pi_2 = 2\pi_1, \quad \pi_3 = 3\pi_1 $$

**Step 3: Normalize / 归一化**

$$ \pi_1 + \pi_2 + \pi_3 = \pi_1 + 2\pi_1 + 3\pi_1 = 6\pi_1 = 1 $$

Therefore / 因此：
$$ \pi_1 = \frac{1}{6} $$

Substituting back / 代回：
$$ \pi_2 = 2 \cdot \frac{1}{6} = \frac{1}{3}, \quad \pi_3 = 3 \cdot \frac{1}{6} = \frac{1}{2} $$

**Solution / 解：**
$$ \pi = \left(\frac{1}{6}, \frac{1}{3}, \frac{1}{2}\right) $$

**Check / 验证：** Using the discarded third equation / 使用被丢弃的第三个方程：
$$ \pi_3 = \frac{1}{4}\pi_1 + \frac{1}{4}\pi_2 + \frac{3}{4}\pi_3 = \frac{1}{4} \cdot \frac{1}{6} + \frac{1}{4} \cdot \frac{1}{3} + \frac{3}{4} \cdot \frac{1}{2} = \frac{1}{24} + \frac{2}{24} + \frac{9}{24} = \frac{12}{24} = \frac{1}{2} $$
✓ Correct / 正确！

---

### Topic 3: Existence and Uniqueness / 存在性和唯一性

#### Theorem 9.1: The Fundamental Theorem / 基本定理

**中文解释：** 这个定理是本章的核心。它告诉我们什么时候平稳分布存在，以及是否唯一。关键在于链的不可约性和正常返性。

**English explanation:** This theorem is the core of this chapter. It tells us when a stationary distribution exists and whether it is unique. The key lies in the chain's irreducibility and positive recurrence.

**Theorem 9.1.** Consider an irreducible Markov chain.

- **If the Markov chain is positive recurrent**, then a stationary distribution π exists, is unique, and is given by πᵢ = 1/μᵢ, where μᵢ is the expected return time to state i.
  
  **如果马尔可夫链是正常返的**，那么平稳分布π存在、唯一，且由πᵢ = 1/μᵢ给出，其中μᵢ是返回状态i的期望时间。

- **If the Markov chain is null recurrent or transient**, then no stationary distribution exists.
  
  **如果马尔可夫链是零常返或瞬时性的**，那么不存在平稳分布。

**Symbol explanation / 符号说明：**

| Symbol | Meaning (English) | 含义（中文） |
|--------|-------------------|--------------|
| πᵢ | Stationary probability of state i | 状态i的平稳概率 |
| μᵢ | Expected return time to state i | 返回状态i的期望时间 |
| 1/μᵢ | Reciprocal of expected return time | 期望返回时间的倒数 |

**Key implications / 关键含义：**

1. **For finite irreducible chains / 对于有限不可约链**: All finite irreducible Markov chains are positive recurrent, so they always have a unique stationary distribution. / 所有有限不可约马尔可夫链都是正常返的，所以它们总是有唯一的平稳分布。

2. **For infinite irreducible chains / 对于无限不可约链**: The stationary distribution may or may not exist, depending on whether the chain is positive recurrent. / 平稳分布可能存在也可能不存在，取决于链是否正常返。

3. **Relationship with expected return times / 与期望返回时间的关系**: Once we have π, we get μᵢ = 1/πᵢ for free. / 一旦我们得到π，就可以直接得到μᵢ = 1/πᵢ。

#### Example: No-Claims Discount Chain / 例子：无索赔折扣链

**中文解释：** 在我们的无索赔折扣链例子中，链是有限的且不可约的，因此它是正常返的。根据定理，存在唯一的平稳分布，我们已求出为π = (1/13, 3/13, 9/13)。由此我们可以直接得到期望返回时间：
- μ₁ = 1/π₁ = 13
- μ₂ = 1/π₂ = 13/3 ≈ 4.33
- μ₃ = 1/π₃ = 13/9 ≈ 1.44

**English explanation:** In our no-claims discount chain example, the chain is finite and irreducible, so it is positive recurrent. By the theorem, a unique stationary distribution exists, which we found to be π = (1/13, 3/13, 9/13). From this we can directly obtain the expected return times:
- μ₁ = 1/π₁ = 13
- μ₂ = 1/π₂ = 13/3 ≈ 4.33
- μ₃ = 1/π₃ = 13/9 ≈ 1.44

#### Example 9.2: Simple Random Walk / 例9.2：简单随机游走

**中文解释：** 考虑简单随机游走，其中p ≠ 0, 1。这个链是不可约的。当p = 1/2时，它是零常返的；当p ≠ 1/2时，它是瞬时性的。无论哪种情况，定理告诉我们：不存在平稳分布。

**English explanation:** Consider the simple random walk with p ≠ 0, 1. This chain is irreducible. When p = 1/2, it is null recurrent; when p ≠ 1/2, it is transient. In either case, the theorem tells us: no stationary distribution exists.

#### Example 9.3: Reducible Chain with Multiple Closed Classes / 例9.3：具有多个闭类的可约链

Consider the Markov chain with transition matrix:

$$ P = $$
\begin{pmatrix} \frac{1}{2} & \frac{1}{2} & 0 & 0 \\ \frac{1}{2} & \frac{1}{2} & 0 & 0 \\ 0 & 0 & \frac{1}{4} & \frac{3}{4} \\ 0 & 0 & \frac{1}{2} & \frac{1}{2} \end{pmatrix}
$$ $$

**中文解释：** 这个链有两个闭的正常返类：{1, 2}和{3, 4}。由于链不是不可约的，定理9.1不直接适用。我们需要分析这种情况。

**English explanation:** This chain has two closed positive recurrent classes: {1, 2} and {3, 4}. Since the chain is not irreducible, Theorem 9.1 does not directly apply. We need to analyze this situation.

**Solving π = πP / 求解π = πP：**

$$ \pi_1 = \frac{1}{2}\pi_1 + \frac{1}{2}\pi_2 \implies \pi_1 = \pi_2 $$
$$ \pi_2 = \frac{1}{2}\pi_1 + \frac{1}{2}\pi_2 \implies \pi_1 = \pi_2 $$
$$ \pi_3 = \frac{1}{4}\pi_3 + \frac{1}{2}\pi_4 \implies 3\pi_3 = 2\pi_4 $$
$$ \pi_4 = \frac{3}{4}\pi_3 + \frac{1}{2}\pi_4 \implies 3\pi_3 = 2\pi_4 $$

We also have the normalization condition / 还有归一化条件：
$$ \pi_1 + \pi_2 + \pi_3 + \pi_4 = 1 $$

**中文解释：** 注意我们得到了相同的约束条件两次。设π₁ + π₂ = α和π₃ + π₄ = 1 - α，其中α ∈ [0, 1]是一个自由参数。那么：

**English explanation:** Notice we get the same constraints twice. Let π₁ + π₂ = α and π₃ + π₄ = 1 - α, where α ∈ [0, 1] is a free parameter. Then:

$$ \pi = \left(\frac{1}{2}\alpha, \frac{1}{2}\alpha, \frac{2}{5}(1-\alpha), \frac{3}{5}(1-\alpha)\right) $$

is a stationary distribution for any 0 ≤ α ≤ 1. So we have **infinitely many** stationary distributions!

**中文解释：** 这意味着当链有多个正常返类时，我们可以将概率质量以任意比例分配到不同的类上，每个类内部再按照该类自身的平稳分布分配。这产生了无穷多个平稳分布。

**English explanation:** This means that when the chain has multiple positive recurrent classes, we can distribute the probability mass in any proportion among the different classes, and within each class distribute according to that class's own stationary distribution. This yields infinitely many stationary distributions.

#### Summary: Reducible Chains / 可约链总结

**中文解释：** 对于非不可约（可约）的马尔可夫链，平稳分布的存在性和数量取决于正常返类的数量：

**English explanation:** For non-irreducible (reducible) Markov chains, the existence and number of stationary distributions depend on the number of positive recurrent classes:

| Scenario / 情况 | Result / 结果 |
|-----------------|---------------|
| No positive recurrent classes / 没有正常返类 | No stationary distribution / 无平稳分布 |
| Exactly one positive recurrent class / 恰好一个正常返类 | Unique stationary distribution, supported only on that closed class / 唯一平稳分布，仅支撑在该闭类上 |
| Multiple positive recurrent classes / 多个正常返类 | Infinitely many stationary distributions / 无穷多个平稳分布 |

---

### Topic 4: Proof of Existence and Uniqueness (Optional) / 存在性和唯一性的证明（可选）

**中文解释：** 这一小节是可选且不考试的。但为了完整性，我们提供证明。证明分为两部分：存在性和唯一性。

**English explanation:** This subsection is optional and not examinable. But for completeness, we provide the proof. The proof has two parts: existence and uniqueness.

#### Existence: Every Positive Recurrent Markov Chain Has a Stationary Distribution / 存在性：每个正常返马尔可夫链都有平稳