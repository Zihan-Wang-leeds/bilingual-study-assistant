# Section 15: Poisson process in infinitesimal time periods

> MATH2702 - 自学教材 / Self-Study Guide
> 生成时间: 2026-07-20 15:44
> 来源页: 76-78

---

# MATH2702: Stochastic Processes / 随机过程

## Section 15: Poisson Process in Infinitesimal Time Periods / 泊松过程的无穷小时段定义

---

### 📋 Section Overview / 章节概览

**中文解释：** 本章节介绍泊松过程的第三种定义方式——通过无穷小时段内的增量行为来定义。前两种定义分别是：基于增量服从泊松分布的定义，以及基于停留时间服从指数分布的定义。这第三种定义方法通过观察极短时间τ内发生的事件数量来刻画泊松过程。这种方法的一个显著优点是它不需要直接假设具体的分布形式，因此看起来更"自然"或"不可避免"。此外，它还展示了马尔可夫过程与微分方程之间的联系。不过，在实际计算中，使用泊松分布或指数分布的定义通常更为简便。

**English explanation:** This section introduces the third definition of the Poisson process — through its behavior in infinitesimal time periods. The first two definitions were: one based on increments having Poisson distribution, and one based on holding times having exponential distribution. This third definition characterizes the Poisson process by observing the number of events occurring in a very short time period τ. A significant advantage of this approach is that it does not require direct assumptions about the distributions involved, making it seem more "natural" or "inevitable". Additionally, it shows the connection between Markov processes and differential equations. However, for actual calculations, the Poisson or exponential definitions are usually easier to work with.

**Why this matters / 为什么重要：**
- 提供了一种更直观的理解方式，不需要预先知道泊松分布或指数分布
- 建立了随机过程与微分方程之间的桥梁
- 为后续学习更复杂的连续时间马尔可夫链打下基础
- 在证明两个泊松过程之和仍为泊松过程时特别方便

---

### 🎯 Learning Objectives / 学习目标

完成本章学习后，你应该能够：

1. **理解无穷小时段定义**：能够用数学语言描述泊松过程在极短时间τ内的行为
2. **掌握小o记号**：理解并正确使用小o记号（little-o notation）来表示高阶无穷小量
3. **应用无穷小时段定义**：能够用该定义证明两个独立泊松过程之和仍为泊松过程
4. **推导科尔莫戈罗夫前向方程**：从无穷小时段定义出发，推导出泊松过程的微分方程
5. **验证泊松分布解**：证明科尔莫戈罗夫前向方程的解就是泊松分布
6. **理解三种定义的等价性**：认识到泊松过程的三种定义（泊松增量、指数停留时间、无穷小时段）是等价的

---

### 📚 Prerequisites / 前置知识

在学习本章之前，你需要掌握以下内容：

| 前置知识 | 具体要求 |
|---------|---------|
| 泊松过程的前两种定义 | 知道泊松过程可以通过独立增量服从泊松分布来定义，也知道停留时间服从指数分布 |
| 概率论基础 | 理解概率、独立事件、条件概率等基本概念 |
| 微积分基础 | 掌握导数、极限的基本概念 |
| 小o记号 | 了解高阶无穷小的概念（本章会详细讲解） |
| 微分方程 | 能够解简单的一阶线性微分方程 |

---

### 📖 Core Content / 核心内容

---

#### Topic 1: Little-o Notation / 小o记号

**Intuition / 直觉理解**

**中文解释：** 小o记号是一种数学工具，用来表示那些相对于某个参考量来说"微不足道"的量。想象你有一个非常小的数τ（比如0.001），那么τ²（0.000001）就比τ小得多。当我们说某个量是o(τ)时，意思是这个量相对于τ来说可以忽略不计——当τ趋近于0时，这个量比τ更快地趋近于0。例如，τ²、τ³、2τ²等都是o(τ)。在泊松过程的无穷小时段分析中，我们经常忽略这些高阶无穷小量，因为它们对最终结果没有影响。

