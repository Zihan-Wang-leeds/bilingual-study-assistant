# Section 3: Discrete time Markov chains

> MATH2702 - 自学教材 / Self-Study Guide
> 生成时间: 2026-07-20 15:36
> 来源页: 19-21

---

# Chapter 3: Discrete Time Markov Chains / 离散时间马尔可夫链

## 📋 Section Overview / 章节概览

**中文解释：** 本章介绍离散时间马尔可夫链（Discrete Time Markov Chains）的基本理论。马尔可夫链是描述随机过程的重要工具，其核心特征是"马尔可夫性"——未来状态只依赖于当前状态，而与过去历史无关。我们将学习如何定义马尔可夫链、计算多步转移概率，以及掌握查普曼-科尔莫戈罗夫方程（Chapman-Kolmogorov equations）。这些概念在物理学、金融学、计算机科学等领域有广泛应用。

**English explanation:** This chapter introduces the fundamental theory of Discrete Time Markov Chains. Markov chains are important tools for describing stochastic processes, with the core feature being the "Markov property" — future states depend only on the current state, not on the past history. We will learn how to define Markov chains, calculate multi-step transition probabilities, and master the Chapman-Kolmogorov equations. These concepts have wide applications in physics, finance, computer science, and other fields.

---

## 🎯 Learning Objectives / 学习目标

完成本章学习后，你应该能够：

1. **定义** 时间齐次离散时间马尔可夫链，包括初始分布和转移概率
2. **计算** 多步转移概率，使用条件概率和矩阵乘法
3. **应用** 查普曼-科尔莫戈罗夫方程解决实际问题
4. **解释** 转移矩阵的性质和随机矩阵的概念
5. **分析** 两状态马尔可夫链的例子，如打印机故障模型

After completing this chapter, you should be able to:

1. **Define** time-homogeneous discrete-time Markov chains, including initial distribution and transition probabilities
2. **Calculate** multi-step transition probabilities using conditional probability and matrix multiplication
3. **Apply** the Chapman-Kolmogorov equations to solve practical problems
4. **Explain** properties of transition matrices and the concept of stochastic matrices
5. **Analyze** two-state Markov chain examples, such as the printer failure model

---

## 📚 Prerequisites / 前置知识

在学习本章之前，你应该熟悉：

- **概率论基础**：条件概率、全概率公式、随机变量
- **矩阵运算**：矩阵乘法、矩阵幂
- **随机过程基本概念**：状态空间、时间索引

Before studying this chapter, you should be familiar with:

- **Basic probability theory**: conditional probability, law of total probability, random variables
- **Matrix operations**: matrix multiplication, matrix powers
- **Basic stochastic process concepts**: state space, time index

---

## 📖 Core Content / 核心内容

### Topic 1: Definition of Time-Homogeneous Discrete-Time Markov Chains / 时间齐次离散时间马尔可夫链的定义

#### Intuition / 直觉理解

**中文解释：** 想象一个系统，它在离散的时间点（如每天、每小时）上处于某个状态。马尔可夫链描述了这个系统如何从一个状态转移到另一个状态。关键假设是：系统未来的状态只取决于它当前的状态，而不取决于它过去是如何到达当前状态的。这就像说："你的下一步只取决于你现在在哪里，而不取决于你之前走过的路。"

**English explanation:** Imagine a system that is in some state at discrete time points (e.g., every day, every hour). A Markov chain describes how this system transitions from one state to another. The key assumption is: the future state of the system depends only on its current state, not on how it arrived at that state. This is like saying: "Your next step depends only on where you are now, not on the path you took to get there."

**Real-world analogy / 现实类比：** 考虑一个简单的随机游走（simple random walk）：一个人在数轴上，每一步以概率 $p$ 向右移动一格，以概率 $q$ 向左移动一格。他下一步的位置只取决于他当前的位置，而不取决于他之前走过的具体路径。

**English analogy:** Consider a simple random walk: a person on a number line, at each step moves right with probability $p$ and left with probability $q$. Their next position depends only on their current position, not on the specific path they took to get there.

