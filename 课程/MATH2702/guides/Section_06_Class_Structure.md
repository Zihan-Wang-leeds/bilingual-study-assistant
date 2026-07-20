# Section 6: Class structure

> MATH2702 - 自学教材 / Self-Study Guide
> 生成时间: 2026-07-20 15:38
> 来源页: 35-39

---

# 📘 MATH2702: Markov Chains Study Guide / 马尔可夫链学习指南

## Section 6: Communicating Classes and Periodicity / 通信类与周期性

---

### 📋 Section Overview / 章节概览

**中文解释：** 本章节是马尔可夫链理论中非常关键的一部分。我们将学习如何分析一个复杂的马尔可夫链，将其分解成更小的、可以独立研究的"通信类"。同时，我们还会研究状态的"周期性"——即系统在状态之间循环的规律性。这两个概念对于理解马尔可夫链的长期行为至关重要。

**English explanation:** This section is a crucial part of Markov chain theory. We will learn how to analyze a complex Markov chain by breaking it down into smaller "communicating classes" that can be studied independently. We will also study the "periodicity" of states — the regularity with which the system cycles between states. These two concepts are essential for understanding the long-term behavior of Markov chains.

**Why this matters / 为什么重要：**
- **中文：** 在实际应用中，比如金融模型、排队系统、流行病模型等，我们经常需要知道系统是否会进入某个"陷阱"状态（吸收态），或者系统是否会周期性地循环。理解通信类和周期性可以帮助我们预测系统的长期行为。
- **English:** In real-world applications like financial models, queueing systems, epidemic models, etc., we often need to know whether the system will enter a "trap" state (absorbing state) or whether it will cycle periodically. Understanding communicating classes and periodicity helps us predict the long-term behavior of the system.

---

### 🎯 Learning Objectives / 学习目标

By the end of this section, you should be able to / 学完本节后，你应该能够：

1. **Define and identify communicating classes** / 定义并识别通信类：理解状态之间的"可达"和"通信"关系，并能将状态空间划分为通信类。
2. **Determine if a Markov chain is irreducible** / 判断马尔可夫链是否不可约：理解不可约性的概念，并能判断一个链是否可以被分解。
3. **Identify closed classes and absorbing states** / 识别封闭类和吸收态：理解封闭类的概念，并能识别吸收态。
4. **Calculate the period of a state** / 计算状态的周期：理解周期的定义，并能计算给定状态的周期。
5. **Prove that states in the same communicating class have the same period** / 证明同一通信类中的状态具有相同的周期：理解并能够复现定理6.2的证明。
6. **Apply these concepts to examples** / 将这些概念应用于例题：能够分析简单随机游走、赌徒破产、流行病模型等例子。

---

### 📚 Prerequisites / 前置知识

Before starting this section, you should be familiar with / 开始本节前，你应该熟悉：

- **中文：**
  - 马尔可夫链的基本定义（状态空间、转移矩阵、转移概率）
  - 查普曼-科尔莫戈罗夫方程（Chapman-Kolmogorov equations）
  - 最大公约数（gcd）的概念
  - 等价关系的基本性质（自反性、对称性、传递性）

- **English:**
  - Basic definition of Markov chains (state space, transition matrix, transition probabilities)
  - Chapman-Kolmogorov equations
  - Concept of greatest common divisor (gcd)
  - Basic properties of equivalence relations (reflexivity, symmetry, transitivity)

---

### 📖 Core Content / 核心内容

---

#### Topic 1: Communicating Classes / 通信类

##### Intuition / 直觉理解

**中文解释：** 想象一个大型的社交网络，比如微信或微博。有些用户之间可以直接或间接地联系（比如通过共同好友），而有些用户则完全无法联系。在马尔可夫链中，我们也有类似的概念：如果从状态i可以到达状态j，并且从状态j也可以回到状态i，那么这两个状态就是"通信"的。所有相互通信的状态组成一个"通信类"。