**English explanation:** The little-o notation is a mathematical tool used to represent quantities that are "negligible" compared to a reference quantity. Imagine you have a very small number τ (say 0.001), then τ² (0.000001) is much smaller than τ. When we say a quantity is o(τ), it means this quantity is negligible compared to τ — as τ approaches 0, this quantity approaches 0 faster than τ does. For example, τ², τ³, 2τ² are all o(τ). In the analysis of Poisson processes over infinitesimal time periods, we often ignore these higher-order infinitesimals because they don't affect the final result.

**Formal Definition / 形式化定义**

**English definition:**
A function f(τ) is said to be o(τ) (little-o of τ) if:
$$
\frac{f(τ)}{τ} \to 0 \quad \text{as} \quad τ \to 0
$$

**中文解释：** 一个函数f(τ)被称为o(τ)（τ的小o），如果当τ趋近于0时，f(τ)/τ也趋近于0。换句话说，f(τ)比τ更快地趋近于0。

**Symbol explanation / 符号说明：**

| 符号 | 中文含义 | English meaning |
|-----|---------|----------------|
| f(τ) | 某个关于τ的函数 | some function of τ |
| o(τ) | 比τ更高阶的无穷小 | higher-order infinitesimal compared to τ |
| τ → 0 | τ趋近于0 | τ approaches 0 |
| f(τ)/τ → 0 | f(τ)除以τ后趋近于0 | f(τ) divided by τ approaches 0 |

**Examples / 例子：**

| 函数 | 是否属于o(τ) | 原因 |
|-----|-------------|------|
| τ² | 是 | τ²/τ = τ → 0 |
| τ³ | 是 | τ³/τ = τ² → 0 |
| 5τ² | 是 | 5τ²/τ = 5τ → 0 |
| 2τ | 否 | 2τ/τ = 2 → 2 ≠ 0 |
| sin(τ²) | 是 | sin(τ²)/τ → 0 |
| τ | 否 | τ/τ = 1 → 1 ≠ 0 |

---

#### Topic 2: Definition 3 - Increments in Infinitesimal Time / 定义3：无穷小时段内的增量

**Intuition / 直觉理解**

**中文解释：** 让我们思考一个计数过程X(t)，它记录到时间t为止发生的事件总数。现在考虑一个非常短的时间段，长度为τ。在这个极短的时间段内，我们直观地认为：

1. 很可能没有任何事件发生（概率接近1）
2. 可能有一个事件发生，且这个概率大致与时间段长度τ成正比
3. 几乎不可能有两个或更多事件发生

这些假设看起来非常自然和合理，不需要我们事先知道泊松分布或指数分布。正是这些"弱"假设定义了泊松过程。

**English explanation:** Let's consider a counting process X(t) that records the total number of events that have occurred up to time t. Now consider a very short time period of length τ. In this extremely short time period, we intuitively believe:

1. It's very likely that no events occur (probability close to 1)
2. It's possible that one event occurs, and this probability is roughly proportional to the time period length τ
3. It's extremely unlikely that two or more events occur in such a short time

These assumptions seem very natural and reasonable, and they don't require us to know about Poisson or exponential distributions beforehand. It is precisely these "weak" assumptions that define the Poisson process.

**Formal Definition / 形式化定义**

**English definition:**
Let (X(t)) be a stochastic process counting arrivals over time. Consider the number of arrivals in a very small time period of length τ, which is X(t+τ) - X(t). The infinitesimal increment probabilities are:

$$
\mathbb{P}(X(t+τ) - X(t) = j) = 
\begin{cases}
1 - λτ + o(τ) & \text{if } j = 0, \\
λτ + o(τ) & \text{if } j = 1, \\
o(τ) & \text{if } j \ge 2.
\end{cases}
$$

as τ → 0.

**中文解释：** 设X(t)是一个计数到达事件的随机过程。考虑一个长度为τ的极短时间段内的到达数量，即X(t+τ) - X(t)。当τ趋近于0时，这个增量的概率分布为：

