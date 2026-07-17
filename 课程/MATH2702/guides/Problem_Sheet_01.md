# Problem Sheet 1 - 详细解答 / Detailed Solutions

> MATH2702 Stochastic Processes
> 生成时间 / Generated: 2026-07-17 15:10
> 来源页 / Source Pages: 17-18

---

好的，作为大学随机过程课程的导师，我将为您提供这份习题集的完整、逐步的解答。

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

**中文翻译:**
在为随时间变化的量设计模型时，需要做出许多决定：
*   状态空间是离散的还是连续的？
*   时间的索引集是离散的还是连续的？
*   模型是确定性的还是随机的？
*   如果选择了随机模型，假设马尔可夫性质成立是否合理？
对于以下场景，你会如何决定：
(a) 每周追踪民调中，对首相持正面看法的英国选民百分比。
(b) 一个足球联赛俱乐部在整个赛季中获得的积分。
(c) 放入烤箱的一碗水的温度。
(d) 利兹大学图书馆内的人数。

**Knowledge Points / 考查知识点:**
- 随机过程建模的基本概念：状态空间、时间索引集、确定性与随机性、马尔可夫性质。

**Step-by-Step Solution / 逐步解答:**

**(a) The percentage of UK voters with a positive opinion of the Prime Minister in a weekly tracking poll.**
*   **Step 1: State Space / 状态空间**
    *   **What:** The percentage is a continuous value between 0% and 100%.
    *   **Why:** It can take any real number in that interval (e.g., 42.5%, 51.3%).
    *   **Decision:** Continuous state space.
*   **Step 2: Time Index Set / 时间索引集**
    *   **What:** The poll is conducted weekly.
    *   **Why:** Observations are made at specific, separate points in time (week 1, week 2, ...).
    *   **Decision:** Discrete time index set.
*   **Step 3: Deterministic or Stochastic / 确定性或随机性**
    *   **What:** The percentage is influenced by many unpredictable factors (news events, economic data, etc.).
    *   **Why:** It's impossible to predict the exact future percentage with certainty.
    *   **Decision:** Stochastic model.
*   **Step 4: Markov Property / 马尔可夫性质**
    *   **What:** The Markov property means the future depends only on the present, not the past.
    *   **Why:** Public opinion often has momentum. Today's approval rating is a strong predictor of next week's, but the full history of how we got there might also matter (e.g., a long-term trend). However, as a first approximation, the Markov property is often assumed in such models (e.g., polling models). It's a reasonable simplifying assumption, though not perfectly accurate.
    *   **Decision:** Reasonable to assume as a first approximation.

**(b) The number of points won by a football league club throughout the season.**
*   **Step 1: State Space / 状态空间**
    *   **What:** Points are awarded in whole numbers (0 for a loss, 1 for a draw, 3 for a win).
    *   **Why:** The total is a sum of these integer values.
    *   **Decision:** Discrete state space.
*   **Step 2: Time Index Set / 时间索引集**
    *   **What:** Points are updated after each match, which occurs at discrete times.
    *   **Why:** The season is a sequence of match days.
    *   **Decision:** Discrete time index set.
*   **Step 3: Deterministic or Stochastic / 确定性或随机性**
    *   **What:** The outcome of each match is uncertain.
    *   **Why:** It depends on the performance of the team and its opponents, which is random.
    *   **Decision:** Stochastic model.
