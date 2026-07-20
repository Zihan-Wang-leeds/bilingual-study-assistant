# Section 7: Hitting times

> MATH2702 - 自学教材 / Self-Study Guide
> 生成时间: 2026-07-20 15:39
> 来源页: 40-43

---

# MATH2702: Markov Chains and Random Processes

## Section 7: Hitting Times / 击中时间

---

### 📋 Section Overview / 章节概览

**中文解释：**
本章节研究马尔可夫链中一个核心问题：从某个起始状态出发，需要多长时间才能首次到达某个目标状态或状态集合？以及到达的概率是多少？这些问题在赌博破产问题、排队论、网络分析等领域都有重要应用。我们将学习如何通过"首次步条件化"（conditioning on the first step）的方法来求解击中概率和期望击中时间，并特别分析简单随机游走的返回性质。

**English explanation:**
This section investigates a core question in Markov chains: starting from a given state, how long does it take to first reach a target state or set of states? And what is the probability of ever reaching it? These questions have important applications in gambler's ruin problems, queueing theory, network analysis, and many other fields. We will learn how to find hitting probabilities and expected hitting times using the method of "conditioning on the first step," and specifically analyze the return properties of simple random walks.

---

### 🎯 Learning Objectives / 学习目标

完成本章学习后，你应该能够：

1. **定义** 击中概率、期望击中时间、返回概率和期望返回时间，并理解它们之间的区别
2. **应用** 首次步条件化方法建立关于击中概率和期望击中时间的方程
3. **求解** 由条件化方法得到的线性方程组，计算具体的击中概率和期望击中时间
4. **分析** 简单随机游走的击中概率和返回性质，理解对称与非对称随机游走的本质区别
5. **解释** 为什么对称随机游走的返回概率为1但期望返回时间为无穷大

**English objectives:**
After completing this section, you should be able to:
1. **Define** hitting probability, expected hitting time, return probability, and expected return time, and understand their differences
2. **Apply** the conditioning on the first step method to set up equations for hitting probabilities and expected hitting times
3. **Solve** the resulting systems of linear equations to compute specific hitting probabilities and expected hitting times
4. **Analyze** the hitting probabilities and return properties of simple random walks, understanding the fundamental difference between symmetric and asymmetric walks
5. **Explain** why the symmetric random walk has return probability 1 but infinite expected return time

---

### 📚 Prerequisites / 前置知识

在开始本章之前，请确保你熟悉以下内容：

**中文解释：**
- **马尔可夫链的基本概念**：状态空间、转移概率、转移矩阵
- **条件概率和全概率公式**：特别是条件化于第一次转移
- **条件期望**：理解条件期望的含义和计算方法
- **简单随机游走**：定义和基本性质
- **赌博破产问题**：第3节的内容，因为本章是这些思想的推广

**English explanation:**
- **Basic concepts of Markov chains**: state space, transition probabilities, transition matrix
- **Conditional probability and law of total probability**: especially conditioning on the first step
- **Conditional expectation**: understanding its meaning and computation
- **Simple random walk**: definition and basic properties
- **Gambler's ruin problem**: content from Section 3, as this section generalizes those ideas

---

### 📖 Core Content / 核心内容

---

#### Topic 7.1: Hitting Probabilities and Expected Hitting Times / 击中概率与期望击中时间

##### Intuition / 直觉理解

**中文解释：**
想象你在一个城市的地铁系统中随机游走。你想知道从当前车站出发，最终到达某个特定车站（比如市中心）的概率有多大？以及平均需要多少站才能到达？这就是"击中概率"和"期望击中时间"要回答的问题。

关键思想是：我们可以通过"条件化于第一步"来建立方程。也就是说，我们考虑第一步走到哪里，然后利用马尔可夫性质（未来只依赖于当前状态），将问题转化为从新状态出发的类似问题。这样我们就得到了一个关于未知击中概率的方程（或方程组）。

**English explanation:**
Imagine you're randomly wandering in a city's subway system. You want to know: starting from your current station, what's the probability of eventually reaching a specific station (like the city center)? And on average, how many stops will it take? These are the questions that "hitting probability" and "expected hitting time" answer.

The key idea is: we can set up equations by "conditioning on the first step." That is, we consider where the first step takes us, and then use the Markov property (the future depends only on the current state) to transform the problem into a similar problem starting from the new state. This gives us an equation (or system of equations) for the unknown hitting probability.

##### Formal Definition / 形式化定义

**Definition 7.1 (Hitting Time / 击中时间).** Let $(X_n)$ be a Markov chain on state space $\mathcal{S}$. Let $H_A$ be a random variable representing the hitting time to hit the set $A \subset \mathcal{S}$, given by

