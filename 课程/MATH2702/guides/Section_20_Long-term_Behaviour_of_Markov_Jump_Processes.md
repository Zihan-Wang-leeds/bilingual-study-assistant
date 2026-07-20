# Section 20: Long-term behaviour of Markov jump processes

> MATH2702 - 自学教材 / Self-Study Guide
> 生成时间: 2026-07-20 15:58
> 来源页: 94-98

---

# MATH2702: Markov Jump Processes - Long-term Behaviour / 马尔可夫跳跃过程的长期行为

## 📋 Section Overview / 章节概览

**中文解释：** 本章节研究连续时间马尔可夫跳跃过程的长期行为。与离散时间马尔可夫链类似，我们关注两个核心问题：(1) 是否存在一个平稳分布（stationary distribution），使得过程在长时间后不再随时间变化？(2) 过程是否收敛到某个平衡分布（equilibrium distribution）？以及(3) 长期来看，过程在每个状态上花费的时间比例是多少？这些问题的答案对于理解排队系统、化学反应动力学、生物种群模型等实际应用至关重要。

**English explanation:** This section studies the long-term behaviour of continuous-time Markov jump processes. Similar to discrete-time Markov chains, we focus on three core questions: (1) Does there exist a stationary distribution such that the process no longer changes over time? (2) Does the process converge to an equilibrium distribution? and (3) What is the long-run proportion of time spent in each state? The answers to these questions are crucial for understanding queueing systems, chemical reaction kinetics, biological population models, and many other real-world applications.

**Why this matters / 为什么重要：** 在实际应用中，我们通常不关心过程的短期波动，而是关心其长期稳定行为。例如，一个电话交换系统长期来看有多少条线路被占用？一个化学反应系统最终会达到什么平衡状态？这些问题的答案都依赖于本章的理论。

## 🎯 Learning Objectives / 学习目标

完成本章学习后，你应该能够：

1. **定义并识别** 连续时间马尔可夫跳跃过程的平稳分布，理解其与生成矩阵Q的关系
2. **求解** 平稳分布通过解方程πQ = 0
3. **理解** 极限定理（Limit Theorem）和遍历定理（Ergodic Theorem）的内容和区别
4. **判断** 一个不可约马尔可夫跳跃过程是否存在平稳分布（正返则存在，零返或瞬过则不存在）
5. **应用** 可逆性（reversibility）和细致平衡（detailed balance）条件
6. **计算** 给定生成矩阵Q的平稳分布

## 📚 Prerequisites / 前置知识

在开始本章之前，你应该已经掌握：

- **离散时间马尔可夫链的平稳分布**：理解πP = π的含义
- **离散时间极限定理和遍历定理**：知道什么是平衡分布
- **连续时间马尔可夫跳跃过程的基本概念**：生成矩阵Q、转移半群P(t)、跳跃链
- **不可约性（irreducibility）**：状态空间中的每个状态都能到达其他所有状态
- **正返、零返、瞬过**：状态分类的基本概念

## 📖 Core Content / 核心内容

### Topic 1: Stationary Distributions / 平稳分布

#### Intuition / 直觉理解

**中文解释：** 想象一个系统在长时间运行后，其状态分布不再随时间变化。也就是说，无论你观察系统在什么时间点，它处于某个特定状态的概率都是相同的。这个不变的分布就是平稳分布。在离散时间中，我们通过πP = π来找到它；在连续时间中，我们通过πQ = 0来找到它。为什么是πQ = 0？因为Q描述了状态变化的"速率"，当这些速率导致的净变化为零时，分布就稳定了。

**English explanation:** Imagine a system that, after running for a long time, has a state distribution that no longer changes over time. That is, no matter when you observe the system, the probability of being in a particular state is the same. This unchanging distribution is the stationary distribution. In discrete time, we find it via πP = π; in continuous time, we find it via πQ = 0. Why πQ = 0? Because Q describes the "rate" of state changes, and when the net change caused by these rates is zero, the distribution stabilizes.

