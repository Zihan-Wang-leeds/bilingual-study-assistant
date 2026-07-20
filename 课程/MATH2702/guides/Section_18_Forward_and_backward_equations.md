# Section 18: Forward and backward equations

> MATH2702 - 自学教材 / Self-Study Guide
> 生成时间: 2026-07-20 15:57
> 来源页: 86-90

---

# 📚 Section 18: Forward and Backward Equations / 正向方程与反向方程

## 📋 Section Overview / 章节概览

**中文解释：** 本章节是连续时间马尔可夫跳变过程的核心内容。我们将学习如何在无穷小时间间隔内描述过程的转移行为，推导出控制转移概率演化的微分方程（正向方程和反向方程），并介绍矩阵指数作为这些方程的解。这些工具是理解和计算连续时间马尔可夫过程转移概率的基础。

**English explanation:** This section is the core content of continuous-time Markov jump processes. We will learn how to describe the transition behavior of the process in infinitesimal time intervals, derive the differential equations (forward and backward equations) that govern the evolution of transition probabilities, and introduce the matrix exponential as the solution to these equations. These tools are fundamental for understanding and computing transition probabilities of continuous-time Markov processes.

## 🎯 Learning Objectives / 学习目标

完成本章学习后，你应该能够：

1. **理解无穷小时间内的转移行为**：能够用生成矩阵Q的元素描述在极短时间τ内的转移概率
2. **掌握Chapman-Kolmogorov方程**：理解连续时间下的半群性质
3. **推导正向方程和反向方程**：从Chapman-Kolmogorov方程出发，推导出P'(t) = P(t)Q和P'(t) = QP(t)
4. **理解矩阵指数**：掌握矩阵指数的定义和性质，以及它如何作为正向和反向方程的解
5. **应用矩阵指数计算转移概率**：能够使用e^(tQ)计算有限状态空间下的转移概率矩阵

## 📚 Prerequisites / 前置知识

在开始学习本章之前，你需要掌握：

**中文解释：**
- 离散时间马尔可夫链的基本概念（转移矩阵、n步转移概率）
- 指数分布的性质（特别是无记忆性）
- 泰勒级数展开
- 矩阵乘法和矩阵幂
- 微分方程的基本解法

**English explanation:**
- Basic concepts of discrete-time Markov chains (transition matrix, n-step transition probabilities)
- Properties of exponential distribution (especially the memoryless property)
- Taylor series expansion
- Matrix multiplication and matrix powers
- Basic methods for solving differential equations

---

## 📖 Core Content / 核心内容

### 18.1 Transitions in Infinitesimal Time Periods / 无穷小时间段内的转移

#### Intuition / 直觉理解

**中文解释：** 想象一个粒子在状态空间中随机移动。在离散时间马尔可夫链中，我们每隔一个固定时间步长观察一次状态变化。但在连续时间马尔可夫跳变过程中，状态变化可以在任意时刻发生。关键问题是：在一个非常短的时间τ内，从状态i出发，会发生什么？

由于指数分布的无记忆性，从状态i出发后，等待下一次跳跃的时间T服从参数为q_i的指数分布（其中q_i = -q_ii，即生成矩阵Q中第i行对角元素的绝对值）。在极短时间τ内，要么没有跳跃（概率约为1 - q_iτ），要么恰好发生一次跳跃到状态j（概率约为q_ijτ），发生两次或更多次跳跃的概率是比τ更高阶的无穷小量o(τ)。

**English explanation:** Imagine a particle moving randomly in a state space. In discrete-time Markov chains, we observe state changes at fixed time intervals. However, in continuous-time Markov jump processes, state changes can occur at any time. The key question is: what happens in a very short time τ, starting from state i?

Due to the memoryless property of the exponential distribution, the waiting time T until the next jump from state i follows an exponential distribution with rate q_i (where q_i = -q_ii, the absolute value of the diagonal element in row i of the generator matrix Q). In a very short time τ, either no jump occurs (probability approximately 1 - q_iτ), or exactly one jump occurs to state j (probability approximately q_ijτ), and the probability of two or more jumps is of order o(τ), which is negligible compared to τ.