**English explanation:** Imagine a large social network, like WeChat or Weibo. Some users can contact each other directly or indirectly (e.g., through mutual friends), while others cannot contact each other at all. In Markov chains, we have a similar concept: if we can get from state i to state j, and from state j back to state i, then these two states "communicate." All states that communicate with each other form a "communicating class."

**Analogy / 类比：**
- **中文：** 想象一个城市的地铁系统。有些地铁站之间可以互相到达（比如在同一线路上），有些则不能。如果两个站可以互相到达，它们就在同一个"通信类"中。
- **English:** Imagine a city's subway system. Some stations can reach each other (e.g., on the same line), while others cannot. If two stations can reach each other, they are in the same "communicating class."

##### Formal Definition / 形式化定义

**Definition 6.1 (Accessibility and Communication / 可达性与通信性)**

Consider a Markov chain on a state space $\mathcal{S}$ with transition matrix $\mathbf{P}$.

**English:** We say that state $j \in \mathcal{S}$ is **accessible** from state $i \in \mathcal{S}$ and write $i \to j$ if, for some $n$, $p_{ij}(n) > 0$.

**中文解释：** 我们说状态 $j \in \mathcal{S}$ 从状态 $i \in \mathcal{S}$ **可达**，记作 $i \to j$，如果存在某个步数 $n$，使得 $p_{ij}(n) > 0$。这意味着从状态 $i$ 出发，经过 $n$ 步后，有一定概率（正概率）到达状态 $j$。

**English:** If $i \to j$ and $j \to i$, we say that $i$ **communicates with** $j$ and write $i \leftrightarrow j$.

**中文解释：** 如果 $i \to j$ 且 $j \to i$，我们说 $i$ 与 $j$ **通信**，记作 $i \leftrightarrow j$。这意味着两个状态之间可以互相到达。

**Symbol Explanation / 符号说明：**

| Symbol / 符号 | Meaning / 含义 | Chinese Explanation / 中文解释 |
|---------------|----------------|-------------------------------|
| $\mathcal{S}$ | State space | 状态空间，所有可能状态的集合 |
| $\mathbf{P}$ | Transition matrix | 转移矩阵，包含所有一步转移概率 |
| $p_{ij}(n)$ | n-step transition probability from i to j | 从状态i到状态j的n步转移概率 |
| $i \to j$ | j is accessible from i | j从i可达 |
| $i \leftrightarrow j$ | i and j communicate | i与j通信 |

##### Key Properties / 关键性质

**Theorem 6.1: The "Communicates With" Relation is an Equivalence Relation / "通信"关系是等价关系**

**English:** Consider a Markov chain on a state space $\mathcal{S}$ with transition matrix $\mathbf{P}$. Then the "communicates with" relation $\leftrightarrow$ is an equivalence relation; that is, it has the following properties:

**中文解释：** 考虑一个定义在状态空间 $\mathcal{S}$ 上、转移矩阵为 $\mathbf{P}$ 的马尔可夫链。那么"通信"关系 $\leftrightarrow$ 是一个等价关系，即它具有以下性质：

1. **Reflexive / 自反性**: $i \leftrightarrow i$ for all $i$ / 对所有 $i$ 成立
2. **Symmetric / 对称性**: if $i \leftrightarrow j$ then $j \leftrightarrow i$ / 如果 $i \leftrightarrow j$ 则 $j \leftrightarrow i$
3. **Transitive / 传递性**: if $i \leftrightarrow j$ and $j \leftrightarrow k$ then $i \leftrightarrow k$ / 如果 $i \leftrightarrow j$ 且 $j \leftrightarrow k$ 则 $i \leftrightarrow k$

**Proof / 证明：**

**Reflexivity / 自反性：**

**中文解释：** 我们需要证明每个状态都与自身通信。注意 $p_{ii}(0) = 1 > 0$，因为"零步"意味着我们停留在原地。所以 $i \leftrightarrow i$ 对所有 $i$ 成立。

**English:** We need to show that every state communicates with itself. Note that $p_{ii}(0) = 1 > 0$, because in "zero steps" we stay where we are. So $i \leftrightarrow i$ for all $i$.

