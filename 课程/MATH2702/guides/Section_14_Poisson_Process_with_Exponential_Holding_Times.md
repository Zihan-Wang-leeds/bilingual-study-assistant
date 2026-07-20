# Section 14: Poisson process with exponential holding times

> MATH2702 - 自学教材 / Self-Study Guide
> 生成时间: 2026-07-20 15:44
> 来源页: 72-75

---

# 📘 MATH2702: Poisson Process with Exponential Holding Times / 泊松过程与指数停留时间

## 📋 Section Overview / 章节概览

**中文解释：** 本章节是随机过程课程的核心内容之一。我们之前从"固定时间内的到达次数"角度介绍了泊松过程，现在我们将从另一个重要视角来理解它——"固定到达次数所需的时间"。这个视角引入了指数分布，并揭示了泊松过程与指数分布之间的深刻联系。我们将学习：
1. 指数分布及其无记忆性
2. 泊松过程的第二种定义——指数停留时间
3. 连续时间下的马尔可夫性质

**English explanation:** This section is one of the core topics in stochastic processes. Previously, we introduced the Poisson process from the perspective of "the number of arrivals in a fixed time interval." Now, we will understand it from another important perspective—"the time required for a fixed number of arrivals." This perspective introduces the exponential distribution and reveals the deep connection between the Poisson process and the exponential distribution. We will learn:
1. The exponential distribution and its memoryless property
2. The second definition of the Poisson process—exponential holding times
3. The Markov property in continuous time

**Why this matters / 为什么重要：**
- 指数分布是唯一具有无记忆性的连续分布，这使得泊松过程成为最简单的连续时间随机过程
- 理解指数停留时间视角对于后续学习连续时间马尔可夫链至关重要
- 这种视角让我们能够计算"等待时间"的概率，这在排队论、可靠性工程等领域有广泛应用

---

## 🎯 Learning Objectives / 学习目标

完成本章学习后，你应该能够：

1. **理解指数分布**：掌握指数分布的PDF、CDF、期望和方差，特别是无记忆性
2. **证明泊松过程的指数停留时间结构**：能够从独立增量定义推导出指数停留时间
3. **计算等待时间概率**：能够计算与泊松过程相关的各种等待时间概率
4. **应用最小指数分布定理**：能够计算多个独立指数分布的最小值的分布
5. **理解连续时间马尔可夫性质**：能够验证泊松过程满足马尔可夫性质

**English:**
After completing this section, you should be able to:
1. **Understand the exponential distribution**: Master its PDF, CDF, expectation, variance, and especially the memoryless property
2. **Prove the exponential holding time structure of the Poisson process**: Derive exponential holding times from the independent increments definition
3. **Calculate waiting time probabilities**: Compute various waiting time probabilities related to the Poisson process
4. **Apply the minimum of exponentials theorem**: Calculate the distribution of the minimum of multiple independent exponential distributions
5. **Understand the continuous-time Markov property**: Verify that the Poisson process satisfies the Markov property

---

## 📚 Prerequisites / 前置知识

在开始本章之前，请确保你熟悉以下内容：

| 概念 | 中文说明 | English |
|------|----------|---------|
| 泊松分布 | 参数为λ的泊松分布，概率质量函数为 \(P(X=k) = e^{-\lambda}\lambda^k/k!\) | Poisson distribution |
| 条件概率 | \(P(A|B) = P(A\cap B)/P(B)\) | Conditional probability |
| 独立增量 | 泊松过程在不重叠时间区间内的增量是独立的 | Independent increments |
| 期望和方差 | 随机变量的期望和方差的基本计算 | Expectation and variance |
| 极限 | 理解极限的基本概念，特别是ε→0 | Limits |

---

## 📖 Core Content / 核心内容

---

#### Topic 14.1: Exponential Distribution / 指数分布

**Intuition / 直觉理解**

**中文解释：** 指数分布是描述"等待时间"的自然模型。想象你在公交车站等车——公交车到达的时间间隔通常可以用指数分布来建模。为什么？因为指数分布具有一个神奇的性质：**无记忆性**。这意味着，无论你已经等了多久，剩余等待时间的分布与刚开始等的时候完全一样。这就像公交车"忘记"了你已经等了多久。

