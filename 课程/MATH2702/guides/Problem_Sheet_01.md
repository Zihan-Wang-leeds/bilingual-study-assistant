# Problem Sheet 1 - 详细解答 / Detailed Solutions

> MATH2702 Stochastic Processes
> 生成时间 / Generated: 2026-07-20 16:01
> 来源页 / Source Pages: 17-18

---

好的，作为您的大学数学导师，我将为您提供MATH2702：随机过程课程习题集的完整双语解答。我将严格遵循您的要求，为每个问题提供详细的逐步解答。

---

### Question 1 / 第1题

**Problem / 题目原文:**
When designing a model for a quantity that changes over time, one has many decisions to make:
• Discrete or continuous state space?
• Discrete or continuous index set for time?
• Deterministic or stochastic model?
• If a stochastic model is chosen, is it reasonable to assume that the Markov property holds?
What would you decide for the following scenarios:
(a) The percentage of UK voters with a positive opinion of the Prime Minister in a weekly tracking poll.
(b) The number of points won by a football league club throughout the season.
(c) The temperature of a bowl of water placed in an oven.
(d) The number of people inside the University of Leeds library.

**中文翻译 / Chinese Translation:**
在为随时间变化的量设计模型时，我们需要做出许多决定：
• 状态空间是离散的还是连续的？
• 时间的指标集是离散的还是连续的？
• 模型是确定性的还是随机的？
• 如果选择了随机模型，假设马尔可夫性质成立是否合理？
对于以下场景，你会如何决定：
(a) 在每周追踪民调中，对首相持正面看法的英国选民百分比。
(b) 一个足球联赛俱乐部在整个赛季中获得的积分。
(c) 放在烤箱里的一碗水的温度。
(d) 利兹大学图书馆内的人数。

**Knowledge Points / 考查知识点:**
- 随机过程建模的基本概念 / Basic concepts of stochastic process modeling
- 状态空间、时间指标集、确定性与随机性、马尔可夫性质 / State space, time index set, deterministic vs. stochastic, Markov property

**Step-by-Step Solution / 逐步解答:**

**Step 1: 分析场景 (a) - 每周追踪民调中的选民百分比 / Analyze scenario (a) - Percentage of voters in a weekly tracking poll**

**中文思路 / Chinese reasoning:** 首先，我们需要确定状态空间。百分比是一个在0到100之间的连续数值，因此状态空间是连续的。其次，时间指标集是“每周”，这意味着我们在离散的时间点（每周一次）进行观察，所以时间指标集是离散的。第三，由于民调结果会受到许多随机因素（如新闻事件、受访者情绪等）的影响，因此模型应该是随机的。最后，关于马尔可夫性质，下周的民调结果很可能不仅仅取决于本周的结果，还取决于更早的趋势或事件，因此严格满足马尔可夫性质可能不合理，但作为一个近似，可以假设当前的支持率包含了预测未来所需的大部分信息。

**English reasoning:** First, we need to determine the state space. The percentage is a continuous numerical value between 0 and 100, so the state space is continuous. Second, the time index set is "weekly," meaning we observe at discrete points in time (once a week), so the time index set is discrete. Third, because poll results are influenced by many random factors (e.g., news events, respondent mood), the model should be stochastic. Finally, regarding the Markov property, next week's poll result likely depends not only on this week's result but also on earlier trends or events, so strictly satisfying the Markov property may be unreasonable. However, as an approximation, one could assume the current approval rating contains most of the information needed to predict the future.

**Decision / 决定:**
- **State space / 状态空间:** Continuous / 连续
- **Time index / 时间指标:** Discrete / 离散
- **Model type / 模型类型:** Stochastic / 随机
- **Markov property / 马尔可夫性质:** Possibly reasonable as an approximation / 作为近似可能合理

**Step 2: 分析场景 (b) - 足球俱乐部整个赛季的积分 / Analyze scenario (b) - Points of a football club throughout the season**

