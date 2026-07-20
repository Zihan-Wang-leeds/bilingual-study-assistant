# Section 1: Stochastic processes and the Markov property

> MATH2702 - 自学教材 / Self-Study Guide
> 生成时间: 2026-07-20 15:35
> 来源页: 10-13

---

# MATH2702: Stochastic Processes / 随机过程

## Part I: Discrete Time Markov Chains / 第一部分：离散时间马尔可夫链

---

### 📋 Section Overview / 章节概览

**中文解释：** 本章节是MATH2702课程的开篇内容，主要介绍随机过程的基本概念和马尔可夫性质。我们将从确定性模型和随机模型的区别开始，逐步理解什么是随机过程，以及为什么马尔可夫性质如此重要。这一部分为整个课程奠定了理论基础，特别是为后续学习离散时间马尔可夫链和连续时间马尔可夫跳过程做好了准备。

**English explanation:** This section is the opening content of MATH2702, introducing the fundamental concepts of stochastic processes and the Markov property. We will start from the distinction between deterministic and random models, gradually understand what a stochastic process is, and why the Markov property is so important. This part lays the theoretical foundation for the entire course, especially preparing for the subsequent study of discrete-time Markov chains and continuous-time Markov jump processes.

**Why this matters / 为什么重要：**
- 随机过程是现代概率论的核心内容，广泛应用于金融、物理、工程等领域
- Stochastic processes are core to modern probability theory, widely applied in finance, physics, engineering, etc.
- 马尔可夫性质是简化复杂随机系统分析的关键工具
- The Markov property is a key tool for simplifying the analysis of complex random systems

---

### 🎯 Learning Objectives / 学习目标

完成本章节学习后，你应该能够：

1. **区分确定性模型和随机模型** - 理解何时使用哪种模型，以及随机模型（stochastic model）的优势
2. **定义随机过程** - 理解状态空间（state space）和指标集（index set）的概念，以及离散/连续时间的四种组合
3. **理解马尔可夫性质** - 掌握"无记忆性"（memoryless property）的核心思想
4. **运用条件概率和条件期望** - 复习并应用条件概率和条件期望的基本概念
5. **形式化定义马尔可夫链** - 能够写出并解释马尔可夫性质的数学定义

After completing this section, you should be able to:

1. **Distinguish deterministic and random models** - Understand when to use each type and the advantages of stochastic models
2. **Define stochastic processes** - Understand the concepts of state space and index set, and the four combinations of discrete/continuous time and space
3. **Understand the Markov property** - Grasp the core idea of the "memoryless property"
4. **Apply conditional probability and expectation** - Review and apply basic concepts of conditional probability and expectation
5. **Formally define Markov chains** - Write and explain the mathematical definition of the Markov property

---

### 📚 Prerequisites / 前置知识

**中文解释：** 在学习本章节前，你需要掌握以下基础知识：

**English explanation:** Before studying this section, you need to master the following prerequisite knowledge:

| 知识点 | 中文说明 | English Description |
|--------|----------|-------------------|
| 基本概率论 | 随机变量、概率分布、期望值 | Random variables, probability distributions, expectation |
| 条件概率 | ℙ(A|B)的定义和计算 | Definition and calculation of conditional probability |
| 条件期望 | 𝔼(X|Y)的定义和性质 | Definition and properties of conditional expectation |
| 独立性 | 随机变量独立的概念 | Concept of independence of random variables |
| 集合论基础 | 可数集、不可数集的概念 | Basic set theory: countable vs uncountable sets |

---

### 📖 Core Content / 核心内容

---

#### 1.1 Deterministic and Random Models / 确定性与随机模型

##### Intuition / 直觉理解

**中文解释：** 想象一下，我们想要预测明天是否会下雨。如果我们使用一个确定性模型，我们会说"如果温度低于20°C且湿度大于80%，则一定会下雨"——这个模型没有随机性，输出完全由输入决定。但现实世界非常复杂，我们无法精确知道所有影响因素，所以更好的方法是使用随机模型："有70%的概率会下雨"。