#### Formal Definition / 形式化定义

**Definition 20.1 (Stationary Distribution / 平稳分布).** Let (X(t)) be a Markov jump process on a state space S with generator matrix Q and transition semigroup (P(t)). Let π = (π_i) be a distribution on S, meaning π_i ≥ 0 for all i ∈ S and ∑_{i∈S} π_i = 1. We call π a stationary distribution if

π_j = ∑_{i∈S} π_i p_{ij}(t) for all j ∈ S and t ≥ 0,

or equivalently, if π = π P(t) for all t ≥ 0.

**Symbol explanation / 符号说明：**

| Symbol | Meaning (English) | 含义（中文） |
|--------|-------------------|--------------|
| π | Stationary distribution vector | 平稳分布向量 |
| π_i | Probability of being in state i under stationary distribution | 平稳分布下处于状态i的概率 |
| p_{ij}(t) | Transition probability from i to j in time t | 时间t内从i到j的转移概率 |
| P(t) | Transition matrix at time t | 时间t的转移矩阵 |
| Q | Generator matrix | 生成矩阵 |

**中文解释：** 这个定义看起来有点复杂，因为它要求对所有t≥0都成立。但幸运的是，我们有一个更简单的方法：只需解πQ = 0。定理20.1告诉我们，如果πQ = 0，那么π就是平稳分布。

**English explanation:** This definition looks complicated because it requires the condition to hold for all t≥0. But fortunately, we have a much simpler method: just solve πQ = 0. Theorem 20.1 tells us that if πQ = 0, then π is a stationary distribution.

#### Theorem 20.1: Stationary Distribution via πQ = 0 / 通过πQ = 0求平稳分布

**Theorem 20.1.** Let (X(t)) be a Markov jump process on a state space S with generator matrix Q. If π = (π_i) is a distribution with ∑_i π_i q_{ij} = 0 for all j, then π is a stationary distribution. In matrix form, this condition is πQ = 0.

**中文解释：** 这个定理告诉我们，要找到平稳分布，我们不需要计算所有P(t)，只需要解一个线性方程组πQ = 0。这里的0是一个行向量，所有元素都是0。这个方程表示：在平稳分布下，进入每个状态j的"概率流"等于离开该状态的"概率流"。

**English explanation:** This theorem tells us that to find the stationary distribution, we don't need to compute all P(t); we only need to solve a linear system πQ = 0. Here, 0 is a row vector with all elements equal to 0. This equation means: under the stationary distribution, the "probability flow" into each state j equals the "probability flow" out of that state.

#### Proof / 证明

**Proof / 证明：** Suppose πQ = 0. We need to show that πP(t) = π for all t.

**Step 1: Show πP(t) is constant / 第一步：证明πP(t)是常数**

We show that the derivative of πP(t) is zero. Using the backward equation P'(t) = QP(t), we have:

d/dt πP(t) = π d/dt P(t) = π Q P(t) = 0 · P(t) = 0

**中文解释：** 我们利用后向方程（backward equation）P'(t) = QP(t)来求导。因为πQ = 0，所以导数为零，这意味着πP(t)不随时间变化，是一个常数向量。

**English explanation:** We use the backward equation P'(t) = QP(t) to take the derivative. Since πQ = 0, the derivative is zero, which means πP(t) does not change with time; it is a constant vector.

**Step 2: Find the constant value / 第二步：找出常数值**

We can find the constant value by setting t to any convenient value. We pick t = 0. Since P(0) = I (the identity matrix), we have:

πP(t) = πP(0) = πI = π for all t

**中文解释：** 因为πP(t)是常数，它在任何t的值都相同。特别地，在t=0时，P(0)是单位矩阵，所以πP(0) = π。因此，对所有t，πP(t) = π。

**English explanation:** Since πP(t) is constant, its value at any t is the same. In particular, at t=0, P(0) is the identity matrix, so πP(0) = π. Therefore, for all t, πP(t) = π.