*   **Step 4: Markov Property / 马尔可夫性质**
    *   **What:** Does the future points total depend only on the current total?
    *   **Why:** The current points total is a summary of past performance. However, the *distribution* of future points might depend on more than just the current total (e.g., the team's morale, injuries, which are not captured by the points total alone). But if we define the state as just the points total, the Markov property is a simplification. It's a reasonable starting point for a simple model.
    *   **Decision:** Reasonable to assume as a first approximation.

**(c) The temperature of a bowl of water placed in an oven.**
*   **Step 1: State Space / 状态空间**
    *   **What:** Temperature is a continuous physical quantity.
    *   **Why:** It can take any real value within a range.
    *   **Decision:** Continuous state space.
*   **Step 2: Time Index Set / 时间索引集**
    *   **What:** Temperature changes continuously over time.
    *   **Why:** It's a physical process that doesn't jump from one value to another at discrete instants.
    *   **Decision:** Continuous time index set.
*   **Step 3: Deterministic or Stochastic / 确定性或随机性**
    *   **What:** The heating process is governed by the laws of thermodynamics.
    *   **Why:** Given the oven temperature, the initial water temperature, and the bowl's properties, the temperature at any future time can be predicted with high accuracy using Newton's Law of Cooling/Heating. There is very little randomness.
    *   **Decision:** Deterministic model.
*   **Step 4: Markov Property / 马尔可夫性质**
    *   **What:** N/A for a deterministic model.
    *   **Why:** The Markov property is a concept for stochastic processes.
    *   **Decision:** Not applicable.

**(d) The number of people inside the University of Leeds library.**
*   **Step 1: State Space / 状态空间**
    *   **What:** The number of people is a count.
    *   **Why:** It can only be a non-negative integer (0, 1, 2, ...).
    *   **Decision:** Discrete state space.
*   **Step 2: Time Index Set / 时间索引集**
    *   **What:** The number changes whenever someone enters or leaves.
    *   **Why:** These events can happen at any moment. The process evolves continuously.
    *   **Decision:** Continuous time index set.
*   **Step 3: Deterministic or Stochastic / 确定性或随机性**
    *   **What:** The arrivals and departures of individuals are unpredictable.
    *   **Why:** We cannot know exactly when the next person will walk in.
    *   **Decision:** Stochastic model.
*   **Step 4: Markov Property / 马尔可夫性质**
    *   **What:** Does the future number of people depend only on the current number?
    *   **Why:** The time until the next arrival or departure often depends only on the current state (e.g., if the library is full, no one else can enter). The future evolution is independent of how we reached the current number. This is a classic example of a continuous-time Markov chain (a birth-death process).
    *   **Decision:** Very reasonable to assume.

**Final Answer / 最终答案:**
| Scenario | State Space | Time Index | Model Type | Markov Property |
| :--- | :--- | :--- | :--- | :--- |
| (a) Voter Opinion | Continuous | Discrete | Stochastic | Reasonable |
| (b) Football Points | Discrete | Discrete | Stochastic | Reasonable |
| (c) Water Temperature | Continuous | Continuous | Deterministic | N/A |
| (d) Library People | Discrete | Continuous | Stochastic | Very Reasonable |

**Key Insight / 解题要点:**
The choice of model depends on the fundamental nature of the quantity being observed: whether it is counted or measured, observed at specific times or continuously, and whether its evolution is predictable or random.

---

### Question 2 / 第2题

**Problem / 题目原文:**
A fair six-sided dice is rolled twice, resulting in the values \(X_1, X_2 \in \{1,2,\dots,6\}\). Let \(Y = X_1 + X_2\) be the total score. Calculate:
(a) the probability \(\mathbb{P}(Y = 9)\);
(b) the conditional probability \(\mathbb{P}(Y = 9 \mid X_1 = x)\) for \(x = 1,2,\dots,6\);
(c) the conditional probability \(\mathbb{P}(X_1 = x \mid Y = 9)\) for \(x = 1,2,\dots,6\).

**中文翻译:**
一个公平的六面骰子掷两次，得到结果 \(X_1, X_2 \in \{1,2,\dots,6\}\)。令 \(Y = X_1 + X_2\) 为总点数。计算：
(a) 概率 \(\mathbb{P}(Y = 9)\);
(b) 条件概率 \(\mathbb{P}(Y = 9 \mid X_1 = x)\)，其中 \(x = 1,2,\dots,6\);
(c) 条件概率 \(\mathbb{P}(X_1 = x \mid Y = 9)\)，其中 \(x = 1,2,\dots,6\)。

**Knowledge Points / 考查知识点:**
- 古典概型、条件概率、全概率公式、贝叶斯定理。

**Step-by-Step Solution / 逐步解答:**

**(a) \(\mathbb{P}(Y = 9)\)**
*   **Step 1: Define the sample space / 定义样本空间**
    *   **What:** The experiment is rolling a fair die twice.
    *   **Why:** We need to know the total number of equally likely outcomes.
    *   **Working:** The sample space \(\Omega = \{(x_1, x_2) : x_1, x_2 \in \{1,2,\dots,6\}\}\). The total number of outcomes is \(|\Omega| = 6 \times 6 = 36\).
*   **Step 2: Identify favorable outcomes / 识别有利结果**
    *   **What:** Find all pairs \((x_1, x_2)\) such that \(x_1 + x_2 = 9\).
    *   **Why:** These are the outcomes that satisfy the event \(Y=9\).
    *   **Working:** The pairs are: (3,6), (4,5), (5,4), (6,3). There are 4 favorable outcomes.
*   **Step 3: Calculate probability / 计算概率**
    *   **What:** Use the classical definition of probability for equally likely outcomes.
    *   **Why:** \(\mathbb{P}(\text{Event}) = \frac{\text{Number of favorable outcomes}}{\text{Total number of outcomes}}\).
    *   **Working:** \(\mathbb{P}(Y=9) = \frac{4}{36} = \frac{1}{9}\).
    *   **Intermediate Result:** \(\mathbb{P}(Y=9) = 1/9\).

**(b) \(\mathbb{P}(Y = 9 \mid X_1 = x)\) for \(x = 1,2,\dots,6\)**
*   **Step 1: Apply the definition of conditional probability / 应用条件概率的定义**
    *   **What:** \(\mathbb{P}(Y=9 \mid X_1=x) = \frac{\mathbb{P}(Y=9 \cap X_1=x)}{\mathbb{P}(X_1=x)}\).
    *   **Why:** This is the fundamental definition.
*   **Step 2: Calculate for each \(x\) / 对每个 \(x\) 进行计算**
    *   **What:** Since the die is fair, \(\mathbb{P}(X_1=x) = 1/6\) for all \(x\). The event \(\{Y=9 \cap X_1=x\}\) means the first roll is \(x\) and the second roll is \(9-x\).
    *   **Why:** We need the second roll to be exactly \(9-x\) to make the sum 9.
    *   **Working:**
        *   If \(x=1,2\), then \(9-x = 8,7\), which are impossible outcomes for a die. So \(\mathbb{P}(Y=9 \cap X_1=x) = 0\). Therefore \(\mathbb{P}(Y=9 \mid X_1=x) = 0\).
        *   If \(x=3\), then \(9-3=6\). The event is \((3,6)\). \(\mathbb{P}(Y=9 \cap X_1=3) = \frac{1}{36}\). So \(\mathbb{P}(Y=9 \mid X_1=3) = \frac{1/36}{1/6} = \frac{1}{6}\).
        *   If \(x=4\), then \(9-4=5\). The event is \((4,5)\). \(\mathbb{P}(Y=9 \cap X_1=4) = \frac{1}{36}\). So \(\mathbb{P}(Y=9 \mid X_1=4) = \frac{1}{6}\).
        *   If \(x=5\), then \(9-5=4\). The event is \((5,4)\). \(\mathbb{P}(Y=9 \cap X_1=5) = \frac{1}{36}\). So \(\mathbb{P}(Y=9 \mid X_1=5) = \frac{1}{6}\).
        *   If \(x=6\), then \(9-6=3\). The event is \((6,3)\). \(\mathbb{P}(Y=9 \cap X_1=6) = \frac{1}{36}\). So \(\mathbb{P}(Y=9 \mid X_1=6) = \frac{1}{6}\).
*   **Step 3: Summarize results / 总结结果**
    *   **Final Answer for (b):**
        *   \(\mathbb{P}(Y=9 \mid X_1=1) = 0\)
        *   \(\mathbb{P}(Y=9 \mid X_1=2) = 0\)
        *   \(\mathbb{P}(Y=9 \mid X_1=3) = 1/6\)
        *   \(\mathbb{P}(Y=9 \mid X_1=4) = 1/6\)
        *   \(\mathbb{P}(Y=9 \mid X_1=5) = 1/6\)
        *   \(\mathbb{P}(Y=9 \mid X_1=6) = 1/6\)

**(c) \(\mathbb{P}(X_1 = x \mid Y = 9)\) for \(x = 1,2,\dots,6\)**
*   **Step 1: Apply Bayes' Theorem / 应用贝叶斯定理**
    *   **What:** \(\mathbb{P}(X_1=x \mid Y=9) = \frac{\mathbb{P}(Y=9 \mid X_1=x) \mathbb{P}(X_1=x)}{\mathbb{P}(Y=9)}\).
    *   **Why:** This is the standard formula for reversing the conditioning.
*   **Step 2: Plug in known values / 代入已知值**
    *   **What:** We know \(\mathbb{P}(Y=9) = 1/9\), \(\mathbb{P}(X_1=x) = 1/6\), and \(\mathbb{P}(Y=9 \mid X_1=x)\) from part (b).
    *   **Why:** We have all the components.
    *   **Working:**
        *   For \(x=1,2\): \(\mathbb{P}(X_1=x \mid Y=9) = \frac{0 \times (1/6)}{1/9} = 0\).
        *   For \(x=3,4,5,6\): \(\mathbb{P}(X_1=x \mid Y=9) = \frac{(1/6) \times (1/6)}{1/9} = \frac{1/36}{1/9} = \frac{1}{36} \times \frac{9}{1} = \frac{9}{36} = \frac{1}{4}\).
*   **Step 3: Verify / 验证**
    *   **What:** The sum of probabilities over all \(x\) should be 1.
    *   **Why:** This is a basic property of probability distributions.
    *   **Working:** \(0 + 0 + 1/4 + 1/4 + 1/4 + 1/4 = 1\). Correct.
*   **Final Answer for (c):**
    *   \(\mathbb{P}(X_1=1 \mid Y=9) = 0\)
    *   \(\mathbb{P}(X_1=2 \mid Y=9) = 0\)
    *   \(\mathbb{P}(X_1=3 \mid Y=9) = 1/4\)
    *   \(\mathbb{P}(X_1=4 \mid Y=9) = 1/4\)
    *   \(\mathbb{P}(X_1=5 \mid Y=9) = 1/4\)
    *   \(\mathbb{P}(X_1=6 \mid Y=9) = 1/4\)

**Final Answer / 最终答案:**
(a) \(\boxed{\frac{1}{9}}\)
(b) \(\boxed{\mathbb{P}(Y=9 \mid X_1=x) = 0 \text{ for } x=1,2; \quad \mathbb{P}(Y=9 \mid X_1=x) = \frac{1}{6} \text{ for } x=3,4,5,6}\)
(c) \(\boxed{\mathbb{P}(X_1=x \mid Y=9) = 0 \text{ for } x=1,2; \quad \mathbb{P}(X_1=x \mid Y=9) = \frac{1}{4} \text{ for } x=3,4,5,6}\)

**Key Insight / 解题要点:**
Conditional probability can be calculated directly from the sample space, and Bayes' Theorem provides a systematic way to "invert" the conditioning.

---

### Question 3 / 第3题

**Problem / 题目原文:**
Let \((X_n)\) be a simple random walk starting from \(X_0 = 0\) and that at each step goes up one with probability \(p\) or down one with probability \(q = 1-p\). What are:
(a) \(\mathbb{P}(X_5 = 3)\),
(b) \(\mathbb{P}(X_5 = 3 \mid X_2 = 2)\),
(c) \(\mathbb{P}(X_n = n-2)\),
(d) \(\mathbb{E}X_4\),
(e) \(\mathbb{E}(X_6 \mid X_4)\),

**中文翻译:**
设 \((X_n)\) 是一个简单随机游走，从 \(X_0 = 0\) 开始，每一步以概率 \(p\) 向上移动一步，或以概率 \(q = 1-p\) 向下移动一步。求：
(a) \(\mathbb{P}(X_5 = 3)\),
(b) \(\mathbb{P}(X_5 = 3 \mid X_2 = 2)\),
(c) \(\mathbb{P}(X_n = n-2)\),
(d) \(\mathbb{E}X_4\),
(e) \(\mathbb{E}(X_6 \mid X_4)\),

**Knowledge Points / 考查知识点:**
- 简单随机游走的分布、条件概率、马尔可夫性质、期望、条件期望。

**Step-by-Step Solution / 逐步解答:**

**(a) \(\mathbb{P}(X_5 = 3)\)**
*   **Step 1: Model the position / 对位置建模**
    *   **What:** \(X_n = U_1 + U_2 + \dots + U_n\), where \(U_i\) are i.i.d. steps. \(U_i = +1\) with probability \(p\), and \(U_i = -1\) with probability \(q\).
    *   **Why:** This is the definition of a simple random walk.
*   **Step 2: Relate position to number of up steps / 将位置与向上步数关联**
    *   **What:** Let \(N_n\) be the number of up steps in the first \(n\) steps. Then the number of down steps is \(n - N_n\).
    *   **Why:** The position is \(X_n = N_n - (n - N_n) = 2N_n - n\).
    *   **Working:** For \(X_5 = 3\), we have \(3 = 2N_5 - 5 \implies 2N_5 = 8 \implies N_5 = 4\). So we need exactly 4 up steps and 1 down step in 5 steps.
*   **Step 3: Calculate the probability / 计算概率**
    *   **What:** \(N_n\) follows a Binomial distribution: \(N_n \sim \text{Binomial}(n, p)\).
    *   **Why:** Each step is an independent Bernoulli trial with success probability \(p\).
    *   **Working:** \(\mathbb{P}(X_5 = 3) = \mathbb{P}(N_5 = 4) = \binom{5}{4} p^4 q^{1} = 5 p^4 q\).
    *   **Intermediate Result:** \(\mathbb{P}(X_5 = 3) = 5 p^4 q\).

**(b) \(\mathbb{P}(X_5 = 3 \mid X_2 = 2)\)**
*   **Step 1: Use the Markov property / 使用马尔可夫性质**
    *   **What:** The simple random walk has the Markov property. The future depends only on the present state, not the past.
    *   **Why:** Given the position at time 2, the steps from time 3 to 5 are independent of the past.
    *   **Working:** \(\mathbb{P}(X_5 = 3 \mid X_2 = 2) = \mathbb{P}(X_5 - X_2 = 1 \mid X_2 = 2)\). Since increments are independent of the past, this is \(\mathbb{P}(X_3' = 1)\), where \(X_3'\) is a random walk starting from 0 and taking 3 steps.
*   **Step 2: Calculate the probability for the increment / 计算增量的概率**
    *   **What:** We need the probability that a random walk starting at 0 ends at 1 after 3 steps.
    *   **Why:** \(X_5 - X_2\) is the sum of 3 independent steps.
    *   **Working:** For \(X_3' = 1\), we have \(1 = 2N_3 - 3 \implies 2N_3 = 4 \implies N_3 = 2\). So we need exactly 2 up steps and 1 down step in 3 steps.
    *   **Calculation:** \(\mathbb{P}(X_3' = 1) = \binom{3}{2} p^2 q^{1} = 3 p^2 q\).
    *   **Intermediate Result:** \(\mathbb{P}(X_5 = 3 \mid X_2 = 2) = 3 p^2 q\).

**(c) \(\mathbb{P}(X_n = n-2)\)**
*   **Step 1: Relate position to number of up steps / 将位置与向上步数关联**
    *   **What:** \(X_n = 2N_n - n\).
    *   **Why:** We need to find \(N_n\) such that \(X_n = n-2\).
    *   **Working:** \(n-2 = 2N_n - n \implies 2N_n = 2n - 2 \implies N_n = n-1\).
*   **Step 2: Calculate the probability / 计算概率**
    *   **What:** We need exactly \(n-1\) up steps and 1 down step in \(n\) steps.
    *   **Why:** This is a specific outcome of the Binomial distribution.
    *   **Working:** \(\mathbb{P}(X_n = n-2) = \mathbb{P}(N_n = n-1) = \binom{n}{n-1} p^{n-1} q^{1} = n p^{n-1} q\).
    *   **Intermediate Result:** \(\mathbb{P}(X_n = n-2) = n p^{n-1} q\).

**(d) \(\mathbb{E}X_4\)**
*   **Step 1: Express expectation as sum of expectations / 将期望表示为期望之和**
    *   **What:** \(X_4 = U_1 + U_2 + U_3 + U_4\).
    *   **Why:** Expectation is linear.
    *   **Working:** \(\mathbb{E}X_4 = \mathbb{E}[U_1 + U_2 + U_3 + U_4] = \mathbb{E}U_1 + \mathbb{E}U_2 + \mathbb{E}U_3 + \mathbb{E}U_4\).
*   **Step 2: Calculate the expectation of a single step / 计算单步的期望**
    *   **What:** \(\mathbb{E}U_i = (1) \cdot p + (-1) \cdot q = p - q\).
    *   **Why:** This is the definition of expectation for a discrete random variable.
    *   **Working:** \(\mathbb{E}X_4 = 4(p - q)\).
    *   **Intermediate Result:** \(\mathbb{E}X_4 = 4(p - q)\).

**(e) \(\mathbb{E}(X_6 \mid X_4)\)**
*   **Step 1: Use the Markov property and linearity of conditional expectation / 使用马尔可夫性质和条件期望的线性性**
    *   **What:** \(X_6 = X_4 + (X_6 - X_4)\). The increment \(X_6 - X_4 = U_5 + U_6\) is independent of \(X_4\).
    *   **Why:** The future steps are independent of the past and present.
    *   **Working:** \(\mathbb{E}(X_6 \mid X_4) = \mathbb{E}(X_4 + (X_6 - X_4) \mid X_4) = \mathbb{E}(X_4 \mid X_4) + \mathbb{E}(X_6 - X_4 \mid X_4)\).
*   **Step 2: Simplify the conditional expectations / 简化条件期望**
    *   **What:**
        *   \(\mathbb{E}(X_4 \mid X_4) = X_4\) (the conditional expectation of a known quantity is itself).
        *   \(\mathbb{E}(X_6 - X_4 \mid X_4) = \mathbb{E}(U_5 + U_6 \mid X_4) = \mathbb{E