**English explanation:** Imagine we want to predict whether it will rain tomorrow. If we use a deterministic model, we would say "if temperature is below 20°C and humidity is above 80%, then it will definitely rain" — this model has no randomness, the output is completely determined by the inputs. But the real world is extremely complex, and we cannot know all influencing factors precisely, so a better approach is to use a stochastic model: "there is a 70% probability of rain."

**Key distinction / 关键区别：**

| 特征 | 确定性模型 | 随机模型 |
|------|-----------|---------|
| 中文 | 输出完全由输入决定 | 输出包含随机性 |
| English | Output completely determined by inputs | Output includes randomness |
| 示例 | 月球轨道预测 | 苹果股票价格 |
| 适用场景 | 系统简单、不确定性小 | 系统复杂、不确定性大 |

**Real-world examples / 实际应用示例：**

1. **月球轨道 (Moon's orbit)** : 物理定律精确，小行星撞击影响微小 → 确定性模型足够
2. **苹果股票 (Apple shares)** : 每日价格变化高度不确定 → 需要随机模型

> **重要提示：** 随机模型（stochastic model）这个词来自希腊语"stochastikos"，意为"善于猜测"。在中文中，"随机"和"stochastic"都强调不确定性。

> **Important note:** The word "stochastic" comes from Greek "stochastikos," meaning "skilled at guessing." Both "随机" and "stochastic" emphasize uncertainty.

---

#### 1.2 Stochastic Processes / 随机过程

##### Intuition / 直觉理解

**中文解释：** 假设我们要研究一家保险公司在2024年全年的理赔数量。如果我们只关心总数，一个随机变量（比如泊松分布）就足够了。但如果我们想追踪理赔数量如何随时间变化——比如月初多还是月末多，节假日是否有变化——我们就需要一个随机过程。

**English explanation:** Suppose we want to study the total number of claims to an insurance company in 2024. If we only care about the total, a single random variable (like a Poisson distribution) is sufficient. But if we want to track how the number of claims changes over time — like whether there are more at the beginning of the month or the end, whether holidays make a difference — we need a stochastic process.

##### Formal Definition / 形式化定义

**Definition 1.1 (Stochastic Process / 随机过程):**

A stochastic process, usually written as $(X_n)$, is an indexed sequence of random variables that are (usually) dependent on each other.

一个随机过程，通常记为$(X_n)$，是一个索引化的随机变量序列，这些随机变量通常相互依赖。

**Key Components / 关键组成部分：**

| 符号 | 中文名称 | English Name | 说明 |
|------|---------|-------------|------|
| $X_n$ | 第n个随机变量 | n-th random variable | 过程在时刻n的状态 |
| $\mathcal{S}$ | 状态空间 | State space | 所有可能取值的集合 |
| $n$ | 时间指标 | Time index | 表示测量时刻 |

##### State Space / 状态空间

**中文解释：** 状态空间$\mathcal{S}$是随机过程可能取值的集合。它可以是离散的（distinct outcomes）或连续的（continuum of outcomes）。

**English explanation:** The state space $\mathcal{S}$ is the set of possible values the stochastic process can take. It can be discrete (distinct outcomes) or continuous (continuum of outcomes).

**Types of State Spaces / 状态空间类型：**

| 类型 | 中文说明 | English Description | 示例 |
|------|---------|-------------------|------|
| 离散有限 | 有限个不同结果 | Finite distinct outcomes | $\mathcal{S} = \{\text{Heads}, \text{Tails}\}$ |
| 离散无限 | 可数无限个结果 | Countably infinite outcomes | $\mathcal{S} = \mathbb{Z}_+ = \{0, 1, 2, \ldots\}$ |
| 连续 | 不可数无限个结果 | Uncountably infinite outcomes | $\mathcal{S} = \mathbb{R}_+ = \{x \in \mathbb{R}: x \geq 0\}$ |

**Examples / 示例：**

- **硬币抛掷 (Coin flip)** : $\mathcal{S} = \{\text{Heads}, \text{Tails}\}$ — 离散有限
- **保险理赔计数 (Insurance claims)** : $\mathcal{S} = \mathbb{Z}_+ = \{0, 1, 2, \ldots\}$ — 离散无限
- **降雨量 (Rainfall amount)** : $\mathcal{S} = \mathbb{R}_+ = \{x \in \mathbb{R}: x \geq 0\}$ — 连续
- **气体粒子位置 (Gas particle position)** : $\mathcal{S} \subset \mathbb{R}^3$ — 连续（三维空间）

##### Time Index / 时间指标

**中文解释：** 时间指标集决定了我们何时测量过程。它也可以是离散的或连续的。

**English explanation:** The index set determines when we measure the process. It can also be discrete or continuous.

**Types of Time / 时间类型：**

| 类型 | 中文说明 | English Description | 表示法 |
|------|---------|-------------------|--------|
| 离散时间 | 在特定时间点采样 | Sampled at distinct points | $n = 0, 1, 2, \ldots$ |
| 连续时间 | 持续监控 | Monitored constantly | $t \in \mathbb{R}_+ = \{x \in \mathbb{R}: x \geq 0\}$ |

**Example / 示例：**
- 保险理赔：每天统计一次 → 离散时间 $n = 1, 2, \ldots, 365$
- 保险理赔：每次理赔后更新 → 连续时间 $t$ 表示全年时间

##### Four Combinations / 四种组合

**中文解释：** 根据状态空间和时间指标的离散/连续性质，我们得到四种组合。本课程主要关注两种。

**English explanation:** Based on the discrete/continuous nature of state space and time index, we get four combinations. This course focuses mainly on two.

| 组合 | 时间 | 状态空间 | 示例 | 本课程覆盖 |
|-----|------|---------|------|-----------|
| 1 | 离散 | 离散 | 每节课出勤学生数 | ✅ **主要** (马尔可夫链) |
| 2 | 离散 | 连续 | 利兹每日最高温度 | ⚠️ 简要提及 |
| 3 | 连续 | 离散 | 网页访问量随时间变化 | ✅ **主要** (马尔可夫跳过程) |
| 4 | 连续 | 连续 | FTSE 100指数水平 | ❌ 超出范围 (见MATH3734) |

**Detailed examples / 详细示例：**

**Combination 1: Discrete time, discrete space / 离散时间，离散空间**
- **Example:** Number of students attending each lecture of a maths module
- **中文示例：** 数学模块每节课的出勤学生数
- **Course relevance:** This is the main topic of the first half — **Markov chains**

**Combination 2: Discrete time, continuous space / 离散时间，连续空间**
- **Example:** Daily maximum temperature in Leeds
- **中文示例：** 利兹每日最高温度
- **Course relevance:** Briefly mentioned, but not a major focus

**Combination 3: Continuous time, discrete space / 连续时间，离散空间**
- **Example:** Number of visitors to a webpage over time
- **中文示例：** 网页访问量随时间变化
- **Course relevance:** This is the main topic of the second half — **Markov jump processes**

**Combination 4: Continuous time, continuous space / 连续时间，连续空间**
- **Example:** Level of the FTSE 100 share index over time
- **中文示例：** FTSE 100指数水平随时间变化
- **Course relevance:** Outside scope of this course (see MATH3734 Stochastic Calculus for Finance)

---

#### 1.3 Markov Property / 马尔可夫性质

##### Intuition / 直觉理解

**中文解释：** 想象你在玩一个简单的棋盘游戏。你掷骰子，然后向前移动相应的格数。假设你现在在第$X_n$格。关于下一步你会移动到哪一格$X_{n+1}$，我们能说什么？

1. $X_{n+1}$是随机的，因为它取决于骰子的结果
2. $X_{n+1}$取决于你现在的位置$X_n$，因为骰子点数会加到当前格数上
3. **关键点：** 给定你现在的位置$X_n$，$X_{n+1}$不再依赖于你之前走过的路径$X_0, X_1, \ldots, X_{n-1}$

**English explanation:** Imagine playing a simple board game. You roll dice and move that many squares forward. Suppose you are currently on square $X_n$. What can we say about which square $X_{n+1}$ you move to next?

1. $X_{n+1}$ is random, since it depends on the roll of the dice
2. $X_{n+1}$ depends on where you are now $X_n$, since the dice score will be added to your current square
3. **Key point:** Given where you are now $X_n$, $X_{n+1}$ does not depend any further on which sequence of squares $X_0, X_1, \ldots, X_{n-1}$ you used to get here

**The "Memoryless" Property / "无记忆"性质：**

**中文解释：** 第三点就是马尔可夫性质的核心——"无记忆性"。就好像过程忘记了它是如何到达这里的：我们只需要记住到达了哪个格子，而不需要记住之前经过了哪些格子。数学上表达为："给定现在，过去和未来是条件独立的"。

**English explanation:** The third point is the core of the Markov property — the "memoryless property." It's as if the process forgot how it got here: we only need to remember what square we have reached, not which squares we used to get here. Mathematically: "the past and the future are conditionally independent given the present."

##### Review: Conditional Probability / 复习：条件概率

**中文解释：** 在正式定义马尔可夫性质之前，我们需要复习条件概率和条件期望的概念。

**English explanation:** Before formally defining the Markov property, we need to review the concepts of conditional probability and conditional expectation.

**Conditional Probability / 条件概率：**

For events $A$ and $B$ (with $\mathbb{P}(B) > 0$):
$$\mathbb{P}(A \mid B) = \frac{\mathbb{P}(A \cap B)}{\mathbb{P}(B)}$$

**中文解释：** 条件概率$\mathbb{P}(A \mid B)$表示在事件$B$确定发生的情况下，事件$A$发生的概率。注意，我们总是隐含假设条件事件（$B$）的概率严格大于0。

**English explanation:** Conditional probability $\mathbb{P}(A \mid B)$ represents the probability that event $A$ occurs given that event $B$ definitely occurs. Note that we always implicitly assume the conditioning event ($B$) has strictly positive probability.

**Conditional Expectation / 条件期望：**

For a random variable $X$ taking values in state space $\mathcal{S}$ and event $B$ (with $\mathbb{P}(B) > 0$):
$$\mathbb{E}(X \mid B) = \sum_{s \in \mathcal{S}} s \mathbb{P}(X = s \mid B)$$

**中文解释：** 条件期望$\mathbb{E}(X \mid B)$是在已知事件$B$发生的情况下，随机变量$X$的期望值。注意这是一个数值（number）。

**English explanation:** Conditional expectation $\mathbb{E}(X \mid B)$ is the expected value of random variable $X$ given that event $B$ occurs. Note that this is a number.

**Conditioning on Another Random Variable / 以另一个随机变量为条件：**

We can also condition on some other random variable $Y$, writing $\mathbb{E}(X \mid Y)$. In this case, the conditional expectation is also a random variable representing our "best guess" at $X$ given that we know $Y$.

**中文解释：** 我们也可以以另一个随机变量$Y$为条件，记为$\mathbb{E}(X \mid Y)$。此时条件期望也是一个随机变量，代表在已知$Y$的情况下我们对$X$的"最佳猜测"。

**Formal definition / 形式化定义：**

For the event $B = \{Y = b\}$, we define a function:
$$f(b) = \mathbb{E}(X \mid Y = b) = \sum_{s \in \mathcal{S}} s \mathbb{P}(X = s \mid Y = b)$$

Then $\mathbb{E}(X \mid Y)$ is the random variable that takes value $\mathbb{E}(X \mid Y = b)$ when $Y = b$, i.e., it is the function $f(Y)$.

**中文解释：** 首先定义函数$f(b)$为给定$Y=b$时$X$的条件期望。然后$\mathbb{E}(X \mid Y)$就是一个随机变量，当$Y=b$时取值为$f(b)$，即$f(Y)$。

##### Worked Example 1.1 / 例题1.1

**Problem / 问题：**
Let $Z_1, Z_2$ be the outcomes of rolling independent fair dice and $Y = Z_1$, $X = Z_1 + Z_2$. Find $\mathbb{E}(X \mid Y)$.

设$Z_1, Z_2$是独立公平骰子的结果，$Y = Z_1$，$X = Z_1 + Z_2$。求$\mathbb{E}(X \mid Y)$。

**Solution / 解答：**

**Step 1: Intuition / 第一步：直觉理解**

**中文解释：** 我们的最佳猜测是：已知$Y$（第一个骰子的结果），那么$X = Y + Z_2$。由于$Z_2$是独立公平骰子，其期望值为3.5。所以$\mathbb{E}(X \mid Y) = Y + 3.5$。

**English explanation:** Our best guess is: given $Y$ (the result of the first die), then $X = Y + Z_2$. Since $Z_2$ is an independent fair die, its expectation is 3.5. So $\mathbb{E}(X \mid Y) = Y + 3.5$.

**Step 2: Formal derivation / 第二步：形式化推导**

Using linearity of conditional expectation (条件期望的线性性):
$$\mathbb{E}(X \mid Y) = \mathbb{E}(Z_1 + Z_2 \mid Z_1) = \mathbb{E}(Z_1 \mid Z_1) + \mathbb{E}(Z_2 \mid Z_1)$$

**Step 3: Evaluate each term / 第三步：计算每一项**

**For $\mathbb{E}(Z_1 \mid Z_1)$:**
- **中文解释：** 如果我们已经知道$Z_1$的值，那么对$Z_1$的"最佳猜测"就是它本身。形式化地，函数$f_1(s) = s$满足$f_1(s) = \mathbb{E}(Z_1 \mid Z_1 = s)$。
- **English explanation:** If we already know the value of $Z_1$, then our "best guess" for $Z_1$ is itself. Formally, the function $f_1(s) = s$ satisfies $f_1(s) = \mathbb{E}(Z_1 \mid Z_1 = s)$.
- Therefore: $\mathbb{E}(Z_1 \mid Z_1) = Z_1$

**For $\mathbb{E}(Z_2 \mid Z_1)$:**
- **中文解释：** $Z_1$和$Z_2$独立，所以知道$Z_1$对猜测$Z_2$没有帮助。最佳猜测就是$Z_2$的无条件期望$\mathbb{E}(Z_2) = 3.5$。
- **English explanation:** $Z_1$ and $Z_2$ are independent, so knowing $Z_1$ does not help us guess $Z_2$. Our best guess is simply the unconditional expectation $\mathbb{E}(Z_2) = 3.5$.
- Formally: $f_2(s) = \mathbb{E}(Z_2) = 3.5$ for every $s \in \{1, 2, 3, 4, 5, 6\}$
- Therefore: $\mathbb{E}(Z_2 \mid Z_1) = \mathbb{E}(Z_2) = 3.5$

**Step 4: Combine / 第四步：合并**
$$\mathbb{E}(X \mid Y) = Z_1 + 3.5 = Y + 3.5$$

**Final Answer / 最终答案：**
$$\boxed{\mathbb{E}(X \mid Y) = Y + 3.5}$$

**Key insight / 关键洞察：**

**中文解释：** 另一种理解方式是：我们可以把$Y$当作已知常数，然后像计算普通期望一样计算条件期望。即$\mathbb{E}(X \mid Y) = \mathbb{E}(Y + Z_2 \mid Y) = Y + \mathbb{E}(Z_2) = Y + 3.5$。

**English explanation:** Another way to think of this: we can treat $Y$ as a known constant and then compute the conditional expectation in the same way as we did when conditioning on an event. That is, $\mathbb{E}(X \mid Y) = \mathbb{E}(Y + Z_2 \mid Y) = Y + \mathbb{E}(Z_2) = Y + 3.5$.

---

##### Formal Definition of Markov Property / 马尔可夫性质的形式化定义

**Definition 1.2 (Markov Property / 马尔可夫性质):**

Let $(X_n) = (X_0, X_1, X_2, \ldots)$ be a stochastic process in discrete time $n = 0, 1, 2, \ldots$ and discrete space $\mathcal{S}$. Then we say that $(X_n)$ has the **Markov property** if, for all times $n$ and all states $x_0, x_1, \ldots, x_n, x_{n+1} \in \mathcal{S}$ we have:

$$\mathbb{P}(X_{n+1} = x_{n+1} \mid X_n = x_n, X_{n-1} = x_{n-1}, \ldots, X_0 = x_0) = \mathbb{P}(X_{n+1} = x_{n+1} \mid X_n = x_n)$$

**中文解释：** 设$(X_n)$是一个离散时间、离散状态的随机过程。我们说$(X_n)$具有马尔可夫性质，如果对于所有时间$n$和所有状态$x_0, x_1, \ldots, x_n, x_{n+1} \in \mathcal{S}$，上式成立。

**English explanation:** Let $(X_n)$ be a stochastic process in discrete time and discrete space. We say $(X_n)$ has the Markov property if, for all times $n$ and all states, the above equation holds.

**Meaning of the equation / 等式的含义：**

| 部分 | 中文说明 | English Explanation |
|------|---------|-------------------|
| 左边 | 给定整个历史（从$X_0$到$X_n$），下一步到$x_{n+1}$的概率 | Probability of going to $x_{n+1}$ next, conditioned on the entire history |
| 右边 | 仅给定当前位置$X_n$，下一步到$x_{n+1}$的概率 | Probability of going to $x_{n+1}$ next, conditioned only on where we are now |
| 等式 | 两者相等 → 历史信息不提供额外价值 | They are equal → history provides no additional information |

**Key insight / 关键洞察：**

**中文解释：** 马尔可夫性质告诉我们：**只有当前位置重要，历史路径不重要**。这使得随机过程的研究大大简化，因为我们只需要追踪当前位置，而可以忘记之前的所有历史。

**English explanation:** The Markov property tells us: **only the current position matters, the historical path does not**. This greatly simplifies the study of stochastic processes, as we only have to keep track of where we are now and can forget about the entire history that came before.

**Continuous time version / 连续时间版本：**

**中文解释：** 对于连续时间过程也有类似的定义，我们将在课程后半部分学习。

**English explanation:** There is a similar definition for continuous time processes, which we will come to later in the course.

---

### 🔗 Connections / 知识关联

**中文解释：** 本章节的内容与课程其他部分紧密相连：

**English explanation:** This section's content is closely connected to other parts of the course:

| 连接方向 | 中文说明 | English Explanation |
|---------|---------|-------------------|
| **向前连接** | 下一节将学习最重要的离散时间马尔可夫链示例：**随机游走** | The next section will study the most important example of discrete-time Markov chains: **random walk** |
| **向后连接** | 条件概率和条件期望是概率论的基础知识 | Conditional probability and expectation are fundamental knowledge from probability theory |
| **课程后半部分** | 连续时间马尔可夫跳过程是离散时间马尔可夫链的推广 | Continuous-time Markov jump processes are generalizations of discrete-time Markov chains |
| **后续课程** | 连续时间连续空间的马尔可夫过程（如布朗运动）在MATH3734中学习 | Continuous-time continuous-space Markov processes (like Brownian motion) are studied in MATH3734 |

---

### ⚠️ Common Mistakes / 常见误区

**Mistake 1: Confusing deterministic and stochastic models / 混淆确定性和随机模型**

**中文解释：** 学生常认为"随机模型就是不确定的，所以不好"。实际上，对于复杂系统，随机模型往往更准确，因为它能反映真实世界的不确定性。

**English explanation:** Students often think "stochastic models are uncertain, so they are bad." In reality, for complex systems, stochastic models are often more accurate because they reflect the uncertainty of the real world.

**Mistake 2: Misunderstanding the Markov property / 误解马尔可夫性质**

**中文解释：** 马尔可夫性质不是说"未来独立于过去"，而是说"给定现在，未来条件独立于过去"。现在的位置提供了所有相关信息。

**English explanation:** The Markov property does NOT say "the future is independent of the past." It says "given the present, the future is conditionally independent of the past." The current position provides all relevant information.

**Mistake 3: Forgetting the positivity condition / 忘记概率为正的条件**

**中文解释：** 在写条件概率$\mathbb{P}(A \mid B)$时，总是隐含假设$\mathbb{P}(B) > 0$。如果$\mathbb{P}(B) = 0$，条件概率没有定义。

**English explanation:** When writing conditional probability $\mathbb{P}(A \mid B)$, we always implicitly assume $\mathbb{P}(B) > 0$. If $\mathbb{P}(B) = 0$, the conditional probability