**Symmetry / 对称性：**

**中文解释：** 从定义来看，$i \leftrightarrow j$ 的定义在交换 $i$ 和 $j$ 时是对称的（因为定义要求 $i \to j$ 且 $j \to i$）。所以对称性自然成立。

**English:** By definition, $i \leftrightarrow j$ is symmetric under swapping $i$ and $j$ (since the definition requires both $i \to j$ and $j \to i$). So symmetry holds automatically.

**Transitivity / 传递性：**

**中文解释：** 这是最有趣的部分。如果我们可以从 $i$ 到 $j$，也可以从 $j$ 到 $k$，那么我们可以通过 $j$ 作为"中转站"从 $i$ 到 $k$。我们需要用数学语言严格表达这一点。

**English:** This is the most interesting part. If we can get from $i$ to $j$ and from $j$ to $k$, then we can get from $i$ to $k$ by going via $j$. We need to express this formally in mathematical language.

**Step-by-step reasoning / 逐步推理：**

1. **中文：** 由于 $i \to j$，存在某个 $n$ 使得 $p_{ij}(n) > 0$。
   **English:** Since $i \to j$, there exists some $n$ such that $p_{ij}(n) > 0$.

2. **中文：** 由于 $j \to k$，存在某个 $m$ 使得 $p_{jk}(m) > 0$。
   **English:** Since $j \to k$, there exists some $m$ such that $p_{jk}(m) > 0$.

3. **中文：** 根据查普曼-科尔莫戈罗夫方程，我们有：
   **English:** By the Chapman-Kolmogorov equations, we have:
   
   $$p_{ik}(n+m) = \sum_{l \in \mathcal{S}} p_{il}(n) p_{lk}(m) \geq p_{ij}(n) p_{jk}(m) > 0$$
   
   **中文解释：** 这个求和是对所有中间状态 $l$ 进行的。我们特别关注 $l = j$ 这一项，因为 $p_{ij}(n) > 0$ 且 $p_{jk}(m) > 0$，所以这一项是正数。由于求和中的所有项都是非负的，整个和至少等于这一项，因此也是正数。所以 $i \to k$。

   **English:** This sum is over all intermediate states $l$. We focus on the term $l = j$, because $p_{ij}(n) > 0$ and $p_{jk}(m) > 0$, so this term is positive. Since all terms in the sum are non-negative, the entire sum is at least this term, hence also positive. So $i \to k$.

4. **中文：** 同样的论证，交换 $k$ 和 $i$ 的位置，可以得到 $k \to i$。因此 $i \leftrightarrow k$。
   **English:** The same argument with $k$ and $i$ swapped gives $k \to i$ as well, so $i \leftrightarrow k$.

**Important Consequence / 重要推论：**

**中文解释：** 等价关系的一个重要性质是它将集合 $\mathcal{S}$ 划分为等价类。每个状态 $i$ 恰好属于一个等价类，这个类就是所有与 $i$ 通信的状态的集合。在马尔可夫链的语境中，我们称这些等价类为**通信类**。

**English:** A key fact about equivalence relations is that they partition the space $\mathcal{S}$ into equivalence classes. Each state $i$ belongs to exactly one equivalence class, and that class is the set of states $j$ such that $i \leftrightarrow j$. In this context, we call these **communicating classes**.

##### Worked Examples / 例题

**Example 6.1: Simple Random Walk / 简单随机游走**

**中文解释：** 考虑简单随机游走，其中 $p$ 不是 0 或 1。从状态 $i$ 出发，我们可以通过向上走 $j-i$ 步到达 $j > i$，也可以通过向下走 $i-j$ 步到达 $j < i$。因此，每个状态都可以到达其他任何状态，整个状态空间 $\mathcal{S} = \mathbb{Z}$ 是一个通信类。

**English:** Consider the simple random walk, provided $p$ is not 0 or 1. From state $i$, we can get to $j > i$ by going up $j-i$ times, and we can get to $j < i$ by going down $i-j$ times. Therefore, every state communicates with every other state, and the whole state space $\mathcal{S} = \mathbb{Z}$ is one communicating class.

