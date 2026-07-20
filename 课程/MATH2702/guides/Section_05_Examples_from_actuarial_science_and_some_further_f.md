# Section 5: Examples from actuarial science and some further fun examples

> MATH2702 - 自学教材 / Self-Study Guide
> 生成时间: 2026-07-20 15:38
> 来源页: 30-34

---

# MATH2702: Stochastic Processes / 随机过程

## Section 5: Examples from Actuarial Science and Further Fun Examples / 精算学实例与更多趣味例子

---

### 📋 Section Overview / 章节概览

**中文解释：** 本章节将介绍几个来自精算学和物理学的实际例子，展示如何运用马尔可夫链（Markov chain）和鞅（martingale）等随机过程工具来解决实际问题。这些例子包括：汽车保险的无索赔折扣模型、猴子打字问题（一个有趣的鞅例子）、具有记忆的事故模型，以及物理学中的伊辛模型（Ising model）。通过这些例子，你将学会如何识别一个过程是否为马尔可夫链，以及当过程不是马尔可夫链时，如何通过巧妙的方法（如扩展状态空间或变换随机变量）将其转化为马尔可夫链。

**English explanation:** This section introduces several practical examples from actuarial science and physics, demonstrating how to apply stochastic process tools such as Markov chains and martingales to solve real-world problems. These examples include: a simple no-claims discount model for motor insurance, a monkey typing problem (a fun martingale example), an accident model with memory, and the Ising model from physics. Through these examples, you will learn how to identify whether a process is a Markov chain, and when it is not, how to cleverly transform it into a Markov chain (by expanding the state space or transforming random variables).

---

### 🎯 Learning Objectives / 学习目标

完成本章学习后，你应该能够：

1. **构建马尔可夫链模型**：能够将简单的保险折扣系统建模为马尔可夫链，并计算转移概率矩阵。
2. **应用鞅与可选停止定理**：理解如何使用鞅和可选停止定理（Optional Stopping Theorem）计算复杂随机事件的期望时间。
3. **识别非马尔可夫过程**：能够判断一个随机过程是否满足马尔可夫性质。
4. **转化非马尔可夫过程**：学会通过重新定义状态空间或变换随机变量，将非马尔可夫过程转化为马尔可夫链。
5. **理解时间齐次与非齐次马尔可夫链**：区分时间齐次（time-homogeneous）和时间非齐次（time-inhomogeneous）马尔可夫链。
6. **认识伊辛模型**：了解伊辛模型的基本概念及其与马尔可夫链的联系。

After completing this section, you should be able to:
1. **Construct Markov chain models**: Model simple insurance discount systems as Markov chains and compute transition probability matrices.
2. **Apply martingales and optional stopping**: Use martingales and the Optional Stopping Theorem to calculate expected times of complex random events.
3. **Identify non-Markov processes**: Determine whether a stochastic process satisfies the Markov property.
4. **Transform non-Markov processes**: Learn to convert non-Markov processes into Markov chains by redefining the state space or transforming random variables.
5. **Understand time-homogeneous vs. time-inhomogeneous Markov chains**: Distinguish between these two types of Markov chains.
6. **Recognize the Ising model**: Understand the basic concepts of the Ising model and its connection to Markov chains.

---

### 📚 Prerequisites / 前置知识

在开始本章之前，你应该已经掌握：

- **马尔可夫链的基本概念**：状态空间、转移概率、转移矩阵、n步转移概率
- **条件概率与条件期望**：特别是条件概率的定义和计算
- **鞅的基本概念**：鞅的定义、可选停止定理
- **矩阵乘法**：能够计算矩阵的幂

Before starting this section, you should already know:
- **Basic concepts of Markov chains**: state space, transition probabilities, transition matrix, n-step transition probabilities
- **Conditional probability and conditional expectation**: especially the definition and calculation of conditional probability
- **Basic concepts of martingales**: definition of martingale, Optional Stopping Theorem
- **Matrix multiplication**: ability to compute powers of matrices

---

## 📖 Core Content / 核心内容

---