**Note / 注：** Strictly speaking, taking π outside the derivative in the first step is only formally justified when the state space is finite, but the result is true for general processes.

**中文解释：** 严格来说，在第一步中将π提到导数外面只在状态空间有限时才有形式上的严格证明，但该结果对一般过程也成立。

**English explanation:** Strictly speaking, taking π outside the derivative in the first step is only formally justified when the state space is finite, but the result is true for general processes.

#### Worked Example 20.1 / 例题20.1

**Example 20.1.** Consider the Markov jump process with generator matrix:

Q = $$
\begin{pmatrix}
-2   2   0 \\
1  -3   2 \\
0   1  -1
\end{pmatrix}
$$

Find the stationary distribution.

**Solution / 解答：**

**Step 1: Write out the equations / 第一步：写出方程**

We write out the equations of (π₁, π₂, π₃) Q = (0, 0, 0) coordinate by coordinate:

(π₁, π₂, π₃) $$
\begin{pmatrix}
-2   2   0 \\
1  -3   2 \\
0   1  -1
\end{pmatrix}
$$

This gives three equations:

- For column 1: -2π₁ + 1·π₂ + 0·π₃ = 0 → -2π₁ + π₂ = 0
- For column 2: 2π₁ + (-3)π₂ + 1·π₃ = 0 → 2π₁ - 3π₂ + π₃ = 0
- For column 3: 0·π₁ + 2π₂ + (-1)π₃ = 0 → 2π₂ - π₃ = 0

**中文解释：** 我们逐列写出方程。注意，Q的每一列对应一个状态j，方程∑ᵢπᵢqᵢⱼ = 0表示进入状态j的净概率流为零。我们得到三个方程，但只有两个是独立的（因为行和为0的性质）。

**English explanation:** We write out the equations column by column. Note that each column of Q corresponds to a state j, and the equation ∑ᵢπᵢqᵢⱼ = 0 means the net probability flow into state j is zero. We get three equations, but only two are independent (due to the row sum property).

**Step 2: Discard one equation / 第二步：舍弃一个方程**

We discard one equation. I will discard the second one as it is the most complicated.

Remaining equations:
- -2π₁ + π₂ = 0
- 2π₂ - π₃ = 0

**中文解释：** 由于三个方程中只有两个是独立的，我们可以舍弃一个。通常选择舍弃最复杂的那个方程。

**English explanation:** Since only two of the three equations are independent, we can discard one. Usually we discard the most complicated one.

**Step 3: Choose a working variable / 第三步：选择工作变量**

I will pick π₂ since it appears in both remaining equations.

From -2π₁ + π₂ = 0: π₁ = (1/2)π₂
From 2π₂ - π₃ = 0: π₃ = 2π₂

**中文解释：** 我们选择π₂作为工作变量，用π₂表示其他变量。从第一个方程得到π₁ = π₂/2，从第三个方程得到π₃ = 2π₂。

**English explanation:** We choose π₂ as the working variable and express other variables in terms of π₂. From the first equation we get π₁ = π₂/2, and from the third equation we get π₃ = 2π₂.

**Step 4: Use the normalising condition / 第四步：使用归一化条件**

π₁ + π₂ + π₃ = (1/2 + 1 + 2)π₂ = (7/2)π₂ = 1

This gives π₂ = 2/7.

Hence:
- π₁ = (1/2)(2/7) = 1/7
- π₃ = 2(2/7) = 4/7

**中文解释：** 归一化条件∑πᵢ = 1确保我们得到的是一个概率分布。代入π₁和π₃的表达式，解出π₂ = 2/7，然后得到π₁ = 1/7，π₃ = 4/7。

**English explanation:** The normalising condition ∑πᵢ = 1 ensures we get a probability distribution. Substituting the expressions for π₁ and π₃, we solve for π₂ = 2/7, then get π₁ = 1/7 and π₃ = 4/7.