#### Formal Definition / 形式化定义

**Definition 3.1 (定义 3.1): Time-Homogeneous Discrete-Time Markov Chain / 时间齐次离散时间马尔可夫链**

**English (formal):** Let $(\lambda_i)$ be a probability distribution on a sample space $\mathcal{S}$. Let $p_{ij}$, where $i, j \in \mathcal{S}$, be such that $p_{ij} \geq 0$ for all $i, j$, and $\sum_j p_{ij} = 1$ for all $i$. Let the time index be $n = 0, 1, 2, \dots$. Then the **time homogeneous discrete time Markov process** or **Markov chain** $(X_n)$ with **initial distribution** $(\lambda_i)$ and **transition probabilities** $(p_{ij})$ is defined by

$$\mathbb{P}(X_0 = i) = \lambda_i,$$

$$\mathbb{P}(X_{n+1} = j \mid X_n = i, X_{n-1} = x_{n-1}, \dots, X_0 = x_0) = \mathbb{P}(X_{n+1} = j \mid X_n = i) = p_{ij}.$$

**中文解释：** 定义包含两个部分：

1. **初始分布 (initial distribution)** $(\lambda_i)$：描述系统在时间 $n=0$ 时处于各个状态的概率分布。$\lambda_i = \mathbb{P}(X_0 = i)$ 表示初始时刻处于状态 $i$ 的概率。

2. **转移概率 (transition probabilities)** $(p_{ij})$：描述系统从一个状态转移到另一个状态的概率。$p_{ij} = \mathbb{P}(X_{n+1} = j \mid X_n = i)$ 表示当前处于状态 $i$，下一步转移到状态 $j$ 的概率。

**关键条件：**
- $p_{ij} \geq 0$：概率非负
- $\sum_j p_{ij} = 1$：从状态 $i$ 出发，转移到所有可能状态的概率之和为 1

**时间齐次性 (time homogeneity)**：转移概率 $p_{ij}$ 不依赖于时间 $n$，即无论在哪一步，从状态 $i$ 到状态 $j$ 的转移概率都相同。

**English explanation:** The definition consists of two parts:

1. **Initial distribution** $(\lambda_i)$: Describes the probability distribution of the system being in each state at time $n=0$. $\lambda_i = \mathbb{P}(X_0 = i)$ is the probability of being in state $i$ initially.

2. **Transition probabilities** $(p_{ij})$: Describe the probability of transitioning from one state to another. $p_{ij} = \mathbb{P}(X_{n+1} = j \mid X_n = i)$ is the probability of moving to state $j$ given current state $i$.

**Key conditions:**
- $p_{ij} \geq 0$: probabilities are non-negative
- $\sum_j p_{ij} = 1$: from state $i$, the sum of probabilities of transitioning to all possible states equals 1

**Time homogeneity**: The transition probabilities $p_{ij}$ do not depend on time $n$, meaning the same transition probabilities apply at every step.

#### Symbol Explanation Table / 符号解释表

| Symbol | Meaning (English) | 含义（中文） |
|--------|-------------------|--------------|
| $\mathcal{S}$ | State space | 状态空间 |
| $X_n$ | State at time $n$ | 时间 $n$ 的状态 |
| $\lambda_i$ | Initial probability of state $i$ | 初始状态 $i$ 的概率 |
| $p_{ij}$ | Transition probability from $i$ to $j$ | 从 $i$ 到 $j$ 的转移概率 |
| $n$ | Time index | 时间索引 |

#### Example 3.1: Simple Random Walk / 简单随机游走

**中文解释：** 简单随机游走是马尔可夫链的一个基本例子。考虑一个在整数点上的随机游走：
- 状态空间 $\mathcal{S} = \mathbb{Z}$（所有整数）
- 初始分布：$\lambda_0 = 1$（从 0 开始），其他 $\lambda_i = 0$
- 转移概率：$p_{i,i+1} = p$（向右），$p_{i,i-1} = q$（向左），其他为 0

