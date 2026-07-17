# Section 13: Poisson Process with Poisson Increments

> MATH2702 Stochastic Processes - 自学教材
> 生成时间: 2026-07-17 14:52
> 来源页: 69-71

---

# MATH2702 Study Guide / 学习指南
## Section 13: Poisson Process with Poisson Increments / 泊松过程与泊松增量

---

### 📋 Section Overview / 章节概览

This section introduces the **Poisson Process (泊松过程)** , a fundamental continuous-time stochastic process with discrete state space. We begin with a review of the **Poisson distribution (泊松分布)** and then define the Poisson process through its key property: **independent Poisson increments (独立泊松增量)** . We also explore how to combine and split Poisson processes through **summed (求和)** and **marked (标记)** processes.

**Why this matters / 为什么重要**: The Poisson process is the building block for modeling random arrivals over time - from phone calls at a call center, insurance claims, emails, to radioactive decay. Understanding it is essential for queueing theory, reliability engineering, finance, and many other fields. This is the foundation for **continuous-time Markov chains (连续时间马尔可夫链)** , which we will study next.

---

### 🎯 Learning Objectives / 学习目标

After completing this section, you will be able to:

1. **Recall and apply** the Poisson distribution's properties (mean, variance, sum, marking)
2. **Define** the Poisson process using the independent Poisson increments property
3. **Calculate** probabilities for Poisson process events over any time interval
4. **Apply** the summed Poisson process theorem to combine independent processes
5. **Apply** the marked Poisson process theorem to split a process
6. **Solve** real-world problems using Poisson process models

---

### 📚 Prerequisites / 前置知识

Before studying this section, you should be familiar with:

- **Probability distributions (概率分布)** : Especially the Poisson distribution
- **Independence (独立性)** : What it means for random variables to be independent
- **Expectation and variance (期望与方差)** : Basic properties
- **Discrete-time stochastic processes (离散时间随机过程)** : From earlier chapters (random walks, Markov chains)
- **Basic calculus (基础微积分)** : For understanding rates and time intervals

---

### 📖 Core Content / 核心内容

---

#### Topic 1: Poisson Distribution Review / 泊松分布回顾

**Intuition / 直觉理解**

The **Poisson distribution (泊松分布)** models the number of "arrivals" (事件发生次数) that occur in a fixed interval of time or space, when these events happen at a constant average rate and independently of each other.

**Analogy / 类比**: Imagine you are watching raindrops fall on a square meter of pavement. On average, 10 drops fall per minute. The actual number in any given minute follows a Poisson distribution with rate λ = 10. Some minutes you might see 8 drops, others 12, but the average is 10.

**Formal Definition / 形式化定义**

A discrete random variable (离散随机变量) \(X\) has a **Poisson distribution (泊松分布)** with rate (速率) \(\lambda\), written \(X \sim \text{Po}(\lambda)\), if its **probability mass function (概率质量函数, PMF)** is:

\[
\mathbb{P}(X = n) = \frac{e^{-\lambda} \lambda^n}{n!}, \quad n = 0, 1, 2, \ldots
\]

**Symbol explanation / 符号说明**:
- \(X\): random variable representing the number of arrivals (表示到达次数的随机变量)
- \(\lambda\) (lambda): the rate parameter, the average number of arrivals (速率参数，平均到达次数)
- \(n\): a specific number of arrivals (具体的到达次数)
- \(e\): Euler's number, approximately 2.71828 (自然常数)
- \(n!\): n factorial = n × (n-1) × ... × 2 × 1 (n的阶乘)
- \(\mathbb{P}(X = n)\): probability that exactly n arrivals occur (恰好发生n次到达的概率)

**Key Properties / 关键性质**

The textbook lists three important properties:

1. **Expectation and Variance (期望与方差)** :
   \[
   \mathbb{E}[X] = \lambda, \quad \text{Var}(X) = \lambda
   \]
   - \(\mathbb{E}[X]\): expected value (mean) of X (期望值/均值)
   - \(\text{Var}(X)\): variance of X (方差)
   - Note: For Poisson, mean = variance (均值等于方差)

2. **Sum of Independent Poisson Variables (独立泊松变量之和)** :
   If \(X \sim \text{Po}(\lambda)\) and \(Y \sim \text{Po}(\mu)\) are independent (独立), then:
   \[
   X + Y \sim \text{Po}(\lambda + \mu)
   \]
   - The sum of two independent Poisson random variables is also Poisson
   - The rates add together