#### Formal Definition / 形式化定义

**中文解释：** 设(X(t))为连续时间马尔可夫跳变过程，生成矩阵为Q。对于任意状态i，定义q_i = -q_ii（即从状态i出发的总跳跃率）。在极短时间τ内，转移概率可以表示为：

**English explanation:** Let (X(t)) be a continuous-time Markov jump process with generator matrix Q. For any state i, define q_i = -q_ii (the total jump rate from state i). In a very short time τ, the transition probabilities can be expressed as:

$$\mathbb{P}(X(t+\tau) = j \mid X(t) = i) = \begin{cases} 1 - q_i\tau + o(\tau) & \text{for } i = j \\ q_{ij}\tau + o(\tau) & \text{for } i \neq j \end{cases}$$

**Symbol Explanation / 符号说明：**

| Symbol | 中文含义 | English Meaning |
|--------|----------|-----------------|
| X(t) | 时刻t的状态 | State at time t |
| q_i | 从状态i出发的总跳跃率 = -q_ii | Total jump rate from state i = -q_ii |
| q_ij | 从状态i到状态j的跳跃率 | Jump rate from state i to state j |
| τ | 极短的时间间隔 | Very short time interval |
| o(τ) | 比τ更高阶的无穷小量 | Higher-order infinitesimal compared to τ |

**Derivation / 推导过程：**

**中文解释：** 推导基于指数分布的性质。从状态i出发，等待时间T ∼ Exp(q_i)。根据无记忆性，在时间τ内不移动的概率为：
ℙ(T > τ) = e^{-q_iτ}

使用泰勒展开e^x = 1 + x + o(x)（当x→0时），得到：
e^{-q_iτ} = 1 - q_iτ + o(τ)

移动到状态j的概率为：
ℙ(T ≤ τ) × r_ij = (q_iτ + o(τ)) × (q_ij/q_i) = q_ijτ + o(τ)

其中r_ij = q_ij/q_i是从状态i跳到状态j的概率（跳跃链的转移概率）。

**English explanation:** The derivation is based on properties of the exponential distribution. Starting from state i, the waiting time T ∼ Exp(q_i). By the memoryless property, the probability of not moving in time τ is:
ℙ(T > τ) = e^{-q_iτ}

Using the Taylor expansion e^x = 1 + x + o(x) as x→0, we get:
e^{-q_iτ} = 1 - q_iτ + o(τ)

The probability of moving to state j is:
ℙ(T ≤ τ) × r_ij = (q_iτ + o(τ)) × (q_ij/q_i) = q_ijτ + o(τ)

where r_ij = q_ij/q_i is the probability of jumping from state i to state j (the jump chain transition probability).

---

### 18.2 Transition Semigroup and the Forward and Backward Equations / 转移半群与正向和反向方程

#### Intuition / 直觉理解

**中文解释：** 在离散时间马尔可夫链中，我们有n步转移概率p_ij(n)和转移矩阵P，并且P(n) = P^n。在连续时间中，我们需要找到从生成矩阵Q到转移概率矩阵P(t)的映射。这里的关键工具是Chapman-Kolmogorov方程和微分方程。

Chapman-Kolmogorov方程告诉我们：从状态i到状态j，经过时间s+t，可以先在时间s内到达某个中间状态k，再在时间t内从k到达j。对所有可能的中间状态k求和。

通过考虑一个无穷小的时间增量τ，我们可以得到关于P(t)的微分方程。这有两种方式：将τ放在"前面"（即先走τ时间，再走t时间）得到反向方程；将τ放在"后面"（即先走t时间，再走τ时间）得到正向方程。

**English explanation:** In discrete-time Markov chains, we have n-step transition probabilities p_ij(n) and transition matrix P, with P(n) = P^n. In continuous time, we need to find the mapping from the generator matrix Q to the transition probability matrix P(t). The key tools here are the Chapman-Kolmogorov equations and differential equations.

The Chapman-Kolmogorov equation tells us: to go from state i to state j in time s+t, we can first go from i to some intermediate state k in time s, then from k to j in time t, summing over all possible intermediate states k.

