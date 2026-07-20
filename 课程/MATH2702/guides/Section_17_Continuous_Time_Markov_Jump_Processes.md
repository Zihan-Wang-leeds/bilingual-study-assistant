# Section 17: Continuous time Markov jump processes

> MATH2702 - 自学教材 / Self-Study Guide
> 生成时间: 2026-07-20 15:46
> 来源页: 83-85

---

# 📘 MATH2702: Continuous Time Markov Jump Processes / 连续时间马尔可夫跳跃过程

## 📋 Section Overview / 章节概览

**中文解释：** 本章节介绍连续时间马尔可夫跳跃过程（Continuous Time Markov Jump Processes）。与离散时间马尔可夫链不同，这里的"时间"是连续的，系统可以在任意时刻发生状态变化。我们将学习如何通过"跳跃链"（Jump Chain）和"停留时间"（Holding Times）来完全描述这类过程。这是随机过程理论中非常重要的一环，广泛应用于排队论、可靠性工程、生物统计等领域。

**English explanation:** This section introduces Continuous Time Markov Jump Processes (CTMJPs). Unlike discrete-time Markov chains where time is measured in steps, here "time" is continuous, and the system can change state at any moment. We will learn how to fully describe such processes using the "Jump Chain" and "Holding Times". This is a crucial part of stochastic process theory, widely applied in queueing theory, reliability engineering, biostatistics, and many other fields.

**Why this matters / 为什么重要：**
- Real-world processes often evolve in continuous time (e.g., radioactive decay, customer arrivals, chemical reactions) / 现实世界中的过程通常在连续时间中演化（如放射性衰变、顾客到达、化学反应）
- Understanding CTMJPs is essential for advanced topics like queueing theory and birth-death processes / 理解CTMJP是学习排队论和生灭过程等高级主题的基础

---

## 🎯 Learning Objectives / 学习目标

After completing this section, you should be able to / 完成本节后，你应该能够：

1. **Define** a continuous time Markov jump process in terms of its generator matrix Q and jump chain / **定义**连续时间马尔可夫跳跃过程，使用生成矩阵Q和跳跃链
2. **Calculate** the holding time distribution and transition probabilities from the generator matrix / **计算**从生成矩阵得到的停留时间分布和转移概率
3. **Construct** the jump chain transition matrix R from the generator matrix Q / **构造**从生成矩阵Q到跳跃链转移矩阵R
4. **Identify** absorbing states and understand their implications / **识别**吸收态并理解其含义
5. **Recognize** the potential for explosion in infinite state spaces / **认识**无限状态空间中可能发生的"爆炸"现象
6. **Apply** these concepts to simple examples like Poisson processes / **应用**这些概念到简单例子，如泊松过程

---

## 📚 Prerequisites / 前置知识

**中文解释：** 在学习本节之前，你需要掌握以下内容：

**English explanation:** Before studying this section, you need to master the following:

| Prerequisite / 前置知识 | Why needed / 为什么需要 |
|------------------------|------------------------|
| Discrete-time Markov chains / 离散时间马尔可夫链 | The jump chain is a discrete-time Markov chain / 跳跃链本身就是离散时间马尔可夫链 |
| Exponential distribution / 指数分布 | Holding times are exponentially distributed / 停留时间服从指数分布 |
| Memoryless property / 无记忆性 | This property justifies using exponential distribution for holding times / 这个性质证明了使用指数分布作为停留时间的合理性 |
| Theorem 14.2 (minimum of exponentials) / 定理14.2（指数分布的最小值） | Used to derive the total rate and jump probabilities / 用于推导总速率和跳跃概率 |
| Basic matrix operations / 基本矩阵运算 | Needed to work with generator matrix Q / 处理生成矩阵Q时需要 |

---

## 📖 Core Content / 核心内容

### Topic 1: Intuition and Basic Setup / 直觉与基本设定

#### Intuition / 直觉理解