**中文思路 / Chinese reasoning:** 状态空间：积分是整数（赢球得3分，平局得1分，输球得0分），因此状态空间是离散的。时间指标集：比赛是按轮次进行的，我们在每场比赛后观察积分，所以时间是离散的。模型类型：比赛结果受球队状态、对手、伤病等随机因素影响，因此是随机的。马尔可夫性质：下一场比赛后的积分完全取决于当前积分和下一场比赛的结果。而下一场比赛的结果可能不仅仅取决于当前积分（例如，球队士气可能受近期连胜或连败影响），但当前积分是预测未来积分的一个关键且充分的统计量。因此，假设马尔可夫性质是合理的。

**English reasoning:** State space: Points are integers (3 for a win, 1 for a draw, 0 for a loss), so the state space is discrete. Time index set: Matches are played in rounds, and we observe points after each match, so time is discrete. Model type: Match outcomes are influenced by random factors like team form, opponents, and injuries, so it is stochastic. Markov property: The points after the next match depend entirely on the current points and the result of the next match. While the next match's result might depend on more than just current points (e.g., team morale from a winning/losing streak), the current points are a key and sufficient statistic for predicting future points. Therefore, assuming the Markov property is reasonable.

**Decision / 决定:**
- **State space / 状态空间:** Discrete / 离散
- **Time index / 时间指标:** Discrete / 离散
- **Model type / 模型类型:** Stochastic / 随机
- **Markov property / 马尔可夫性质:** Reasonable / 合理

**Step 3: 分析场景 (c) - 烤箱中一碗水的温度 / Analyze scenario (c) - Temperature of a bowl of water in an oven**

**中文思路 / Chinese reasoning:** 状态空间：温度是一个连续的物理量，因此状态空间是连续的。时间指标集：温度是随时间连续变化的，因此时间指标集是连续的。模型类型：如果烤箱温度恒定且我们知道热力学定律，我们可以用微分方程精确预测温度变化，因此模型可以是确定性的。然而，如果考虑微小波动或初始条件的微小不确定性，随机模型也可能适用。但通常，这是一个经典的确定性过程。马尔可夫性质：在经典热力学中，未来的温度完全由当前温度决定（给定环境条件），与过去的历史无关。因此，马尔可夫性质成立。

**English reasoning:** State space: Temperature is a continuous physical quantity, so the state space is continuous. Time index set: Temperature changes continuously over time, so the time index set is continuous. Model type: If the oven temperature is constant and we know the laws of thermodynamics, we can predict the temperature change precisely using differential equations, so the model can be deterministic. However, if we consider tiny fluctuations or slight uncertainty in initial conditions, a stochastic model could also apply. Typically, this is a classic deterministic process. Markov property: In classical thermodynamics, the future temperature is completely determined by the current temperature (given environmental conditions), independent of the past history. Therefore, the Markov property holds.

**Decision / 决定:**
- **State space / 状态空间:** Continuous / 连续
- **Time index / 时间指标:** Continuous / 连续
- **Model type / 模型类型:** Deterministic / 确定性
- **Markov property / 马尔可夫性质:** Holds (for a deterministic model) / 成立（对于确定性模型）

**Step 4: 分析场景 (d) - 利兹大学图书馆内的人数 / Analyze scenario (d) - Number of people in the University of Leeds library**

**中文思路 / Chinese reasoning:** 状态空间：人数是整数（0, 1, 2, ...），因此状态空间是离散的。时间指标集：人数随时间连续变化（人们随时进出），因此时间指标集是连续的。模型类型：人们到达和离开图书馆的时间是随机的，因此模型是随机的。马尔可夫性质：未来的人数变化（例如，下一分钟的人数）很可能只取决于当前的人数，因为人们到达和离开的速率通常只与当前人数有关（例如，当图书馆满时，离开速率增加，到达速率可能减少）。因此，假设马尔可夫性质是合理的。

**English reasoning:** State space: The number of people is an integer (0, 1, 2, ...), so the state space is discrete. Time index set: The number of people changes continuously over time (people enter and leave at any time), so the time index set is continuous. Model type: The times at which people arrive and leave are random, so the model is stochastic. Markov property: The future change in the number of people (e.g., the number in the next minute) likely depends only on the current number, as the rates of arrival and departure usually depend only on the current occupancy (e.g., when the library is full, the departure rate increases and the arrival rate may decrease). Therefore, assuming the Markov property is reasonable.