### Topic 5.1: A Simple No-Claims Discount Model / 简单的无索赔折扣模型

#### Intuition / 直觉理解

**中文解释：** 想象你是一家汽车保险公司的精算师。公司为投保人提供折扣奖励：如果一年内没有发生事故，投保人可以获得更高的折扣；如果发生事故，折扣会降低。这种系统天然地具有"记忆"——未来的折扣水平只取决于当前的折扣水平和是否发生事故，而与更早的历史无关。这正是马尔可夫性质的核心思想：未来只依赖于现在，而不依赖于过去。

**English explanation:** Imagine you are an actuary at a car insurance company. The company offers discount rewards to policyholders: if no accident occurs in a year, the policyholder moves up to a higher discount level; if an accident occurs, the discount decreases. This system naturally has "memory" — the future discount level depends only on the current discount level and whether an accident occurs, not on the earlier history. This is exactly the core idea of the Markov property: the future depends only on the present, not on the past.

#### Formal Definition / 形式化定义

**中文解释：** 保险公司将投保人分为三个折扣等级：
- **状态1（State 1）**：无折扣（no discount）
- **状态2（State 2）**：25%折扣（25% discount）
- **状态3（State 3）**：50%折扣（50% discount）

新投保人从无折扣（状态1）开始。规则如下：
- 如果一年内无索赔（accident-free），投保人上升一个折扣等级。如果已经在状态3且无索赔，则保持在状态3。
- 如果一年内至少有一次索赔（at least one claim），投保人下降一个折扣等级。如果已经在状态1且有索赔，则保持在状态1。

保险公司估计，投保人无索赔年的概率为 $\frac{3}{4}$。

**English explanation:** The insurance company classifies policyholders into three discount levels:
- **State 1**: No discount
- **State 2**: 25% discount
- **State 3**: 50% discount

New policyholders start with no discount (state 1). The rules are:
- If a year is accident-free, the policyholder moves up one discount level. If already in state 3 and accident-free, they remain in state 3.
- If a year has at least one claim, the policyholder moves down one discount level. If already in state 1 and has a claim, they remain in state 1.

The insurance company believes the probability of a claim-free year is $\frac{3}{4}$.

**马尔可夫链的构建 / Construction of the Markov chain:**

这是一个直接的马尔可夫链模型：
- **状态空间（state space）** $\mathcal{S} = \{1, 2, 3\}$ 是离散的
- **时间指标（time index）** 是离散的，每年一个折扣水平
- **马尔可夫性质（Markov property）** 成立：未来状态的概率完全由当前状态决定
- **时间齐次（time-homogeneous）**：一步转移概率不随时间变化

This is a direct Markov chain model:
- The state space $\mathcal{S} = \{1, 2, 3\}$ is discrete
- The time index is discrete, with one discount level per year
- The Markov property holds: the probability of being in a certain state at a future time is completely determined by the present state
- It is time-homogeneous: the one-step transition probabilities are not time-dependent

**转移概率矩阵 / Transition Probability Matrix:**

$$P = $$
\begin{pmatrix}
\frac{1}{4} & \frac{3}{4} & 0 \\
\frac{1}{4} & 0 & \frac{3}{4} \\
0 & \frac{1}{4} & \frac{3}{4}
\end{pmatrix}
$$$$

**符号解释 / Symbol Explanation:**

| Symbol / 符号 | Meaning / 含义 |
|:---:|:---|
| $P_{ij}$ | 从状态i到状态j的一步转移概率 / One-step transition probability from state i to state j |
| $\frac{1}{4}$ | 有索赔的概率（1 - 3/4）/ Probability of having a claim |
| $\frac{3}{4}$ | 无索赔的概率 / Probability of being claim-free |
| $0$ | 不可能的直接转移 / Impossible direct transition |

**转移图 / Transition Diagram:**

```
1 → 2 → 3
↑   ↓   ↑
└───┴───┘
```

具体来说：
- 从状态1：有1/4的概率留在状态1（有索赔），3/4的概率到状态2（无索赔）
- 从状态2：有1/4的概率回到状态1（有索赔），3/4的概率到状态3（无索赔）
- 从状态3：有1/4的概率回到状态2（有索赔），3/4的概率留在状态3（无索赔）

