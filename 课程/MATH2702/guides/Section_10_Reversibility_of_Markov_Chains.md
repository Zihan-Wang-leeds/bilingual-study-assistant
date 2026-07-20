# Section 10: Reversibility of Markov chains

> MATH2702 - 自学教材 / Self-Study Guide
> 生成时间: 2026-07-20 15:41
> 来源页: 57-61

---

# 📘 Section 10: Reversibility of Markov Chains / 马尔可夫链的可逆性

## 📋 Section Overview / 章节概览

**中文解释：** 本章节探讨马尔可夫链的一个重要性质——可逆性。当我们从平稳分布出发运行一个马尔可夫链时，正向运行和反向运行在概率意义上是否看起来相同？这个问题引出了时间反转链（time reversed chain）的概念、细致平衡条件（detailed balance conditions）以及可逆性的判定条件。这些概念在统计物理、排队论和蒙特卡洛方法等领域有重要应用。

**English explanation:** This section explores an important property of Markov chains — reversibility. When we run a Markov chain starting from its stationary distribution, does it "look" the same (in a probabilistic sense) when run forwards as when run backwards? This question leads to the concepts of the time reversed chain, detailed balance conditions, and criteria for reversibility. These concepts have important applications in statistical physics, queueing theory, and Monte Carlo methods.

## 🎯 Learning Objectives / 学习目标

完成本章学习后，你应该能够：

1. **定义时间反转链**并计算其转移概率 / **Define the time reversed chain** and compute its transition probabilities
2. **理解并应用细致平衡条件**来判断马尔可夫链的可逆性 / **Understand and apply detailed balance conditions** to determine reversibility of a Markov chain
3. **证明满足细致平衡条件的分布是平稳分布** / **Prove that a distribution satisfying detailed balance is stationary**
4. **利用细致平衡方程求解平稳分布** / **Solve for stationary distributions using detailed balance equations**
5. **判断马尔可夫链的图是否为树**，并利用树性质判断可逆性 / **Determine if a Markov chain's graph is a tree** and use this to check reversibility
6. **区分可逆与不可逆马尔可夫链** / **Distinguish between reversible and non-reversible Markov chains**

## 📚 Prerequisites / 前置知识

**中文解释：** 在学习本章之前，你需要掌握以下内容：

**English explanation:** Before studying this chapter, you need to master the following:

- **马尔可夫链的基本概念**：状态空间、转移概率、转移矩阵 / **Basic Markov chain concepts**: state space, transition probabilities, transition matrix
- **平稳分布的定义和性质**：π = πP 以及平稳分布的存在性 / **Definition and properties of stationary distribution**: π = πP and existence of stationary distribution
- **不可约性和正常返性**：不可约马尔可夫链有唯一平稳分布 / **Irreducibility and positive recurrence**: irreducible Markov chains have a unique stationary distribution
- **期望返回时间**：μᵢ 表示返回状态 i 的期望时间 / **Expected return time**: μᵢ denotes the expected return time to state i

## 📖 Core Content / 核心内容

### Topic 1: Time Reversal of a Markov Chain / 马尔可夫链的时间反转

#### Intuition / 直觉理解

**中文解释：** 想象你正在观看一段马尔可夫链运行的录像。如果有人告诉你这段录像是正向播放还是反向播放，你能分辨出来吗？对于一般的马尔可夫链，正向和反向看起来是不同的。但是，如果马尔可夫链从平稳分布出发，反向过程实际上也是一个马尔可夫链，只是转移概率发生了变化。这个反向过程被称为"时间反转链"。

**English explanation:** Imagine you're watching a video of a Markov chain running. If someone tells you the video is playing forwards or backwards, can you tell the difference? For a general Markov chain, the forward and backward processes look different. However, if the Markov chain starts from its stationary distribution, the reversed process is actually also a Markov chain, just with different transition probabilities. This reversed process is called the "time reversed chain."

#### Formal Definition / 形式化定义

**Definition 10.1 (Time Reversed Chain / 时间反转链).** Let $(X_n)_{n\in\mathbb{N}}$ be a Markov chain on state space $\mathcal{S}$. For a fixed integer $N$, define the **reversed chain** $Y_n := X_{N-n}$.