- 没有事件发生（j=0）的概率：1 - λτ + o(τ)
- 恰好一个事件发生（j=1）的概率：λτ + o(τ)
- 两个或更多事件发生（j≥2）的概率：o(τ)

**Symbol explanation / 符号说明：**

| 符号 | 中文含义 | English meaning |
|-----|---------|----------------|
| X(t) | 到时间t为止的事件总数 | total number of events up to time t |
| τ | 极短的时间段长度 | very short time period length |
| X(t+τ) - X(t) | 时间段(t, t+τ]内的事件数 | number of events in time interval (t, t+τ] |
| λ | 泊松过程的速率（强度） | rate (intensity) of the Poisson process |
| o(τ) | 比τ更高阶的无穷小 | higher-order infinitesimal compared to τ |
| ℙ(·) | 概率 | probability |

**Key insight / 关键洞察：**

**中文解释：** 注意这些概率之和必须为1。验证一下：
- 当j=0时：1 - λτ + o(τ)
- 当j=1时：λτ + o(τ)
- 当j≥2时：o(τ)
总和 = (1 - λτ + o(τ)) + (λτ + o(τ)) + o(τ) = 1 + o(τ) → 1（当τ→0时）

这验证了我们的定义是自洽的。

**English explanation:** Note that these probabilities must sum to 1. Let's verify:
- For j=0: 1 - λτ + o(τ)
- For j=1: λτ + o(τ)
- For j≥2: o(τ)
Sum = (1 - λτ + o(τ)) + (λτ + o(τ)) + o(τ) = 1 + o(τ) → 1 (as τ→0)

This confirms our definition is self-consistent.

---

#### Topic 3: Theorem 15.1 - Equivalence Theorem / 定理15.1：等价性定理

**Formal Statement / 正式陈述**

**English theorem:**
**Theorem 15.1.** Let (X(t)) be a stochastic process with the following properties:
1. X(0) = 0;
2. Infinitesimal increments: X(t+τ) - X(t) has the structure in (11) above, as τ → 0;
3. Independent increments: X(t₂) - X(t₁) and X(t₄) - X(t₃) are independent for all t₁ ≤ t₂ ≤ t₃ ≤ t₄.

Then (X(t)) is a Poisson process with rate λ.

**中文解释：**
**定理15.1.** 设X(t)是一个随机过程，满足以下性质：
1. X(0) = 0（初始时刻没有事件发生）；
2. 无穷小增量性质：X(t+τ) - X(t)在τ→0时具有上述(11)式中的结构；
3. 独立增量性质：对于任意t₁ ≤ t₂ ≤ t₃ ≤ t₄，增量X(t₂) - X(t₁)与X(t₄) - X(t₃)相互独立。

那么X(t)是一个速率为λ的泊松过程。

**Why this matters / 为什么重要：**

**中文解释：** 这个定理告诉我们，只要一个随机过程满足这三个看似简单的条件，它就一定是泊松过程。这意味着我们可以用这些"弱"条件来识别泊松过程，而不需要直接验证增量是否服从泊松分布。这在实际应用中非常有用，因为验证这些条件通常比直接验证泊松分布更容易。

**English explanation:** This theorem tells us that if a stochastic process satisfies these three seemingly simple conditions, it must be a Poisson process. This means we can identify Poisson processes using these "weak" conditions, without directly verifying that increments follow a Poisson distribution. This is very useful in applications because verifying these conditions is usually easier than directly verifying the Poisson distribution.

**Comparison with other definitions / 与其他定义的比较：**

| 性质 | 泊松增量定义 | 指数停留时间定义 | 无穷小时段定义 |
|-----|------------|----------------|--------------|
| X(0)=0 | ✓ | ✓ | ✓ |
| 独立增量 | ✓ | ✓ | ✓ |
| 平稳增量 | ✓ | ✓ | ✓ |
| 增量分布 | 泊松分布 | 隐含 | 无穷小概率结构 |
| 停留时间分布 | 隐含 | 指数分布 | 隐含 |

---

#### Topic 4: Example - Sum of Two Poisson Processes / 例题：两个泊松过程之和