By considering an infinitesimal time increment τ, we can derive differential equations for P(t). There are two ways: putting τ "in front" (first go for time τ, then for time t) gives the backward equation; putting τ "behind" (first go for time t, then for time τ) gives the forward equation.

#### Formal Definition / 形式化定义

**中文解释：** 定义转移概率p_ij(t) = ℙ(X(t) = j | X(0) = i)，以及转移概率矩阵P(t) = (p_ij(t) : i, j ∈ 𝒮)。

**English explanation:** Define the transition probability p_ij(t) = ℙ(X(t) = j | X(0) = i), and the transition probability matrix P(t) = (p_ij(t) : i, j ∈ 𝒮).

**Chapman-Kolmogorov Equations / Chapman-Kolmogorov方程：**

$$p_{ij}(s+t) = \sum_{k \in \mathcal{S}} p_{ik}(s)p_{kj}(t)$$

矩阵形式：P(s+t) = P(s)P(t)

**Symbol Explanation / 符号说明：**

| Symbol | 中文含义 | English Meaning |
|--------|----------|-----------------|
| p_ij(t) | 从i出发经过时间t到达j的概率 | Probability of going from i to j in time t |
| P(t) | 转移概率矩阵 | Transition probability matrix |
| 𝒮 | 状态空间 | State space |
| s, t | 时间参数 | Time parameters |

**Forward Equation / 正向方程：**

$$P'(t) = P(t)Q, \quad P(0) = I$$

**Backward Equation / 反向方程：**

$$P'(t) = QP(t), \quad P(0) = I$$

#### Derivation of Forward Equation / 正向方程的推导

**中文解释：** 我们从Chapman-Kolmogorov方程出发，考虑一个无穷小的时间增量τ：

p_ij(t+τ) = Σ_k p_ik(t)p_kj(τ)

将p_kj(τ)用无穷小时间内的转移概率替换：
- 当k = j时：p_jj(τ) = 1 - q_jτ + o(τ)
- 当k ≠ j时：p_kj(τ) = q_kjτ + o(τ)

代入得到：
p_ij(t+τ) = p_ij(t)(1 - q_jτ) + Σ_{k≠j} p_ik(t)q_kjτ + o(τ)
= p_ij(t) + Σ_k p_ik(t)q_kjτ + o(τ)

注意这里利用了q_jj = -q_j，所以当k=j时，p_ij(t)q_jjτ = p_ij(t)(-q_j)τ，与前面的p_ij(t)(-q_jτ)项合并。

移项并除以τ：
[p_ij(t+τ) - p_ij(t)]/τ = Σ_k p_ik(t)q_kj + o(τ)/τ

令τ→0，得到正向方程：
p'_ij(t) = Σ_k p_ik(t)q_kj

矩阵形式：P'(t) = P(t)Q

**English explanation:** We start from the Chapman-Kolmogorov equation and consider an infinitesimal time increment τ:

p_ij(t+τ) = Σ_k p_ik(t)p_kj(τ)

Replace p_kj(τ) with the infinitesimal-time transition probabilities:
- When k = j: p_jj(τ) = 1 - q_jτ + o(τ)
- When k ≠ j: p_kj(τ) = q_kjτ + o(τ)

Substituting gives:
p_ij(t+τ) = p_ij(t)(1 - q_jτ) + Σ_{k≠j} p_ik(t)q_kjτ + o(τ)
= p_ij(t) + Σ_k p_ik(t)q_kjτ + o(τ)

Note that we used q_jj = -q_j, so when k=j, p_ij(t)q_jjτ = p_ij(t)(-q_j)τ, which combines with the p_ij(t)(-q_jτ) term.

Rearranging and dividing by τ:
[p_ij(t+τ) - p_ij(t)]/τ = Σ_k p_ik(t)q_kj + o(τ)/τ

Taking τ→0 gives the forward equation:
p'_ij(t) = Σ_k p_ik(t)q_kj

In matrix form: P'(t) = P(t)Q