**中文解释：** 设 $(X_n)_{n\in\mathbb{N}}$ 是状态空间 $\mathcal{S}$ 上的一个马尔可夫链。对于固定的整数 $N$，定义**反转链** $Y_n := X_{N-n}$。注意 $(Y_0, \ldots, Y_N) = (X_N, \ldots, X_0)$，所以 $(Y_n)_{n=0}^N$ 是如果我们"反向"运行 $X_n$ 时看到的状态序列。

**English explanation:** Let $(X_n)_{n\in\mathbb{N}}$ be a Markov chain on state space $\mathcal{S}$. For a fixed integer $N$, define the **reversed chain** $Y_n := X_{N-n}$. Note that $(Y_0, \ldots, Y_N) = (X_N, \ldots, X_0)$, so $(Y_n)_{n=0}^N$ is the sequence of states we will see if we run $X_n$ "backwards."

| Symbol / 符号 | Meaning / 含义 |
|:---:|:---|
| $(X_n)_{n\in\mathbb{N}}$ | Original Markov chain / 原始马尔可夫链 |
| $\mathcal{S}$ | State space / 状态空间 |
| $N$ | Fixed time horizon / 固定时间范围 |
| $Y_n$ | Reversed chain at time n / 时间n的反转链 |
| $X_{N-n}$ | Original chain at time N-n / 原始链在时间N-n的状态 |

#### Theorem 10.1: Transition Probabilities of the Reversed Chain / 反转链的转移概率

**Theorem 10.1.** Suppose $(X_n)_{n\in\mathbb{N}}$ is an irreducible positive recurrent Markov chain on state space $\mathcal{S}$ started from its stationary distribution $\pi$. The reversed chain $(Y_n)_{n=0}^N$ is an irreducible positive recurrent Markov chain with transition probabilities

$$\hat{p}(x, y) = \frac{\pi(y) p(y, x)}{\pi(x)}$$

for $x, y \in \mathcal{S}$.

The stationary distribution for $Y_n$ is also $\pi$.

**中文解释：** 这个定理告诉我们，如果原始马尔可夫链 $(X_n)$ 是不可约且正常返的，并且从平稳分布 $\pi$ 出发，那么反转链 $(Y_n)$ 也是一个不可约且正常返的马尔可夫链。它的转移概率 $\hat{p}(x, y)$ 由公式 $\hat{p}(x, y) = \pi(y) p(y, x) / \pi(x)$ 给出。注意这个公式中出现了原始链的转移概率 $p(y, x)$（注意顺序是反的！），以及平稳分布 $\pi$。反转链的平稳分布仍然是 $\pi$。

**English explanation:** This theorem tells us that if the original Markov chain $(X_n)$ is irreducible and positive recurrent, and starts from its stationary distribution $\pi$, then the reversed chain $(Y_n)$ is also an irreducible and positive recurrent Markov chain. Its transition probability $\hat{p}(x, y)$ is given by the formula $\hat{p}(x, y) = \pi(y) p(y, x) / \pi(x)$. Note that this formula involves the original chain's transition probability $p(y, x)$ (note the reversed order!) and the stationary distribution $\pi$. The stationary distribution for the reversed chain is also $\pi$.

| Symbol / 符号 | Meaning / 含义 |
|:---:|:---|
| $\hat{p}(x, y)$ | Transition probability of reversed chain from x to y / 反转链从x到y的转移概率 |
| $\pi(y)$ | Stationary probability of state y / 状态y的平稳概率 |
| $p(y, x)$ | Original chain's transition probability from y to x / 原始链从y到x的转移概率 |
| $\pi(x)$ | Stationary probability of state x / 状态x的平稳概率 |

#### Proof / 证明

**中文解释：** 我们来证明这个定理。对于 $k < N$ 和可能的状态序列 $x_0, \ldots, x_k, x_{k+1} \in \mathcal{S}$，我们需要证明反转链满足马尔可夫性质，并找出其转移概率。

**English explanation:** Let's prove this theorem. For $k < N$ and a possible sequence of states $x_0, \ldots, x_k, x_{k+1} \in \mathcal{S}$, we need to show that the reversed chain satisfies the Markov property and find its transition probabilities.