**English explanation:** The exponential distribution is a natural model for describing "waiting times." Imagine you are waiting at a bus stop—the time intervals between bus arrivals can typically be modeled using the exponential distribution. Why? Because the exponential distribution has a magical property: **memorylessness**. This means that no matter how long you have already waited, the distribution of the remaining waiting time is exactly the same as when you first started waiting. It's as if the bus "forgets" how long you've been waiting.

**Real-world examples / 实际应用：**
- 灯泡损坏的时间 / Time until a light bulb breaks
- 公交车到达的时间间隔 / Times between bus arrivals
- 银行账户取款的时间间隔 / Time between withdrawals from a bank account
- 放射性衰变的时间 / Time until radioactive decay

---

**Formal Definition / 形式化定义**

**Definition 14.1 (Exponential Distribution / 指数分布):** A continuous random variable \(T\) has the exponential distribution with rate \(\lambda > 0\), written as \(T \sim \text{Exp}(\lambda)\), if it has the probability density function (PDF):

\[
f(t) = \lambda e^{-\lambda t} \quad \text{for } t \geq 0
\]

**Symbol Explanation / 符号说明：**

| Symbol | 中文含义 | English Meaning |
|--------|----------|-----------------|
| \(T\) | 随机变量，表示等待时间 | Random variable representing waiting time |
| \(\lambda\) | 速率参数，单位时间内事件发生的平均次数 | Rate parameter, average number of events per unit time |
| \(f(t)\) | 概率密度函数 | Probability density function |
| \(t\) | 时间变量 | Time variable |

**Key Properties / 关键性质：**

1. **Cumulative Distribution Function (CDF) / 累积分布函数：**
   \[
   F(t) = \mathbb{P}(T \leq t) = 1 - e^{-\lambda t}
   \]

2. **Tail Probability / 尾部概率（更常用）：**
   \[
   \mathbb{P}(T > t) = 1 - F(t) = e^{-\lambda t}
   \]

3. **Expectation / 期望：**
   \[
   \mathbb{E}[T] = \frac{1}{\lambda}
   \]

4. **Variance / 方差：**
   \[
   \text{Var}(T) = \frac{1}{\lambda^2}
   \]

**中文解释：** 注意，速率参数λ越大，期望等待时间1/λ就越小。例如，如果公交车平均每小时来4趟（λ=4），那么平均等待时间就是1/4小时=15分钟。尾部概率\(\mathbb{P}(T > t) = e^{-\lambda t}\)表示等待时间超过t的概率，这在计算中非常方便。

**English explanation:** Note that the larger the rate parameter λ, the smaller the expected waiting time 1/λ. For example, if buses arrive at an average rate of 4 per hour (λ=4), then the average waiting time is 1/4 hour = 15 minutes. The tail probability \(\mathbb{P}(T > t) = e^{-\lambda t}\) represents the probability that the waiting time exceeds t, which is very convenient in calculations.

---

**Theorem 14.1: Memoryless Property / 无记忆性定理**

**中文解释：** 这是指数分布最重要的性质。它说：如果你已经等待了时间s，那么再等待额外时间t的概率，与从0开始等待时间t的概率完全相同。换句话说，指数分布"忘记"了已经过去的时间。

**English explanation:** This is the most important property of the exponential distribution. It states: if you have already waited for time s, the probability of waiting an additional time t is exactly the same as the probability of waiting time t from the beginning. In other words, the exponential distribution "forgets" the time that has already passed.

**Theorem 14.1:** Let \(T \sim \text{Exp}(\lambda)\). Then, for any \(s, t \geq 0\):

\[
\mathbb{P}(T > t + s \mid T > t) = \mathbb{P}(T > s)
\]

**Proof / 证明：**

**中文解释：** 证明利用了条件概率的基本公式和指数分布的尾部概率。

**English explanation:** The proof uses the basic formula for conditional probability and the tail probability of the exponential distribution.

