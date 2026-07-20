# Section 13: Poisson process with Poisson increments

> MATH2702 - 自学教材 / Self-Study Guide
> 生成时间: 2026-07-20 15:43
> 来源页: 69-71

---

# MATH2702: Stochastic Processes / 随机过程

## Section 13: Poisson Process with Poisson Increments / 泊松过程与泊松增量

---

### 📋 Section Overview / 章节概览

**中文解释：** 本节是连续时间马尔可夫跳跃过程（Continuous Time Markov Jump Processes）的第一部分。我们将学习泊松过程（Poisson Process），这是一种在连续时间中、离散状态空间上的随机过程。泊松过程是随机过程理论中最基础、最重要的模型之一，广泛应用于排队论、保险精算、通信网络等领域。本节从泊松分布开始复习，然后给出泊松过程的定义（通过泊松增量），最后讨论泊松过程的求和与标记性质。

**English explanation:** This section is the first part of Continuous Time Markov Jump Processes. We will study the Poisson Process, a stochastic process in continuous time with discrete state space. The Poisson process is one of the most fundamental and important models in stochastic process theory, widely used in queueing theory, actuarial science, telecommunications, and many other fields. This section begins with a review of the Poisson distribution, then provides the definition of the Poisson process (via Poisson increments), and finally discusses the summation and marking properties of Poisson processes.

**Why this matters / 为什么重要：**
- The Poisson process models random arrivals over time (e.g., customer arrivals, phone calls, insurance claims)
- 泊松过程模拟随时间发生的随机到达事件（如顾客到达、电话呼叫、保险索赔）
- It is the building block for more complex continuous-time Markov processes
- 它是更复杂连续时间马尔可夫过程的基础构件

---

### 🎯 Learning Objectives / 学习目标

After completing this section, you should be able to / 完成本节后，你应该能够：

1. **Recall and apply** properties of the Poisson distribution, including expectation, variance, and the sum of independent Poisson variables / **回忆并应用**泊松分布的性质，包括期望、方差和独立泊松变量的和
2. **Define** the Poisson process using the Poisson increments definition / **定义**泊松过程（使用泊松增量定义）
3. **Calculate** probabilities for the Poisson process over any time interval / **计算**泊松过程在任意时间区间上的概率
4. **Apply** the summed Poisson process theorem to combine independent Poisson processes / **应用**泊松过程求和定理来合并独立的泊松过程
5. **Apply** the marked Poisson process theorem to split a Poisson process / **应用**泊松过程标记定理来分割一个泊松过程
6. **Solve** real-world problems using Poisson process models / **使用**泊松过程模型解决实际问题

---

### 📚 Prerequisites / 前置知识

Before studying this section, you should be familiar with / 在学习本节之前，你应该熟悉：

- **Poisson distribution** / **泊松分布**: probability mass function, expectation, variance
- **Independent random variables** / **独立随机变量**: definition and properties
- **Basic probability** / **基础概率**: probability calculations, conditional probability
- **Discrete-time Markov chains** / **离散时间马尔可夫链** (from previous sections): understanding of state space, transition probabilities

---

### 📖 Core Content / 核心内容

---

#### Topic 1: Poisson Distribution Review / 泊松分布复习

##### Intuition / 直觉理解

**中文解释：** 泊松分布是概率论中最重要的离散分布之一。它通常用来模拟在固定时间段内"到达"事件的数量。想象一个呼叫中心：在一小时内，你会接到多少个电话？这个数量通常可以用泊松分布来建模。泊松分布的关键参数是速率 λ（lambda），它表示单位时间内事件的平均发生次数。

**English explanation:** The Poisson distribution is one of the most important discrete distributions in probability theory. It is typically used to model the number of "arrivals" in a fixed period of time. Imagine a call centre: how many calls will you receive in one hour? This number can usually be modelled using the Poisson distribution. The key parameter of the Poisson distribution is the rate λ (lambda), which represents the average number of events occurring per unit time.