**中文解释：** 想象你正在观察一个系统，它可以在多个状态之间切换。与离散时间马尔可夫链不同，这里的时间是连续的——系统可以在任何时刻发生变化。关键思想是：系统在某个状态停留一段时间（称为"停留时间"），然后突然"跳跃"到另一个状态。这个过程由两个独立的部分组成：
1. **跳到哪里**：由跳跃链决定，这是一个离散时间马尔可夫链
2. **等待多久**：由停留时间决定，这些时间必须服从指数分布

**English explanation:** Imagine you are observing a system that can switch between multiple states. Unlike discrete-time Markov chains, time here is continuous — the system can change at any moment. The key idea is: the system stays in a state for some time (called the "holding time"), then suddenly "jumps" to another state. This process is composed of two independent parts:
1. **Where to jump**: Determined by the jump chain, which is a discrete-time Markov chain
2. **How long to wait**: Determined by the holding times, which must follow an exponential distribution

**Why exponential? / 为什么是指数分布？**
- The exponential distribution is the **only** continuous distribution with the **memoryless property** / 指数分布是**唯一**具有**无记忆性**的连续分布
- Memoryless property: $P(T > s + t \mid T > s) = P(T > t)$ / 无记忆性：$P(T > s + t \mid T > s) = P(T > t)$
- This preserves the Markov property: the future depends only on the present state, not on how long we've been there / 这保持了马尔可夫性质：未来只依赖于当前状态，而不依赖于我们已经在那里停留了多久

#### Formal Definition / 形式化定义

**中文解释：** 考虑一个马尔可夫跳跃过程 $(X(t))$，其状态空间为 $\mathcal{S}$。假设我们在状态 $i \in \mathcal{S}$。我们想要跳跃到另一个状态 $j \neq i$ 的**转移速率**记为 $q_{ij} \geq 0$。这意味着，经过一个服从指数分布 $\text{Exp}(q_{ij})$ 的时间后（如果过程还没有跳跃），它将跳跃到状态 $j$。

**English explanation:** Consider a Markov jump process $(X(t))$ on a state space $\mathcal{S}$. Suppose we are at a state $i \in \mathcal{S}$. The **transition rate** at which we wish to jump to another state $j \neq i$ is written as $q_{ij} \geq 0$. This means that, after a time with an exponential distribution $\text{Exp}(q_{ij})$, if the process has not jumped yet, it will jump to state $j$.

**Conventions / 约定：**
- If $q_{ij} = 0$ for some $j \neq i$, we will never jump from $i$ to $j$ / 如果 $q_{ij} = 0$，我们永远不会从 $i$ 跳到 $j$
- If $q_{ij} = 0$ for all $j \neq i$, then $i$ is an **absorbing state** — we stay there forever / 如果对所有 $j \neq i$ 都有 $q_{ij} = 0$，那么 $i$ 是**吸收态**——我们永远停留在那里

#### Key Formula: Total Rate and Jump Probabilities / 关键公式：总速率和跳跃概率

**中文解释：** 从状态 $i$ 出发，有多个可能跳跃到的状态 $j$，每个都等待一个 $\text{Exp}(q_{ij})$ 的时间。哪一个时间会先结束，导致过程跳跃到那个状态？以及我们要等多久才会发生第一次跳跃？答案由定理14.2给出。

**English explanation:** From state $i$, there are many other states $j$ we could jump to, each waiting for a time $\text{Exp}(q_{ij})$. Which of these times will be up first, leading the process to jump to that state? And how long will it be until that first time is up and we move? The answer is given by Theorem 14.2.

**Theorem 14.2 Result / 定理14.2的结果：**

The minimum of independent exponential random variables is itself exponential, with rate equal to the sum of the rates / 独立指数随机变量的最小值本身也服从指数分布，其速率等于各速率之和：

$$q_i := \sum_{j \neq i} q_{ij}$$

The probability that we move to a particular state $j \neq i$ is / 我们跳跃到特定状态 $j \neq i$ 的概率是：

$$r_{ij} := \frac{q_{ij}}{\sum_{j \neq i} q_{ij}} = \frac{q_{ij}}{q_i}$$

**Symbol Table / 符号表：**