**Decision / 决定:**
- **State space / 状态空间:** Discrete / 离散
- **Time index / 时间指标:** Continuous / 连续
- **Model type / 模型类型:** Stochastic / 随机
- **Markov property / 马尔可夫性质:** Reasonable / 合理

**Final Answer / 最终答案:**
| Scenario / 场景 | State Space / 状态空间 | Time Index / 时间指标 | Model Type / 模型类型 | Markov Property / 马尔可夫性质 |
| :--- | :--- | :--- | :--- | :--- |
| (a) Voter percentage / 选民百分比 | Continuous / 连续 | Discrete / 离散 | Stochastic / 随机 | Possibly reasonable / 可能合理 |
| (b) Football points / 足球积分 | Discrete / 离散 | Discrete / 离散 | Stochastic / 随机 | Reasonable / 合理 |
| (c) Water temperature / 水温 | Continuous / 连续 | Continuous / 连续 | Deterministic / 确定性 | Holds / 成立 |
| (d) Library people / 图书馆人数 | Discrete / 离散 | Continuous / 连续 | Stochastic / 随机 | Reasonable / 合理 |

**Key Insight / 解题要点:**
- 建模的第一步是明确这些基本特征，因为它们决定了使用哪种数学工具（例如，离散时间马尔可夫链、连续时间马尔可夫链、随机微分方程等）。 / The first step in modeling is to clarify these basic features, as they determine which mathematical tools to use (e.g., discrete-time Markov chains, continuous-time Markov chains, stochastic differential equations, etc.).

---

### Question 2 / 第2题

**Problem / 题目原文:**
A fair six-sided dice is rolled twice, resulting in the values $X_1, X_2 \in \{1, 2, \dots, 6\}$. Let $Y = X_1 + X_2$ be the total score. Calculate:
(a) the probability $\mathbb{P}(Y = 9)$;
(b) the conditional probability $\mathbb{P}(Y = 9 \mid X_1 = x)$ for $x = 1, 2, \dots, 6$;
(c) the conditional probability $\mathbb{P}(X_1 = x \mid Y = 9)$ for $x = 1, 2, \dots, 6$.

**中文翻译 / Chinese Translation:**
一个公平的六面骰子被掷两次，得到的结果为 $X_1, X_2 \in \{1, 2, \dots, 6\}$。令 $Y = X_1 + X_2$ 为总点数。计算：
(a) 概率 $\mathbb{P}(Y = 9)$；
(b) 条件概率 $\mathbb{P}(Y = 9 \mid X_1 = x)$，其中 $x = 1, 2, \dots, 6$；
(c) 条件概率 $\mathbb{P}(X_1 = x \mid Y = 9)$，其中 $x = 1, 2, \dots, 6$。

**Knowledge Points / 考查知识点:**
- 概率论基础 / Basic probability theory
- 条件概率 / Conditional probability
- 全概率公式 / Law of total probability
- 贝叶斯定理 / Bayes' theorem

**Step-by-Step Solution / 逐步解答:**

**(a) $\mathbb{P}(Y = 9)$**

**Step 1: 确定所有可能的结果总数 / Determine the total number of possible outcomes**

**中文思路 / Chinese reasoning:** 掷两次公平的骰子，每次有6种结果，因此总共有 $6 \times 6 = 36$ 种等可能的结果。这是计算概率的基础。

**English reasoning:** Rolling a fair die twice, each roll has 6 outcomes, so there are $6 \times 6 = 36$ equally likely outcomes in total. This is the basis for calculating the probability.

**计算过程 / Working:**
$$|\Omega| = 6 \times 6 = 36$$

**Step 2: 找出使 $Y=9$ 的结果 / Find the outcomes that result in $Y=9$**