**Real-world examples / 实际应用例子：**
- Number of calls to a call centre in one hour / 呼叫中心一小时内接到的电话数量
- Number of claims to an insurance company in one year / 保险公司一年内收到的索赔数量
- Number of particles decaying from radioactive material in one second / 放射性物质一秒钟内衰变的粒子数量

##### Formal Definition / 形式化定义

**Definition / 定义：** A discrete random variable $X$ has a Poisson distribution with rate $\lambda$, written $X \sim \text{Po}(\lambda)$, if its probability mass function (PMF) is:

$$
\mathbb{P}(X = n) = \frac{e^{-\lambda} \lambda^n}{n!}, \quad n = 0, 1, 2, \ldots
$$

**Symbol explanation / 符号说明：**

| Symbol | Meaning (English) | 含义（中文） |
|--------|-------------------|--------------|
| $X$ | Random variable | 随机变量 |
| $\lambda$ | Rate parameter (mean number of events per unit time) | 速率参数（单位时间内事件的平均数） |
| $n$ | Number of events | 事件数量 |
| $e$ | Euler's number (≈ 2.71828) | 欧拉数 |
| $\mathbb{P}(X = n)$ | Probability that X equals n | X等于n的概率 |

**中文解释：** 这个公式告诉我们，在固定时间段内恰好发生n次事件的概率。注意分母是n的阶乘，这保证了所有概率之和为1。当λ较小时，分布集中在0附近；当λ较大时，分布更分散，近似于正态分布。

**English explanation:** This formula tells us the probability that exactly n events occur in a fixed time period. Note that the denominator is n factorial, which ensures all probabilities sum to 1. When λ is small, the distribution is concentrated near 0; when λ is large, the distribution is more spread out and approximates a normal distribution.

##### Key Properties / 关键性质

**Property 1: Expectation and Variance / 性质1：期望和方差**

$$
\mathbb{E}[X] = \lambda \quad \text{and} \quad \text{Var}(X) = \lambda
$$

**中文解释：** 泊松分布的一个独特性质是它的期望和方差相等，都等于λ。这意味着如果平均每小时接到10个电话（λ=10），那么方差也是10，标准差约为√10 ≈ 3.16。

**English explanation:** A unique property of the Poisson distribution is that its expectation and variance are equal, both equal to λ. This means if you receive an average of 10 calls per hour (λ=10), then the variance is also 10, and the standard deviation is approximately √10 ≈ 3.16.

**Property 2: Sum of Independent Poisson Variables / 性质2：独立泊松变量的和**

If $X \sim \text{Po}(\lambda)$ and $Y \sim \text{Po}(\mu)$ are independent, then:

$$
X + Y \sim \text{Po}(\lambda + \mu)
$$

**中文解释：** 两个独立泊松随机变量的和仍然服从泊松分布，其参数是原参数之和。例如，如果大学邮箱每小时收到4封邮件（λ=4），个人邮箱每小时收到2封邮件（μ=2），那么总邮件数服从Po(6)分布。

**English explanation:** The sum of two independent Poisson random variables is still Poisson distributed, with parameter equal to the sum of the original parameters. For example, if a university email receives 4 emails per hour (λ=4) and a personal email receives 2 emails per hour (μ=2), then the total number of emails follows a Po(6) distribution.

**Property 3: Marking Property / 性质3：标记性质**

Let $X \sim \text{Po}(\lambda)$ represent some arrivals, and independently "mark" each arrival with probability $p$. Then:
- The number of marked arrivals $Y \sim \text{Po}(p\lambda)$
- The number of unmarked arrivals $Z \sim \text{Po}((1-p)\lambda)$
- $Y$ and $Z$ are independent

**中文解释：** 这个性质说：如果我们有一个泊松过程，每个到达事件独立地以概率p被"标记"，那么标记事件的数量和未标记事件的数量都服从泊松分布，并且它们相互独立。这个性质可能对你是新的，但它在后面会非常有用。

**English explanation:** This property states: if we have a Poisson process, and each arrival is independently "marked" with probability p, then the number of marked events and the number of unmarked events both follow Poisson distributions, and they are independent of each other. This property may be new to you, but it will be very useful later.