| Symbol / 符号 | Meaning / 含义 | Chinese / 中文 |
|---------------|----------------|----------------|
| $q_{ij}$ | Transition rate from $i$ to $j$ | 从 $i$ 到 $j$ 的转移速率 |
| $q_i$ | Total rate out of state $i$ | 离开状态 $i$ 的总速率 |
| $r_{ij}$ | Probability of jumping from $i$ to $j$ | 从 $i$ 跳跃到 $j$ 的概率 |
| $\text{Exp}(\lambda)$ | Exponential distribution with rate $\lambda$ | 速率为 $\lambda$ 的指数分布 |

**Important note / 重要说明：** If $i$ is an absorbing state, then by convention we put $r_{ii} = 1$ and $r_{ij} = 0$ for $j \neq i$ / 如果 $i$ 是吸收态，按约定我们设 $r_{ii} = 1$，且对 $j \neq i$ 设 $r_{ij} = 0$。

---

### Topic 2: The Generator Matrix Q / 生成矩阵Q

#### Formal Definition / 形式化定义

**中文解释：** 将所有转移速率 $q_{ij}$ 写成一个矩阵，称为**生成矩阵** Q。其定义如下：
- **非对角线元素**：$q_{ij}$，对于 $i \neq j$（这些是正的或0）
- **对角线元素**：$q_{ii} = -q_i = -\sum_{j \neq i} q_{ij}$（这些是负的或0）

**English explanation:** It is convenient to write all the transition rates $q_{ij}$ down in a **generator matrix** Q defined as follows:
- **Off-diagonal entries**: $q_{ij}$, for $i \neq j$ (these are positive or 0)
- **Diagonal entries**: $q_{ii} = -q_i = -\sum_{j \neq i} q_{ij}$ (these are negative or 0)

**Key property / 关键性质：** Each row sums to 0 / 每一行之和为0：
$$\sum_j q_{ij} = 0 \quad \text{for all } i$$

**Why "generator"? / 为什么叫"生成矩阵"？**
- It "generates" the process — from Q we can derive all properties of the process / 它"生成"了过程——从Q我们可以推导出过程的所有性质
- It plays a role similar to the transition matrix in discrete time / 它扮演的角色类似于离散时间中的转移矩阵

#### Structure of Q / Q的结构

**中文解释：** 生成矩阵Q具有以下结构特点：
- 非对角线元素 $q_{ij} \geq 0$（$i \neq j$）
- 对角线元素 $q_{ii} \leq 0$
- 每一行之和为0

**English explanation:** The generator matrix Q has the following structural characteristics:
- Off-diagonal entries $q_{ij} \geq 0$ ($i \neq j$)
- Diagonal entries $q_{ii} \leq 0$
- Each row sums to 0

**Example / 示例：**
For a 3-state system with rates as shown in the diagram on page 83:

$$Q = $$
\begin{pmatrix}
-2 & 2 & 0 \\
1 & -3 & 2 \\
0 & 1 & -1
\end{pmatrix}
$$$$

**Verification / 验证：**
- Row 1: $-2 + 2 + 0 = 0$ ✓
- Row 2: $1 + (-3) + 2 = 0$ ✓
- Row 3: $0 + 1 + (-1) = 0$ ✓

---

### Topic 3: The Jump Chain (Yₙ) / 跳跃链(Yₙ)

#### Definition / 定义

**中文解释：** 跳跃链 $(Y_n)$ 是与连续时间过程 $(X(t))$ 相关联的离散时间马尔可夫链。它记录的是过程在每次跳跃后所处的状态，而不考虑跳跃发生的时间。具体定义如下：
- $Y_0 = X(0)$（从相同的初始状态开始）
- $Y_n =$ 第 $n$ 次跳跃后 $(X(t))$ 所处的状态

**English explanation:** The jump chain $(Y_n)$ is a discrete-time Markov chain associated with the continuous-time process $(X(t))$. It records the state the process is in after each jump, without considering when the jumps occur. Specifically:
- $Y_0 = X(0)$ (starts from the same initial state)
- $Y_n =$ state of $X(t)$ just after the $n$th jump