$$H_A = \min\{n \in \{0, 1, 2, \ldots\} : X_n \in A\}$$

**中文解释：**
$H_A$ 是首次进入集合 $A$ 的时间（步数）。如果链条永远不进入 $A$，则 $H_A = \infty$。最常见的特殊情况是 $A = \{j\}$ 只包含一个状态，此时记 $H_j = \min\{n \in \{0, 1, 2, \ldots\} : X_n = j\}$。

**English explanation:**
$H_A$ is the first time (number of steps) the chain enters set $A$. If the chain never enters $A$, then $H_A = \infty$. The most common special case is $A = \{j\}$ containing a single state, in which case we write $H_j = \min\{n \in \{0, 1, 2, \ldots\} : X_n = j\}$.

**Definition (Hitting Probability / 击中概率).** The hitting probability $h_i^A$ of set $A$ starting from state $i$ is

$$h_i^A = \mathbb{P}(X_n \in A \text{ for some } n \geq 0 \mid X_0 = i) = \mathbb{P}(H_A < \infty \mid X_0 = i)$$

**中文解释：**
$h_i^A$ 是从状态 $i$ 出发，最终会进入集合 $A$ 的概率。当 $A = \{j\}$ 时，记 $h_{ij}$ 为从 $i$ 出发击中 $j$ 的概率。

**English explanation:**
$h_i^A$ is the probability that, starting from state $i$, the chain will eventually enter set $A$. When $A = \{j\}$, we write $h_{ij}$ for the probability of hitting $j$ starting from $i$.

**Definition (Expected Hitting Time / 期望击中时间).** The expected hitting time $\eta_i^A$ of set $A$ starting from state $i$ is

$$\eta_i^A = \mathbb{E}(H_A \mid X_0 = i)$$

**中文解释：**
$\eta_i^A$ 是从状态 $i$ 出发，首次进入集合 $A$ 所需的平均步数。显然，只有当 $h_i^A = 1$（即一定能击中）时，$\eta_i^A$ 才可能是有限的。

**English explanation:**
$\eta_i^A$ is the expected number of steps to first enter set $A$, starting from state $i$. Clearly, $\eta_i^A$ can only be finite if $h_i^A = 1$ (i.e., hitting is certain).

**Summary Table / 符号总结表：**

| Symbol | Meaning (English) | 含义（中文） |
|--------|-------------------|--------------|
| $H_A$ | Hitting time of set $A$ | 击中集合 $A$ 的时间 |
| $H_j$ | Hitting time of state $j$ | 击中状态 $j$ 的时间 |
| $h_i^A$ | Hitting probability of $A$ from $i$ | 从 $i$ 出发击中 $A$ 的概率 |
| $h_{ij}$ | Hitting probability of $j$ from $i$ | 从 $i$ 出发击中 $j$ 的概率 |
| $\eta_i^A$ | Expected hitting time of $A$ from $i$ | 从 $i$ 出发击中 $A$ 的期望时间 |
| $\eta_{ij}$ | Expected hitting time of $j$ from $i$ | 从 $i$ 出发击中 $j$ 的期望时间 |

##### Key Properties / 关键性质

**中文解释：**
击中概率和期望击中时间可以通过"条件化于第一步"来求解。基本思想是：从状态 $i$ 出发，第一步走到某个状态 $j$ 的概率是 $p_{ij}$，然后从 $j$ 出发的问题与原问题结构相同。利用全概率公式，我们可以建立方程。

**English explanation:**
Hitting probabilities and expected hitting times can be found by "conditioning on the first step." The basic idea is: starting from state $i$, the first step goes to state $j$ with probability $p_{ij}$, and then the problem from $j$ has the same structure as the original problem. Using the law of total probability, we can set up equations.

**General Formula for Hitting Probabilities / 击中概率的一般公式：**

$$h_i^A = \begin{cases}
\sum_{j \in \mathcal{S}} p_{ij} h_j^A & \text{if } i \notin A \\
1 & \text{if } i \in A
\end{cases}$$

**中文解释：**
- 如果 $i \notin A$（起始状态不在目标集合中），则 $h_i^A = \sum_j p_{ij} h_j^A$。这意味着：第一步走到 $j$ 的概率乘以从 $j$ 出发击中 $A$ 的概率，对所有可能的 $j$ 求和。
- 如果 $i \in A$（起始状态已经在目标集合中），则 $h_i^A = 1$，因为我们已经"击中"了。

**Important Note / 重要说明：** 如果这些方程有多个解，那么击中概率实际上是最小的非负解（the smallest non-negative solution）。