**Answer / 答案：** The stationary distribution is π = (1/7, 2/7, 4/7).

#### Theorem 20.2: Existence and Uniqueness / 存在性和唯一性

**Theorem 20.2.** Consider an irreducible Markov jump process on state space S with generator matrix Q.

- If the Markov jump process is **positive recurrent**, then a stationary distribution π exists, is unique, and is given by π_i = 1/(q_i μ_i), where μ_i is the expected return time to state i (unless the state space is a single absorbing state i, in which case π_i = 1).
- If the Markov jump process is **null recurrent** or **transient**, then no stationary distribution exists.

**中文解释：** 这个定理给出了平稳分布存在且唯一的条件。与离散时间情况类似，需要两个条件：不可约性（irreducibility）和正返性（positive recurrence）。但与离散时间不同的是，连续时间中平稳分布的表达式多了一个因子1/qᵢ。这个因子表示在状态i中平均停留的时间（直到跳走）。注意，如果状态空间只有一个吸收态i，那么πᵢ = 1。

**English explanation:** This theorem gives the conditions for the existence and uniqueness of a stationary distribution. Similar to the discrete-time case, two conditions are needed: irreducibility and positive recurrence. However, unlike the discrete-time case, the expression for the stationary distribution in continuous time has an extra factor of 1/qᵢ. This factor represents the average time spent in state i (until jumping). Note that if the state space is a single absorbing state i, then πᵢ = 1.

**Key difference from discrete time / 与离散时间的关键区别：**

| Aspect | Discrete Time | Continuous Time |
|--------|---------------|-----------------|
| Stationary distribution equation | πP = π | πQ = 0 |
| Expression for πᵢ | πᵢ = 1/μᵢ | πᵢ = 1/(qᵢμᵢ) |
| Periodicity condition needed? | Yes (aperiodic) | No |

### Topic 2: Reversibility and Detailed Balance / 可逆性和细致平衡

#### Intuition / 直觉理解

**中文解释：** 可逆性是一个很强的性质。如果一个马尔可夫过程是可逆的，那么从长远来看，过程正向运行和反向运行在统计上是不可区分的。这意味着，如果你录制了过程的一段视频然后倒放，你无法判断哪一个是正向的。细致平衡条件π(x)Q(x,y) = π(y)Q(y,x)正是这种可逆性的数学表达：在平稳分布下，从状态x到y的"概率流"等于从y到x的"概率流"。

**English explanation:** Reversibility is a strong property. If a Markov process is reversible, then in the long run, the process running forward and backward are statistically indistinguishable. This means that if you record a video of the process and play it backwards, you cannot tell which is the forward version. The detailed balance condition π(x)Q(x,y) = π(y)Q(y,x) is the mathematical expression of this reversibility: under the stationary distribution, the "probability flow" from state x to y equals the "probability flow" from y to x.

#### Formal Definition / 形式化定义

**Definition 20.2 (Reversibility / 可逆性).** Let (X(t)) be a Markov jump process on S with generator matrix Q. If there is a distribution π on S such that Q and π satisfy the **detailed balance conditions**

π(x) Q(x,y) = π(y) Q(y,x) for all x, y ∈ S

then we say that (X(t)) is **reversible**.

**中文解释：** 注意，细致平衡条件是对所有状态对(x,y)都成立。如果存在一个分布π满足这个条件，那么π就是平稳分布（可以验证）。但反过来不一定成立：一个平稳分布不一定满足细致平衡条件。可逆性是一个比存在平稳分布更强的条件。

**English explanation:** Note that the detailed balance condition must hold for all pairs of states (x,y). If there exists a distribution π satisfying this condition, then π is a stationary distribution (this can be verified). But the converse is not necessarily true: a stationary distribution does not necessarily satisfy the detailed balance condition. Reversibility is a stronger condition than the existence of a stationary distribution.

**Example / 例子：** The Markov jump process given in Example 20.1 is reversible. Let's verify:

For states 1 and 2: π₁Q(1,2) = (1/7)(2) = 2/7, π₂Q(2,1) = (2/7)(1) = 2/7 ✓
For states 2 and 3: π₂Q(2,3) = (2/7)(2) = 4/7, π₃Q(3,2) = (4/7)(1) = 4/7 ✓
For states 1 and 3: π₁Q(1,3) = (1/7)(0) = 0, π₃Q(3,1) = (4/7)(0) = 0 ✓

All pairs satisfy the condition, so the process is reversible.

### Topic 3: Convergence to Equilibrium / 收敛到平衡

#### Intuition / 直觉理解

**中文解释：** 极限定理研究的是：当时间t趋于无穷时，过程处于某个状态j的概率ℙ(X(t) = j)的极限行为。如果这个极限存在且与初始分布无关，我们就称这个极限为平衡分布（equilibrium distribution）。与离散时间不同，连续时间马尔可夫跳跃过程不需要周期性条件（aperiodicity condition），因为连续时间本身就能保证"非周期性"。

**English explanation:** The limit theorem studies the limiting behaviour of the probability ℙ(X(t) = j) as time t goes to infinity. If this limit exists and is independent of the initial distribution, we call this limit the equilibrium distribution. Unlike discrete time, continuous-time Markov jump processes do not need an aperiodicity condition, because continuous time itself ensures "aperiodicity."

#### Theorem 20.3: Limit Theorem / 极限定理

**Theorem 20.3 (Limit Theorem / 极限定理).** Let (X(t)) be an irreducible Markov jump process with generator matrix Q. Then for any initial distribution λ, we have that ℙ(X(t) = j) → 1/(q_j μ_j) as t → ∞ for all j, where μ_j is the expected return time to state j (unless the state space is a single absorbing state j, in which case ℙ(X(t) = j) → 1).

- Suppose (X(t)) is **positive recurrent**. Then there is an equilibrium distribution which is the unique stationary distribution π given by π_j = 1/(q_j μ_j) (unless the state space is a single absorbing state j, in which case π_j = 1), and ℙ(X(t) = j) → π_j for all j.
- Suppose (X(t)) is **null recurrent** or **transient**. Then ℙ(X(t) = j) → 0 for all j, and there is no equilibrium distribution.

**中文解释：** 这个定理告诉我们三件事：
1. 对于不可约的马尔可夫跳跃过程，ℙ(X(t) = j)的极限总是存在，且等于1/(q_j μ_j)。
2. 如果过程是正返的，这个极限就是平稳分布π_j，而且与初始分布无关。这意味着无论过程从哪里开始，长时间后处于状态j的概率都趋近于π_j。
3. 如果过程是零返或瞬过的，那么极限为0，不存在平衡分布。

注意：与离散时间不同，这里不需要周期性条件！

**English explanation:** This theorem tells us three things:
1. For an irreducible Markov jump process, the limit of ℙ(X(t) = j) always exists and equals 1/(q_j μ_j).
2. If the process is positive recurrent, this limit is the stationary distribution π_j, and it is independent of the initial distribution. This means that no matter where the process starts, the probability of being in state j after a long time approaches π_j.
3. If the process is null recurrent or transient, the limit is 0, and no equilibrium distribution exists.

Note: Unlike discrete time, no aperiodicity condition is needed here!

**Implication for transition matrix / 对转移矩阵的影响：**

For the positive recurrent case, if we take the initial distribution to be "starting in state i with certainty," we see that:

p_{ij}(t) = ℙ(X(t) = j | X(0) = i) → π_j

Hence P(t) has the limiting value:

lim_{t→∞} P(t) = $$
\begin{pmatrix}
π₁  π₂  ⋯  πₙ \\
π₁  π₂  ⋯  πₙ \\
⋮   ⋮   ⋮   ⋮ \\
π₁  π₂  ⋯  πₙ
\end{pmatrix}
$$