3. **Marking Property (标记性质)** :
   Let \(X \sim \text{Po}(\lambda)\) represent arrivals. Independently "mark" each arrival with probability \(p\). Then:
   - Number of marked arrivals \(Y \sim \text{Po}(p\lambda)\)
   - Number of unmarked arrivals \(Z \sim \text{Po}((1-p)\lambda)\)
   - \(Y\) and \(Z\) are independent

**Note from textbook / 教材注**: The textbook says "I say 'recall', but it is OK if the third one is new to you." (我说"回顾"，但第三个性质对你来说是新的也没关系。)

**Common Applications / 常见应用**:
- Number of calls to a call centre in one hour (一小时内呼叫中心的电话数)
- Number of claims to an insurance company in one year (一年内保险公司的索赔数)
- Number of particles decaying from radioactive material in one second (一秒内放射性物质衰变的粒子数)

---

#### Topic 2: Definition of Poisson Process / 泊松过程的定义

**Intuition / 直觉理解**

Instead of just counting arrivals in a fixed time period, we now want to model the **entire evolution** of arrivals over time. This is a **stochastic process (随机过程)** with:
- **State space (状态空间)** : \(\mathcal{S} = \mathbb{Z}_+ = \{0, 1, 2, \ldots\}\) (discrete, counting number of arrivals)
- **Time (时间)** : \(t \in [0, \infty)\) (continuous)

**Notation note / 符号说明**: In continuous time, we write \(X(t)\) instead of \(X_n\) (which was used for discrete time).

**Analogy / 类比**: Imagine you are at a bus stop. The number of buses that have arrived by time \(t\) is \(X(t)\). At time 0, no buses have arrived: \(X(0) = 0\). In any interval of length \(s\), the number of new arrivals follows a Poisson distribution with rate proportional to \(s\).

**Formal Definition / 形式化定义**

**Definition 13.1: Poisson Process (泊松过程)**

The **Poisson process (泊松过程)** with rate \(\lambda\) is a stochastic process \((X(t))\) with continuous time \(t \in [0, \infty)\) and discrete state space \(\mathcal{S} = \mathbb{Z}_+\) satisfying:

1. **Initial condition (初始条件)** : \(X(0) = 0\)

2. **Poisson increments (泊松增量)** : For all \(s, t > 0\):
   \[
   X(t+s) - X(t) \sim \text{Po}(\lambda s)
   \]
   - The number of arrivals in any interval of length \(s\) follows a Poisson distribution with mean \(\lambda s\)
   - The rate is proportional to the interval length

3. **Independent increments (独立增量)** : For all \(t_1 \leq t_2 \leq t_3 \leq t_4\):
   \[
   X(t_2) - X(t_1) \text{ and } X(t_4) - X(t_3) \text{ are independent}
   \]
   - Arrivals in non-overlapping time intervals are independent
   - **Important**: Overlapping intervals are NOT independent (重叠区间不独立)

**Symbol explanation / 符号说明**:
- \(X(t)\): number of arrivals up to time \(t\) (截至时间t的到达次数)
- \(\lambda\) (lambda): rate parameter, average number of arrivals per unit time (速率参数，单位时间平均到达次数)
- \(s\): length of time interval (时间区间长度)
- \(t\): starting time (起始时间)
- \(\text{Po}(\lambda s)\): Poisson distribution with mean \(\lambda s\) (均值为\(\lambda s\)的泊松分布)

**Historical Note / 历史注记**:
- The Poisson process was discovered in the first decade of the 20th century (20世纪第一个十年)
- Named after the Poisson distribution
- Important contributors: **Filip Lundberg** (Swedish actuary/mathematician) and **A.K. Erlang** (Danish engineer/mathematician)
- **Siméon Denis Poisson** (French mathematician/physicist) studied the distribution in 1837
- **Abraham de Moivre** (French mathematician) used it over 100 years earlier

---

#### Topic 3: Worked Examples / 例题

**Example 13.1: Insurance Claims / 保险索赔**

**Problem / 问题**: Claims arrive at an insurance company at a rate of \(\lambda = 8\) per hour, modeled as a Poisson process. What is the probability there are no claims in a given 15-minute period?

**Solution / 解答**:

**Step 1**: Determine the time interval length.
- 15 minutes = 15/60 = 0.25 hours
- So \(s = 0.25\)

**Step 2**: Find the mean number of claims in this interval.
- By property 2: \(X(t+0.25) - X(t) \sim \text{Po}(\lambda s) = \text{Po}(8 \times 0.25) = \text{Po}(2)\)
- Mean = 2 claims per 15-minute period