**Intuition / 直觉理解**

**中文解释：** 假设有两个独立的泊松过程：X(t)表示类型A事件的到达（速率为λ），Y(t)表示类型B事件的到达（速率为μ）。如果我们只关心总的事件数Z(t) = X(t) + Y(t)，那么Z(t)也是一个泊松过程，其速率为λ+μ。这个结论直观上很容易理解：两个独立的事件流合并后，总的事件到达速率就是各自速率的和。

**English explanation:** Suppose we have two independent Poisson processes: X(t) counts arrivals of type A events (rate λ), and Y(t) counts arrivals of type B events (rate μ). If we only care about the total number of events Z(t) = X(t) + Y(t), then Z(t) is also a Poisson process with rate λ+μ. This conclusion is intuitively easy to understand: when two independent event streams are merged, the total arrival rate is the sum of the individual rates.

**Worked Example / 例题详解**

**Problem / 问题：** 证明两个独立泊松过程之和仍为泊松过程。

**Solution / 解答：**

**Step 1: Check the infinitesimal probabilities for Z(t) / 步骤1：检查Z(t)的无穷小概率**

**中文解释：** 我们需要验证Z(t)满足无穷小时段定义中的三个概率条件。首先计算在极短时间τ内没有事件发生的概率。

**English explanation:** We need to verify that Z(t) satisfies the three probability conditions in the infinitesimal definition. First, calculate the probability of no events occurring in a very short time τ.

$$
\mathbb{P}(Z(t+τ) - Z(t) = 0) = \mathbb{P}(X(t+τ) - X(t) = 0) \cdot \mathbb{P}(Y(t+τ) - Y(t) = 0)
$$

**中文解释：** 因为Z(t)只有在X(t)和Y(t)都没有增加时才会保持不变。由于X和Y独立，这个概率等于各自概率的乘积。

**English explanation:** Because Z(t) stays the same only when neither X(t) nor Y(t) increases. Since X and Y are independent, this probability equals the product of their individual probabilities.

**Step 2: Substitute the infinitesimal probabilities / 步骤2：代入无穷小概率**

$$
\begin{aligned}
\mathbb{P}(Z(t+τ) - Z(t) = 0) &= (1 - λτ + o(τ))(1 - μτ + o(τ)) \\
&= 1 - λτ - μτ + λμτ^2 + o(τ) \\
&= 1 - (λ + μ)τ + o(τ)
\end{aligned}
$$

**中文解释：** 展开乘积后，λμτ²项是o(τ)（因为τ²比τ更快地趋近于0），所以它被吸收到o(τ)中。最终得到1 - (λ+μ)τ + o(τ)，这正是速率为λ+μ的泊松过程在j=0时的概率形式。

**English explanation:** After expanding the product, the λμτ² term is o(τ) (since τ² approaches 0 faster than τ), so it gets absorbed into o(τ). We finally get 1 - (λ+μ)τ + o(τ), which is exactly the probability form for j=0 of a Poisson process with rate λ+μ.

**Step 3: Calculate the probability of exactly one event / 步骤3：计算恰好一个事件的概率**

$$
\begin{aligned}
\mathbb{P}(Z(t+τ) - Z(t) = 1) &= \mathbb{P}(X(t+τ) - X(t) = 1) \cdot \mathbb{P}(Y(t+τ) - Y(t) = 0) \\
&\quad + \mathbb{P}(X(t+τ) - X(t) = 0) \cdot \mathbb{P}(Y(t+τ) - Y(t) = 1)
\end{aligned}
$$

**中文解释：** Z(t)增加1有两种方式：要么X增加1而Y不变，要么X不变而Y增加1。这两种情况互斥，所以概率相加。

**English explanation:** Z(t) increases by 1 in two ways: either X increases by 1 while Y stays the same, or X stays the same while Y increases by 1. These two cases are mutually exclusive, so their probabilities add.

**Step 4: Substitute and simplify / 步骤4：代入并化简**

