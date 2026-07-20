# Section 11: Long-term behaviour of Markov chains

> MATH2702 - 自学教材 / Self-Study Guide
> 生成时间: 2026-07-20 15:42
> 来源页: 62-66

---

# MATH2702: Markov Chains / 马尔可夫链

## Section 11: Long-term Behaviour of Markov Chains / 马尔可夫链的长期行为

---

### 📋 Section Overview / 章节概览

**中文解释：** 本章节是马尔可夫链理论的核心内容，研究马尔可夫链在长期运行后的行为。我们将探讨两个关键问题：(1) 马尔可夫链的概率分布是否会收敛到一个稳定的"平衡分布"？(2) 在长期运行中，链在每个状态上花费的时间比例是多少？这两个问题分别由极限定理（Limit Theorem）和遍历定理（Ergodic Theorem）回答。这些结果将之前学过的所有概念——不可约性、周期性、常返性、正常返性、返回时间、平稳分布——整合在一起，形成对马尔可夫链长期行为的完整理解。

**English explanation:** This section is the core of Markov chain theory, studying the behavior of a Markov chain after it has been running for a long time. We explore two key questions: (1) Does the probability distribution of the Markov chain converge to a stable "equilibrium distribution"? (2) In the long run, what proportion of time does the chain spend in each state? These questions are answered by the Limit Theorem and the Ergodic Theorem, respectively. These results bring together all the concepts we've learned—irreducibility, periodicity, recurrence, positive recurrence, return times, stationary distributions—into a complete understanding of the long-term behavior of Markov chains.

**Why this matters / 为什么重要：**
- **中文：** 这些定理是马尔可夫链在实际应用中的基础。例如，在排队论中，我们想知道长期等待时间的分布；在保险精算中，我们需要计算长期折扣率；在网页排名（PageRank）算法中，我们关心长期访问每个网页的概率。没有这些定理，马尔可夫链就只是一个数学玩具。
- **English:** These theorems are the foundation for practical applications of Markov chains. For example, in queueing theory, we want to know the long-term distribution of waiting times; in actuarial science, we need to calculate long-term discount rates; in the PageRank algorithm, we care about the long-term probability of visiting each webpage. Without these theorems, Markov chains would remain a mathematical toy.

---

### 🎯 Learning Objectives / 学习目标

After completing this section, you should be able to / 完成本节后，你应该能够：

1. **Define and identify equilibrium distributions / 定义并识别平衡分布：** Understand what it means for a distribution to be an equilibrium distribution and how it differs from a stationary distribution.

2. **Apply the Limit Theorem / 应用极限定理：** Determine when a Markov chain converges to an equilibrium distribution, and compute the limiting distribution for irreducible, aperiodic, positive recurrent chains.

3. **Apply the Ergodic Theorem / 应用遍历定理：** Compute the long-run proportion of time spent in each state for irreducible, positive recurrent chains, even when the chain is periodic.

4. **Recognize when convergence fails / 识别何时不收敛：** Identify cases where the limit theorem does not apply (periodic chains, null recurrent or transient chains, reducible chains).

5. **Interpret the relationship between stationary and equilibrium distributions / 理解平稳分布与平衡分布的关系：** Understand that an equilibrium distribution must be stationary, but a stationary distribution is not necessarily an equilibrium distribution.

6. **Compute long-term averages / 计算长期平均值：** Use the stationary distribution to compute long-term expected values, such as average discounts or costs.

---

### 📚 Prerequisites / 前置知识

Before studying this section, you should be familiar with / 在学习本节之前，你应该熟悉：

| Concept / 概念 | What you need to know / 你需要知道 |
|----------------|-------------------------------------|
| Markov chains / 马尔可夫链 | Definition, transition matrix, n-step transition probabilities |
| Irreducibility / 不可约性 | All states communicate with each other |
| Periodicity / 周期性 | Period of a state, aperiodic chains (period 1) |
| Recurrence and transience / 常返性与瞬时性 | Recurrent states return with probability 1; transient states may not return |
| Positive vs null recurrence / 正常返与零常返 | Positive recurrent: expected return time is finite; null recurrent: expected return time is infinite |
| Stationary distribution / 平稳分布 | A distribution π such that πP = π |
| Expected return time / 期望返回时间 | μⱼ = expected time to return to state j |