**Step 3**: Calculate the probability of 0 claims.
\[
\mathbb{P}(\text{no claims}) = \frac{e^{-2} \times 2^0}{0!} = e^{-2} = 0.135
\]

**Answer / 答案**: The probability is \(e^{-2} \approx 0.135\) or 13.5%.

---

**Example 13.2: Professor's Visitors / 教授访客**

**Problem / 问题**: A professor receives visitors to her office at a rate of \(\lambda = 2.5\) per day, modeled as a Poisson process. What is the probability she gets at least one visitor every day this (5-day) week?

**Solution / 解答**:

**Step 1**: Find probability of at least one visitor on any given day.
- For one day, \(s = 1\), so \(X(t+1) - X(t) \sim \text{Po}(2.5)\)
- Probability of at least one = 1 - probability of zero
\[
\mathbb{P}(\text{at least 1}) = 1 - \frac{e^{-2.5} \times 2.5^0}{0!} = 1 - e^{-2.5} = 0.918
\]

**Step 2**: Use independence across days.
- By property 3 (independent increments), the numbers of visitors on different days are independent
- Probability of at least one each day for 5 days:
\[
(0.918)^5 = 0.652
\]

**Answer / 答案**: The probability is approximately 0.652 or 65.2%.

---

#### Topic 4: Summed and Marked Poisson Processes / 求和与标记泊松过程

**Intuition / 直觉理解**

- **Summed process (求和过程)** : If you have two independent Poisson processes, their sum is also a Poisson process. This is like combining two streams of arrivals into one.
- **Marked process (标记过程)** : If you have one Poisson process and each arrival is independently classified (marked) into one of two categories, each category forms its own Poisson process, and they are independent.

**Analogy / 类比**:
- **Summed**: Emails arrive at your university account (rate 4/hr) and personal account (rate 2/hr). Total emails = sum of two Poisson processes.
- **Marked**: All goals in a football match (rate 2.72/game). Each goal is independently marked as "home" (probability 0.56) or "away" (probability 0.44).

---

**Theorem 13.1: Summed Poisson Process (求和泊松过程)**

**Statement / 陈述**:
Let \((X(t))\) and \((Y(t))\) be independent Poisson processes with rates \(\lambda\) and \(\mu\) respectively. Then the process \((Z(t))\) given by:
\[
Z(t) = X(t) + Y(t)
\]
is a Poisson process with rate \(\lambda + \mu\).

**Symbol explanation / 符号说明**:
- \(X(t)\): first Poisson process with rate \(\lambda\) (第一个速率为\(\lambda\)的泊松过程)
- \(Y(t)\): second Poisson process with rate \(\mu\) (第二个速率为\(\mu\)的泊松过程)
- \(Z(t) = X(t) + Y(t)\): sum process (求和过程)
- Rate of \(Z\): \(\lambda + \mu\) (速率相加)

**Proof / 证明**: The proof is assigned as a problem on Problem Sheet 7 (作业单7). The key idea is to verify the three defining properties of a Poisson process for \(Z(t)\).

---

**Example 13.3: Combined Emails / 合并邮件**

**Problem / 问题**: A student receives emails to her university address at a rate of \(\lambda = 4\) emails per hour, and to her personal address at a rate of \(\mu = 2\) per hour. Using a Poisson process model, what is the probability the student receives 3 or fewer emails in a 30-minute period?

**Solution / 解答**:

**Step 1**: Find the combined rate.
- By Theorem 13.1, total emails follow a Poisson process with rate \(\lambda + \mu = 4 + 2 = 6\) per hour

**Step 2**: Find the mean for 30 minutes.
- 30 minutes = 0.5 hours
- Mean = \(6 \times 0.5 = 3\) emails in 30 minutes
- So \(Z(0.5) \sim \text{Po}(3)\)

**Step 3**: Calculate probability of 3 or fewer.
\[
\mathbb{P}(Z \leq 3) = \sum_{n=0}^{3} \frac{e^{-3} \times 3^n}{n!}
\]

\[
= \frac{e^{-3} \times 3^0}{0!} + \frac{e^{-3} \times 3^1}{1!} + \frac{e^{-3} \times 3^2}{2!} + \frac{e^{-3} \times 3^3}{3!}
\]

\[
= e^{-3} \left(1 + 3 + \frac{9}{2} + \frac{27}{6}\right)
\]