$$
\begin{aligned}
\mathbb{P}(Z(t+τ) - Z(t) = 1) &= (λτ + o(τ))(1 - μτ + o(τ)) + (1 - λτ + o(τ))(μτ + o(τ)) \\
&= λτ - λμτ^2 + o(τ) + μτ - λμτ^2 + o(τ) \\
&= (λ + μ)τ + o(τ)
\end{aligned}
$$

**中文解释：** 展开后，所有λμτ²项都是o(τ)，最终得到(λ+μ)τ + o(τ)，这正是速率为λ+μ的泊松过程在j=1时的概率形式。

**English explanation:** After expansion, all λμτ² terms are o(τ), and we finally get (λ+μ)τ + o(τ), which is exactly the probability form for j=1 of a Poisson process with rate λ+μ.

**Step 5: Check the probability of two or more events / 步骤5：检查两个或更多事件的概率**

**中文解释：** 由于所有概率之和必须为1，且我们已经得到j=0和j=1的概率，那么j≥2的概率自然就是o(τ)。我们也可以直接推理：要发生两个或更多事件，要么X发生至少两个事件，要么Y发生至少两个事件，要么X和Y各发生一个事件——这些概率都是o(τ)。

**English explanation:** Since all probabilities must sum to 1, and we already have the probabilities for j=0 and j=1, the probability for j≥2 is naturally o(τ). We can also reason directly: for two or more events to occur, either X has at least two events, or Y has at least two events, or X and Y each have one event — all these probabilities are o(τ).

**Conclusion / 结论：**

**中文解释：** Z(t)满足无穷小时段定义中的所有三个条件，且速率为λ+μ。因此，Z(t)是一个速率为λ+μ的泊松过程。这个证明比使用泊松增量定义更加简洁。

**English explanation:** Z(t) satisfies all three conditions in the infinitesimal definition with rate λ+μ. Therefore, Z(t) is a Poisson process with rate λ+μ. This proof is more concise than using the Poisson increment definition.

---

#### Topic 5: Forward Equations and Proof of Equivalence / 前向方程与等价性证明

**Intuition / 直觉理解**

**中文解释：** 现在我们要证明定理15.1，即满足无穷小时段定义的过程确实是泊松过程。证明的思路是：从无穷小时段的概率出发，推导出关于pⱼ(t) = ℙ(X(t) = j)的微分方程（称为科尔莫戈罗夫前向方程），然后验证泊松分布是这些方程的解。由于微分方程的解是唯一的，这就证明了X(t)服从泊松分布。

**English explanation:** Now we need to prove Theorem 15.1, that a process satisfying the infinitesimal definition is indeed a Poisson process. The proof strategy is: starting from the infinitesimal probabilities, derive differential equations (called Kolmogorov forward equations) for pⱼ(t) = ℙ(X(t) = j), then verify that the Poisson distribution is the solution to these equations. Since the solution to differential equations is unique, this proves that X(t) follows a Poisson distribution.

**Key simplification / 关键简化：**

**中文解释：** 由于无穷小时段定义中的概率是时间齐次的（不依赖于起始时间t），我们只需要考虑从0开始的情况，即s=0。这样我们只需要证明X(t) ∼ Po(λt)。

**English explanation:** Since the probabilities in the infinitesimal definition are time-homogeneous (do not depend on the starting time t), we only need to consider the case starting from 0, i.e., s=0. So we just need to prove that X(t) ∼ Po(λt).

**Derivation of Forward Equations / 前向方程的推导**

**Step 1: Write the equation for pⱼ(t+τ) / 步骤1：写出pⱼ(t+τ)的方程**

For j ≥ 1:

$$
p_j(t+τ) = (1 - λτ + o(τ))p_j(t) + (λτ + o(τ))p_{j-1}(t) + o(τ)
$$

**中文解释：** 在时间t+τ时处于状态j，有两种可能的方式：
1. 在时间t时已经在状态j，然后在时间段(t, t+τ]内没有新事件发生。概率为(1-λτ+o(τ))pⱼ(t)
2. 在时间t时处于状态j-1，然后在时间段(t, t+τ]内恰好发生一个事件。概率为(λτ+o(τ))pⱼ₋₁(t)
3. 其他所有可能性（如从j-2跳上来，或从j跳上去又跳回来等）的概率都是o(τ)