**Step 1: 计算条件概率 / Compute the conditional probability**

$$\mathbb{P}(Y_{k+1} = x_{k+1} | Y_k = x_k, \ldots, Y_1 = x_1, Y_0 = x_0)$$

**中文解释：** 根据定义 $Y_n = X_{N-n}$，我们可以将 $Y$ 的事件转换为 $X$ 的事件。

**English explanation:** By definition $Y_n = X_{N-n}$, we can convert events in $Y$ to events in $X$.

$$= \mathbb{P}(X_{N-k-1} = x_{k+1} | X_{N-k} = x_k, \ldots, X_{N-1} = x_1, X_N = x_0)$$

**Step 2: 应用"反向马尔可夫性质" / Apply the "backwards Markov property"**

**中文解释：** 这里我们使用习题集4中的"反向马尔可夫性质"。这个性质告诉我们，给定过去的状态，未来只依赖于最近的状态。在反向过程中，这意味着给定 $X_{N-k}$，$X_{N-k-1}$ 与更早的状态 $X_{N-k+1}, \ldots, X_N$ 条件独立。

**English explanation:** Here we use the "backwards Markov property" from Problem sheet 4. This property tells us that given past states, the future depends only on the most recent state. In the reversed process, this means that given $X_{N-k}$, $X_{N-k-1}$ is conditionally independent of earlier states $X_{N-k+1}, \ldots, X_N$.

$$= \mathbb{P}(X_{N-k-1} = x_{k+1} | X_{N-k} = x_k)$$

**Step 3: 用联合概率表示 / Express using joint probability**

$$= \frac{\mathbb{P}(X_{N-k-1} = x_{k+1}, X_{N-k} = x_k)}{\mathbb{P}(X_{N-k} = x_k)}$$

**Step 4: 利用平稳分布 / Use the stationary distribution**

**中文解释：** 因为 $X_n$ 从平稳分布出发，所以 $\mathbb{P}(X_n = x) = \pi(x)$ 对所有 $n$ 成立。同时，联合概率 $\mathbb{P}(X_{N-k-1} = x_{k+1}, X_{N-k} = x_k) = \pi(x_{k+1}) p(x_{k+1}, x_k)$。

**English explanation:** Because $X_n$ starts from its stationary distribution, we have $\mathbb{P}(X_n = x) = \pi(x)$ for all $n$. Also, the joint probability $\mathbb{P}(X_{N-k-1} = x_{k+1}, X_{N-k} = x_k) = \pi(x_{k+1}) p(x_{k+1}, x_k)$.

$$= \frac{\pi(x_{k+1}) p(x_{k+1}, x_k)}{\pi(x_k)}$$

**中文解释：** 这就证明了反转链的转移概率为 $\hat{p}(x_k, x_{k+1}) = \pi(x_{k+1}) p(x_{k+1}, x_k) / \pi(x_k)$，并且条件概率只依赖于当前状态 $x_k$，不依赖于更早的历史，所以反转链确实是马尔可夫链。

**English explanation:** This proves that the reversed chain has transition probabilities $\hat{p}(x_k, x_{k+1}) = \pi(x_{k+1}) p(x_{k+1}, x_k) / \pi(x_k)$, and the conditional probability depends only on the current state $x_k$, not on earlier history, so the reversed chain is indeed a Markov chain.

**Step 5: 不可约性和平稳分布 / Irreducibility and stationary distribution**

**中文解释：** 不可约性来自 $X_n$ 的不可约性。因为 $\mathbb{P}(X_n = x) = \pi(x)$，所以 $\mathbb{P}(Y_n = x) = \pi(x)$ 对 $n = 0, 1, \ldots, N$ 成立，因此 $\pi$ 也是反转链的平稳分布。

**English explanation:** Irreducibility follows from the irreducibility of $X_n$. Since $\mathbb{P}(X_n = x) = \pi(x)$, we also have $\mathbb{P}(Y_n = x) = \pi(x)$ for $n = 0, 1, \ldots, N$, so $\pi$ is the stationary distribution for the reversed chain as well.

---

### Topic 2: The Detailed Balance Equations / 细致平衡方程