**English explanation:** The simple random walk is a basic example of a Markov chain. Consider a random walk on integer points:
- State space $\mathcal{S} = \mathbb{Z}$ (all integers)
- Initial distribution: $\lambda_0 = 1$ (start at 0), other $\lambda_i = 0$
- Transition probabilities: $p_{i,i+1} = p$ (right), $p_{i,i-1} = q$ (left), others 0

#### Transition Matrix / 转移矩阵

**中文解释：** 当状态空间有限时，我们可以将转移概率 $p_{ij}$ 写成矩阵形式，称为**转移矩阵 (transition matrix)** $\mathbf{P}$，其第 $(i,j)$ 个元素为 $p_{ij}$。条件 $\sum_j p_{ij} = 1$ 意味着矩阵的每一行元素之和为 1。这样的矩阵称为**随机矩阵 (stochastic matrix)** 或**右随机矩阵 (right stochastic matrix)**。

**English explanation:** When the state space is finite, we can write the transition probabilities $p_{ij}$ in matrix form, called the **transition matrix** $\mathbf{P}$, whose $(i,j)$-th entry is $p_{ij}$. The condition $\sum_j p_{ij} = 1$ means each row of the matrix sums to 1. Such a matrix is called a **stochastic matrix** or **right stochastic matrix**.

**Notation note / 符号说明：** 有时为了可读性，我们使用 $p(i,j)$ 代替 $p_{ij}$，特别是当下标复杂时。例如，$p(x_N, x_{N-1})$ 比 $p_{x_N x_{N-1}}$ 更容易阅读。

**English notation note:** Sometimes we write $p(i,j)$ instead of $p_{ij}$ for readability, especially when subscripts are complex. For example, $p(x_N, x_{N-1})$ is easier to read than $p_{x_N x_{N-1}}$.

#### Example 3.1 (continued): Computing Joint Probabilities / 计算联合概率

**中文解释：** 现在我们用马尔可夫链的定义来计算一些基本概率。

**问题 1：** $\mathbb{P}(X_0 = i \text{ and } X_1 = j)$ 是多少？

**解答：** 首先必须从状态 $i$ 开始，然后从 $i$ 转移到 $j$，所以
$$\mathbb{P}(X_0 = i \text{ and } X_1 = j) = \mathbb{P}(X_0 = i) \cdot \mathbb{P}(X_1 = j \mid X_0 = i) = \lambda_i p_{ij}.$$

**问题 2：** $\mathbb{P}(X_{n+2} = j \text{ and } X_{n+1} = k \mid X_n = i)$ 是多少？

**解答：** 首先必须从 $i$ 转移到 $k$，然后从 $k$ 转移到 $j$，所以
$$\mathbb{P}(X_{n+2} = j \text{ and } X_{n+1} = k \mid X_n = i) = \mathbb{P}(X_{n+1} = k \mid X_n = i) \cdot \mathbb{P}(X_{n+2} = j \mid X_{n+1} = k) = p_{ik} p_{kj}.$$

注意，$\mathbb{P}(X_{n+2} = j \mid X_{n+1} = k)$ 不依赖于 $X_n$，这正是马尔可夫性质（Markov property）的体现。

**English explanation:** Now we use the definition of Markov chains to compute some basic probabilities.

**Question 1:** What is $\mathbb{P}(X_0 = i \text{ and } X_1 = j)$?

**Solution:** First we must start at state $i$, then transition from $i$ to $j$, so
$$\mathbb{P}(X_0 = i \text{ and } X_1 = j) = \mathbb{P}(X_0 = i) \cdot \mathbb{P}(X_1 = j \mid X_0 = i) = \lambda_i p_{ij}.$$

**Question 2:** What is $\mathbb{P}(X_{n+2} = j \text{ and } X_{n+1} = k \mid X_n = i)$?

**Solution:** First we must transition from $i$ to $k$, then from $k$ to $j$, so
$$\mathbb{P}(X_{n+2} = j \text{ and } X_{n+1} = k \mid X_n = i) = \mathbb{P}(X_{n+1} = k \mid X_n = i) \cdot \mathbb{P}(X_{n+2} = j \mid X_{n+1} = k) = p_{ik} p_{kj}.$$