\[
\begin{aligned}
\mathbb{P}(T > t + s \mid T > t) &= \frac{\mathbb{P}(T > t + s \text{ and } T > t)}{\mathbb{P}(T > t)} \\
&= \frac{\mathbb{P}(T > t + s)}{\mathbb{P}(T > t)} \quad \text{(因为 } T > t+s \text{ 蕴含 } T > t\text{)} \\
&= \frac{e^{-\lambda(t+s)}}{e^{-\lambda t}} \\
&= e^{-\lambda s} \\
&= \mathbb{P}(T > s)
\end{aligned}
\]

**Step-by-step explanation / 逐步解释：**

| Step | 中文解释 | English Explanation |
|------|----------|---------------------|
| 1 | 使用条件概率公式 \(P(A|B) = P(A\cap B)/P(B)\) | Use conditional probability formula |
| 2 | 事件 \(\{T > t+s\}\) 蕴含 \(\{T > t\}\)，所以交集就是 \(\{T > t+s\}\) | Event \(\{T > t+s\}\) implies \(\{T > t\}\), so intersection is just \(\{T > t+s\}\) |
| 3 | 代入指数分布的尾部概率公式 | Substitute the exponential tail probability formula |
| 4 | 化简指数表达式 | Simplify the exponential expression |
| 5 | 得到与初始等待时间s相同的尾部概率 | Obtain the same tail probability as waiting time s from start |

---

**Theorem 14.2: Minimum of Independent Exponentials / 独立指数分布的最小值**

**中文解释：** 这个定理告诉我们：如果有n个独立的指数分布随机变量，分别具有不同的速率参数，那么它们的最小值仍然服从指数分布，其速率参数等于所有速率参数之和。此外，某个特定变量是最小值的概率与其速率参数成正比。

**English explanation:** This theorem tells us: if we have n independent exponential random variables with different rate parameters, then their minimum still follows an exponential distribution, with rate parameter equal to the sum of all rate parameters. Furthermore, the probability that a particular variable is the minimum is proportional to its rate parameter.

**Theorem 14.2:** Let \(T_1 \sim \text{Exp}(\lambda_1), T_2 \sim \text{Exp}(\lambda_2), \ldots, T_n \sim \text{Exp}(\lambda_n)\) be independent exponential distributions, and let \(T\) be the minimum:

\[
T = \min\{T_1, T_2, \ldots, T_n\}
\]

Then:

1. **Distribution of the minimum / 最小值的分布：**
   \[
   T \sim \text{Exp}(\lambda_1 + \lambda_2 + \cdots + \lambda_n)
   \]

2. **Probability that \(T_j\) is the minimum / \(T_j\)是最小值的概率：**
   \[
   \mathbb{P}(T = T_j) = \frac{\lambda_j}{\lambda_1 + \lambda_2 + \cdots + \lambda_n}
   \]

**Proof / 证明：**

**中文解释：** 这个证明留作习题（Problem Sheet 7, Question 4），但我们可以给出证明思路：
- 对于第一部分，利用 \(\mathbb{P}(T > t) = \mathbb{P}(T_1 > t, T_2 > t, \ldots, T_n > t)\)，因为最小值大于t当且仅当所有变量都大于t
- 由于独立性，这个概率等于各尾部概率的乘积
- 对于第二部分，考虑\(T_j\)是最小值的概率，可以通过积分或条件概率来证明

**English explanation:** This proof is left as an exercise (Problem Sheet 7, Question 4), but we can give the proof idea:
- For part 1, use \(\mathbb{P}(T > t) = \mathbb{P}(T_1 > t, T_2 > t, \ldots, T_n > t)\), because the minimum is greater than t if and only if all variables are greater than t
- Due to independence, this probability equals the product of the individual tail probabilities
- For part 2, consider the probability that \(T_j\) is the minimum, which can be proved through integration or conditional probability

**Intuitive understanding / 直觉理解：**

**中文解释：** 想象有n个独立的"闹钟"，每个闹钟以不同的速率λ_i响铃。第一个响的闹钟就是最小值。由于指数分布的无记忆性，这些闹钟"竞争"谁先响，速率越大的闹钟越可能先响。所有闹钟一起"竞争"时，整体速率就是各速率之和。

**English explanation:** Imagine n independent "alarms," each ringing at a different rate λ_i. The first alarm to ring is the minimum. Due to the memoryless property of the exponential distribution, these alarms "compete" for who rings first—the alarm with the larger rate is more likely to ring first. When all alarms "compete" together, the overall rate is the sum of the individual rates.