Specifically:
- From state 1: probability 1/4 to stay in state 1 (claim), 3/4 to go to state 2 (no claim)
- From state 2: probability 1/4 to go back to state 1 (claim), 3/4 to go to state 3 (no claim)
- From state 3: probability 1/4 to go back to state 2 (claim), 3/4 to stay in state 3 (no claim)

#### Worked Example / 例题

**Example 5.1 / 例5.1**

**问题 / Problem:** 假设你目前没有折扣（状态1），问三年后你获得50%折扣（状态3）的概率是多少？

What is the probability of having a 50% reduction to your premium three years from now, given that you currently have no reduction on the premium?

**解 / Solution:**

我们需要计算三步转移概率 $p_{13}(3) = \mathbb{P}(X_3 = 3 \mid X_0 = 1)$。

We need to find the three-step transition probability $p_{13}(3) = \mathbb{P}(X_3 = 3 \mid X_0 = 1)$.

**方法一：路径求和法 / Method 1: Path Summation**

**中文解释：** 我们找出所有从状态1出发，经过三步到达状态3的路径。每条路径的概率等于各步转移概率的乘积。然后将所有路径的概率相加。

**English explanation:** We find all paths starting from state 1 that reach state 3 in exactly three steps. The probability of each path is the product of the transition probabilities along the path. Then we sum the probabilities of all such paths.

可能的路径（Possible paths）：
1. $1 \rightarrow 1 \rightarrow 2 \rightarrow 3$
2. $1 \rightarrow 2 \rightarrow 3 \rightarrow 3$

计算每条路径的概率（Calculate the probability of each path）：

路径1（Path 1）：
$$p_{11} \cdot p_{12} \cdot p_{23} = \frac{1}{4} \cdot \frac{3}{4} \cdot \frac{3}{4} = \frac{9}{64}$$

路径2（Path 2）：
$$p_{12} \cdot p_{23} \cdot p_{33} = \frac{3}{4} \cdot \frac{3}{4} \cdot \frac{3}{4} = \frac{27}{64}$$

总和（Sum）：
$$p_{13}(3) = \frac{9}{64} + \frac{27}{64} = \frac{36}{64} = \frac{9}{16}$$

**方法二：矩阵乘法法 / Method 2: Matrix Multiplication**

**中文解释：** 三步转移概率矩阵 $P^{(3)}$ 等于 $P^3 = P \cdot P \cdot P$。我们可以通过矩阵乘法计算。

**English explanation:** The three-step transition probability matrix $P^{(3)}$ equals $P^3 = P \cdot P \cdot P$. We can compute this by matrix multiplication.

$$P^3 = P \cdot P \cdot P = \frac{1}{64} $$
\begin{pmatrix}
7 & 21 & 36 \\
7 & 12 & 45 \\
4 & 15 & 45
\end{pmatrix}
$$$$

**符号解释 / Symbol Explanation:**

| Entry / 元素 | Meaning / 含义 |
|:---:|:---|
| 右上角元素36/64 | $p_{13}(3)$，从状态1到状态3的三步概率 / Three-step probability from state 1 to state 3 |
| 其他元素 | 其他状态之间的三步转移概率 / Other three-step transition probabilities |

因此，$p_{13}(3) = \frac{36}{64} = \frac{9}{16}$，与路径求和法结果一致。

Therefore, $p_{13}(3) = \frac{36}{64} = \frac{9}{16}$, which matches the path summation result.

---

### Topic 5.2: A Fun Martingale Example - The Monkey Typing Problem / 有趣的鞅例子 - 猴子打字问题

#### Intuition / 直觉理解

**中文解释：** 想象一只猴子在打字机上随机敲击键盘，每次从26个英文字母中均匀随机选择一个。我们想知道，猴子需要敲击多少次，才能首次打出单词"ABRACADABRA"？这个问题看似简单，但直接计算非常复杂。一个巧妙的方法是使用"赌徒策略"：在每个新字母被敲击之前，都有一个赌徒加入游戏，他们按照特定的策略下注，直到单词被完整打出。通过分析赌徒的总财富，我们可以利用鞅和可选停止定理来求出期望打字次数。