#### Derivation of Backward Equation / 反向方程的推导

**中文解释：** 反向方程的推导与正向方程类似，但将无穷小时间增量τ放在前面：

p_ij(t+τ) = Σ_k p_ik(τ)p_kj(t)

按照同样的步骤，将p_ik(τ)用无穷小时间内的转移概率替换，最终得到：
P'(t) = QP(t)

注意正向方程和反向方程的区别：在正向方程中，Q在右边（P(t)Q）；在反向方程中，Q在左边（QP(t)）。当状态空间有限时，两者有相同的唯一解。

**English explanation:** The derivation of the backward equation is similar to the forward equation, but the infinitesimal time increment τ is placed in front:

p_ij(t+τ) = Σ_k p_ik(τ)p_kj(t)

Following the same steps, replacing p_ik(τ) with the infinitesimal-time transition probabilities, we obtain:
P'(t) = QP(t)

Note the difference between the forward and backward equations: in the forward equation, Q is on the right (P(t)Q); in the backward equation, Q is on the left (QP(t)). When the state space is finite, both have the same unique solution.

---

### 18.3 Matrix Exponential / 矩阵指数

#### Intuition / 直觉理解

**中文解释：** 在离散时间中，给定转移矩阵P，n步转移概率为P^n。在连续时间中，给定生成矩阵Q，时间t的转移概率矩阵为e^(tQ)。矩阵指数扮演了类似"连续时间版本的矩阵幂"的角色。实际上，生成矩阵Q可以被比喻为"转移矩阵P的对数"——虽然这只是一个比喻，不是严格的数学陈述。

矩阵指数通过泰勒级数定义，与普通指数函数类似，只是将标量x替换为矩阵A，将1替换为单位矩阵I。

**English explanation:** In discrete time, given the transition matrix P, the n-step transition probability is P^n. In continuous time, given the generator matrix Q, the transition probability matrix at time t is e^(tQ). The matrix exponential plays the role of a "continuous-time version of matrix powers." In fact, the generator matrix Q can be metaphorically thought of as "the logarithm of the transition matrix P" — although this is just a metaphor, not a rigorous mathematical statement.

The matrix exponential is defined through its Taylor series, similar to the ordinary exponential function, but replacing the scalar x with a matrix A and replacing 1 with the identity matrix I.

#### Formal Definition / 形式化定义

**中文解释：** 对于任意方阵A，矩阵指数定义为：

**English explanation:** For any square matrix A, the matrix exponential is defined as:

$$e^A = \exp(A) = \sum_{n=0}^{\infty} \frac{A^n}{n!} = I + A + \frac{1}{2}A^2 + \frac{1}{6}A^3 + \cdots$$

其中A^0 = I（单位矩阵）。

**Symbol Explanation / 符号说明：**

| Symbol | 中文含义 | English Meaning |
|--------|----------|-----------------|
| e^A | 矩阵A的指数 | Exponential of matrix A |
| A^n | 矩阵A的n次幂 | n-th power of matrix A |
| n! | n的阶乘 | n factorial |
| I | 单位矩阵 | Identity matrix |

#### Key Properties / 关键性质

**中文解释：** 矩阵指数具有以下重要性质，这些性质与普通指数函数类似：

**English explanation:** The matrix exponential has the following important properties, similar to the ordinary exponential function:

1. **矩阵与其指数可交换**：Ae^A = e^A A（因为A^n A = A A^n）
2. **指数性质**：(e^A)^t = e^(tA)
3. **导数性质**：d/dt e^(tA) = A e^(tA) = e^(tA) A
4. **半群性质**：e^((s+t)A) = e^(sA) e^(tA)

**中文解释：** 特别地，对于生成矩阵Q，我们有：

d/dt e^(tQ) = e^(tQ) Q = Q e^(tQ)

这与正向方程P'(t) = P(t)Q和反向方程P'(t) = QP(t)完全一致。因此，P(t) = e^(tQ)是正向和反向方程的解，且满足初始条件P(0) = e^(0Q) = I。

**English explanation:** In particular, for the generator matrix Q, we have:

d/dt e^(tQ) = e^(tQ) Q = Q e^(tQ)

This matches exactly with the forward equation P'(t) = P(t)Q and the backward equation P'(t) = QP(t). Therefore, P(t) = e^(tQ) is the solution to both the forward and backward equations, satisfying the initial condition P(0) = e^(0Q) = I.

#### Theorem 18.1 / 定理18.1

**中文解释：** 定理18.1总结了连续时间马尔可夫跳变过程的核心结果：

**English explanation:** Theorem 18.1 summarizes the core results for continuous-time Markov jump processes:

**Theorem 18.1.** Let (X(t)) be a time-homogeneous continuous-time Markov jump process with generator matrix Q. Let (P(t)) be the transition semigroup, where P(t) = (p_ij(t)) is defined by p_ij(t) = ℙ(X(t) = j | X(0) = i).

Then (P(t)) is the minimal nonnegative solution to the forward equation:
P'(t) = P(t)Q, P(0) = I

and is also the minimal nonnegative solution to the backward equation:
P'(t) = QP(t), P(0) = I

When the state space 𝒮 is finite, the forward and backward equations both have a unique solution given by the matrix exponential:
P(t) = e^(tQ)

**中文解释：** 定理中的"最小非负解"意味着在状态空间无限时，可能存在多个解，但转移半群是其中最小的非负解。当状态空间有限时，解是唯一的，就是矩阵指数。

**English explanation:** The term "minimal nonnegative solution" in the theorem means that when the state space is infinite, there may be multiple solutions, but the transition semigroup is the smallest nonnegative one. When the state space is finite, the solution is unique and is given by the matrix exponential.

---

## 🔗 Connections / 知识关联

**中文解释：** 本章内容与以下主题紧密相关：

1. **离散时间马尔可夫链（前置知识）**：连续时间马尔可夫跳变过程是离散时间马尔可夫链的自然推广。在离散时间中，我们有转移矩阵P和n步转移概率P^n；在连续时间中，我们有生成矩阵Q和转移概率矩阵P(t) = e^(tQ)。

2. **指数分布（前置知识）**：连续时间马尔可夫跳变过程的停留时间服从指数分布，这是由无记忆性决定的。

3. **跳跃链（第17章）**：连续时间马尔可夫跳变过程可以分解为跳跃链（离散时间马尔可夫链）和指数分布的停留时间。

4. **后续章节**：第19章将讨论通信类、击中时间、常返性和瞬变性，这些概念在离散时间中已经学习过，现在推广到连续时间。

**English explanation:** This chapter is closely related to the following topics:

1. **Discrete-time Markov chains (prerequisite)**: Continuous-time Markov jump processes are a natural generalization of discrete-time Markov chains. In discrete time, we have the transition matrix P and n-step transition probabilities P^n; in continuous time, we have the generator matrix Q and transition probability matrix P(t) = e^(tQ).

2. **Exponential distribution (prerequisite)**: The holding times of continuous-time Markov jump processes follow exponential distributions, determined by the memoryless property.

3. **Jump chain (Chapter 17)**: A continuous-time Markov jump process can be decomposed into a jump chain (a discrete-time Markov chain) and exponentially distributed holding times.

4. **Subsequent chapters**: Chapter 19 will discuss communicating classes, hitting times, recurrence, and transience, concepts already learned in discrete time, now generalized to continuous time.

---

## ⚠️ Common Mistakes / 常见误区

1. **混淆正向方程和反向方程**
   - **中文解释：** 正向方程是P'(t) = P(t)Q（Q在右边），反向方程是P'(t) = QP(t)（Q在左边）。很多学生容易搞混哪个是哪个。记住：正向方程中，Q在"后面"（右边），对应"先走t时间，再走τ时间"的推导方式。
   - **English explanation:** The forward equation is P'(t) = P(t)Q (Q on the right), and the backward equation is P'(t) = QP(t) (Q on the left). Many students confuse which is which. Remember: in the forward equation, Q is "behind" (on the right), corresponding to the derivation that "first go for time t, then for time τ."