#### Intuition / 直觉理解

**中文解释：** 现在我们回到最初的问题：从平稳分布出发的马尔可夫链，正向运行和反向运行看起来是否相同？如果转移概率相同，即 $\hat{p}(x, y) = p(x, y)$，那么正向和反向就不可区分。这等价于 $\pi(x) p(x, y) = \pi(y) p(y, x)$，这就是"细致平衡条件"（detailed balance conditions）。满足这个条件的马尔可夫链被称为"可逆的"（reversible）。

**English explanation:** Now we return to our original question: does a Markov chain started from its stationary distribution look the same forwards as backwards? If the transition probabilities are the same, i.e., $\hat{p}(x, y) = p(x, y)$, then forwards and backwards are indistinguishable. This is equivalent to $\pi(x) p(x, y) = \pi(y) p(y, x)$, which is called the "detailed balance conditions." A Markov chain satisfying this condition is called "reversible."

#### Formal Definition / 形式化定义

**Definition 10.2 (Reversible Markov Chain / 可逆马尔可夫链).** Let $(X_n)_{n\in\mathbb{N}}$ be a Markov chain on state space $\mathcal{S}$ with transition probabilities $p_{xy}$. If there is a probability distribution $\pi$ on $\mathcal{S}$ such that $X_n$ and $\pi$ satisfy the **detailed balance conditions**

$$\pi_x p_{xy} = \pi_y p_{yx}$$

for all $x, y \in \mathcal{S}$, then we say that $X_n$ is **reversible**.

**中文解释：** 定义中的关键条件是 $\pi_x p_{xy} = \pi_y p_{yx}$ 对所有状态对 $(x, y)$ 成立。这个条件被称为"细致平衡"，因为它要求从 $x$ 到 $y$ 的"概率流"（$\pi_x p_{xy}$）等于从 $y$ 到 $x$ 的"概率流"（$\pi_y p_{yx}$）。注意，这里 $\pi_x$ 是平稳分布中状态 $x$ 的概率，$p_{xy}$ 是从 $x$ 到 $y$ 的转移概率。

**English explanation:** The key condition in the definition is $\pi_x p_{xy} = \pi_y p_{yx}$ for all pairs of states $(x, y)$. This condition is called "detailed balance" because it requires that the "probability flow" from $x$ to $y$ ($\pi_x p_{xy}$) equals the "probability flow" from $y$ to $x$ ($\pi_y p_{yx}$). Note that $\pi_x$ is the probability of state $x$ in the stationary distribution, and $p_{xy}$ is the transition probability from $x$ to $y$.

| Symbol / 符号 | Meaning / 含义 |
|:---:|:---|
| $\pi_x$ | Stationary probability of state x / 状态x的平稳概率 |
| $p_{xy}$ | Transition probability from x to y / 从x到y的转移概率 |
| $\pi_x p_{xy}$ | Probability flow from x to y / 从x到y的概率流 |
| $\pi_y p_{yx}$ | Probability flow from y to x / 从y到x的概率流 |

#### Corollary 10.1: Detailed Balance Implies Stationarity / 细致平衡蕴含平稳性

**Corollary 10.1.** Any distribution $\pi$ that satisfies the detailed balance conditions for a Markov chain $X_n$ on $\mathcal{S}$ with transition probabilities $p(x, y)$ is a stationary distribution for $X_n$.

**中文解释：** 这个推论告诉我们，如果我们找到一个分布 $\pi$ 满足细致平衡条件，那么 $\pi$ 自动就是平稳分布。这意味着细致平衡是比平稳性更强的条件——所有可逆链的平稳分布都满足细致平衡，但并非所有平稳分布都满足细致平衡（如后面的例子所示）。

**English explanation:** This corollary tells us that if we find a distribution $\pi$ that satisfies the detailed balance conditions, then $\pi$ is automatically a stationary distribution. This means detailed balance is a stronger condition than stationarity — all reversible chains have stationary distributions satisfying detailed balance, but not all stationary distributions satisfy detailed balance (as shown in the example below).

**Proof / 证明（作为练习）**

**中文解释：** 这个推论的证明留作练习。提示：对 $j$ 求和 $\sum_i \pi_i p_{ij}$，利用细致平衡条件和 $\sum_i p_{ji} = 1$。