**English explanation:** Imagine a monkey randomly typing on a keyboard, each time uniformly selecting one of the 26 English letters. We want to know: how many keystrokes are needed for the monkey to first type the word "ABRACADABRA"? This problem seems simple but is very complex to compute directly. A clever approach uses a "gambler strategy": before each new letter is typed, a new gambler joins the game, betting according to a specific strategy until the word is completely typed. By analyzing the total wealth of all gamblers, we can use martingales and the Optional Stopping Theorem to find the expected number of keystrokes.

#### Formal Definition / 形式化定义

**中文解释：** 猴子每次从26个字母中独立均匀随机地选择一个字母，即每个字母被选中的概率为 $\frac{1}{26}$。设 $T$ 为首次出现单词"ABRACADABRA"时已经打出的字母总数。我们要求 $\mathbb{E}(T)$。

**English explanation:** The monkey repeatedly types any of the 26 letters of the English alphabet independently with equal probability $\frac{1}{26}$. Let $T$ be the total number of letters that have been typed when the entire word "ABRACADABRA" first appears. We want to find $\mathbb{E}(T)$.

**赌徒策略 / Gambler Strategy:**

**中文解释：** 在每个新字母被敲击之前，都有一个赌徒加入游戏。每个赌徒的策略如下：
1. 先押注£1赌下一个字母是"A"。如果不是"A"，赌徒输光并退出游戏。
2. 如果是"A"，赌徒赢得£26，然后将全部£26押注下一个字母是"B"。
3. 如果不是"B"，赌徒输光并退出。如果是"B"，赌徒赢得£26²，然后押注第三个字母是"R"。
4. 如此继续，直到赌徒输光，或者单词"ABRACADABRA"被完整打出。如果单词被完整打出，赌徒带着£26¹¹退出游戏。

**English explanation:** Before each new letter is typed, a new gambler arrives. Each gambler follows this strategy:
1. First bets £1 on the letter "A". If the letter typed is not "A", the gambler loses and exits the game.
2. If the letter typed is "A", the gambler receives £26 and then bets this entire amount on the next letter being "B".
3. If the next letter is not "B", the gambler loses everything and exits. If it is "B", they receive £26² and bet on the third letter being "R".
4. This continues until the gambler loses or until "ABRACADABRA" has been typed out, in which case they exit with £26¹¹.

**注意 / Note:** 单词"ABRACADABRA"有11个字母，所以最大赢利是£26¹¹。

**Note:** The word "ABRACADABRA" has 11 letters, so the maximum winnings are £26¹¹.

#### 鞅的构建 / Construction of the Martingale

**中文解释：** 设 $X_n$ 为第 $n$ 个字母被敲击后，所有仍在游戏中的赌徒的总财富。定义 $M_n = X_n - n$。可以证明 $M_n$ 是一个鞅。

**English explanation:** Let $X_n$ be the total wealth of all gamblers in play after the $n$th letter has been typed. Define $M_n = X_n - n$. It can be shown that $M_n$ is a martingale.

**为什么是鞅？/ Why is it a martingale?**

**中文解释：** 在游戏进行过程中，每个仍在游戏中的赌徒有 $\frac{25}{26}$ 的概率输光所有钱，有 $\frac{1}{26}$ 的概率将钱翻26倍。已经输光的赌徒财富保持为0。因此，除了新加入的赌徒带来£1之外，所有赌徒的总财富期望值不变。所以：

$$\mathbb{E}(M_{n+1} \mid X_1, \ldots, X_n) = X_n + 1 - (n+1) = X_n - n = M_n$$

同时，$\mathbb{E}|M_n| < \infty$ 也很容易验证（它被 $n$ 和 $26$ 的幂次之和的上界所控制）。