\[
= e^{-3} \left(1 + 3 + 4.5 + 4.5\right) = 13e^{-3}
\]

\[
= 13 \times 0.0498 = 0.647
\]

**Answer / 答案**: The probability is approximately 0.647 or 64.7%.

---

**Theorem 13.2: Marked Poisson Process (标记泊松过程)**

**Statement / 陈述**:
Let \((X(t))\) be a Poisson process with rate \(\lambda\). Each arrival is independently marked with probability \(p\). Then:
- The marked process \((Y(t))\) is a Poisson process with rate \(p\lambda\)
- The unmarked process \((Z(t))\) is a Poisson process with rate \((1-p)\lambda\)
- \((Y(t))\) and \((Z(t))\) are independent

**Symbol explanation / 符号说明**:
- \(X(t)\): original Poisson process with rate \(\lambda\) (原始泊松过程，速率为\(\lambda\))
- \(p\): probability of marking each arrival (标记每个到达的概率)
- \(Y(t)\): marked arrivals (标记的到达)
- \(Z(t)\): unmarked arrivals (未标记的到达)
- Rate of \(Y\): \(p\lambda\) (标记过程的速率)
- Rate of \(Z\): \((1-p)\lambda\) (未标记过程的速率)

**Proof / 证明**: The textbook states "Given the third fact that you were 'reminded' of, it is easy to check the necessary properties." (基于之前"回顾"的第三个性质，很容易验证必要的性质。) This refers to the marking property of the Poisson distribution.

---

**Example 13.4: Football Goals / 足球进球**

**Problem / 问题**: In the 2019/20 English Premier League football season, an average of \(\lambda = 2.72\) goals were scored per game, with a proportion \(p = 0.56\) of them scored by the home team. If we model this as a Poisson process, what is the probability a match ends in a 1-1 draw?

**Solution / 解答**:

**Step 1**: Find rates for home and away goals.
- Home goals: rate = \(p\lambda = 0.56 \times 2.72 = 1.52\) per game
- Away goals: rate = \((1-p)\lambda = 0.44 \times 2.72 = 1.20\) per game

**Step 2**: By Theorem 13.2, home and away goals are independent Poisson processes.

**Step 3**: Calculate probability of exactly 1 home goal AND exactly 1 away goal.
\[
\mathbb{P}(\text{Home}=1) = \frac{e^{-1.52} \times 1.52^1}{1!} = 1.52e^{-1.52}
\]
\[
\mathbb{P}(\text{Away}=1) = \frac{e^{-1.20} \times 1.20^1}{1!} = 1.20e^{-1.20}
\]

**Step 4**: By independence:
\[
\mathbb{P}(1\text{-}1 \text{ draw}) = (1.52e^{-1.52}) \times (1.20e^{-1.20})
\]
\[
= 1.52 \times 1.20 \times e^{-(1.52+1.20)}
\]
\[
= 1.824 \times e^{-2.72}
\]
\[
= 1.824 \times 0.0658 = 0.12
\]

**Answer / 答案**: The probability is approximately 0.12 or 12%.

---

### 🔗 Connections / 知识关联

**Previous topics / 之前的内容**:
- **Discrete-time Markov chains (离散时间马尔可夫链)** : The Poisson process is a continuous-time Markov chain
- **Random walks (随机游走)** : Both are fundamental stochastic processes
- **Poisson distribution (泊松分布)** : The foundation for the Poisson process

**Future topics / 后续内容**:
- **Section 14**: The Poisson process viewed through inter-arrival times (指数分布)
- **Continuous-time Markov chains (连续时间马尔可夫链)** : The Poisson process is the simplest example
- **Queueing theory (排队论)** : Poisson processes model arrival streams
- **Renewal theory (更新理论)** : Generalization of Poisson processes

**Key insight / 关键洞察**: The Poisson process bridges discrete-time Markov chains (which we studied) and continuous-time Markov chains (which we will study next). It's the "bridge" between these two worlds.

---

### ⚠️ Common Mistakes / 常见误区

1. **Confusing Poisson distribution with Poisson process (混淆泊松分布与泊松过程)**
   - Poisson distribution: models count in a FIXED interval
   - Poisson process: models the ENTIRE evolution over time
   - Remember: The process uses the distribution as a building block

2. **Forgetting that increments must be for NON-OVERLAPPING intervals (忘记增量必须用于非重叠区间)**
   - \(X(3) - X(1)\) and \(X(4) - X(2)\) are NOT independent (they overlap from time 2 to 3)
   - Only intervals that don't overlap at all are independent