**English explanation:**
- If $i \notin A$ (starting state is not in the target set), then $h_i^A = \sum_j p_{ij} h_j^A$. This means: sum over all possible $j$ of (probability of first step to $j$) × (probability of hitting $A$ from $j$).
- If $i \in A$ (starting state is already in the target set), then $h_i^A = 1$, because we have already "hit" it.

**General Formula for Expected Hitting Times / 期望击中时间的一般公式：**

$$\eta_i^A = \begin{cases}
1 + \sum_{j \in \mathcal{S}} p_{ij} \eta_j^A & \text{if } i \notin A \\
0 & \text{if } i \in A
\end{cases}$$

**中文解释：**
- 如果 $i \notin A$，则 $\eta_i^A = 1 + \sum_j p_{ij} \eta_j^A$。这里的"1"代表第一步花费的时间，然后加上从新状态出发的期望剩余时间。
- 如果 $i \in A$，则 $\eta_i^A = 0$，因为我们已经到达了。

**English explanation:**
- If $i \notin A$, then $\eta_i^A = 1 + \sum_j p_{ij} \eta_j^A$. The "1" accounts for the time taken by the first step, plus the expected remaining time from the new state.
- If $i \in A$, then $\eta_i^A = 0$, because we have already arrived.

##### Worked Example 7.1: Hitting Probability / 例题7.1：击中概率

**Problem / 问题：** Consider a Markov chain with transition matrix

$$P = $$
\begin{pmatrix}
\frac{1}{5} & \frac{1}{5} & \frac{1}{5} & \frac{2}{5} \\
0 & 1 & 0 & 0 \\
\frac{1}{2} & 0 & \frac{1}{2} & 0 \\
0 & 0 & 0 & 1
\end{pmatrix}
$$$$

Calculate the probability that the chain is absorbed at state 2 when started from state 1. / 计算从状态1出发，链条最终被状态2吸收的概率。

**Solution / 解答：**

**Step 1: Identify what we need / 第一步：确定我们需要什么**

We need $h_{12}$, the hitting probability of state 2 starting from state 1. / 我们需要 $h_{12}$，即从状态1出发击中状态2的概率。

**Step 2: Set up equations by conditioning on the first step / 第二步：通过条件化于第一步建立方程**

**中文解释：**
从状态1出发，第一步有四种可能：
- 以概率 $p_{11} = 1/5$ 留在状态1，然后问题重新开始，击中概率仍为 $h_{12}$
- 以概率 $p_{12} = 1/5$ 到达状态2，此时已经击中，概率为 $h_{22}$
- 以概率 $p_{13} = 1/5$ 到达状态3，然后从状态3出发，击中概率为 $h_{32}$
- 以概率 $p_{14} = 2/5$ 到达状态4，然后从状态4出发，击中概率为 $h_{42}$

**English explanation:**
Starting from state 1, the first step has four possibilities:
- With probability $p_{11} = 1/5$, stay at state 1, then the problem restarts with hitting probability $h_{12}$
- With probability $p_{12} = 1/5$, reach state 2, already hit, probability $h_{22}$
- With probability $p_{13} = 1/5$, reach state 3, then hitting probability from state 3 is $h_{32}$
- With probability $p_{14} = 2/5$, reach state 4, then hitting probability from state 4 is $h_{42}$

Using the law of total probability / 使用全概率公式：

$$h_{12} = p_{11}h_{12} + p_{12}h_{22} + p_{13}h_{32} + p_{14}h_{42}$$

$$h_{12} = \frac{1}{5}h_{12} + \frac{1}{5}h_{22} + \frac{1}{5}h_{32} + \frac{2}{5}h_{42}$$

**Step 3: Find the other hitting probabilities / 第三步：找出其他击中概率**

**中文解释：**
我们需要 $h_{22}$、$h_{32}$ 和 $h_{42}$。

- $h_{22} = 1$：因为状态2是吸收态，从状态2出发已经"在"状态2了。
- $h_{42} = 0$：因为状态4是吸收态，且状态4不会转移到状态2（从转移矩阵看，状态4只能留在状态4）。
- $h_{32}$：需要从状态3出发，条件化于第一步。

**English explanation:**
We need $h_{22}$, $h_{32}$, and $h_{42}$.

- $h_{22} = 1$: Because state 2 is absorbing, starting from state 2 we are "already there."
- $h_{42} = 0$: Because state 4 is absorbing and state 4 cannot transition to state 2 (from the transition matrix, state 4 only stays at state 4).
- $h_{32}$: Need to condition on the first step from state 3.

For $h_{32}$ / 对于 $h_{32}$：