**中文思路 / Chinese reasoning:** 我们需要找出所有 $(X_1, X_2)$ 的组合，使得 $X_1 + X_2 = 9$。由于 $X_1$ 和 $X_2$ 的取值范围都是1到6，我们可以列出所有可能的组合。

**English reasoning:** We need to find all pairs $(X_1, X_2)$ such that $X_1 + X_2 = 9$. Since $X_1$ and $X_2$ both range from 1 to 6, we can list all possible combinations.

**计算过程 / Working:**
可能的组合是 / The possible pairs are:
$(3, 6), (4, 5), (5, 4), (6, 3)$
总共有4种结果 / There are 4 such outcomes.

**Step 3: 计算概率 / Calculate the probability**

**中文思路 / Chinese reasoning:** 概率等于有利结果数除以总结果数。

**English reasoning:** The probability is the number of favorable outcomes divided by the total number of outcomes.

**计算过程 / Working:**
$$\mathbb{P}(Y=9) = \frac{\text{Number of outcomes where } Y=9}{\text{Total number of outcomes}} = \frac{4}{36} = \frac{1}{9}$$

**Explanation of working / 过程解释:** 分子4是使总和为9的组合数，分母36是所有可能的投掷结果总数。化简分数得到1/9。 / The numerator 4 is the number of combinations summing to 9, and the denominator 36 is the total number of possible roll outcomes. Simplifying the fraction gives 1/9.

**Final Answer for (a) / (a)的最终答案:**
$$\boxed{\mathbb{P}(Y=9) = \frac{1}{9}}$$

**(b) $\mathbb{P}(Y = 9 \mid X_1 = x)$ for $x = 1, 2, \dots, 6$**

**Step 1: 理解条件概率 / Understand conditional probability**

**中文思路 / Chinese reasoning:** 条件概率 $\mathbb{P}(Y=9 \mid X_1=x)$ 表示在已知第一次掷出结果为 $x$ 的条件下，两次总和为9的概率。由于两次投掷是独立的，给定 $X_1=x$ 后，$Y=9$ 当且仅当 $X_2 = 9 - x$。

**English reasoning:** The conditional probability $\mathbb{P}(Y=9 \mid X_1=x)$ is the probability that the total is 9 given that the first roll resulted in $x$. Since the two rolls are independent, given $X_1=x$, $Y=9$ if and only if $X_2 = 9 - x$.

**Step 2: 对每个 $x$ 计算概率 / Calculate the probability for each $x$**

**中文思路 / Chinese reasoning:** 对于每个 $x$，我们需要检查 $9-x$ 是否在 $X_2$ 的可能取值 $\{1, \dots, 6\}$ 内。如果在，则概率为 $1/6$（因为第二次掷出特定数字的概率是 $1/6$）；如果不在，则概率为0。

**English reasoning:** For each $x$, we need to check if $9-x$ is within the possible values of $X_2$, which is $\{1, \dots, 6\}$. If it is, the probability is $1/6$ (since the probability of rolling a specific number on the second die is $1/6$); if not, the probability is 0.

**计算过程 / Working:**
- $x=1$: $9-1=8 \notin \{1,\dots,6\}$ → $\mathbb{P}(Y=9 \mid X_1=1) = 0$
- $x=2$: $9-2=7 \notin \{1,\dots,6\}$ → $\mathbb{P}(Y=9 \mid X_1=2) = 0$
- $x=3$: $9-3=6 \in \{1,\dots,6\}$ → $\mathbb{P}(Y=9 \mid X_1=3) = \frac{1}{6}$
- $x=4$: $9-4=5 \in \{1,\dots,6\}$ → $\mathbb{P}(Y=9 \mid X_1=4) = \frac{1}{6}$
- $x=5$: $9-5=4 \in \{1,\dots,6\}$ → $\mathbb{P}(Y=9 \mid X_1=5) = \frac{1}{6}$
- $x=6$: $9-6=3 \in \{1,\dots,6\}$ → $\mathbb{P}(Y=9 \mid X_1=6) = \frac{1}{6}$