---

#### Topic 2: Definition of Poisson Process via Poisson Increments / 通过泊松增量定义泊松过程

##### Intuition / 直觉理解

**中文解释：** 现在我们不只是想模拟固定时间段内的到达数量，而是想连续地模拟随时间变化的总到达数量。这是一个连续时间、离散状态空间的随机过程。想象一个呼叫中心，每小时平均接到100个电话。我们假设：从0开始计数，第一个小时内的电话数服从Po(100)，第二个小时内的电话数也服从Po(100)且与第一个小时独立，两小时内的电话数服从Po(200)，半小时内的电话数服从Po(50)。这些性质定义了泊松过程。

**English explanation:** Now, instead of just modelling the number of arrivals in a fixed amount of time, we want to continuously model the total number of arrivals as it changes over time. This is a stochastic process with continuous time and discrete state space. Imagine a call centre receiving an average of 100 calls per hour. We assume: we start counting at 0, the number of calls in the first hour follows Po(100), the number in the second hour also follows Po(100) and is independent of the first hour, the number in a two-hour period follows Po(200), and the number in a half-hour period follows Po(50). These properties define the Poisson process.

**Notation note / 符号说明：** In continuous time, we normally write stochastic processes as $(X(t))$, with the time variable being $t$ in brackets, rather than a subscript $n$ as we had in discrete time. / 在连续时间中，我们通常将随机过程写为$(X(t))$，时间变量用括号中的t表示，而不是像离散时间中那样用下标n。

##### Formal Definition / 形式化定义

**Definition 13.1: Poisson Process / 定义13.1：泊松过程**

The Poisson process with rate $\lambda$ is defined as follows. It is a stochastic process $(X(t))$ with continuous time $t \in [0, \infty)$ and discrete state space $\mathcal{S} = \mathbb{Z}_+ = \{0, 1, 2, \ldots\}$ with the following properties:

1. **Initial condition / 初始条件：** $X(0) = 0$
2. **Poisson increments / 泊松增量：** $X(t+s) - X(t) \sim \text{Po}(\lambda s)$ for all $s, t > 0$
3. **Independent increments / 独立增量：** $X(t_2) - X(t_1)$ and $X(t_4) - X(t_3)$ are independent for all $t_1 \leq t_2 \leq t_3 \leq t_4$

**Symbol explanation / 符号说明：**

| Symbol | Meaning (English) | 含义（中文） |
|--------|-------------------|--------------|
| $X(t)$ | Number of arrivals up to time t | 截至时间t的到达总数 |
| $\lambda$ | Rate of arrivals per unit time | 单位时间内的到达率 |
| $s$ | Length of time interval | 时间区间长度 |
| $t$ | Starting time | 起始时间 |
| $\mathbb{Z}_+$ | Non-negative integers | 非负整数集合 |
| $t_1 \leq t_2 \leq t_3 \leq t_4$ | Non-overlapping time intervals | 不重叠的时间区间 |

**中文解释：** 定义中的三个条件非常重要：
1. 初始条件：在时间0时，还没有任何到达事件发生。
2. 泊松增量：在任何长度为s的时间区间内，到达事件的数量服从参数为λs的泊松分布。注意，这个分布只依赖于区间长度s，而不依赖于起始时间t（这就是"平稳增量"性质）。
3. 独立增量：不重叠的时间区间内的到达数量是相互独立的。注意，重叠的时间区间不会有独立增量，因为重叠部分的到达会被两个区间都计数。

**English explanation:** The three conditions in the definition are very important:
1. Initial condition: at time 0, no arrivals have occurred yet.
2. Poisson increments: in any time interval of length s, the number of arrivals follows a Poisson distribution with parameter λs. Note that this distribution only depends on the interval length s, not on the starting time t (this is the "stationary increments" property).
3. Independent increments: the numbers of arrivals in non-overlapping time intervals are independent of each other. Note that overlapping time intervals will not have independent increments, as arrivals in the overlap will count for both intervals.