---

#### Topic 14.2: Definition 2 - Exponential Holding Times / 第二种定义——指数停留时间

**Intuition / 直觉理解**

**中文解释：** 现在我们用另一种方式来描述泊松过程。想象一个计数器从0开始，每次事件发生后，我们等待一个指数分布的时间，然后计数器加1。这样，过程就由一系列独立的指数分布"停留时间"（holding times）构成。这种描述方式与之前"固定时间内到达次数服从泊松分布"的定义是等价的。

**English explanation:** Now we describe the Poisson process in another way. Imagine a counter starting at 0. After each event occurs, we wait an exponentially distributed amount of time, then increment the counter by 1. Thus, the process consists of a sequence of independent exponentially distributed "holding times." This description is equivalent to the previous definition that "the number of arrivals in a fixed time follows a Poisson distribution."

**Formal Definition / 形式化定义**

**Definition 14.2 (Poisson Process via Exponential Holding Times / 通过指数停留时间定义泊松过程):**

A process \((X(t))\) with the following properties is a Poisson process with rate \(\lambda\):

- Start with \(X(0) = 0\)
- Let \(T_1, T_2, \ldots \sim \text{Exp}(\lambda)\) be the holding times, all independent
- Then:
  \[
  X(t) = 
  \begin{cases}
  0 & \text{for } 0 \leq t < T_1 \\
  1 & \text{for } T_1 \leq t < T_1 + T_2 \\
  2 & \text{for } T_1 + T_2 \leq t < T_1 + T_2 + T_3 \\
  \vdots & \vdots
  \end{cases}
  \]

**Symbol Explanation / 符号说明：**

| Symbol | 中文含义 | English Meaning |
|--------|----------|-----------------|
| \(X(t)\) | 到时间t为止的事件总数 | Total number of events up to time t |
| \(T_i\) | 第i个停留时间（第i-1次到第i次事件之间的时间） | The i-th holding time (time between the (i-1)-th and i-th events) |
| \(\lambda\) | 事件发生的速率 | Rate of event occurrence |
| \(t\) | 时间变量 | Time variable |

---

**Theorem 14.3: Equivalence of Definitions / 定义的等价性**

**中文解释：** 这个定理证明了我们之前学过的泊松过程定义（独立泊松增量）与指数停留时间定义是等价的。也就是说，无论从哪个角度定义，我们得到的是同一个随机过程。

**English explanation:** This theorem proves that the Poisson process definition we learned before (independent Poisson increments) is equivalent to the exponential holding time definition. In other words, no matter which angle we use to define it, we get the same stochastic process.

**Theorem 14.3:** Let \((X(t))\) be a Poisson process with rate \(\lambda\), as defined by its independent Poisson increments (see Subsection 13.2). Then \((X(t))\) has the exponential holding times structure described above.

**Proof / 证明：**

**中文解释：** 证明分为两步：首先证明第一个停留时间T₁服从Exp(λ)，然后证明给定T₁后，第二个停留时间T₂也服从Exp(λ)且与T₁独立。通过归纳法，可以证明所有停留时间都是独立同分布的Exp(λ)。

**English explanation:** The proof proceeds in two steps: first prove that the first holding time T₁ follows Exp(λ), then prove that given T₁, the second holding time T₂ also follows Exp(λ) and is independent of T₁. By induction, all holding times are i.i.d. Exp(λ).

**Step 1: Distribution of the first holding time / 第一个停留时间的分布**

\[
\begin{aligned}
\mathbb{P}(T_1 > t_1) &= \mathbb{P}(X(t_1) - X(0) = 0) \\
&= e^{-\lambda t_1} \frac{(\lambda t_1)^0}{0!} \\
&= e^{-\lambda t_1}
\end{aligned}
\]

**中文解释：** 第一个事件在时间t₁之后发生，意味着在区间[0, t₁]内没有事件发生，即X(t₁) - X(0) = 0。根据泊松过程的定义，这个概率就是泊松分布中k=0的概率，即\(e^{-\lambda t_1}\)。这正是Exp(λ)的尾部概率。