with each row the same.

**中文解释：** 这意味着当t很大时，转移概率p_{ij}(t)不再依赖于起始状态i，只依赖于目标状态j。转移矩阵的每一行都变成了相同的平稳分布向量。这是一个非常重要的性质：长时间后，过程"忘记"了它从哪里开始。

**English explanation:** This means that when t is large, the transition probability p_{ij}(t) no longer depends on the starting state i, only on the target state j. Each row of the transition matrix becomes the same stationary distribution vector. This is a very important property: after a long time, the process "forgets" where it started.

### Topic 4: Ergodic Theorem / 遍历定理

#### Intuition / 直觉理解

**中文解释：** 极限定理告诉我们的是"概率"的极限，而遍历定理告诉我们的是"时间比例"的极限。具体来说，遍历定理研究的是：在长时间运行中，过程在状态j上花费的时间占总时间的比例。这个比例由V_j(t)/t给出，其中V_j(t) = ∫₀ᵗ 𝕀[X(s) = j] ds是到时间t为止在状态j上花费的总时间。

**English explanation:** The limit theorem tells us about the limit of "probability," while the ergodic theorem tells us about the limit of "time proportion." Specifically, the ergodic theorem studies: over a long run, what proportion of total time does the process spend in state j? This proportion is given by V_j(t)/t, where V_j(t) = ∫₀ᵗ 𝕀[X(s) = j] ds is the total time spent in state j up to time t.

**Key difference / 关键区别：**
- **Limit Theorem (极限定理)**: ℙ(X(t) = j) → π_j — 概率的极限
- **Ergodic Theorem (遍历定理)**: V_j(t)/t → π_j — 时间比例的极限

**中文解释：** 对于遍历过程（ergodic process），这两个极限是相等的。这意味着"时间平均"等于"概率平均"——这是遍历性的核心思想。

**English explanation:** For an ergodic process, these two limits are equal. This means "time average" equals "probability average" — this is the core idea of ergodicity.

#### Formal Definition of V_j(t) / V_j(t)的形式化定义

We write:

V_j(t) = ∫₀ᵗ 𝕀[X(s) = j] ds

for the total amount of time spent in state j up to time t.

**Symbol explanation / 符号说明：**

| Symbol | Meaning (English) | 含义（中文） |
|--------|-------------------|--------------|
| V_j(t) | Total time in state j up to time t | 到时间t为止在状态j上的总时间 |
| 𝕀[X(s) = j] | Indicator function (1 if X(s)=j, 0 otherwise) | 指示函数（若X(s)=j则为1，否则为0） |
| ∫₀ᵗ | Integral from 0 to t | 从0到t的积分 |

**中文解释：** 指示函数𝕀[X(s) = j]在过程处于状态j时为1，否则为0。所以积分∫₀ᵗ 𝕀[X(s) = j] ds就是过程在状态j上花费的总时间。V_j(t)/t就是到时间t为止在状态j上花费的时间比例。

**English explanation:** The indicator function 𝕀[X(s) = j] is 1 when the process is in state j and 0 otherwise. So the integral ∫₀ᵗ 𝕀[X(s) = j] ds is the total time the process spends in state j. V_j(t)/t is the proportion of time spent in state j up to time t.

#### Theorem 20.4: Ergodic Theorem / 遍历定理

**Theorem 20.4 (Ergodic Theorem / 遍历定理).** Let (X(t)) be an irreducible Markov jump process with generator matrix Q. Then for any initial distribution λ, we have that V_j(t)/t → 1/(q_j μ_j) almost surely as t → ∞, where μ_j is the expected return time to state j (unless the state space is a single absorbing state j, in which case V_j(t)/t → 1 almost surely).

- Suppose (X(t)) is **positive recurrent**. Then there is a unique stationary distribution π given by π_j = 1/(q_j μ_j) (unless the state space is a single absorbing state j, in which case π_j = 1), and V_j(t)/t → π_j almost