**Example 6.2: Gambler's Ruin / 赌徒破产**

**中文解释：** 考虑定义在 $\{0, 1, \ldots, m\}$ 上的赌徒破产马尔可夫链。这里有三个通信类：
- 破产状态 $\{0\}$ 和 $\{m\}$ 各自不与任何其他状态通信，所以每个都是一个单独的类。
- 剩余的状态 $\{1, 2, \ldots, m-1\}$ 都在同一个类中，类似于简单随机游走。

**English:** Consider the gambler's ruin Markov chain on $\{0, 1, \ldots, m\}$. There are three communicating classes:
- The ruin states $\{0\}$ and $\{m\}$ each don't communicate with any other states, so each is a class by themselves.
- The remaining states $\{1, 2, \ldots, m-1\}$ are all in the same class, like the simple random walk.

**Example 6.3: Healthy-Sick-Dead Epidemic Model / 健康-生病-死亡流行病模型**

**中文解释：** 考虑一个简单的流行病模型，有三个状态：健康（H）、生病（S）和死亡（D）。转移矩阵为：

**English:** Consider a simple epidemic model with three states: healthy (H), sick (S), and dead (D). The transition matrix is:

$$\mathbf{P} = $$
\begin{pmatrix}
p_{HH} & p_{HS} & 0 \\
p_{SH} & p_{SS} & p_{SD} \\
0 & 0 & 1
\end{pmatrix}
$$$$

**中文解释：** 从转移矩阵可以看出：
- H和S可以互相通信（你可以被感染或康复）
- D只与自身通信（死者不会康复）

因此，状态空间 $\mathcal{S} = \{H, S, D\}$ 被划分为两个通信类：$\{H, S\}$ 和 $\{D\}$。

**English:** From the transition matrix we can see:
- H and S communicate with each other (you can become infected or recover)
- D only communicates with itself (the dead do not recover)

Hence, the state space $\mathcal{S} = \{H, S, D\}$ partitions into two communicating classes: $\{H, S\}$ and $\{D\}$.

##### Additional Definitions / 补充定义

**Definition 6.2: Irreducibility, Closed Classes, and Absorbing States / 不可约性、封闭类和吸收态**

**1. Irreducible Markov Chain / 不可约马尔可夫链**

**English:** If the entire state space $\mathcal{S}$ is one communicating class, we say that the Markov chain is **irreducible**.

**中文解释：** 如果整个状态空间 $\mathcal{S}$ 是一个通信类，我们就说这个马尔可夫链是**不可约**的。这意味着链不能被分解成更小的部分。

**2. Closed Class / 封闭类**

**English:** We say that a communicating class is **closed** if no state outside the class is accessible from any state within the class. That is, class $C \subset \mathcal{S}$ is closed if whenever there exist $i \in C$ and $j \in \mathcal{S}$ with $i \to j$, then $j \in C$ also.

**中文解释：** 我们说一个通信类是**封闭**的，如果从类内的任何状态都无法到达类外的任何状态。也就是说，类 $C \subset \mathcal{S}$ 是封闭的，如果每当存在 $i \in C$ 和 $j \in \mathcal{S}$ 且 $i \to j$ 时，必有 $j \in C$。

**English:** If a class is not closed, we say it is **open**.

**中文解释：** 如果一个类不是封闭的，我们就说它是**开放**的。

**3. Absorbing State / 吸收态**

**English:** If a state $i$ is in a communicating class $\{i\}$ by itself and that class is closed, then we say state $i$ is **absorbing**.

**中文解释：** 如果一个状态 $i$ 独自构成一个通信类 $\{i\}$，并且这个类是封闭的，那么我们就说状态 $i$ 是**吸收**的。

**Intuitive Explanations / 直观解释：**

**中文：**
- 不可约马尔可夫链：不能分解成更小的部分。
- 封闭类：一旦进入这个类，就无法离开。
- 吸收态：一旦到达这个状态，就无法离开。