**English explanation:** Being in state j at time t+τ can happen in two ways:
1. Already in state j at time t, and no new events occur in (t, t+τ]. Probability: (1-λτ+o(τ))pⱼ(t)
2. In state j-1 at time t, and exactly one event occurs in (t, t+τ]. Probability: (λτ+o(τ))pⱼ₋₁(t)
3. All other possibilities (like jumping from j-2, or jumping up and back from j, etc.) have probability o(τ)

**Step 2: Rearrange to get the increment / 步骤2：整理得到增量形式**

$$
p_j(t+τ) - p_j(t) = -λτ p_j(t) + λτ p_{j-1}(t) + o(τ)
$$

**中文解释：** 将pⱼ(t)移到左边，合并同类项。注意"常数乘以o(τ)"仍然是o(τ)。

**English explanation:** Move pⱼ(t) to the left side and combine like terms. Note that "constant times o(τ)" is still o(τ).

**Step 3: Divide by τ and take the limit / 步骤3：除以τ并取极限**

$$
\frac{p_j(t+τ) - p_j(t)}{τ} = -λ p_j(t) + λ p_{j-1}(t) + \frac{o(τ)}{τ}
$$

As τ → 0:
- The left side becomes the derivative: p'ⱼ(t)
- The term o(τ)/τ → 0

**中文解释：** 左边是差商，当τ→0时趋近于导数p'ⱼ(t)。右边o(τ)/τ项根据小o记号的定义趋近于0。这样就得到了微分方程。

**English explanation:** The left side is the difference quotient, which approaches the derivative p'ⱼ(t) as τ→0. The o(τ)/τ term approaches 0 by the definition of little-o notation. This gives us the differential equation.

**Step 4: The differential equation for j ≥ 1 / 步骤4：j ≥ 1的微分方程**

$$
p'_j(t) = -λ p_j(t) + λ p_{j-1}(t)
$$

with initial condition pⱼ(0) = 0 for j ≥ 1 (since we start at 0).

**Step 5: The special case j = 0 / 步骤5：j = 0的特殊情况**

For j = 0:

$$
p_0(t+τ) = (1 - λτ + o(τ))p_0(t)
$$

**中文解释：** 要保持在状态0，必须在时间t时已经在状态0，并且在时间段(t, t+τ]内没有事件发生。没有其他方式可以到达状态0（因为事件只能增加计数，不能减少）。

**English explanation:** To stay in state 0, we must already be in state 0 at time t, and have no events in (t, t+τ]. There is no other way to reach state 0 (since events can only increase the count, not decrease it).

Rearranging and taking the limit:

$$
p'_0(t) = -λ p_0(t)
$$

with initial condition p₀(0) = 1 (since we always start at 0).

**Summary of Forward Equations / 前向方程总结**

$$
\begin{cases}
p'_0(t) = -λ p_0(t), & p_0(0) = 1 \\
p'_j(t) = -λ p_j(t) + λ p_{j-1}(t), & p_j(0) = 0 \quad \text{for } j \ge 1
\end{cases}
$$

**中文解释：** 这就是科尔莫戈罗夫前向方程（Kolmogorov forward equations）。它们描述了泊松过程的状态概率随时间演化的规律。

**English explanation:** These are the Kolmogorov forward equations. They describe how the state probabilities of the Poisson process evolve over time.

**Verification of the Poisson Solution / 验证泊松分布解**

**中文解释：** 现在我们要验证泊松分布pⱼ(t) = e^{-λt}(λt)ʲ/j! 确实满足这些方程。

**English explanation:** Now we verify that the Poisson distribution pⱼ(t) = e^{-λt}(λt)ʲ/j! indeed satisfies these equations.

**Case j = 0 / 情况 j = 0:**

$$
p_0(t) = e^{-λt}
$$

**中文解释：** 这是泊松分布在j=