**English explanation:** While the game is still running, each gambler still in play loses their money with probability $\frac{25}{26}$ and multiplies it by 26 with probability $\frac{1}{26}$. Gamblers that have already lost remain at 0 winnings. So the gamblers' total wealth does not change except for the new gambler who brings in £1. Hence:

$$\mathbb{E}(M_{n+1} \mid X_1, \ldots, X_n) = X_n + 1 - (n+1) = X_n - n = M_n$$

Also, $\mathbb{E}|M_n| < \infty$ is easy to see (it is bounded above by the maximum of $n$ and a finite sum of 26 raised to powers $\leq 11$).

#### 应用可选停止定理 / Applying the Optional Stopping Theorem

**中文解释：** 停止鞅 $M_{T \wedge n}$ 是有界的（被 $1 + 26 + 26^2 + \ldots + 26^{11}$ 所界），且 $\mathbb{P}(T < \infty) = 1$（因为 $T$ 被几何随机变量所控制），所以我们可以使用可选停止定理。

**English explanation:** The stopped martingale $M_{T \wedge n}$ is bounded (by $1 + 26 + 26^2 + \ldots + 26^{11}$) and $\mathbb{P}(T < \infty) = 1$ (it is dominated by a geometric random variable), so we can use optional stopping.

$$0 = \mathbb{E}(M_0) = \mathbb{E}(M_T) = \mathbb{E}(X_T) - \mathbb{E}(T)$$

因此 $\mathbb{E}(T) = \mathbb{E}(X_T)$。

Therefore $\mathbb{E}(T) = \mathbb{E}(X_T)$.

#### 关键观察 / Key Observation

**中文解释：** 在时间 $T$（游戏停止时），只有3个赌徒仍在游戏中：
1. 在 $T-11$ 时刻加入的赌徒，成功押注了整个单词"ABRACADABRA"，赢得了 £26¹¹
2. 在 $T-4$ 时刻加入的赌徒，成功押注了"ABRA"（前4个字母），赢得了 £26⁴
3. 在 $T$ 时刻刚刚加入的赌徒，成功押注了"A"，赢得了 £26

**English explanation:** At time $T$ (when the game stops), there are only 3 gamblers in play:
1. The one who arrived at $T-11$ and won £26¹¹ by successfully betting on "ABRACADABRA"
2. The one who arrived at $T-4$ and won £26⁴ by successfully betting on "ABRA"
3. The one who just arrived at $T$ and won £26 by successfully betting on "A"

**为什么是这些赌徒？/ Why these gamblers?**

**中文解释：** 这是因为单词"ABRACADABRA"具有自相似性（self-similarity）。注意"ABRA"是单词的前4个字母，而"A"是第一个字母。当单词被完整打出时，最后几个字母恰好与单词的开头部分匹配，这使得之前的一些赌徒也获得了成功。

**English explanation:** This is because the word "ABRACADABRA" has self-similarity. Note that "ABRA" is the first 4 letters of the word, and "A" is the first letter. When the complete word is typed, the last few letters happen to match the beginning of the word, which allows some earlier gamblers to also be successful.

**计算期望值 / Computing the Expected Value:**

$$\mathbb{E}(T) = \mathbb{E}(X_T) = X_T = 26^{11} + 26^4 + 26 \approx 3.7 \times 10^{15}$$

**中文解释：** 这个数字大得惊人！如果猴子每秒打一个字母，大约需要1亿年才能打出"ABRACADABRA"。注意，单词中的重复模式（"ABRA"和"A"）导致了期望值中的 $26^4$ 和 $26$ 项，增加了期望时间。

**English explanation:** This number is astonishingly large! If the monkey types one letter per second, it would take about 100 million years to type "ABRACADABRA". Notice that the repetitions in "ABRACADABRA" led to the terms $26^4$ and $26$ being included in $\mathbb{E}(T)$, increasing it.

---

### Topic 5.3: An Accident Model with Memory / 具有记忆的事故模型

#### Intuition / 直觉理解