If you are unsure about any of these, review Sections 8-10 of the course materials before proceeding.

---

### 📖 Core Content / 核心内容

---

#### Topic 1: Convergence to Equilibrium / 收敛到平衡

##### Intuition / 直觉理解

**中文解释：** 想象一个马尔可夫链从某个初始状态开始运行。随着时间的推移，链的状态分布可能会逐渐"忘记"它的初始状态，并趋近于一个稳定的分布。这个稳定的分布就是"平衡分布"（equilibrium distribution）。例如，考虑一个简单的两状态"打印机"链：打印机要么工作（状态0），要么故障（状态1）。无论你最初看到打印机是什么状态，经过足够长的时间后，打印机处于工作状态的概率会趋近于一个固定值，这个值不依赖于初始状态。这就是收敛到平衡。

**English explanation:** Imagine a Markov chain starting from some initial state. As time passes, the distribution of the chain's state may gradually "forget" its initial state and approach a stable distribution. This stable distribution is called the "equilibrium distribution." For example, consider a simple two-state "printer" chain: the printer is either working (state 0) or broken (state 1). No matter what state you initially observe the printer in, after enough time, the probability that the printer is working approaches a fixed value that does not depend on the initial state. This is convergence to equilibrium.

**Key insight / 关键洞察：** The equilibrium distribution represents the "long-term average behavior" of the chain, independent of where it started.

##### Formal Definition / 形式化定义

**Definition 11.1 (Equilibrium Distribution / 平衡分布)**

Let (Xₙ) be a Markov chain on a state space 𝒮 with transition matrix P. Suppose there exists a distribution p* = (p*ᵢ) on 𝒮 (so p*ᵢ ≥ 0 and Σᵢ p*ᵢ = 1) such that, whatever the initial distribution λ = (λᵢ), we have ℙ(Xₙ = j) → p*ⱼ as n → ∞ for all j ∈ 𝒮. Then we say that p* is an **equilibrium distribution**.

**Symbol explanation / 符号说明：**

| Symbol / 符号 | Meaning / 含义 |
|---------------|----------------|
| (Xₙ) | The Markov chain / 马尔可夫链 |
| 𝒮 | State space / 状态空间 |
| P | Transition matrix / 转移矩阵 |
| p* = (p*ᵢ) | A candidate equilibrium distribution / 候选平衡分布 |
| λ = (λᵢ) | Initial distribution / 初始分布 |
| ℙ(Xₙ = j) | Probability that the chain is in state j at time n / 链在时间n处于状态j的概率 |
| → | Converges to / 收敛到 |

**Key points / 关键点：**
- The convergence must hold for **every** initial distribution λ.
- The limit p*ⱼ is the same regardless of where the chain started.
- There can be at most one equilibrium distribution (if it exists).

##### The Limit Theorem / 极限定理

**Theorem 11.1 (Limit Theorem / 极限定理)**

Let (Xₙ) be an irreducible and aperiodic Markov chain. Then for any initial distribution λ, we have that ℙ(Xₙ = j) → 1/μⱼ as n → ∞, where μⱼ is the expected return time to state j.

**In particular / 特别地：**

- **Positive recurrent case / 正常返情况：** Suppose (Xₙ) is positive recurrent. Then the unique stationary distribution π given by πⱼ = 1/μⱼ is the equilibrium distribution, so ℙ(Xₙ = j) → πⱼ for all j.

- **Null recurrent or transient case / 零常返或瞬时情况：** Suppose (Xₙ) is null recurrent or transient. Then ℙ(Xₙ = j) → 0 for all j, and there is no equilibrium distribution.

**Symbol explanation / 符号说明：**