Note that $\mathbb{P}(X_{n+2} = j \mid X_{n+1} = k)$ does not depend on $X_n$, which is a manifestation of the Markov property.

---

### Topic 2: A Two-State Example / 两状态例子

#### Intuition / 直觉理解

**中文解释：** 考虑一个最简单的马尔可夫链，只有两个状态：0 和 1。这可以模拟许多现实场景，比如：
- 打印机：状态 0 = 故障，状态 1 = 正常工作
- 天气：状态 0 = 下雨，状态 1 = 晴天
- 机器：状态 0 = 关闭，状态 1 = 运行

**English explanation:** Consider the simplest Markov chain with only two states: 0 and 1. This can model many real-world scenarios, such as:
- Printer: state 0 = broken, state 1 = working
- Weather: state 0 = rainy, state 1 = sunny
- Machine: state 0 = off, state 1 = running

#### Formal Definition / 形式化定义

**中文解释：** 两状态马尔可夫链的状态空间为 $\mathcal{S} = \{0, 1\}$，转移矩阵为：

$$\mathbf{P} = $$
\begin{pmatrix} p_{00} & p_{01} \\ p_{10} & p_{11} \end{pmatrix}
$$ = $$
\begin{pmatrix} 1-\alpha & \alpha \\ \beta & 1-\beta \end{pmatrix}
$$$$

其中 $0 < \alpha, \beta < 1$。

**参数含义：**
- $\alpha = p_{01}$：从状态 0 转移到状态 1 的概率
- $1-\alpha = p_{00}$：从状态 0 留在状态 0 的概率
- $\beta = p_{10}$：从状态 1 转移到状态 0 的概率
- $1-\beta = p_{11}$：从状态 1 留在状态 1 的概率

**English explanation:** The two-state Markov chain has state space $\mathcal{S} = \{0, 1\}$ and transition matrix:

$$\mathbf{P} = $$
\begin{pmatrix} p_{00} & p_{01} \\ p_{10} & p_{11} \end{pmatrix}
$$ = $$
\begin{pmatrix} 1-\alpha & \alpha \\ \beta & 1-\beta \end{pmatrix}
$$$$

where $0 < \alpha, \beta < 1$.

**Parameter meanings:**
- $\alpha = p_{01}$: probability of transitioning from state 0 to state 1
- $1-\alpha = p_{00}$: probability of staying in state 0
- $\beta = p_{10}$: probability of transitioning from state 1 to state 0
- $1-\beta = p_{11}$: probability of staying in state 1

#### Transition Diagram / 转移图

**中文解释：** 我们可以用转移图（transition diagram）来直观表示马尔可夫链。图中，圆圈表示状态，箭头表示转移概率。如果 $p_{ij} = 0$，则不画箭头。

**English explanation:** We can use a transition diagram to visually represent a Markov chain. In the diagram, circles represent states and arrows represent transition probabilities. If $p_{ij} = 0$, the arrow is not drawn.

```
Figure 2: Transition diagram for the two-state Markov chain / 两状态马尔可夫链转移图

        α
   0 -----→ 1
   ↑       ↓
   |   β   |
   |       |
   1-α     1-β
   ←-------→
```

**中文解释：** 图中显示：
- 从状态 0 出发：以概率 $\alpha$ 到状态 1，以概率 $1-\alpha$ 留在状态 0
- 从状态 1 出发：以概率 $\beta$ 到状态 0，以概率 $1-\beta$ 留在状态 1

**English explanation:** The diagram shows:
- From state 0: with probability $\alpha$ go to state 1, with probability $1-\alpha$ stay in state 0
- From state 1: with probability $\beta$ go to state 0, with probability $1-\beta$ stay in state 1

#### Real-World Application: Broken Printer / 实际应用：故障打印机