**Historical note / 历史注记：** The Poisson process was discovered in the first decade of the 20th century, and the process was named after the distribution. Important work was done by the Swedish actuary and mathematician Filip Lundberg and the Danish engineer and mathematician A.K. Erlang. / 泊松过程在20世纪第一个十年被发现，该过程以分布命名。瑞典精算师兼数学家Filip Lundberg和丹麦工程师兼数学家A.K. Erlang做出了重要贡献。

##### Worked Examples / 例题

**Example 13.1: Insurance Claims / 保险索赔**

**Problem / 问题：** Claims arrive at an insurance company at a rate of $\lambda = 8$ per hour, modelled as a Poisson process. What is the probability there are no claims in a given 15 minute period?

**中文解释：** 保险公司每小时平均收到8个索赔，建模为泊松过程。求在任意15分钟内没有索赔的概率。

**Solution / 解答：**

**Step 1: Determine the time interval / 步骤1：确定时间区间**
15 minutes = 15/60 = 0.25 hours

**Step 2: Find the Poisson parameter / 步骤2：找到泊松参数**
By property 2, the number of claims in 15 minutes has a Poisson distribution with mean:
$$\lambda s = 8 \times 0.25 = 2$$

**Step 3: Calculate the probability / 步骤3：计算概率**
The probability there are no claims (n=0) is:
$$\mathbb{P}(X = 0) = \frac{e^{-2} \times 2^0}{0!} = e^{-2} = 0.135$$

**Answer / 答案：** 0.135 or 13.5%

**中文解释：** 注意，0! = 1，任何数的0次方等于1，所以公式简化为e^{-λs}。这里e^{-2} ≈ 0.135，意味着在任意15分钟内，有13.5%的概率没有索赔到达。

**English explanation:** Note that 0! = 1 and any number to the power of 0 equals 1, so the formula simplifies to e^{-λs}. Here e^{-2} ≈ 0.135, meaning there is a 13.5% probability of no claims arriving in any given 15-minute period.

---

**Example 13.2: Professor's Visitors / 教授的访客**

**Problem / 问题：** A professor receives visitors to her office at a rate of $\lambda = 2.5$ per day, modelled as a Poisson process. What is the probability she gets at least one visitor every day this (5-day) week?

**中文解释：** 教授每天平均接待2.5位访客，建模为泊松过程。求本周（5天）每天至少有一位访客的概率。

**Solution / 解答：**

**Step 1: Probability of at least one visitor on a given day / 步骤1：某天至少有一位访客的概率**
$$\mathbb{P}(\text{at least one}) = 1 - \mathbb{P}(\text{no visitors}) = 1 - \frac{e^{-2.5} \times 2.5^0}{0!} = 1 - e^{-2.5} = 0.918$$

**Step 2: Use independence across days / 步骤2：利用天与天之间的独立性**
By property 3 (independent increments), the numbers of visitors on different days are independent. So the probability of getting at least one visitor each day this week is:
$$0.918^5 = 0.652$$

**Answer / 答案：** 0.652 or 65.2%

**中文解释：** 这里我们利用了独立增量性质：不同天的访客数量是独立的。注意，我们假设"一天"是长度为1的时间区间，且这些区间不重叠。每天至少一位访客的概率是0.918，5天都满足的概率就是0.918^5。

**English explanation:** Here we use the independent increments property: the numbers of visitors on different days are independent. Note that we assume a "day" is a time interval of length 1, and these intervals do not overlap. The probability of at least one visitor per day is 0.918, and the probability this holds for all 5 days is 0.918^5.

---

#### Topic 3: Summed and Marked Poisson Processes / 泊松过程的求和与标记

##### Intuition / 直觉理解

**中文解释：** 现在我们讨论泊松过程的两个重要操作：求和与标记。求和是将两个独立的泊松过程合并成一个；标记是将一个泊松过程分割成两个。这两个操作是互逆的，在实际应用中非常有用。