**English explanation:** The proof of this corollary is left as an exercise. Hint: Sum $\sum_i \pi_i p_{ij}$ over $i$, use the detailed balance condition and $\sum_i p_{ji} = 1$.

#### Worked Example 10.1: Discrete-Time Queue / 离散时间排队

**中文解释：** 这个例子展示了如何使用细致平衡方程来求解一个排队系统的平稳分布。考虑一个离散时间排队系统：在每个时间步，以概率 $p$ 到达一个顾客，以概率 $q$ 服务一个顾客（如果队列非空）。队列长度 $X_n$ 是一个马尔可夫链。

**English explanation:** This example shows how to use detailed balance equations to find the stationary distribution of a queueing system. Consider a discrete-time queue: at each time step, a customer arrives with probability $p$, and a customer is served with probability $q$ (if the queue is non-empty). The queue length $X_n$ is a Markov chain.

**Step 1: 找出转移概率 / Find the transition probabilities**

**中文解释：** 在每个时间步，队列长度最多变化1（最多一个到达，最多一个离开）。所以如果 $|i - j| > 1$，则 $p_{ij} = 0$。对于 $i > 0$，有三种情况：

**English explanation:** At each time step, the queue length changes by at most 1 (at most one arrival and at most one departure). So if $|i - j| > 1$, then $p_{ij} = 0$. For $i > 0$, there are three cases:

- $p_{i,i+1} = p(1-q)$：到达但不服务 / arrival but no service
- $p_{ii} = pq + (1-p)(1-q)$：同时到达和服务，或都没有 / both arrival and service, or neither
- $p_{i,i-1} = (1-p)q$：服务但不到达 / service but no arrival

对于 $i = 0$（空队列），没有顾客可以离开，所以：
- $p_{00} = (1-p)(1-q)$：没有到达也没有服务 / no arrival and no service
- $p_{01} = p$：有到达 / arrival occurs
- $p_{0,-1} = 0$：不可能有离开 / no departure possible

**Step 2: 应用细致平衡方程 / Apply detailed balance equations**

**中文解释：** 我们假设存在一个分布 $\pi$ 满足细致平衡条件 $\pi_i p_{ij} = \pi_j p_{ji}$。取 $j = i+1$，对于 $i > 0$：

**English explanation:** We assume there exists a distribution $\pi$ satisfying the detailed balance condition $\pi_i p_{ij} = \pi_j p_{ji}$. Take $j = i+1$, for $i > 0$:

$$\pi_i p(1-q) = \pi_{i+1} (1-p)q$$

整理得到 / Rearranging gives:

$$\pi_{i+1} = \frac{p}{1-p} \cdot \frac{1-q}{q} \pi_i$$

对于 $i = 0$ / For $i = 0$:

$$\pi_0 p = \pi_1 (1-p)q$$

整理得到 / Rearranging gives:

$$\pi_1 = \frac{p}{1-p} \cdot \frac{1}{q} \pi_0$$

**Step 3: 迭代求解 / Solve by iteration**

**中文解释：** 通过迭代第一个等式 $i$ 次，然后使用第二个等式，对于 $i > 0$：

**English explanation:** By iterating the first equality $i$ times and then using the second, for $i > 0$:

$$\pi_{i+1} = \left(\frac{p}{1-p}\right)^{i+1} \left(\frac{1-q}{q}\right)^i \frac{1}{q} \pi_0$$

**Step 4: 归一化条件 / Normalization condition**

**中文解释：** 我们需要 $\sum_{i \geq 0} \pi_i = 1$。注意，如果 $p > q$，则 $\pi_i \to \infty$，这意味着队列长度会无限增长。所以我们假设 $q > p$（服务率大于到达率）。

**English explanation:** We need $\sum_{i \geq 0} \pi_i = 1$. Note that if $p > q$, then $\pi_i \to \infty$, which means the queue length grows without bound. So we assume $q > p$ (service rate > arrival rate).

$$\pi_0 + \pi_0 \frac{p}{1-p} \frac{1}{q} \sum_{i \geq 0} \left(\frac{p(1-q)}{(1-p)q}\right)^i = 1$$