2. **忽略o(τ)项**
   - **中文解释：** 在推导过程中，o(τ)项是关键的，它表示比τ更高阶的无穷小量。在取极限τ→0时，o(τ)/τ→0。忽略o(τ)项会导致推导不严谨。
   - **English explanation:** In the derivation, the o(τ) term is crucial; it represents a quantity that goes to zero faster than τ. When taking the limit τ→0, o(τ)/τ→0. Ignoring the o(τ) term would make the derivation non-rigorous.

3. **矩阵指数与标量指数的混淆**
   - **中文解释：** 虽然矩阵指数与标量指数有类似的性质，但要注意矩阵乘法不满足交换律（一般情况下AB ≠ BA）。不过，矩阵与其自身的指数是可交换的（Ae^A = e^A A），因为A^n A = A A^n。
   - **English explanation:** Although the matrix exponential has similar properties to the scalar exponential, note that matrix multiplication is not commutative in general (AB ≠ BA). However, a matrix commutes with its own exponential (Ae^A = e^A A) because A^n A = A A^n.

4. **状态空间无限时的解的唯一性**
   - **中文解释：** 定理18.1指出，当状态空间无限时，正向和反向方程可能有多个解，转移半群是"最小非负解"。但在有限状态空间下，解是唯一的，就是矩阵指数。
   - **English explanation:** Theorem 18.1 states that when the state space is infinite, the forward and backward equations may have multiple solutions, and the transition semigroup is the "minimal nonnegative solution." However, for finite state spaces, the solution is unique and is given by the matrix exponential.

5. **生成矩阵Q与转移矩阵P的关系**
   - **中文解释：** 生成矩阵Q的行和为0（每行对角元素等于负的该行非对角元素之和），而转移矩阵P的行和为1。Q类似于"连续时间版本的转移矩阵的导数"。
   - **English explanation:** The generator matrix Q has row sums equal to 0 (each diagonal element equals the negative sum of off-diagonal elements in that row), while the transition matrix P has row sums equal to 1. Q is like the "continuous-time version of the derivative of the transition matrix."

---

## ✍️ Practice / 练习

### Question 1 / 问题1

**中文解释：** 考虑一个马尔可夫跳变过程，状态空间𝒮 = {1, 2}，生成矩阵为：
Q = [[-α, α], [β, -β]]
其中α, β > 0。

(a) 写出p_11(t)的Kolmogorov正向方程，包括初始条件。
(b) 证明：p'_11(t) + (α+β)p_11(t) = β
(c) 解这个微分方程，求出p_11(t)。

**English explanation:** Consider a Markov jump process with state space 𝒮 = {1, 2} and generator matrix:
Q = [[-α, α], [β, -β]]
where α, β > 0.

(a) Write down the Kolmogorov forward equation for p_11(t), including the initial condition.
(b) Show that: p'_11(t) + (α+β)p_11(t) = β
(c) Solve this differential equation to find p_11(t).

**Hint / 提示：** 正向方程是p'_ij(t) = Σ_k p_ik(t)q_kj。对于p_11(t)，需要用到p_11(t)和p_12(t)，且p_12(t) = 1 - p_11(t)。解微分方程时，先求齐次解（假设形式为e^(λt)），再找一个特解，最后用初始条件确定常数。

### Question 2 / 问题2

**中文解释：** 继续问题1的设置。

(a) 证明：Q² = -(α+β)Q
(b) 由此写出Q^n（n≥1）用Q表示的表达式。
(c) 证明：P(t) = e^(tQ) = I + [Q/(α+β)](1 - e^(-(α+β)t))
(d) 由此求出p_11(t)，并验证与问题1(c)的结果一致。

**English explanation:** Continue with the setup of Question 1.

(a) Show that Q² = -(α+β)Q
(b) Hence, write down Q^n for n≥1 in terms of Q.
(c) Show that P(t) = e^(tQ) = I + [Q/(α+β)](1 - e^(-(α+β)t))
(d) What is p_11(t)? Check your answer agrees with Question 1(c).

**Hint / 提示：** 利用Q²与Q的关系，可以简化