3. **Mixing up rate and mean (混淆速率与均值)**
   - Rate \(\lambda\) is per unit time
   - Mean for interval of length \(s\) is \(\lambda s\)
   - Example: If \(\lambda = 8\) per hour, mean for 15 min = \(8 \times 0.25 = 2\)

4. **Forgetting to convert time units (忘记转换时间单位)**
   - Always ensure rate and time interval use the same units
   - If rate is per hour, time must be in hours

5. **Applying summed process theorem without checking independence (未检查独立性就应用求和定理)**
   - Theorem 13.1 requires \(X(t)\) and \(Y(t)\) to be INDEPENDENT
   - If they are dependent, the sum may not be a Poisson process

---

### ✍️ Practice / 练习

**Question 1**: A radioactive source emits particles at a rate of \(\lambda = 3\) per second, modeled as a Poisson process. What is the probability that exactly 5 particles are emitted in a 2-second interval?

**Hint / 提示**: 
- First find the mean for a 2-second interval: \(\lambda s = 3 \times 2 = 6\)
- Then use the Poisson PMF: \(\mathbb{P}(X = 5) = \frac{e^{-6} \times 6^5}{5!}\)

---

**Question 2**: Two independent Poisson processes have rates \(\lambda_1 = 2\) and \(\lambda_2 = 3\) per hour. What is the probability that in a 30-minute period, the total number of arrivals from both processes is at least 4?

**Hint / 提示**:
- Use Theorem 13.1 to find the combined rate
- Convert 30 minutes to hours
- Calculate \(\mathbb{P}(Z \geq 4) = 1 - \mathbb{P}(Z \leq 3)\)

---

**Question 3**: A Poisson process with rate \(\lambda = 10\) per hour has each arrival independently marked as "urgent" with probability \(p = 0.3\). What is the probability that in a 1-hour period, there are exactly 2 urgent arrivals and exactly 5 non-urgent arrivals?

**Hint / 提示**:
- Use Theorem 13.2: urgent process rate = \(0.3 \times 10 = 3\), non-urgent rate = \(0.7 \times 10 = 7\)
- They are independent
- Calculate \(\mathbb{P}(\text{urgent}=2) \times \mathbb{P}(\text{non-urgent}=5)\)

---

**Question 4**: A call center receives calls at a rate of 20 per hour. What is the probability that the center receives its first call within the first 3 minutes of operation?

**Hint / 提示**:
- This is about the time until the first arrival
- Think: "no calls in first 3 minutes" means \(X(0.05) = 0\) (3 minutes = 0.05 hours)
- Then probability of first call within 3 minutes = \(1 - \mathbb{P}(\text{no calls in 3 min})\)

---

**Question 5**: True or False: If \(X(t)\) is a Poisson process with rate \(\lambda\), then \(X(5) - X(2)\) and \(X(3) - X(1)\) are independent.

**Hint / 提示**:
- Check if the intervals [2,5] and [1,3] overlap
- Remember: only non-overlapping intervals have independent increments

---

### 📌 Key Takeaways / 要点总结

1. **Poisson distribution (泊松分布)** : \(X \sim \text{Po}(\lambda)\) with PMF \(\mathbb{P}(X=n) = e^{-\lambda}\lambda^n/n!\), mean = variance = \(\lambda\)

2. **Poisson process definition (泊松过程定义)** : Three properties - \(X(0)=0\), Poisson increments \(X(t+s)-X(t) \sim \text{Po}(\lambda s)\), independent increments for non-overlapping intervals

3. **Rate interpretation (速率解释)** : \(\lambda\) is the average number of arrivals per unit time; for interval length \(s\), mean = \(\lambda s\)

4. **Summed Poisson process (求和泊松过程)** : Sum of independent Poisson processes with rates \(\lambda\) and \(\mu\) is Poisson with rate \(\lambda + \mu\)

5. **Marked Poisson process (标记泊松过程)** : Splitting a Poisson process with marking probability \(p\) yields two independent Poisson processes with rates \(p\lambda\) and \((1-p)\lambda\)

6. **Time unit consistency (时间单位一致性)** : Always ensure rate and time interval use the same units

7. **Independence condition (独立性条件)** : Only non-overlapping time intervals have independent increments

---

**Next section preview / 下一节预告**: Section 14 will explore the Poisson process from a different angle - the times between arrivals follow an **exponential distribution (指数分布)** , giving us another way to understand and simulate Poisson processes.