**中文解释：** 这是一个几何级数，公比为 $r = \frac{p(1-q)}{(1-p)q}$。当 $q > p$ 时，$r < 1$，级数收敛到 $1/(1-r)$。

**English explanation:** This is a geometric series with ratio $r = \frac{p(1-q)}{(1-p)q}$. When $q > p$, $r < 1$, the series converges to $1/(1-r)$.

**Step 5: 求解 $\pi_0$ / Solve for $\pi_0$**

$$\pi_0 = \frac{q-p}{q}$$

**中文解释：** 这是队列为空的平稳概率。然后对于 $i \geq 0$：

**English explanation:** This is the stationary probability that the queue is empty. Then for $i \geq 0$:

$$\pi_{i+1} = \left(\frac{p}{1-p}\right)^{i+1} \left(\frac{1-q}{q}\right)^i \frac{q-p}{q^2}$$

**中文解释：** 这个例子展示了细致平衡方程是求解平稳分布的有效工具。我们不需要解全局平衡方程 $\pi = \pi P$，只需要解局部平衡条件。

**English explanation:** This example shows that detailed balance equations are an effective tool for finding stationary distributions. We don't need to solve the global balance equations $\pi = \pi P$, only the local balance conditions.

#### Worked Example 10.2: Non-Reversible Markov Chain / 不可逆马尔可夫链

**中文解释：** 这个例子说明细致平衡对于平稳性来说是充分的，但不是必要的。考虑一个3状态马尔可夫链，转移矩阵为：

**English explanation:** This example shows that detailed balance is sufficient for stationarity, but not necessary. Consider a 3-state Markov chain with transition matrix:

$$P = $$
\begin{pmatrix}
0 & 1 & 0 \\
3/4 & 0 & 1/4 \\
1 & 0 & 0
\end{pmatrix}
$$$$

**中文解释：** 转移图如下所示。状态0以概率1转到状态1，状态1以概率3/4转到状态0、以概率1/4转到状态2，状态2以概率1转到状态0。

**English explanation:** The transition diagram is shown below. State 0 goes to state 1 with probability 1, state 1 goes to state 0 with probability 3/4 and to state 2 with probability 1/4, state 2 goes to state 0 with probability 1.

```
0 → 1 (概率1)
1 → 0 (概率3/4), 1 → 2 (概率1/4)
2 → 0 (概率1)
```

**Step 1: 求解平稳分布 / Find the stationary distribution**

**中文解释：** 解 $\pi = \pi P$：

**English explanation:** Solve $\pi = \pi P$:

$$\pi_0 = \frac{3}{4}\pi_1 + \pi_2$$
$$\pi_1 = \pi_0$$
$$\pi_2 = \frac{1}{4}\pi_1$$

加上归一化条件 $\pi_0 + \pi_1 + \pi_2 = 1$，得到 / With normalization $\pi_0 + \pi_1 + \pi_2 = 1$, we get:

$$\pi = \left(\frac{4}{9}, \frac{4}{9}, \frac{1}{9}\right)$$

**Step 2: 检查细致平衡 / Check detailed balance**

**中文解释：** 检查 $\pi_0 p_{01} = \pi_1 p_{10}$：

**English explanation:** Check $\pi_0 p_{01} = \pi_1 p_{10}$:

$$\pi_0 p_{01} = \frac{4}{9} \times 1 = \frac{4}{9}$$
$$\pi_1 p_{10} = \frac{4}{9} \times \frac{3}{4} = \frac{1}{3}$$

**中文解释：** 因为 $4/9 \neq 1/3$，所以细致平衡条件不成立。这个马尔可夫链不是可逆的，尽管它有平稳分布。

**English explanation:** Since $4/9 \neq 1/3$, the detailed balance condition does not hold. This Markov chain is not reversible, even though it has a stationary distribution.

---

### Topic 3: A Condition for Reversibility / 可逆性的一个条件

#### Intuition / 直觉理解

**中文解释：** 因为并非所有马尔可夫链都是可逆的，我们希望能有一些快速判断可逆性的方法。一个有用的条件是：如果马尔可夫链的图是一棵树（没有环），那么该链一定是可逆的