**English explanation:** The first event occurs after time t₁ means there are no events in the interval [0, t₁], i.e., X(t₁) - X(0) = 0. By the definition of the Poisson process, this probability is the Poisson probability for k=0, which is \(e^{-\lambda t_1}\). This is exactly the tail probability of Exp(λ).

**Step 2: Distribution of the second holding time / 第二个停留时间的分布**

\[
\begin{aligned}
\mathbb{P}(T_2 > t_2 \mid T_1 = t_1) &= \mathbb{P}(X(t_1 + t_2) - X(t_1) = 0) \\
&= e^{-\lambda ((t_1 + t_2) - t_1)} \\
&= e^{-\lambda t_2}
\end{aligned}
\]

**中文解释：** 给定第一个事件发生在时间t₁，第二个事件在额外时间t₂之后发生，意味着在区间[t₁, t₁+t₂]内没有事件发生。由于泊松过程具有独立增量，这个概率与第一个事件无关，仍然是\(e^{-\lambda t_2}\)。这证明了T₂也服从Exp(λ)且与T₁独立。

**English explanation:** Given that the first event occurs at time t₁, the second event occurs after an additional time t₂ means there are no events in the interval [t₁, t₁+t₂]. Due to the independent increments property of the Poisson process, this probability is independent of the first event and is still \(e^{-\lambda t_2}\). This proves that T₂ also follows Exp(λ) and is independent of T₁.

**Technical note on conditioning / 关于条件概率的技术说明：**

**中文解释：** 在证明中，我们条件于事件\(\{T_1 = t_1\}\)，但这个事件的概率为0。严格来说，我们不能直接这样做。为了填补这个漏洞，我们可以考虑事件\(T_1 \in (t_1 - \varepsilon, t_1 + \varepsilon)\)，然后取极限\(\varepsilon \to 0\)。

**English explanation:** In the proof, we conditioned on the event \(\{T_1 = t_1\}\), but this event has probability 0. Strictly speaking, we cannot directly do this. To fill this gap, we can consider the event \(T_1 \in (t_1 - \varepsilon, t_1 + \varepsilon)\) and then take the limit \(\varepsilon \to 0\).

**Rigorous approach / 严格方法：**

\[
\begin{aligned}
\mathbb{P}(T_2 > t_2 \mid T_1 = t_1) &= \lim_{\varepsilon \to 0} \mathbb{P}(T_2 > t_2 \mid T_1 \in (t_1 - \varepsilon, t_1 + \varepsilon)) \\
&\leq \lim_{\varepsilon \to 0} \mathbb{P}(X(t_1 + t_2 + \varepsilon) - X(t_1 - \varepsilon) = 0) \\
&= \lim_{\varepsilon \to 0} e^{-\lambda(t_1 + 2\varepsilon)} = e^{-\lambda t_1}
\end{aligned}
\]

类似地，我们可以得到下界：
\[
\mathbb{P}(T_2 > t_2 \mid T_1 = t_1) \geq \lim_{\varepsilon \to 0} e^{-\lambda(t_1 - 2\varepsilon)} = e^{-\lambda t_1}
\]

因此，通过夹逼定理，我们得到\(\mathbb{P}(T_2 > t_2 \mid T_1 = t_1) = e^{-\lambda t_2}\)。

---

**Worked Example 14.1 / 例题14.1**

**中文解释：** 这是一个"标记泊松过程"（marked Poisson process）的例子。顾客以每小时5人的速率进入书店，每位顾客以概率0.4购买一本书。我们需要计算卖出10本书的期望时间和标准差，以及卖出第一本书需要超过1小时的概率。

**English explanation:** This is an example of a "marked Poisson process." Customers enter a bookstore at a rate of 5 per hour, and each customer buys a book with probability 0.4. We need to calculate the expected time and standard deviation to make 10 sales, and the probability that it takes more than 1 hour to sell the first book.

**Problem / 问题：** Customers visit a second-hand bookshop at a rate of \(\lambda = 5\) per hour. Each customer buys a book with probability \(p = 0.4\).

(a) What is the expected time to make ten sales, and what is the standard deviation?
(b) What is the probability it takes more than an hour to sell the first book?

**Solution / 解答：**

**Part (a):**