| Symbol / 符号 | Meaning / 含义 |
|---------------|----------------|
| μⱼ | Expected return time to state j / 返回状态j的期望时间 |
| πⱼ | Stationary distribution at state j / 状态j的平稳分布 |
| 1/μⱼ | The limiting probability of being in state j / 处于状态j的极限概率 |

**Three conditions for convergence to equilibrium / 收敛到平衡的三个条件：**
1. **Irreducibility / 不可约性** — All states communicate
2. **Aperiodicity / 非周期性** — Period = 1
3. **Positive recurrence / 正常返性** — Expected return times are finite

**Important consequence / 重要推论：**

For an irreducible, aperiodic, positive recurrent Markov chain, the n-step transition matrix converges to a matrix where every row is identical:

lim_{n→∞} P⁽ⁿ⁾ = 
$$
\begin{pmatrix}
π₁    π₂    ⋯    π_N \\
π₁    π₂    ⋯    π_N \\
⋮     ⋮     ⋮     ⋮ \\
π₁    π₂    ⋯    π_N
\end{pmatrix}
$$

This means that after a long time, the probability of being in state j is approximately πⱼ, regardless of the starting state.

##### Theorem 11.2: Equilibrium ⇒ Stationary / 平衡分布必为平稳分布

**Theorem 11.2 / 定理11.2**

If an equilibrium distribution p* does exist, then p* is a stationary distribution.

**中文解释：** 这个定理告诉我们，平衡分布一定是平稳分布。这意味着，如果我们找到了一个平衡分布，那么它必须满足 p*P = p*。这个结果很重要，因为它将平衡分布的概念与我们已经熟悉的平稳分布联系起来。反过来不一定成立：平稳分布不一定是平衡分布（例如，周期链有平稳分布但没有平衡分布）。

**English explanation:** This theorem tells us that an equilibrium distribution must be a stationary distribution. This means that if we find an equilibrium distribution, it must satisfy p*P = p*. This result is important because it connects the concept of equilibrium distribution to the stationary distribution we already know. The converse is not necessarily true: a stationary distribution is not necessarily an equilibrium distribution (for example, a periodic chain has a stationary distribution but no equilibrium distribution).

**Proof / 证明：**

We need to verify that p*P = p*. We have:

Σᵢ p*ᵢ pᵢⱼ = Σᵢ (lim_{n→∞} pₖᵢ⁽ⁿ⁾) pᵢⱼ = lim_{n→∞} Σᵢ pₖᵢ⁽ⁿ⁾ pᵢⱼ = lim_{n→∞} pₖⱼ⁽ⁿ⁺¹⁾ = p*ⱼ

**Step-by-step explanation / 逐步解释：**

| Step / 步骤 | Expression / 表达式 | Explanation / 解释 |
|-------------|---------------------|-------------------|
| 1 | Σᵢ p*ᵢ pᵢⱼ | We want to show this equals p*ⱼ |
| 2 | = Σᵢ (lim_{n→∞} pₖᵢ⁽ⁿ⁾) pᵢⱼ | Replace p*ᵢ with its definition as the limit of n-step probabilities |
| 3 | = lim_{n→∞} Σᵢ pₖᵢ⁽ⁿ⁾ pᵢⱼ | Swap sum and limit (justified for finite state spaces) |
| 4 | = lim_{n→∞} pₖⱼ⁽ⁿ⁺¹⁾ | This is the Chapman-Kolmogorov equation for n+1 steps |
| 5 | = p*ⱼ | By definition of p*ⱼ as the limit |

**Note / 注意：** Strictly speaking, swapping the sum and the limit is only formally justified when the state space is finite, although the theorem is true universally using the dominated convergence theorem.

**Implication / 含义：** This theorem shows that an irreducible Markov chain cannot have an equilibrium distribution if it is null recurrent or transient, as it does not even have a stationary distribution. So the positive recurrent case is the hard (nonexaminable) one.

---

#### Topic 2: Examples of Convergence and Non-convergence / 收敛与不收敛的例子