**Final Answer for (b) / (b)的最终答案:**
$$\boxed{\mathbb{P}(Y=9 \mid X_1=x) = \begin{cases} \frac{1}{6} & \text{if } x = 3, 4, 5, 6 \\ 0 & \text{if } x = 1, 2 \end{cases}}$$

**(c) $\mathbb{P}(X_1 = x \mid Y = 9)$ for $x = 1, 2, \dots, 6$**

**Step 1: 应用贝叶斯定理 / Apply Bayes' theorem**

**中文思路 / Chinese reasoning:** 我们需要计算在已知总和为9的条件下，第一次掷出特定数字的概率。这可以使用条件概率的定义或贝叶斯定理。最直接的方法是使用条件概率公式：$\mathbb{P}(X_1=x \mid Y=9) = \frac{\mathbb{P}(X_1=x \text{ and } Y=9)}{\mathbb{P}(Y=9)}$。

**English reasoning:** We need to calculate the probability of rolling a specific number on the first roll given that the total is 9. This can be done using the definition of conditional probability or Bayes' theorem. The most direct method is to use the conditional probability formula: $\mathbb{P}(X_1=x \mid Y=9) = \frac{\mathbb{P}(X_1=x \text{ and } Y=9)}{\mathbb{P}(Y=9)}$.

**Step 2: 计算联合概率 $\mathbb{P}(X_1=x \text{ and } Y=9)$ / Calculate the joint probability $\mathbb{P}(X_1=x \text{ and } Y=9)$**

**中文思路 / Chinese reasoning:** 事件 $\{X_1=x \text{ and } Y=9\}$ 等价于 $\{X_1=x \text{ and } X_2=9-x\}$。只有当 $9-x$ 在1到6之间时，这个事件才可能发生。由于两次投掷独立，其概率为 $\mathbb{P}(X_1=x) \times \mathbb{P}(X_2=9-x) = \frac{1}{6} \times \frac{1}{6} = \frac{1}{36}$。

**English reasoning:** The event $\{X_1=x \text{ and } Y=9\}$ is equivalent to $\{X_1=x \text{ and } X_2=9-x\}$. This event is only possible if $9-x$ is between 1 and 6. Since the two rolls are independent, its probability is $\mathbb{P}(X_1=x) \times \mathbb{P}(X_2=9-x) = \frac{1}{6} \times \frac{1}{6} = \frac{1}{36}$.

**计算过程 / Working:**
- For $x=3, 4, 5, 6$: $\mathbb{P}(X_1=x \text{ and } Y=9) = \frac{1}{36}$
- For $x=1, 2$: $\mathbb{P}(X_1=x \text{ and } Y=9) = 0$

**Step 3: 计算条件概率 / Calculate the conditional probability**

**中文思路 / Chinese reasoning:** 使用条件概率公式，将联合概率除以 $P(Y=9) = 4/36$。

**English reasoning:** Use the conditional probability formula, dividing the joint probability by $P(Y=9) = 4/36$.

**计算过程 / Working:**
- For $x=3, 4, 5, 6$:
$$\mathbb{P}(X_1=x \mid Y=9) = \frac{1/36}{4/36} = \frac{1}{4}$$
- For $x=1, 2$:
$$\mathbb{P}(X_1=x \mid Y=9) = \frac{0}{4/36} = 0$$

**Final Answer for (c) / (c)的最终答案:**
$$\boxed{\mathbb{P}(X_1=x \mid Y=9) = \begin{cases} \frac{1}{4} & \text{if } x = 3, 4, 5, 6 \\ 0 & \text{if } x = 1, 2 \end{cases}}$$

**Key Insight / 解题要点:**
- 条件概率 $\mathbb{P}(Y=9 \mid X_1=x)$ 和 $\mathbb{P}(X_1=x \mid Y=9)$ 是不同的。前者是在知道第一次结果后对总和的预测，后者是在知道总和后对第一次结果的推断。贝叶斯定理是连接这两种条件概率的桥梁。 / Conditional probabilities $\mathbb{P}(Y=9 \mid X_1=x)$ and $\mathbb{P}(X_1=x \mid Y=9)$ are different. The former is a prediction of the sum given the first roll, the latter is an inference about the first roll given the sum. Bayes' theorem is the bridge connecting these two types of conditional probabilities.