**中文解释：** 首先，卖出的书构成一个标记泊松过程，其速率是原过程速率乘以购买概率：\(p\lambda = 0.4 \times 5 = 2\)。也就是说，书被卖出的速率是每小时2本。

**English explanation:** First, the books sold form a marked Poisson process with rate equal to the original rate times the purchase probability: \(p\lambda = 0.4 \times 5 = 2\). That is, books are sold at a rate of 2 per hour.

**Expected time / 期望时间：**
\[
\mathbb{E}(T_1 + T_2 + \cdots + T_{10}) = 10 \times \mathbb{E}(T_1) = 10 \times \frac{1}{2} = 5 \text{ hours}
\]

**中文解释：** 卖出10本书需要等待10个独立的指数分布停留时间之和。每个停留时间的期望是1/2小时，所以总期望时间是10 × 1/2 = 5小时。

**English explanation:** To sell 10 books, we need to wait for the sum of 10 independent exponential holding times. Each holding time has expectation 1/2 hour, so the total expected time is 10 × 1/2 = 5 hours.

**Variance / 方差：**
\[
\text{Var}(T_1 + T_2 + \cdots + T_{10}) = 10 \times \text{Var}(T_1) = 10 \times \frac{1}{2^2} = 2.5
\]

**Standard deviation / 标准差：**
\[
\sqrt{2.5} = 1.58 \text{ hours}
\]

**中文解释：** 由于停留时间是独立同分布的，总方差等于各方差之和。每个停留时间的方差是1/λ² = 1/4，所以总方差是10 × 1/4 = 2.5，标准差约为1.58小时。

**English explanation:** Since the holding times are i.i.d., the total variance equals the sum of individual variances. Each holding time has variance 1/λ² = 1/4, so the total variance is 10 × 1/4 = 2.5, and the standard deviation is approximately 1.58 hours.

**Part (b):**

**Method 1: Using exponential distribution / 方法1：使用指数分布**

\[
\mathbb{P}(T_1 > 1) = e^{-2 \times 1} = e^{-2} = 0.135
\]

**中文解释：** 第一本书的卖出时间T₁服从Exp(2)，所以超过1小时的概率就是尾部概率\(e^{-2 \times 1} = e^{-2} \approx 0.135\)。

**English explanation:** The time to sell the first book T₁ follows Exp(2), so the probability of exceeding 1 hour is the tail probability \(e^{-2 \times 1} = e^{-2} \approx 0.135\).

**Method 2: Using Poisson increments / 方法2：使用泊松增量**

\[
\mathbb{P}(X(1) = 0) = e^{-2 \times 1} \frac{(2 \times 1)^0}{0!} = e^{-2} = 0.135
\]

**中文解释：** 另一种思路：第一本书在1小时后卖出，等价于在1小时内没有书被卖出，即X(1) = 0。根据泊松分布，这个概率也是\(e^{-2}\)。两种方法得到相同的结果，验证了两种定义的等价性。

**English explanation:** Another way: the first book is sold after 1 hour is equivalent to no books being sold in 1 hour, i.e., X(1) = 0. According to the Poisson distribution, this probability is also \(e^{-2}\). Both methods give the same result, verifying the equivalence of the two definitions.

---

#### Topic 14.3: Markov Property in Continuous Time / 连续时间下的马尔可夫性质

**Intuition / 直觉理解**

**中文解释：** 马尔可夫性质的核心思想是"给定现在，未来与过去无关"。在离散时间中，我们学过这个性质。在连续时间中，这个性质同样重要。泊松过程满足连续时间马尔可夫性质，这可以从两个方面理解：
1. 从独立增量性质来看：未来的增量只依赖于当前状态，与过去无关
2. 从指数停留时间来看：指数分布的无记忆性意味着每次事件发生后，过程"重新开始"

**English explanation:** The core idea of the Markov property is "given the present, the future is independent of the past." We learned this property in discrete time. In continuous time, this property is equally important. The Poisson process satisfies the continuous-time Markov property, which can be understood from two perspectives:
1. From the independent increments property: future increments depend only on the current state, not on the past
2. From the exponential holding times: the memoryless property of the exponential distribution means that after each event, the process "restarts"

---

**Formal Definition / 形式化定义