##### Example 11.1: Two-State "Broken Printer" Chain / 两状态"故障打印机"链

**中文解释：** 回顾我们在问题集3中研究过的两状态打印机链。这个链是不可约的、非周期的、正常返的。因此，根据极限定理，它的平稳分布就是平衡分布。我们之前已经从基本原理证明了这一点。

**English explanation:** Recall the two-state printer chain we studied in Problem Sheet 3. This chain is irreducible, aperiodic, and positive recurrent. Therefore, by the Limit Theorem, its stationary distribution is also the equilibrium distribution. We proved this from first principles earlier.

##### Example 11.2: No-Claims Discount Chain / 无索赔折扣链

**中文解释：** 回忆我们在第6讲中学习的简单无索赔折扣马尔可夫链。这个链是不可约的、非周期的、正常返的。我们之前已经计算出它的唯一平稳分布为：

π = (1/13, 3/13, 9/13) = (0.0769, 0.2308, 0.6923)

根据极限定理，n步转移概率矩阵的每一行都会收敛到π。我们可以用计算机验证：当n=12时，

P¹² = 
$$
\begin{pmatrix}
0.0770   0.2308   0.6923 \\
0.0769   0.2308   0.6923 \\
0.0769   0.2308   0.6923
\end{pmatrix}
$$

其中pᵢⱼ⁽¹²⁾与πⱼ的差异不超过0.001。随着n增大，矩阵越来越接近极限形式。

**English explanation:** Recall the simple no-claims discount Markov chain from Lecture 6. This chain is irreducible, aperiodic, and positive recurrent. We previously computed its unique stationary distribution as:

π = (1/13, 3/13, 9/13) = (0.0769, 0.2308, 0.6923)

By the Limit Theorem, each row of the n-step transition probability matrix converges to π. We can verify using a computer: for n=12,

P¹² = 
$$
\begin{pmatrix}
0.0770   0.2308   0.6923 \\
0.0769   0.2308   0.6923 \\
0.0769   0.2308   0.6923
\end{pmatrix}
$$

where pᵢⱼ⁽¹²⁾ equals πⱼ to within 0.001 for all i, j. As n gets larger, the matrix gets closer and closer to the limiting form.

##### Example 11.3: Simple Random Walk / 简单随机游走

**中文解释：** 简单随机游走（在整数线上每一步以概率p向右、概率1-p向左移动）是：
- 当p=1/2时，零常返（null recurrent）
- 当p≠1/2时，瞬时（transient）

无论哪种情况，对于所有状态i，我们有ℙ(Xₙ = i) → 0，因此不存在平衡分布。这是因为随机游走会"扩散"到越来越大的区域，在任何特定状态上的概率趋近于零。

**English explanation:** The simple random walk (moving right with probability p and left with probability 1-p at each step on the integer line) is:
- Null recurrent when p=1/2
- Transient when p≠1/2

In either case, we have ℙ(Xₙ = i) → 0 for all states i, and there is no equilibrium distribution. This is because the random walk "spreads out" over an increasingly large area, so the probability of being at any specific state approaches zero.

##### Example 11.4: Two-State Periodic Chain / 两状态周期链

**中文解释：** 考虑一个状态空间为𝒮={0,1}的马尔可夫链，转移矩阵为：

P = 
$$
\begin{pmatrix}
0   1 \\
1   0
\end{pmatrix}
$$

每一步我们都从状态0切换到状态1，再切换回来。这个链是不可约的、正常返的，因此它有唯一的平稳分布π=(1/2, 1/2)。

然而，我们并没有收敛到平衡。如果从初始分布(λ₀, λ₁)开始，那么：
- 当n为偶数时，ℙ(Xₙ=0) = λ₀
- 当n为奇数时，ℙ(Xₙ=0) = λ₁

当λ₀≠1/2时，这个序列不收敛。关键在于这个链不是非周期的：它的周期为2，因此极限定理不适用。

**English explanation:** Consider a Markov chain on state space 𝒮={0,1} with transition matrix:

P = 
$$
\begin{pmatrix}
0   1 \\
1   0
\end{pmatrix}
$$

At each step we swap from state 0 to state 1 and back again. This chain is irreducible and positive recurrent, so it has a unique stationary distribution π=(1/2, 1/2).

However, we do not have convergence to equilibrium. If we start from initial distribution (λ₀, λ₁), then:
- For even n, ℙ(Xₙ=0) = λ₀
- For odd n, ℙ(Xₙ=0) = λ₁

When λ₀≠1/2, this does not converge. The point is that this chain is not aperiodic: it has period 2, so the Limit Theorem does not apply.

##### Example 11.5: Reducible Chain with Two Recurrent Classes / 可约链与两个常返类

**中文解释：** 考虑一个状态空间为𝒮={1,2,3}的马尔可夫链，转移图如下所示：

```
1 → 1 (概率3/4), 1 → 2 (概率1/4)
2 → 2 (概率2/3), 2 → 3 (概率1/3)
3 → 3 (概率1), 3 → 2 (概率0)
```

这个链不是不可约的，而是有两个非周期的、正常返的通信类。特别地，它有许多平稳分布，包括(1,0,0)和(0,8/17,9/17)（作为练习，请验证后者）。

如果我们从状态1开始，极限分布是(1,0,0)；如果我们从状态2或3开始，极限分布是(0,8/17,9/17)。因此，极限分布依赖于初始状态，这与平衡分布的定义相矛盾。

随着n→∞，我们有：

P⁽ⁿ⁾ → 
$$
\begin{pmatrix}
1      0      0 \\
0     8/17   9/17 \\
0     8/17   9/17
\end{pmatrix}
$$

**English explanation:** Consider a Markov chain with state space 𝒮={1,2,3} and transition diagram as shown:

```
1 → 1 (prob 3/4), 1 → 2 (prob 1/4)
2 → 2 (prob 2/3), 2 → 3 (prob 1/3)
3 → 3 (prob 1), 3 → 2 (prob 0)
```

This chain is not irreducible, but has two aperiodic and positive recurrent communicating classes. In particular, it has many stationary distributions including (1,0,0) and (0,8/17,9/17) (verify the latter as an exercise).

If we start in state 1, the limiting distribution is (1,0,0); if we start in states 2 or 3, the limiting distribution is (0,8/17,9/17). Therefore, the limiting distribution depends on the initial state, contradicting the definition of an equilibrium distribution.

As n→∞, we have:

P⁽ⁿ⁾ → 
$$
\begin{pmatrix}
1      0      0 \\
0     8/17   9/17 \\
0     8/17   9/17
\end{pmatrix}
$$

---

#### Topic 3: The Ergodic Theorem / 遍历定理

##### Intuition / 直觉理解

**中文解释：** 极限定理研究的是在某个特定时间点n（遥远的未来）链处于状态j的概率。而遍历定理研究的是在长期运行中，链在状态j上花费的时间比例。这是两种不同的"长期行为"：前者是"点态"的（在某个时刻），后者是"平均"的（在一段时间内）。

例如，考虑周期为2的交换链。在遥远的未来某个特定时刻，链处于状态0的概率依赖于初始状态（如果初始状态是0，那么偶数时刻在状态0，奇数时刻在状态1）。但是，在长期运行中，链有一半的时间在状态0，一半的时间在状态1，无论初始状态如何。

**English explanation:** The Limit Theorem looks at the probability that the chain is in state j at some specific point in time n far in the future. The Ergodic Theorem looks at the proportion of time the chain spends in state j over a long period. These are two different types of "long-term behavior": the former is "pointwise" (at a specific moment), the latter is "average" (over a period of time).