**English explanation:** Now we discuss two important operations on Poisson processes: summation and marking. Summation combines two independent Poisson processes into one; marking splits one Poisson process into two. These two operations are inverse to each other and are very useful in practical applications.

##### Theorem 13.1: Summed Poisson Process / 定理13.1：泊松过程求和

**Theorem / 定理：** Let $(X(t))$ and $(Y(t))$ be independent Poisson processes with rates $\lambda$ and $\mu$ respectively. Then the process $(Z(t))$ given by $Z(t) = X(t) + Y(t)$ is a Poisson process with rate $\lambda + \mu$.

**中文解释：** 这个定理说：两个独立泊松过程的和仍然是一个泊松过程，其速率是原速率之和。例如，如果大学邮箱的邮件到达是速率为4的泊松过程，个人邮箱的邮件到达是速率为2的泊松过程，那么总邮件到达就是速率为6的泊松过程。

**English explanation:** This theorem states: the sum of two independent Poisson processes is still a Poisson process, with rate equal to the sum of the original rates. For example, if university email arrivals form a Poisson process with rate 4, and personal email arrivals form a Poisson process with rate 2, then the total email arrivals form a Poisson process with rate 6.

**Proof / 证明：** The proof of this is a question on Problem Sheet 7. / 这个证明是习题7上的一个问题。

**Key insight / 关键洞察：** The proof would need to verify all three properties of the Poisson process definition for $Z(t)$: $Z(0)=0$, Poisson increments, and independent increments. / 证明需要验证$Z(t)$满足泊松过程定义的所有三个性质：$Z(0)=0$、泊松增量和独立增量。

---

**Example 13.3: Student Emails / 学生邮件**

**Problem / 问题：** A student receives emails to her university mail address at a rate of $\lambda = 4$ emails per hour, and to her personal email address at a rate of $\mu = 2$ per hour. Using a Poisson process model, what is the probability the student receives 3 or fewer emails in a 30 minute period?

**中文解释：** 学生大学邮箱每小时收到4封邮件，个人邮箱每小时收到2封邮件。使用泊松过程模型，求学生在30分钟内收到3封或更少邮件的概率。

**Solution / 解答：**

**Step 1: Find the total rate / 步骤1：找到总速率**
The total number of emails is a sum of Poisson processes with rate:
$$\lambda + \mu = 4 + 2 = 6 \text{ per hour}$$

**Step 2: Find the Poisson parameter for 30 minutes / 步骤2：找到30分钟的泊松参数**
30 minutes = 0.5 hours, so the parameter is:
$$(\lambda + \mu) \times 0.5 = 6 \times 0.5 = 3$$

**Step 3: Calculate the probability / 步骤3：计算概率**
The probability that 3 or fewer emails are received is:
$$\mathbb{P}(X \leq 3) = \sum_{n=0}^{3} \frac{e^{-3} \times 3^n}{n!}$$

Let's calculate each term:
- $n=0$: $\frac{e^{-3} \times 3^0}{0!} = e^{-3}$
- $n=1$: $\frac{e^{-3} \times 3^1}{1!} = 3e^{-3}$
- $n=2$: $\frac{e^{-3} \times 3^2}{2!} = \frac{9e^{-3}}{2} = 4.5e^{-3}$
- $n=3$: $\frac{e^{-3} \times 3^3}{3!} = \frac{27e^{-3}}{6} = 4.5e^{-3}$

Sum: $e^{-3} + 3e^{-3} + 4.5e^{-3} + 4.5e^{-3} = 13e^{-3} = 0.647$

**Answer / 答案：** 0.647 or 64.7%

**中文解释：** 注意，我们首先将两个独立的泊松过程相加，得到总速率为6的泊松过程。然后计算半小时内的泊松参数为3。最后计算n=0,1,2,3的概率并求和。13e^{-3} ≈ 0.647，意味着有64.7%的概率在半小时内收到不超过3封邮件。