**English:**
- An irreducible Markov chain: cannot be broken down into smaller pieces.
- A closed class: once you enter this class, you cannot leave.
- An absorbing state: once you reach this state, you cannot leave.

**Example 6.4: Applying These Concepts / 应用这些概念**

**中文解释：** 回顾之前的例子：

**English:** Going back to the previous examples:

1. **Simple Random Walk / 简单随机游走：**
   - **中文：** 整个状态空间是一个通信类，因此必然是封闭的。马尔可夫链只有一个类，所以是不可约的。
   - **English:** The whole state space is one communicating class which must therefore be closed. The Markov chain has only one class, so is irreducible.

2. **Gambler's Ruin / 赌徒破产：**
   - **中文：** 类 $\{0\}$ 和 $\{m\}$ 是封闭的，因为马尔可夫链会永远停留在那里。由于这些封闭类各自只包含一个状态，所以 0 和 $m$ 是吸收态。类 $\{1, 2, \ldots, m-1\}$ 是开放的，因为我们可以通过到达 0 或 $m$ 来离开这个类。赌徒破产链有多个类，所以不是不可约的。
   - **English:** Classes $\{0\}$ and $\{m\}$ are closed, because the Markov chain stays there forever. Since these closed classes consist of only one state each, 0 and $m$ are absorbing states. The class $\{1, 2, \ldots, m-1\}$ is open, as we can escape the class by going to 0 or $m$. The gambler's ruin chain has multiple classes, so is not irreducible.

3. **Healthy-Sick-Dead Chain / 健康-生病-死亡链：**
   - **中文：** 类 $\{D\}$ 是封闭的，所以 D 是吸收态。类 $\{H, S\}$ 是开放的，因为可以通过死亡离开它。这个马尔可夫链不是不可约的。
   - **English:** The class $\{D\}$ is closed, so D is an absorbing state. The class $\{H, S\}$ is open, as one can leave it by dying. The Markov chain is not irreducible.

---

#### Topic 2: Periodicity / 周期性

##### Intuition / 直觉理解

**中文解释：** 在简单随机游走中，我们注意到系统在奇数和偶数状态之间交替。这种"周期性"行为对于理解我们在未来某个时间点会处于哪个状态非常重要。周期的概念是这样的：列出所有从状态 $i$ 出发并回到状态 $i$ 的可能路径的步数，然后取这些步数的最大公约数。

**English:** In the simple random walk, we noted that the system alternates between odd-numbered and even-numbered states. This "periodic" behavior is important for understanding which state we will be in at some point in the future. The idea of period is this: List the number of steps for all possible paths starting and ending in state $i$, then take the greatest common divisor of these numbers.

##### Formal Definition / 形式化定义

**Definition 6.3: Period of a State / 状态的周期**

**English:** Consider a Markov chain with transition matrix $\mathbf{P}$. We say that a state $i \in \mathcal{S}$ has **period** $d_i$, where

$$d_i = \gcd\{ n \in \{1, 2, \ldots\} : p_{ii}(n) > 0 \}$$

where gcd denotes the greatest common divisor.

**中文解释：** 考虑一个转移矩阵为 $\mathbf{P}$ 的马尔可夫链。我们说状态 $i \in \mathcal{S}$ 的**周期**为 $d_i$，其中 $d_i$ 是所有使得 $p_{ii}(n) > 0$ 的正整数 $n$ 的最大公约数。

**English:** If $d_i > 1$, then the state $i$ is called **periodic**; if $d_i = 1$, then $i$ is called **aperiodic**.

**中文解释：** 如果 $d_i > 1$，则状态 $i$ 称为**周期性的**；如果 $d_i = 1$，则 $i$ 称为**非周期性的**。

**Symbol Explanation / 符号说明：**