**中文解释：** 考虑一个打印机模型：
- 状态 0：打印机故障（broken）
- 状态 1：打印机正常工作（working）
- 如果打印机今天故障，明天修好的概率为 $\alpha$
- 如果打印机今天正常工作，明天故障的概率为 $\beta$

**English explanation:** Consider a printer model:
- State 0: printer is broken
- State 1: printer is working
- If the printer is broken today, it will be fixed by tomorrow with probability $\alpha$
- If the printer is working today, it will break down by tomorrow with probability $\beta$

#### Example 3.2: Two-Step Transition Probability / 两步转移概率

**中文解释：** 假设打印机周一正常工作，问周三仍然正常工作的概率是多少？

**问题重述：** 设周一为第 $n$ 天，则周三为第 $n+2$ 天。我们需要计算两步转移概率：
$$p_{11}(2) = \mathbb{P}(X_{n+2} = 1 \mid X_n = 1)$$

**关键方法：** 对第一步进行条件化（conditioning on the first step）——这是本章最重要的技巧。

**解答步骤：**

**步骤 1：** 考虑周二（第一步）的所有可能状态。从状态 1 出发，周二可以是状态 0 或状态 1。

**步骤 2：** 使用全概率公式（law of total probability）：
$$p_{11}(2) = \mathbb{P}(X_{n+1} = 0 \mid X_n = 1) \cdot \mathbb{P}(X_{n+2} = 1 \mid X_{n+1} = 0, X_n = 1) + \mathbb{P}(X_{n+1} = 1 \mid X_n = 1) \cdot \mathbb{P}(X_{n+2} = 1 \mid X_{n+1} = 1, X_n = 1)$$

**步骤 3：** 利用马尔可夫性质，$\mathbb{P}(X_{n+2} = 1 \mid X_{n+1} = k, X_n = 1) = \mathbb{P}(X_{n+2} = 1 \mid X_{n+1} = k)$，所以：
$$p_{11}(2) = \mathbb{P}(X_{n+1} = 0 \mid X_n = 1) \cdot \mathbb{P}(X_{n+2} = 1 \mid X_{n+1} = 0) + \mathbb{P}(X_{n+1} = 1 \mid X_n = 1) \cdot \mathbb{P}(X_{n+2} = 1 \mid X_{n+1} = 1)$$

**步骤 4：** 代入转移概率：
$$p_{11}(2) = p_{10} \cdot p_{01} + p_{11} \cdot p_{11} = \beta \cdot \alpha + (1-\beta) \cdot (1-\beta) = \alpha\beta + (1-\beta)^2$$

**另一种理解方式：** 考虑所有长度为 2 的路径：
- 路径 1 → 0 → 1：概率为 $\beta \cdot \alpha$
- 路径 1 → 1 → 1：概率为 $(1-\beta) \cdot (1-\beta)$
将两条路径的概率相加即得结果。

**English explanation:** Suppose the printer is working on Monday. What is the probability it is also working on Wednesday?

**Problem restatement:** Let Monday be day $n$, then Wednesday is day $n+2$. We need to compute the two-step transition probability:
$$p_{11}(2) = \mathbb{P}(X_{n+2} = 1 \mid X_n = 1)$$

**Key method:** Conditioning on the first step — this is the most important technique in this entire module.

**Solution steps:**

**Step 1:** Consider all possible states on Tuesday (the first step). Starting from state 1, Tuesday can be state 0 or state 1.

**Step 2:** Use the law of total probability:
$$p_{11}(2) = \mathbb{P}(X_{n+1} = 0 \mid X_n = 1) \cdot \mathbb{P}(X_{n+2} = 1 \mid X_{n+1} = 0, X_n = 1) + \mathbb{P}(X_{n+1} = 1 \mid X_n = 1) \cdot \mathbb{P}(X_{n+2} = 1 \mid X_{n+1} = 1, X_n = 1)$$