**English explanation:** Note that we first sum the two independent Poisson processes to get a Poisson process with total rate 6. Then we calculate the Poisson parameter for half an hour as 3. Finally, we calculate and sum the probabilities for n=0,1,2,3. 13e^{-3} ≈ 0.647, meaning there is a 64.7% probability of receiving 3 or fewer emails in half an hour.

---

##### Theorem 13.2: Marked Poisson Process / 定理13.2：泊松过程标记

**Theorem / 定理：** Let $(X(t))$ be a Poisson process with rate $\lambda$. Each arrival is independently marked with probability $p$. Then:
- The marked process $(Y(t))$ is a Poisson process with rate $p\lambda$
- The unmarked process $(Z(t))$ is a Poisson process with rate $(1-p)\lambda$
- $(Y(t))$ and $(Z(t))$ are independent

**中文解释：** 这个定理是泊松分布标记性质在泊松过程中的推广。它说：如果我们有一个速率为λ的泊松过程，每个到达事件独立地以概率p被标记，那么标记事件构成一个速率为pλ的泊松过程，未标记事件构成一个速率为(1-p)λ的泊松过程，并且这两个过程相互独立。

**English explanation:** This theorem is the extension of the Poisson distribution's marking property to the Poisson process. It states: if we have a Poisson process with rate λ, and each arrival is independently marked with probability p, then the marked events form a Poisson process with rate pλ, the unmarked events form a Poisson process with rate (1-p)λ, and these two processes are independent.

**Proof / 证明：** Given the third fact about the Poisson distribution (the marking property), it is easy to check the necessary properties. / 给定泊松分布的第三个性质（标记性质），很容易验证必要的性质。

**Key insight / 关键洞察：** The marking theorem is the "opposite" of the summation theorem: summation combines two processes, while marking splits one process into two. / 标记定理是求和定理的"逆操作"：求和将两个过程合并，标记将一个过程分割成两个。

---

**Example 13.4: Football Goals / 足球进球**

**Problem / 问题：** In the 2019/20 English Premier League football season, an average of $\lambda = 2.72$ goals were scored per game, with a proportion $p = 0.56$ of them scored by the home team. If we model this as a Poisson process, what is the probability a match ends in a 1–1 draw?

**中文解释：** 在2019/20赛季英格兰足球超级联赛中，每场比赛平均进球2.72个，其中56%由主队打进。如果将其建模为泊松过程，求比赛以1-1平局结束的概率。

**Solution / 解答：**

**Step 1: Find the rates for home and away goals / 步骤1：找到主队和客队的进球率**
- Home goals rate: $p\lambda = 0.56 \times 2.72 = 1.52$ goals per game
- Away goals rate: $(1-p)\lambda = 0.44 \times 2.72 = 1.20$ goals per game

**Step 2: Use independence of home and away goals / 步骤2：利用主队和客队进球的独立性**
Under the Poisson process assumption, home and away goals are independent (by the marking theorem).

**Step 3: Calculate the probability / 步骤3：计算概率**
The probability the home team scores exactly 1 goal AND the away team scores exactly 1 goal is:
$$\mathbb{P}(\text{home}=1) \times \mathbb{P}(\text{away}=1)$$

For home goals (Poisson with rate 1.52):
$$\mathbb{P}(\text{home}=1) = \frac{e^{-1.52} \times 1.52^1}{1!} = 1.52e^{-1.52}$$

For away goals (Poisson with rate 1.20):
$$\mathbb{P}(\text{away}=1) = \frac{e^{-1.20} \times 1.20^1}{1!} = 1.20e^{-1.20}$$

Therefore:
$$\mathbb{P}(1-1 \text{ draw}) = 1.52e^{-1.52} \times 1.20e^{-1.20} = 0.12$$

**Answer / 答案：** 0.12 or 12%

**中文解释：** 这个例子展示了标记泊松过程的应用。我们将总进球过程（速率为2.72）标记为主队进球（概率0.56）和客队进球（概率0.44）。根据标记定理，主队进球是速率为1.52的泊松过程，客队进球是速率为1.20的泊松过程，且两者独立。因此1-1平局的概率就是两个泊松