$$h_{32} = p_{32}h_{22} + p_{34}h_{42} = \frac{1}{2}h_{22} + \frac{1}{2}h_{42} = \frac{1}{2} \times 1 + \frac{1}{2} \times 0 = \frac{1}{2}$$

**Step 4: Substitute back / 第四步：代入回原方程**

**中文解释：**
将 $h_{22} = 1$，$h_{32} = 1/2$，$h_{42} = 0$ 代入方程：

$$h_{12} = \frac{1}{5}h_{12} + \frac{1}{5} \times 1 + \frac{1}{5} \times \frac{1}{2} + \frac{2}{5} \times 0$$

$$h_{12} = \frac{1}{5}h_{12} + \frac{1}{5} + \frac{1}{10}$$

$$h_{12} = \frac{1}{5}h_{12} + \frac{3}{10}$$

**English explanation:**
Substituting $h_{22} = 1$, $h_{32} = 1/2$, $h_{42} = 0$ into the equation:

$$h_{12} = \frac{1}{5}h_{12} + \frac{1}{5} \times 1 + \frac{1}{5} \times \frac{1}{2} + \frac{2}{5} \times 0$$

$$h_{12} = \frac{1}{5}h_{12} + \frac{1}{5} + \frac{1}{10}$$

$$h_{12} = \frac{1}{5}h_{12} + \frac{3}{10}$$

**Step 5: Solve for $h_{12}$ / 第五步：解出 $h_{12}$**

$$h_{12} - \frac{1}{5}h_{12} = \frac{3}{10}$$

$$\frac{4}{5}h_{12} = \frac{3}{10}$$

$$h_{12} = \frac{3}{10} \times \frac{5}{4} = \frac{15}{40} = \frac{3}{8}$$

**Answer / 答案：** $h_{12} = \frac{3}{8}$

**中文解释：**
从状态1出发，最终被状态2吸收的概率是3/8。注意这个概率小于1，因为有可能被状态4吸收（概率为5/8）。

**English explanation:**
Starting from state 1, the probability of eventually being absorbed at state 2 is 3/8. Note this probability is less than 1, because there is a possibility of being absorbed at state 4 (probability 5/8).

##### Worked Example 7.2: Expected Hitting Time / 例题7.2：期望击中时间

**Problem / 问题：** Consider the simple no-claims discount chain from Lecture 5, with transition matrix

$$P = $$
\begin{pmatrix}
\frac{1}{4} & \frac{3}{4} & 0 \\
\frac{1}{4} & 0 & \frac{3}{4} \\
0 & \frac{1}{4} & \frac{3}{4}
\end{pmatrix}
$$$$

Given we start in state 1 (no discount), find the expected amount of time until we reach state 3 (50% discount). / 假设我们从状态1（无折扣）出发，求到达状态3（50%折扣）的期望时间。

**Solution / 解答：**

**Step 1: Identify what we need / 第一步：确定我们需要什么**

We need $\eta_{13}$, the expected hitting time of state 3 starting from state 1. / 我们需要 $\eta_{13}$，即从状态1出发击中状态3的期望时间。

**Step 2: Set up equations / 第二步：建立方程**

**中文解释：**
首先，显然 $\eta_{33} = 0$，因为从状态3出发已经到达了目标。对于其他状态，我们条件化于第一步。

**English explanation:**
First, clearly $\eta_{33} = 0$, because starting from state 3 we have already reached the target. For other states, we condition on the first step.

For $\eta_{13}$ / 对于 $\eta_{13}$：

$$\eta_{13} = 1 + p_{11}\eta_{13} + p_{12}\eta_{23} + p_{13}\eta_{33}$$

$$\eta_{13} = 1 + \frac{1}{4}\eta_{13} + \frac{3}{4}\eta_{23} + 0 \times \eta_{33}$$

$$\eta_{13} = 1 + \frac{1}{4}\eta_{13} + \frac{3}{4}\eta_{23}$$

Rearranging / 整理：

$$\eta_{13} - \frac{1}{4}\eta_{13} = 1 + \frac{3}{4}\eta_{23}$$

$$\frac{3}{4}\eta_{13} - \frac{3}{4}\eta_{23} = 1$$

For $\eta_{23}$ / 对于 $\eta_{23}$：

$$\eta_{23} = 1 + p_{21}\eta_{13} + p_{22}\eta_{23} + p_{23}\eta_{33}$$

$$\eta_{23} = 1 + \frac{1}{4}\eta_{13} + 0 \times \eta_{23} + \frac{3}{4} \times 0$$

$$\eta_{23} = 1 + \frac{1}{4}\eta_{13}$$

Rearranging / 整理：