For example, consider the period-2 swapping chain. At a specific moment far in the future, the probability of being in state 0 depends on the initial state (if we start in state 0, we're in state 0 at even times and state 1 at odd times). However, in the long run, the chain spends half its time in state 0 and half in state 1, regardless of the initial state.

**Definition / 定义：**

Let Vⱼ(N) := #{n < N : Xₙ = j} be the total number of visits to state j up to time N.

Then Vⱼ(n)/n is the proportion of time up to time n spent in state j, and its limiting value (if it exists) is the long-run proportion of time spent in state j.

##### Theorem 11.3 (Ergodic Theorem / 遍历定理)

**Theorem 11.3 / 定理11.3**

Let (Xₙ) be an irreducible Markov chain. Then for any initial distribution λ, we have that Vⱼ(n)/n → 1/μⱼ almost surely as n → ∞, where μⱼ is the expected return time to state j.

**In particular / 特别地：**

- **Positive recurrent case / 正常返情况：** Suppose (Xₙ) is positive recurrent. Then there is a unique stationary distribution π given by πⱼ = 1/μⱼ, and Vⱼ(n)/n → πⱼ almost surely for all j.

- **Null recurrent or transient case / 零常返或瞬时情况：** Suppose (Xₙ) is null recurrent or transient. Then Vⱼ(n)/n → 0 almost surely for all j.

**Symbol explanation / 符号说明：**

| Symbol / 符号 | Meaning / 含义 |
|---------------|----------------|
| Vⱼ(N) | Number of visits to state j up to time N / 到时间N为止访问状态j的次数 |
| Vⱼ(n)/n | Proportion of time spent in state j up to time n / 到时间n为止在状态j上花费的时间比例 |
| → | Converges to / 收敛到 |
| almost surely / 几乎必然 | ℙ(Vⱼ(n)/n → 1/μⱼ) = 1, i.e., the convergence happens with probability 1 |

**Key difference from Limit Theorem / 与极限定理的关键区别：**

| Aspect / 方面 | Limit Theorem / 极限定理 | Ergodic Theorem / 遍历定理 |
|----------------|--------------------------|----------------------------|
| What it studies / 研究内容 | ℙ(Xₙ = j) at a specific time n | Vⱼ(n)/n over time up to n |
| Requires aperiodicity? / 需要非周期性？ | Yes / 是 | No / 否 |
| Requires positive recurrence? / 需要正常返？ | Yes for non-zero limit | Yes for non-zero limit |
| Requires irreducibility? / 需要不可约性？ | Yes | Yes |

**Why no aperiodicity needed / 为什么不需要非周期性：** Because we are averaging over time, the periodic fluctuations get averaged out. Even if the chain oscillates between states, the long-term proportion of time spent in each state still converges.

##### Example 11.6: No-Claims Discount Chain (Ergodic) / 无索赔折扣链（遍历）

**中文解释：** 回顾无索赔折扣马尔可夫链。由于这个链是不可约的、正常返的，根据遍历定理，长期在每个状态上花费的时间比例对应于平稳分布π=(1/13, 3/13, 9/13)。

因此，在一个长期持有的保险单的整个生命周期中，平均折扣大约是：

(1/13)×0% + (3/13)×25% + (9/13)×50% = 21/52 = 40.4%

这是一个实际应用：保险公司可以用这个结果来计算长期平均折扣率，从而制定保费策略。

**English explanation:** Recall the no-claims discount Markov chain. Since this chain is irreducible and positive recurrent, by the Ergodic Theorem, the long-term proportion of time spent in each state corresponds to the stationary distribution π=(1/13, 3/13, 9/13).

Therefore, over the lifetime of an insurance policy held for a long period of time, the average discount is approximately:

(1/13)×0% + (3/13)×25% + (9/13)×50% = 21/52 = 40.4%

This is a practical application: insurance companies can use this result to calculate long-term average discount rates and thus formulate premium strategies.

##### Example 11.7: Two-State Swapping Chain (Ergodic) / 两状态交换链（遍历）

**中文解释：** 我们之前看到的周期为2的交换链确实有唯一的平稳分布(1/2, 1/2)，但没有平衡分布，因为它是周期的。然而，根据遍历定理，V₀(n)/n → π₀ = 1/2 且 V₁(n)/n → π₁ = 1/2。

所以，虽然在遥远的未来某个特定