**中文解释：** 有时候，我们面对的自然随机过程并不是马尔可夫链。例如，一个驾驶员的事故概率可能取决于他过去所有年份的事故总数，而不仅仅是最近一年的情况。这种情况下，如果我们直接使用"每年是否有事故"作为状态，过程就不满足马尔可夫性质。但是，我们可以通过巧妙地重新定义随机变量，将非马尔可夫过程转化为马尔可夫链。

**English explanation:** Sometimes, the natural stochastic process we face is not a Markov chain. For example, a driver's accident probability may depend on the total number of accidents in all past years, not just the most recent year. In this case, if we directly use "whether there was an accident each year" as the state, the process does not satisfy the Markov property. However, we can cleverly redefine the random variable to convert the non-Markov process into a Markov chain.

#### Formal Definition / 形式化定义

**中文解释：** 考虑一个不同的驾驶员事故模型。设 $Y_n$ 为第 $n$ 年是否有事故的随机变量：
- $Y_n = 0$：第 $n$ 年无事故（no accident）
- $Y_n = 1$：第 $n$ 年有一次事故（one accident）

（模型不允许一年内发生多次事故。）

**English explanation:** Consider a different driver accident model. Let $Y_n$ be a random variable indicating whether there is an accident in year $n$:
- $Y_n = 0$: no accident in year $n$
- $Y_n = 1$: one accident in year $n$

(The model does not allow for more than one accident in a year.)

**事故概率模型 / Accident Probability Model:**

$$\mathbb{P}(Y_{n+1} = 1 \mid Y_n = y_n, \ldots, Y_2 = y_2, Y_1 = y_1) = \frac{f(y_1 + y_2 + \cdots + y_n)}{g(n)}$$

且 $Y_{n+1} = 0$ 否则（otherwise），其中 $f$ 和 $g$ 是非负递增函数，且对所有 $m$ 满足 $0 \leq f(m) \leq g(m)$。

**符号解释 / Symbol Explanation:**

| Symbol / 符号 | Meaning / 含义 |
|:---:|:---|
| $y_1 + \cdots + y_n$ | 前n年的总事故数 / Total number of accidents in the first n years |
| $f(m)$ | 与总事故数相关的函数 / Function related to total accident count |
| $g(n)$ | 与年数相关的函数 / Function related to number of years |
| $f$ 递增 | 事故越多，未来事故概率越高 / More accidents → higher future accident probability |
| $g$ 递增 | 年数越多，相同事故数下未来事故概率越低 / More years → lower future accident probability for same accident count |

#### 为什么 $(Y_n)$ 不是马尔可夫链？/ Why is $(Y_n)$ not a Markov chain?

**中文解释：** 很明显，$Y_{n+1}$ 不仅依赖于 $Y_n$（今年的事故数），还依赖于整个历史 $Y_1, Y_2, \ldots, Y_n$。因为概率公式中的分子 $f(y_1 + \cdots + y_n)$ 依赖于所有过去年份的事故总数。这违反了马尔可夫性质。

**English explanation:** It's clear that $Y_{n+1}$ depends not only on $Y_n$ (the number of accidents this year), but on the entire history $Y_1, Y_2, \ldots, Y_n$. This is because the numerator $f(y_1 + \cdots + y_n)$ in the probability formula depends on the total number of accidents in all past years. This violates the Markov property.

#### 巧妙的解决方法 / Clever Workaround

**中文解释：** 定义 $X_n = \sum_{i=1}^n Y_i$ 为截至第 $n$ 年的总事故数。那么 $(X_n)$ 是一个马尔可夫链！

**English explanation:** Define $X_n = \sum_{i=1}^n Y_i$ to be the total number of accidents up to year $n$. Then $(X_n)$ is a Markov chain!

**验证马尔可夫性质 / Verifying the Markov Property:**

$$\mathbb{P}(X_{n+1} = x_n + 1 \mid X_n = x_n, \ldots, X_2 = x_2, X_1 = x_1)$$

$$= \mathbb{P}(Y_{n+1} = 1 \mid Y_n = x_n - x_{n-1}, \ldots, Y_2 = x_2 - x_1, Y_1 = x_1)$$

$$= \frac{f((x_n - x_{