$$-\frac{1}{4}\eta_{13} + \eta_{23} = 1$$

**Step 3: Solve the system of equations / 第三步：解方程组**

**中文解释：**
我们有两个方程：
(1) $\frac{3}{4}\eta_{13} - \frac{3}{4}\eta_{23} = 1$
(2) $-\frac{1}{4}\eta_{13} + \eta_{23} = 1$

我们可以用代入法或消元法。这里用消元法：将方程(2)乘以3/4，然后加到方程(1)上。

**English explanation:**
We have two equations:
(1) $\frac{3}{4}\eta_{13} - \frac{3}{4}\eta_{23} = 1$
(2) $-\frac{1}{4}\eta_{13} + \eta_{23} = 1$

We can use substitution or elimination. Here we use elimination: multiply equation (2) by 3/4 and add to equation (1).

Equation (2) × 3/4 / 方程(2)乘以3/4：

$$-\frac{3}{16}\eta_{13} + \frac{3}{4}\eta_{23} = \frac{3}{4}$$

Add to equation (1) / 加到方程(1)：

$$\left(\frac{3}{4} - \frac{3}{16}\right)\eta_{13} + \left(-\frac{3}{4} + \frac{3}{4}\right)\eta_{23} = 1 + \frac{3}{4}$$

$$\left(\frac{12}{16} - \frac{3}{16}\right)\eta_{13} = \frac{7}{4}$$

$$\frac{9}{16}\eta_{13} = \frac{7}{4} = \frac{28}{16}$$

$$\eta_{13} = \frac{28}{9} \approx 3.11$$

**Answer / 答案：** $\eta_{13} = \frac{28}{9} \approx 3.11$

**中文解释：**
从状态1出发，平均需要约3.11步才能到达状态3。注意这个期望时间是有穷的，因为从任何状态出发最终都能到达状态3（链条是不可约的）。

**English explanation:**
Starting from state 1, on average it takes about 3.11 steps to reach state 3. Note this expected time is finite because from any state we can eventually reach state 3 (the chain is irreducible).

---

#### Topic 7.2: Return Times / 返回时间

##### Intuition / 直觉理解

**中文解释：**
对于击中概率 $h_{ii}$ 和期望击中时间 $\eta_{ii}$，从状态 $i$ 出发击中状态 $i$ 的概率总是1（因为一开始就在那里），期望时间总是0。这显然没有提供有用信息。因此我们引入"返回时间"的概念：从状态 $i$ 出发，**第一次回到**状态 $i$ 的时间（不包括初始时刻 $n=0$）。

**English explanation:**
For hitting probability $h_{ii}$ and expected hitting time $\eta_{ii}$, starting from state $i$, the probability of hitting state $i$ is always 1 (we start there) and the expected time is always 0. This clearly provides no useful information. So we introduce the concept of "return time": starting from state $i$, the **first time we come back** to state $i$ (excluding the initial time $n=0$).

##### Formal Definition / 形式化定义

**Definition (Return Time / 返回时间).** Let $M_i$ be the return time to state $i$, defined as

$$M_i = \min\{n \in \{1, 2, \ldots\} : X_n = i\}$$

**中文解释：**
注意 $M_i$ 只考虑 $n = 1, 2, \ldots$，不包括 $n = 0$。所以 $M_i$ 是第一次真正"回来"的时间。

**English explanation:**
Note that $M_i$ only considers $n = 1, 2, \ldots$, not including $n = 0$. So $M_i$ is the first time we actually "come back."

**Definition (Return Probability / 返回概率).** The return probability $m_i$ is

$$m_i = \mathbb{P}(X_n = i \text{ for some } n \geq 1 \mid X_0 = i) = \mathbb{P}(M_i < \infty \mid X_0 = i)$$

**Definition (Expected Return Time / 期望返回时间).** The expected return time $\mu_i$ is

$$\mu_i = \mathbb{E}(M_i \mid X_0 = i)$$

##### Key Properties / 关键性质

**中文解释：**
返回概率和期望返回时间也可以通过条件化于第一步来求解。一般公式为：

$$m_i = \sum_{j \in \mathcal{S}} p_{ij} h_{ji}$$

$$\mu_i = 1 + \sum_{j \in \mathcal{S}} p_{ij} \eta_{ji}$$

其中 $h_{ji}$ 和 $\eta_{ji}$ 是从状态 $j$ 出发击中状态 $i$ 的击中概率和期望击中时间。

**English explanation:**
Return probability and expected return time can also be found by conditioning on the first step. The general formulas are:

$$m_i = \sum_{j \in \mathcal{S}} p_{ij} h_{ji}$$

$$\mu_i = 1