#### Transition Matrix R / 转移矩阵R

**中文解释：** 跳跃链的转移矩阵 R 由以下方式定义：
- 对于 $q_i \neq 0$ 的状态 $i$：$r_{ij} = q_{ij}/q_i$ 对于 $j \neq i$，且 $r_{ii} = 0$
- 对于 $q_i = 0$ 的状态 $i$（吸收态）：$r_{ij} = 0$ 对于 $j \neq i$，且 $r_{ii} = 1$

**English explanation:** The transition matrix R of the jump chain is defined as follows:
- For states $i$ with $q_i \neq 0$: $r_{ij} = q_{ij}/q_i$ for $j \neq i$, and $r_{ii} = 0$
- For states $i$ with $q_i = 0$ (absorbing states): $r_{ij} = 0$ for $j \neq i$, and $r_{ii} = 1$

**Important property / 重要性质：** The jump chain cannot move from a state to itself (unless it's absorbing) / 跳跃链不能从状态移动到自身（除非是吸收态）。

**Example / 示例：**
For the same 3-state system:

$$R = $$
\begin{pmatrix}
0 & 1 & 0 \\
\frac{1}{3} & 0 & \frac{2}{3} \\
0 & 1 & 0
\end{pmatrix}
$$$$

**Verification / 验证：**
- From state 1: $q_1 = 2$, so $r_{12} = 2/2 = 1$, $r_{13} = 0/2 = 0$ ✓
- From state 2: $q_2 = 3$, so $r_{21} = 1/3$, $r_{23} = 2/3$ ✓
- From state 3: $q_3 = 1$, so $r_{32} = 1/1 = 1$, $r_{31} = 0/1 = 0$ ✓

---

### Topic 4: Holding Times / 停留时间

#### Distribution / 分布

**中文解释：** 一旦我们知道跳跃链将如何移动，我们就知道下一个停留时间的分布。从状态 $j$ 出发，停留时间服从指数分布 $\text{Exp}(q_j)$，其中 $q_j = -q_{jj} = \sum_{k \neq j} q_{jk}$。

**English explanation:** Once we know where the jump process will move, we then know what the next holding time will be: from state $j$, the holding time will be $\text{Exp}(q_j)$, where $q_j = -q_{jj} = \sum_{k \neq j} q_{jk}$.

#### Conditional Independence / 条件独立性

**中文解释：** 给定跳跃链 $(Y_n)$，停留时间 $T_1, T_2, \ldots$ 是条件独立的。这意味着，如果我们知道每次跳跃后到达的状态，那么每次停留的时间长度是相互独立的。

**English explanation:** Given the jump chain $(Y_n)$, the holding times $T_1, T_2, \ldots$ are conditionally independent. This means that if we know which state we arrive at after each jump, then the lengths of each stay are independent of each other.

#### Jump Times / 跳跃时间

**中文解释：** 第 $n$ 次跳跃发生的时间 $J_n$ 是前 $n$ 个停留时间的总和：
$$J_n = T_1 + T_2 + \cdots + T_n$$

**English explanation:** The time of the $n$th jump $J_n$ is the sum of the first $n$ holding times:
$$J_n = T_1 + T_2 + \cdots + T_n$$

---

### Topic 5: Complete Definition of the Process / 过程的完整定义

#### Definition 17.1 / 定义17.1

**中文解释：** 现在我们可以给出马尔可夫跳跃过程的完整形式化定义。它由三个部分组成：初始分布、生成矩阵和跳跃链。

**English explanation:** Now we can give the complete formal definition of a Markov jump process. It consists of three parts: the initial distribution, the generator matrix, and the jump chain.

**Definition 17.1 (Formal Definition / 形式化定义):**

1. **Let $\mathcal{S}$ be a set, and $\lambda$ a distribution on $\mathcal{S}$** / 设 $\mathcal{S}$ 是一个集合，$\lambda$ 是 $\mathcal{S}$ 上的一个分布
   - $\lambda$ gives the initial probabilities: $P(X(0) = i) = \lambda_i$ / $\lambda$ 给出初始概率：$P(X(0) = i) = \lambda_i$

2. **Let $Q = (q_{ij} : i, j \in \mathcal{S})$ be a matrix where $q_{ij} \geq 0$ for $i \neq j$ and $\sum_j q_{ij} = 0$ for all $i$, and write $q_i = -q_{ii} = \sum_{j \neq i} q_{ij}$** / 设 $Q = (q_{ij} : i, j \in \mathcal{S})$ 是一个矩阵，其中对于 $i \neq j$ 有 $q_{ij} \geq 0$，且对所有 $i$ 有 $\sum_j q_{ij} = 0$，并记 $q_i = -q_{ii} = \sum_{j \neq i} q_{ij}$

3. **Define $R = (r_{ij} : i, j \in \mathcal{S})$ as follows** / 定义 $R = (r_{ij} : i, j \in \mathcal{S})$ 如下：
   - For $i$ such that $q_i \neq 0$: $r_{ij} = q_{ij}/q_i$ for $j \neq i$, and $r_{ii} = 0$
   - For $i$ such that $q_i = 0$: $r_{ij} = 0$ for $j \neq i$, and $r_{ii} = 1$

4. **The jump chain $(Y_n)$** is the discrete-time Markov chain on $\mathcal{S}$ with initial distribution $\lambda$ and transition matrix $R$ / **跳跃链 $(Y_n)$** 是 $\mathcal{S}$ 上的离散时间马尔可夫链，具有初始分布 $\lambda$ 和转移矩阵 $R$

5. **The holding times $T_1, T_2, \ldots$** have distribution $T_n \sim \text{Exp}(q_{Y_{n-1}})$, and are conditionally independent given $(Y_n)$ / **停留时间 $T_1, T_2, \ldots$** 服从分布 $T_n \sim \text{Exp}(q_{Y_{n-1}})$，并且在给定 $(Y_n)$ 的条件下相互独立

6. **The jump times are $J_n = T_1 + T_2 + \cdots + T_n$** / **跳跃时间**为 $J_n = T_1 + T_2 + \cdots + T_n$

7. **Then the Markov jump process $(X(t))$ is defined by** / **那么马尔可夫跳跃过程 $(X(t))$ 定义为**：
   $$X(t) = \begin{cases}
   Y_0 & \text{for } t < J_1 \\
   Y_n & \text{for } J_n \leq t < J_{n+1}
   \end{cases}$$

**Intuitive interpretation / 直观解释：**
- Before the first jump ($t < J_1$), we are in the initial state $Y_0$ / 在第一次跳跃之前，我们处于初始状态 $Y_0$
- Between the $n$th and $(n+1)$th jumps ($J_n \leq t < J_{n+1}$), we are in state $Y_n$ / 在第 $n$ 次和第 $n+1$ 次跳跃之间，我们处于状态 $Y_n$

---

### Topic 6: Examples / 例题

#### Example 17.1: Three-State System / 三状态系统

**中文解释：** 考虑一个状态空间为 $\mathcal{S} = \{1, 2, 3\}$ 的马尔可夫跳跃过程，其转移速率如下图所示。

**English explanation:** Consider a Markov jump process on a state space $\mathcal{S} = \{1, 2, 3\}$ with transition rates as illustrated in the following transition rate diagram.

**Transition Rate Diagram / 转移速率图：**
```
1 ←→ 2 (rates: 2 from 1→2, 1 from 2→1)
2 → 3 (rate: 2)
3 → 2 (rate: 1)
```

**Step-by-step solution / 逐步求解：**

**Step 1: Write the generator matrix Q / 写出生成矩阵Q**

$$Q = $$
\begin{pmatrix}
-2 & 2 & 0 \\
1 & -3 & 2 \\
0 & 1 & -1
\end{pmatrix}
$$$$

**Explanation / 解释：**
- $q_{12} = 2$ (rate from 1 to 2), $q_{13} = 0$ (no direct transition from 1 to 3)
- $q_{21} = 1$, $q_{23} = 2$
- $q_{31} = 0$, $q_{32} = 1$
- Diagonal: $q_{11} = -(2+0) = -2$, $q_{22} = -(1+2) = -3$, $q_{33} = -(0+1) = -1$

**Step 2: Calculate the total rates / 计算总速率**
- $q_1 = -q_{11} = 2$
- $q_2 = -q_{22} = 3$
- $q_3 = -q_{33} = 1$

**Step 3: Write the jump chain transition matrix R / 写出跳跃链转移矩阵R**

$$R = $$
\begin{pmatrix}
0 & 1 & 0 \\
\frac{1}{3} & 0 & \frac{2}{3} \\
0 & 1 & 0
\end{pmatrix}
$$$$

**Explanation / 解释：**
- From state 1: $r_{12} = 2/2 = 1$, $r_{11} = 0$, $r_{13} = 0$
- From state 2: $r_{21} = 1/3$, $r_{23} = 2/3$, $r_{22} = 0$
- From state 3: $r_{32} = 1/1 = 1$, $r_{31} = 0$, $r_{33} = 0$

**Step 4: Interpret the process / 解释过程**

**中文解释：** 从状态2开始，我们等待一个服从 $\text{Exp}(3)$ 分布的停留时间 $T_1$。然后以概率 $1/3$ 移动到状态1，以概率 $2/3$ 移动到状态3。假设我们移动到状态1，那么我们在状态1停留一个服从 $\text{Exp}(2)$ 分布的时间，然后以概率1跳回状态2。如此继续。

**English explanation:** Starting from state 2, we wait for a holding time $T_1 \sim \text{Exp}(3)$. We then move to state 1 with probability $1/3$ and to state 3 with probability $2/3$. Suppose we move to state 1. Then we stay in state 1 for a time $\text{Exp}(2)$, before moving with certainty back to state 2. And so on.

**Key insight / 关键洞察：**
- The holding time depends on the **current state** / 停留时间取决于**当前状态**
- The jump probabilities depend on the **relative rates** / 跳跃概率取决于**相对速率**
- The process alternates between states, with different average waiting times / 过程在状态之间交替，具有不同的平均等待时间

---

#### Example 17.2: System with an Absorbing State / 含有吸收态的系统

**中文解释：** 考虑一个状态空间为 $\mathcal{S} = \{A, B, C\}$ 的马尔可夫跳跃过程，其中状态C是吸收态。

**English explanation:** Consider a Markov jump process with state space $\mathcal{S} = \{A, B, C\}$, where state C is an absorbing state.

**Transition Rate Diagram / 转移速率图：**
```
A → B (rate: q_AB)
A → C (rate: q_AC)
B → A (rate: q_BA)
B → C (rate: q_BC)
C is absorbing (no outgoing arrows)
```

**Step-by-step solution / 逐步求解：**

**Step 1: Write the generator matrix Q / 写出生成矩阵Q**

$$Q = $$
\begin{pmatrix}
-q_A & q_{AB} & q_{AC} \\
q_{BA} & -q_B & q_{BC} \\
0 & 0 & 0
\end{pmatrix}
$$$$

where / 其中：
- $q_A = q_{AB} + q_{AC}$
- $q_B = q_{BA} + q_{BC}$

**Explanation / 解释：**
- Row A: diagonal is $-(q_{AB} + q_{AC}) = -q_A$, off-diagonals are $q_{AB}$ and $q_{AC}$
- Row B: diagonal is $-(q_{BA} + q_{BC}) = -q_B$, off-diagonals are $q_{BA}$ and $q_{BC}$
- Row C: all zeros (absorbing state — no outgoing transitions) / 全为零（吸收态——没有离开的转移）

**Step 2: Write the jump chain transition matrix R / 写出跳跃链转移矩阵R**

$$R = $$
\begin{pmatrix}
0 & q_{AB}/q_A & q_{AC}/q_A \\
q_{BA}/q_B & 0 & q_{BC}/q_B \\
0 & 0 & 1
\end{pmatrix}
$$$$

**Explanation / 解释：**
- From A: $r_{AB} = q_{AB}/