**Step 3:** Using the Markov property, $\mathbb{P}(X_{n+2} = 1 \mid X_{n+1} = k, X_n = 1) = \mathbb{P}(X_{n+2} = 1 \mid X_{n+1} = k)$, so:
$$p_{11}(2) = \mathbb{P}(X_{n+1} = 0 \mid X_n = 1) \cdot \mathbb{P}(X_{n+2} = 1 \mid X_{n+1} = 0) + \mathbb{P}(X_{n+1} = 1 \mid X_n = 1) \cdot \mathbb{P}(X_{n+2} = 1 \mid X_{n+1} = 1)$$

**Step 4:** Substitute the transition probabilities:
$$p_{11}(2) = p_{10} \cdot p_{01} + p_{11} \cdot p_{11} = \beta \cdot \alpha + (1-\beta) \cdot (1-\beta) = \alpha\beta + (1-\beta)^2$$

**Alternative interpretation:** Consider all length-2 paths:
- Path 1 → 0 → 1: probability $\beta \cdot \alpha$
- Path 1 → 1 → 1: probability $(1-\beta) \cdot (1-\beta)$
Sum the probabilities of both paths to get the result.

---

### Topic 3: n-Step Transition Probabilities / n步转移概率

#### Intuition / 直觉理解

**中文解释：** 我们刚刚计算了两步转移概率。现在我们要推广到任意 $n$ 步的情况。核心思想是：从状态 $i$ 出发，经过 $n$ 步到达状态 $j$，可以分解为一系列中间步骤。每一步的转移概率相乘，然后对所有可能的中间路径求和。

**English explanation:** We just computed two-step transition probabilities. Now we generalize to arbitrary $n$ steps. The core idea is: starting from state $i$, reaching state $j$ after $n$ steps can be decomposed into a series of intermediate steps. Multiply the transition probabilities at each step, then sum over all possible intermediate paths.

#### Formal Definition / 形式化定义

**中文解释：** 定义 $n$ 步转移概率为：
$$p_{ij}(n) = \mathbb{P}(X_n = j \mid X_0 = i)$$

这表示从初始状态 $i$ 出发，经过 $n$ 步后到达状态 $j$ 的概率。

**English explanation:** Define the $n$-step transition probability as:
$$p_{ij}(n) = \mathbb{P}(X_n = j \mid X_0 = i)$$

This represents the probability of being in state $j$ after $n$ steps, starting from initial state $i$.

#### Theorem 3.1: n-Step Transition Probabilities / n步转移概率定理

**Theorem 3.1 (定理 3.1):** Let $(X_n)$ be a Markov chain with state space $\mathcal{S}$ and transition matrix $\mathbf{P} = (p_{ij})$. For $i, j \in \mathcal{S}$, write
$$p_{ij}(n) = \mathbb{P}(X_n = j \mid X_0 = i)$$
for the $n$-step transition probability. Then
$$p_{ij}(n) = \sum_{k_1, k_2, \dots, k_{n-1} \in \mathcal{S}} p_{i k_1} p_{k_1 k_2} \cdots p_{k_{n-2} k_{n-1}} p_{k_{n-1} j}.$$

In particular, $p_{ij}(n)$ is the $(i,j)$-th element of the matrix $\mathbf{P}^n$, and the matrix of $n$-step transition probabilities is given by $\mathbf{P}(n) = \mathbf{P}^n$.

**中文解释：** 这个定理告诉我们两件重要的事情：

1. **路径求和公式：** $n$ 步转移概率等于所有长度为 $n$ 的路径 $i \to k_1 \to k_2 \to \cdots \to k_{n-1} \to j$ 的概率之和。每条路径的概率是各步转移概率的乘积。

2. **矩阵幂公式：** $n$ 步转移概率矩阵 $\mathbf{P}(n)$ 等于转移矩阵 $\mathbf{P}$ 的 $n$ 次幂 $\mathbf{P}^n$。也就是说，$p_{ij}(n)$ 就是矩阵 $\mathbf{P}^n$ 的第 $(i,j)$ 个元素。

**English explanation:** This theorem tells us two important things:

1. **Path sum formula:** The $n$-step transition probability equals the sum of probabilities of all length-$n$ paths $i \to k_1 \to k_2 \to \cdots \to k_{n-1} \to j$. The probability of each path is the product