---

### Question 3 / 第3题

**Problem / 题目原文:**
Let $(X_n)$ be a simple random walk starting from $X_0 = 0$ and that at each step goes up one with probability $p$ or down one with probability $q = 1-p$. What are:
(a) $\mathbb{P}(X_5 = 3)$,
(b) $\mathbb{P}(X_5 = 3 \mid X_2 = 2)$,
(c) $\mathbb{P}(X_n = n-2)$,
(d) $\mathbb{E}X_4$,
(e) $\mathbb{E}(X_6 \mid X_4)$,

**中文翻译 / Chinese Translation:**
令 $(X_n)$ 为一个简单随机游走，从 $X_0 = 0$ 开始，每一步以概率 $p$ 向上移动一步，或以概率 $q = 1-p$ 向下移动一步。求：
(a) $\mathbb{P}(X_5 = 3)$，
(b) $\mathbb{P}(X_5 = 3 \mid X_2 = 2)$，
(c) $\mathbb{P}(X_n = n-2)$，
(d) $\mathbb{E}X_4$，
(e) $\mathbb{E}(X_6 \mid X_4)$。

**Knowledge Points / 考查知识点:**
- 简单随机游走的分布 / Distribution of a simple random walk
- 二项分布 / Binomial distribution
- 马尔可夫性质 / Markov property
- 条件期望 / Conditional expectation

**Step-by-Step Solution / 逐步解答:**

**(a) $\mathbb{P}(X_5 = 3)$**

**Step 1: 确定向上和向下的步数 / Determine the number of up and down steps**

**中文思路 / Chinese reasoning:** 随机游走 $X_n$ 表示在 $n$ 步之后的位置。如果向上走了 $u$ 步，向下走了 $d$ 步，那么 $n = u + d$，并且位置 $X_n = u - d$。我们要求 $X_5 = 3$，所以有 $u + d = 5$ 和 $u - d = 3$。解这个方程组得到 $u$ 和 $d$。

**English reasoning:** The random walk $X_n$ represents the position after $n$ steps. If there are $u$ up steps and $d$ down steps, then $n = u + d$, and the position $X_n = u - d$. We require $X_5 = 3$, so we have $u + d = 5$ and $u - d = 3$. Solving this system gives $u$ and $d$.

**计算过程 / Working:**
$$u + d = 5$$
$$u - d = 3$$
相加得 / Adding gives: $2u = 8 \Rightarrow u = 4$
相减得 / Subtracting gives: $2d = 2 \Rightarrow d = 1$
所以，在5步中，需要向上4步，向下1步。 / So, in 5 steps, we need 4 up steps and 1 down step.

**Step 2: 计算概率 / Calculate the probability**

**中文思路 / Chinese reasoning:** 在 $n=5$ 步中，有 $u=4$ 次向上和 $d=1$ 次向下。这是一个二项分布问题。选择哪一步是向下的有 $\binom{5}{1}$ 种方式。每一步向上的概率是 $p$，向下的概率是 $q$。

**English reasoning:** In $n=5$ steps, we have $u=4$ up steps and $d=1$ down step. This is a binomial distribution problem. There are $\binom{5}{1}$ ways to choose which step is the down step. The probability of an up step is $p$, and a down step is $q$.

**计算过程 / Working:**
$$\mathbb{P}(X_5 = 3) = \binom{5}{1} p^4 q^1 = 5 p^4 q$$

**Explanation of working / 过程解释:** $\binom{5}{1}$ 表示从5步中选择1步作为向下步的组合数。$p^4$ 是4次向上的概率，$q^1$ 是1次向下的概率。 / $\binom{5}{1}$ is the number of ways to choose 1 step out of 5 to be the down step. $p^4$ is the probability of 4 up steps, and $q^1$ is the probability of 1 down step.

**Final Answer for (a) / (a)的最终答案:**
$$\boxed{\mathbb{P}(X_5 = 3) = 5 p