| Symbol / 符号 | Meaning / 含义 | Chinese Explanation / 中文解释 |
|---------------|----------------|-------------------------------|
| $d_i$ | Period of state i | 状态i的周期 |
| $\gcd$ | Greatest common divisor | 最大公约数 |
| $p_{ii}(n)$ | n-step return probability to state i | 从状态i出发n步后回到状态i的概率 |
| $d_i > 1$ | Periodic state | 周期性状态 |
| $d_i = 1$ | Aperiodic state | 非周期性状态 |

##### Worked Examples / 例题

**Example 6.5: Simple Random Walk / 简单随机游走**

**中文解释：** 考虑 $p \neq 0, 1$ 的简单随机游走。我们有 $p_{ii}(n) = 0$ 当 $n$ 为奇数时，因为每一步都会在奇数和偶数之间切换。但 $p_{ii}(2) = 2pq > 0$。因此，所有状态都是周期性的，周期为 $\gcd\{2, 4, 6, \ldots\} = 2$。

**English:** Consider the simple random walk with $p \neq 0, 1$. We have $p_{ii}(n) = 0$ for odd $n$, since we swap from odd to even each step. But $p_{ii}(2) = 2pq > 0$. Therefore, all states are periodic with period $\gcd\{2, 4, 6, \ldots\} = 2$.

**Example 6.6: Gambler's Ruin / 赌徒破产**

**中文解释：** 对于赌徒破产问题，状态 0 和 $m$ 是非周期性的（周期为 1），因为它们是吸收态。剩余的状态 $1, 2, \ldots, m-1$ 的周期为 2，因为我们在奇数和偶数状态之间切换，就像简单随机游走一样。

**English:** For the gambler's ruin, states 0 and $m$ are aperiodic (have period 1), since they are absorbing states. The remaining states $1, 2, \ldots, m-1$ are periodic with period 2, because we swap between odd and even states, as in the simple random walk.

**Example 6.7: Mixed Period Example / 混合周期例子**

**中文解释：** 考虑以下转移图所示的马尔可夫链：

**English:** Consider the Markov chain with transition diagram as shown:

```
2 ←→ 1 ←→ 3 ←→ 4 → 5 ←→ 6 ←→ 7
```

**中文解释：** 重要的是，我们不能从三角形一侧（状态5,6,7）回到圆形一侧（状态1,2,3,4）。因此我们看到有两个通信类：$\{1, 2, 3, 4\}$（开放的）和 $\{5, 6, 7\}$（封闭的）。这个马尔可夫链不是不可约的，也没有吸收态。

**English:** Importantly, we cannot return from the triangle side (states 5,6,7) back to the circle side (states 1,2,3,4). We thus see there are two communicating classes: $\{1, 2, 3, 4\}$ (open) and $\{5, 6, 7\}$ (closed). The Markov chain is not irreducible, and there are no absorbing states.

**中文解释：** 圆形一侧在奇数和偶数状态之间切换（直到从状态4退出到状态5），所以状态1,2,3,4的周期都是2。三角形一侧确定性地循环，意味着状态5,6,7的周期都是3。

**English:** The circle side swaps between odd and even states (until exiting from 4 to 5), so states 1, 2, 3, and 4 all have period 2. The triangle side cycles around with certainty, meaning that states 5, 6, and 7 all have period 3.

##### Key Theorem / 关键定理

**Theorem 6.2: States in the Same Communicating Class Have the Same Period / 同一通信类中的状态具有相同的周期**

**English:** All states in a communicating class have the same period.

**中文解释：** 同一通信类中的所有状态都具有相同的周期。

**Formal Statement / 形式化表述：**

**English:** Consider a Markov chain on a state space $\mathcal{S}$ with transition matrix $\mathbf{P}$. If $i, j \in \mathcal{S}$ are such that $i \leftrightarrow j$, then $d_i = d_j$.

**中文解释：** 考虑一个定义在状态空间 $\mathcal{S}$ 上、转移矩阵为 $\mathbf{P}$ 的马尔可夫链。如果 $i, j \in \mathcal{S}$ 满足 $i \leftrightarrow j$，那么 $d_i = d_j$。

**English:** In particular, in an irreducible Markov chain, all states have the same period $d$. We say