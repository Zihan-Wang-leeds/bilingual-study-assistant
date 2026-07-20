# Section 22: End of Part II: Continuous time Markov jump processes

> MATH2702 - 自学教材 / Self-Study Guide
> 生成时间: 2026-07-20 15:59
> 来源页: 103-105

---

# 📚 MATH2702: Continuous Time Markov Jump Processes - Part II Summary & Problem Sheet 11

## 完整双语学习指南 / Complete Bilingual Study Guide

---

## 📋 Section Overview / 章节概览

**中文解释：** 本章节是课程"连续时间马尔可夫跳跃过程"第二部分的总结，涵盖了从泊松过程到排队论模型的核心概念。我们将回顾所有重要定义、定理和计算方法，并通过两个实际问题（M/M/1队列和M/M/s/s队列）来巩固理解。这部分内容对期末考试至关重要，因为它整合了整门课程的核心知识点。

**English explanation:** This section serves as the summary for Part II of "Continuous Time Markov Jump Processes," covering core concepts from Poisson processes to queueing theory models. We will review all important definitions, theorems, and computational methods, and reinforce understanding through two practical problems (M/M/1 queue and M/M/s/s queue). This content is crucial for the final exam as it integrates the core knowledge points of the entire course.

---

## 🎯 Learning Objectives / 学习目标

完成本部分学习后，你应该能够 / After completing this section, you should be able to:

1. **定义和描述**泊松过程的三种等价定义方式 / **Define and describe** the three equivalent definitions of Poisson processes
2. **执行**与泊松过程相关的基本计算，包括叠加和标记过程 / **Perform** basic calculations related to Poisson processes, including superposition and marking
3. **定义和计算**生灭过程（birth processes），特别是简单生灭过程 / **Define and calculate** birth processes, especially the simple birth process
4. **陈述和推导**向前和向后方程（forward and backward equations）/ **State and derive** the forward and backward equations
5. **求解**平稳分布（stationary distribution）并应用极限定理 / **Solve** for stationary distributions and apply limit theorems
6. **分析**简单排队模型，如M/M/1和M/M/s/s队列 / **Analyze** simple queueing models such as M/M/1 and M/M/s/s queues

---

## 📚 Prerequisites / 前置知识

**中文解释：** 在学习本部分之前，你需要掌握以下基础知识：

**English explanation:** Before studying this section, you need to master the following prerequisite knowledge:

| 概念 / Concept | 中文说明 | English Description |
|---------------|----------|-------------------|
| 指数分布 / Exponential distribution | 无记忆性，参数λ，均值1/λ | Memoryless property, parameter λ, mean 1/λ |
| 泊松分布 / Poisson distribution | 均值为λt，方差为λt | Mean λt, variance λt |
| 马尔可夫链 / Markov chains | 离散时间马尔可夫性质 | Discrete-time Markov property |
| 矩阵乘法 / Matrix multiplication | 转移矩阵的基本运算 | Basic operations with transition matrices |
| 微分方程 / Differential equations | 一阶线性微分方程求解 | Solving first-order linear differential equations |

---

## 📖 Core Content / 核心内容

---

### Topic 1: Summary of Part II / 第二部分总结

#### 1.1 Poisson Process Definitions / 泊松过程的定义

**中文解释：** 泊松过程有三种等价的定义方式，每种方式都从不同角度揭示了过程的本质。理解这三种定义对于掌握整个课程至关重要。

**English explanation:** The Poisson process has three equivalent definitions, each revealing the essence of the process from a different perspective. Understanding all three definitions is crucial for mastering the entire course.

**Definition 1: Independent Poisson Increments / 独立泊松增量定义**

**中文解释：** 对于任意时间区间(s, t]，增量N(t) - N(s)服从均值为λ(t-s)的泊松分布，且不重叠区间上的增量相互独立。

**English explanation:** For any time interval (s, t], the increment N(t) - N(s) follows a Poisson distribution with mean λ(t-s), and increments on non-overlapping intervals are independent.

数学形式 / Mathematical form:
$$P(N(t) - N(s) = k) = \frac{[\lambda(t-s)]^k}{k!} e^{-\lambda(t-s)}, \quad k = 0, 1, 2, \ldots$$

| 符号 / Symbol | 中文含义 | English Meaning |
|---------------|----------|-----------------|
| N(t) | 到时间t为止的事件数 | Number of events by time t |
| λ | 到达率（单位时间平均事件数） | Arrival rate (average events per unit time) |
| k | 事件发生的次数 | Number of events occurring |
| t-s | 时间区间长度 | Length of time interval |

**Definition 2: Independent Exponential Holding Times / 独立指数停留时间定义**

**中文解释：** 事件之间的等待时间（停留时间）是独立同分布的指数随机变量，参数为λ。这意味着事件到达是一个"无记忆"的过程。

**English explanation:** The waiting times between events (holding times) are independent and identically distributed exponential random variables with parameter λ. This means the arrival process is "memoryless."

数学形式 / Mathematical form:
$$P(T_i > t) = e^{-\lambda t}, \quad t \geq 0$$

其中T_i是第i-1次事件到第i次事件之间的时间 / where T_i is the time between the (i-1)th and ith events.

**Definition 3: Infinitesimal Transitions / 无穷小时间内的转移**

**中文解释：** 在极短的时间Δt内，事件发生的概率与Δt成正比，且几乎不可能发生两个或更多事件。

**English explanation:** In an infinitesimally small time Δt, the probability of an event occurring is proportional to Δt, and it's nearly impossible for two or more events to occur.

数学形式 / Mathematical form:
$$P(N(t+\Delta t) - N(t) = 1) = \lambda \Delta t + o(\Delta t)$$
$$P(N(t+\Delta t) - N(t) \geq 2) = o(\Delta t)$$

| 符号 / Symbol | 中文含义 | English Meaning |
|---------------|----------|-----------------|
| Δt | 无穷小时间增量 | Infinitesimal time increment |
| o(Δt) | 比Δt更高阶的无穷小量 | Higher-order infinitesimal than Δt |
| λΔt | 在Δt内发生一次事件的近似概率 | Approximate probability of one event in Δt |

#### 1.2 Basic Calculations with Poisson Processes / 泊松过程的基本计算

**中文解释：** 泊松过程的基本计算包括：计算在给定时间内发生k次事件的概率、计算等待时间的分布、以及处理叠加和标记泊松过程。

**English explanation:** Basic calculations with Poisson processes include: computing the probability of k events in a given time, calculating waiting time distributions, and handling superposition and marking of Poisson processes.

**Summed Poisson Processes / 叠加泊松过程**

**中文解释：** 如果两个独立的泊松过程（速率分别为λ₁和λ₂）叠加，结果仍然是一个泊松过程，速率为λ₁ + λ₂。

**English explanation:** If two independent Poisson processes (with rates λ₁ and λ₂) are superimposed, the result is still a Poisson process with rate λ₁ + λ₂.

**Marked Poisson Processes / 标记泊松过程**

**中文解释：** 每个事件独立地以概率p被标记（或以概率1-p不被标记），则标记事件构成速率为λp的泊松过程，未标记事件构成速率为λ(1-p)的泊松过程。

**English explanation:** If each event is independently marked with probability p (or not marked with probability 1-p), then the marked events form a Poisson process with rate λp, and the unmarked events form a Poisson process with rate λ(1-p).

#### 1.3 Birth Processes / 生灭过程

**中文解释：** 生灭过程是泊松过程的推广，其中事件发生的速率（出生率）取决于当前状态。简单生灭过程（simple birth process）中，出生率与当前人口数成正比。

**English explanation:** Birth processes are generalizations of Poisson processes where the event rate (birth rate) depends on the current state. In the simple birth process, the birth rate is proportional to the current population size.

数学形式 / Mathematical form:
$$q_{i,i+1} = \lambda_i = i\beta$$

其中β是每个个体的出生率，λ_i是总出生率 / where β is the birth rate per individual, and λ_i is the total birth rate.

#### 1.4 Markov Property in Continuous Time / 连续时间马尔可夫性质

**中文解释：** 连续时间马尔可夫性质表明：给定当前状态，过程的未来演化与过去历史无关。这是所有马尔可夫过程的核心性质。

**English explanation:** The continuous-time Markov property states that, given the current state, the future evolution of the process is independent of its past history. This is the core property of all Markov processes.

数学形式 / Mathematical form:
$$P(X(t+s) = j | X(s) = i, X(u) = x_u, 0 \leq u < s) = P(X(t+s) = j | X(s) = i)$$

#### 1.5 Time Inhomogeneous Poisson Processes / 时间非齐次泊松过程

**中文解释：** 时间非齐次泊松过程中，到达率λ(t)随时间变化。增量N(t) - N(s)服从均值为∫ₛᵗ λ(u)du的泊松分布。

**English explanation:** In a time-inhomogeneous Poisson process, the arrival rate λ(t) varies with time. The increment N(t) - N(s) follows a Poisson distribution with mean ∫ₛᵗ λ(u)du.

#### 1.6 Markov Jump Processes / 马尔可夫跳跃过程

**中文解释：** 马尔可夫跳跃过程由两部分组成：(a) 在每个状态停留的时间（指数分布）和跳跃链（离散时间马尔可夫链）；(b) 无穷小时间内的转移概率。

**English explanation:** Markov jump processes consist of two components: (a) holding times (exponential distribution) in each state and the jump chain (discrete-time Markov chain); (b) transition probabilities in infinitesimal time.

#### 1.7 Forward and Backward Equations / 向前和向后方程

**中文解释：** 向前方程和向后方程是描述转移概率随时间演化的微分方程。向前方程关注从当前状态到未来状态的演化，向后方程关注从过去状态到当前状态的演化。

**English explanation:** The forward and backward equations are differential equations describing the evolution of transition probabilities over time. The forward equation focuses on evolution from the current state to future states, while the backward equation focuses on evolution from past states to the current state.

**Forward Equation / 向前方程:**
$$\frac{d}{dt} P_{ij}(t) = \sum_{k \neq j} P_{ik}(t) q_{kj} - P_{ij}(t) \sum_{k \neq j} q_{jk}$$

**Backward Equation / 向后方程:**
$$\frac{d}{dt} P_{ij}(t) = \sum_{k \neq i} q_{ik} P_{kj}(t) - P_{ij}(t) \sum_{k \neq i} q_{ik}$$

#### 1.8 Transition Rate Diagram / 转移速率图

**中文解释：** 转移速率图是表示状态之间转移速率的图形化工具。每个状态用节点表示，转移速率用带箭头的边表示。

**English explanation:** A transition rate diagram is a graphical tool showing the transition rates between states. Each state is represented by a node, and transition rates are represented by directed edges.

#### 1.9 Communicating Classes / 通信类

**中文解释：** 状态空间可以划分为通信类（communicating classes）。如果两个状态可以互相到达，则它们属于同一个通信类。通信类可以是常返的（recurrent）或瞬变的（transient）。

**English explanation:** The state space can be partitioned into communicating classes. If two states can reach each other, they belong to the same communicating class. A communicating class can be recurrent or transient.

#### 1.10 Hitting Probabilities and Expected Hitting Times / 击中概率和期望击中时间

**中文解释：** 击中概率是从某个状态出发，最终到达目标状态的概率。期望击中时间是从某个状态出发，首次到达目标状态所需的平均时间。

**English explanation:** Hitting probability is the probability of eventually reaching a target state starting from a given state. Expected hitting time is the average time required to first reach a target state starting from a given state.

#### 1.11 Stationary Distribution / 平稳分布

**中文解释：** 平稳分布π满足πQ = 0，其中Q是转移速率矩阵。平稳分布描述了过程长期运行后状态的概率分布。

**English explanation:** The stationary distribution π satisfies πQ = 0, where Q is the transition rate matrix. The stationary distribution describes the probability distribution of states after the process has been running for a long time.

#### 1.12 Limit and Ergodic Theorems / 极限定理和遍历定理

**中文解释：** 极限定理描述了当时间趋于无穷时，转移概率的极限行为。遍历定理表明时间平均等于空间平均。

**English explanation:** Limit theorems describe the limiting behavior of transition probabilities as time goes to infinity. Ergodic theorems state that time averages equal space averages.

#### 1.13 Queueing Models / 排队模型

**中文解释：** 课程中学习的排队模型包括M/M/1队列（单服务器，泊松到达，指数服务时间）和M/M/s/s队列（s个服务器，无等待空间）。

**English explanation:** Queueing models studied in the course include M/M/1 queues (single server, Poisson arrivals, exponential service times) and M/M/s/s queues (s servers, no waiting space).

---

### Topic 2: Exam FAQs / 考试常见问题

**中文解释：** 以下是关于期末考试的一些常见问题及其解答。

**English explanation:** Below are some frequently asked questions about the final exam along with their answers.

**Q1: 考试时长是多少？/ How long is the exam?**
A: 考试时长为两小时。/ The exam is two hours.

**Q2: 考试有多少道题？/ How many questions are there in the exam?**
A: 有四道较长的多部分问题，每道20分，长度与往年试卷类似。/ There are four long-ish multi-part questions, worth 20 marks each, of similar length to those on past papers.

**Q3: 考试中需要做R编程吗？/ Is there R work on the exam?**
A: 不需要。/ No.

**Q4: 展示解题过程和清晰解释答案有分数吗？/ Are there marks for showing my working and clearly explaining my answer?**
A: 是的！/ Yes!

---

### Topic 3: Problem Sheet 11 - Question 1: M/M/1 Queue / M/M/1队列

#### 3.1 Part (a): Average Waiting Time in Queue / 队列中平均等待时间

**中文解释：** 考虑一个M/M/1队列，到达率为λ，服务率为μ，且μ < λ（即系统不稳定，队列会无限增长）。我们需要证明队列中个体的平均等待时间为λ/[μ(μ-λ)]。

**English explanation:** Consider an M/M/1 queue with arrival rate λ and service rate μ, with μ < λ (meaning the system is unstable and the queue will grow indefinitely). We need to justify that the average time an individual spends waiting in the queue is λ/[μ(μ-λ)].

**Solution / 解答：**

**中文解释：** 我们在课程中已经知道，队列中平均有λ/(μ-λ)个个体。每个个体需要接受服务，服务时间服从Exp(μ)分布，均值为1/μ。将这两个量相乘，就得到了平均等待时间。

**English explanation:** We saw in lectures that there are on average λ/(μ-λ) individuals in the queue. Each individual will take an Exp(μ) time to be serviced, which has mean 1/μ. Multiplying these gives the result.

数学推导 / Mathematical derivation:
$$\text{Average waiting time} = \frac{\lambda}{\mu - \lambda} \times \frac{1}{\mu} = \frac{\lambda}{\mu(\mu - \lambda)}$$

| 符号 / Symbol | 中文含义 | English Meaning |
|---------------|----------|-----------------|
| λ | 到达率（单位时间到达的顾客数） | Arrival rate (customers per unit time) |
| μ | 服务率（单位时间能服务的顾客数） | Service rate (customers served per unit time) |
| λ/(μ-λ) | 队列中的平均顾客数 | Average number of customers in queue |
| 1/μ | 每个顾客的平均服务时间 | Average service time per customer |

#### 3.2 Part (b): Numerical Example / 数值例子

**中文解释：** 现在考虑一个商店的收银台队列。顾客到达率为每小时28人，在收银台的平均时间为2分钟。我们需要计算顾客在队列中等待的平均时间（以分钟为单位）。

**English explanation:** Now consider the queue for a single cash register in a shop. Customers arrive at a rate of 28 per hour, and the average time at the till is 2 minutes. We need to calculate the average time a customer waits in the queue, in minutes.

**Solution / 解答：**

**中文解释：** 首先统一时间单位。我们使用小时作为时间单位，则λ = 28（每小时28人）。服务时间平均为2分钟，即2/60 = 1/30小时，所以服务率μ = 30（每小时30人）。

**English explanation:** First, unify the time units. We use hours as the time unit, so λ = 28 (28 per hour). The average service time is 2 minutes, which is 2/60 = 1/30 hour, so the service rate μ = 30 (30 per hour).

代入公式 / Substitute into the formula:
$$\text{Average waiting time} = \frac{\lambda}{\mu(\mu - \lambda)} = \frac{28}{30(30 - 28)} = \frac{28}{60} = \frac{7}{15} \text{ hours}$$

转换为分钟 / Convert to minutes:
$$\frac{7}{15} \times 60 = 28 \text{ minutes}$$

所以顾客平均等待28分钟。/ So the average waiting time is 28 minutes.

#### 3.3 Part (c): Two Cash Registers with Random Assignment / 两个收银台随机分配

**中文解释：** 商店决定开设第二个收银台。每个顾客以50:50的概率随机选择其中一个收银台排队。我们需要计算新的平均等待时间，并仔细证明答案。

**English explanation:** The shop decides to open a second cash register. Each customer chooses one of the registers to queue for with 50:50 probability at random. We need to calculate the new average waiting time and carefully justify the answer.

**Solution / 解答：**

**中文解释：** 每个收银台的到达过程现在是一个标记泊松过程（marked Poisson process）。由于每个顾客独立地以概率1/2选择每个收银台，每个收银台的到达率变为λ/2 = 14（每小时14人）。服务率μ保持不变，仍为30。

**English explanation:** The arrival process at each till is now a marked Poisson process. Since each customer independently chooses each till with probability 1/2, the arrival rate at each till becomes λ/2 = 14 (14 per hour). The service rate μ remains unchanged at 30.

代入公式 / Substitute into the formula:
$$\text{Average waiting time} = \frac{\lambda/2}{\mu(\mu - \lambda/2)} = \frac{14}{30(30 - 14)} = \frac{14}{30 \times 16} = \frac{14}{480} = \frac{7}{240} \text{ hours}$$

转换为分钟 / Convert to minutes:
$$\frac{7}{240} \times 60 = \frac{7}{4} = 1.75 \text{ minutes} = 1 \text{ minute } 45 \text{ seconds}$$

所以平均等待时间从28分钟大幅下降到1分45秒。/ So the average waiting time drops dramatically from 28 minutes to 1 minute 45 seconds.

**关键推理 / Key Reasoning:**
1. 每个收银台的到达过程是标记泊松过程，速率为λ/2 / The arrival process at each till is a marked Poisson process with rate λ/2
2. 每个收银台独立运行，服务率仍为μ / Each till operates independently with service rate μ
3. 每个收银台的M/M/1队列的等待时间公式适用 / The M/M/1 queue waiting time formula applies to each till

#### 3.4 Part (d): Improving the Model / 改进模型

**中文解释：** 我们如何改进两个收银台的模型，使其更准确地反映真实的排队行为？这些改进对平均等待时间有什么影响？

**English explanation:** How might we improve the model of a shop with two cash registers to more accurately reflect true queueing behavior? What effect would these improvements have on the average waiting time?

**Solution / 解答：**

**中文解释：** 以下是一些可能的改进及其影响：

**English explanation:** Here are some possible improvements and their effects:

| 改进 / Improvement | 中文说明 | English Description | 对等待时间的影响 / Effect on Waiting Time |
|-------------------|----------|---------------------|------------------------------------------|
| 顾客选择最短队列 / Join shortest queue | 顾客会观察两个队列的长度，选择较短的队列 | Customers observe both queue lengths and choose the shorter one | 减少 / Decrease |
| 队列间转移 / Queue switching | 如果顾客所在的队列变长，他们可以转移到另一个队列 | Customers can switch queues if their queue becomes longer | 减少 / Decrease |
| 动态队列选择 / Dynamic queue selection | 顾客持续监控队列长度并随时调整 | Customers continuously monitor queue lengths and adjust | 减少 / Decrease |

**中文解释：** 在所有情况下，平均等待时间都会减少，因为资源（服务器）得到了更有效的利用。

**English explanation:** In all cases, the average waiting time will decrease because resources (servers) are being used more efficiently.

---

### Topic 4: Problem Sheet 11 - Question 2: M/M/s/s Queue / M/M/s/s队列

#### 4.1 Problem Description / 问题描述

**中文解释：** 电话呼叫中心的电话呼叫被建模为M/M/s/s队列：呼叫到达是速率为λ的泊松过程，通话时长服从参数为μ的指数分布，有s个工作人员接听电话。第二个s表示同时只能有s个呼叫者——如果所有工作人员都在接听电话，新呼叫立即被丢弃，没有排队或等待的机制。

**English explanation:** Telephone calls to a call centre are modelled as an M/M/s/s queue: call arrivals are a Poisson process with rate λ, call lengths are exponential with rate μ, and there are s workers available to answer the phone. The second s denotes that there is only enough phone lines for s callers at a time – if all workers are answering calls, any new calls are immediately dropped, and there is no technology for holding in a queue or waiting for a worker to become free.

#### 4.2 Part (a): Transition Rates / 转移速率

**中文解释：** 令X(t)为时间t时正在接听的电话数量。写出状态i, j ∈ {0, 1, ..., s}, i ≠ j的转移速率qᵢⱼ。

**English explanation:** Let X(t) be the number of calls being answered at time t. Write down the transition rates qᵢⱼ for i, j ∈ {0, 1, ..., s}, i ≠ j.

**Solution / 解答：**

**中文解释：** 转移速率如下：

**English explanation:** The transition rates are as follows:

$$q_{i,i+1} = \lambda \quad \text{for } i = 0, 1, \ldots, s-1$$
$$q_{i,i-1} = i\mu \quad \text{for } i = 1, 2, \ldots, s$$

**中文解释：** 解释：当有至少一个空闲工作人员时（即i < s），新呼叫到达的速率为λ，表示状态从i增加到i+1。当有i个呼叫正在进行时，每个呼叫以速率μ结束，所以总结束速率为iμ，表示状态从i减少到i-1。

**English explanation:** Explanation: When there is at least one free server (i.e., i < s), new calls arrive at rate λ, representing a transition from state i to i+1. When there are i calls in progress, each call ends at rate μ, so the total ending rate is iμ, representing a transition from state i to i-1.

**注意：** 当i = s时，所有工作人员都忙，新呼叫被丢弃，所以没有从s到s+1的转移。/ **Note:** When i = s, all workers are busy, new calls are dropped, so there is no transition from s to s+1.

#### 4.3 Part (b): Erlang's Formula / 埃尔朗公式

**中文解释：** 埃尔朗公式（Erlang's formula）指出，所有s个工作人员都在接听电话的长期时间比例为：

**English explanation:** Erlang's formula states that the long-run proportion of time that all s workers are answering calls is:

$$\frac{\rho^s / s!}{\sum_{i=0}^s \rho^i / i!}$$

其中ρ = λ/μ。/ where ρ = λ/μ.

我们需要证明埃尔朗公式。/ We need to prove Erlang's formula.

**Proof / 证明：**

**中文解释：** 我们首先猜测平稳分布的形式为πⱼ = Cρʲ/j!，其中j = 0, 1, ..., s，C是归一化常数。然后验证这个分布满足πQ = 0。

**English explanation:** We first guess that the stationary distribution has the form πⱼ = Cρʲ/j! for j = 0, 1, ..., s, where C is a normalizing constant. Then we verify that this distribution satisfies πQ = 0.

**Step 1: 归一化常数 / Normalizing Constant**

**中文解释：** 由于所有概率之和必须为1，我们有：

**English explanation:** Since all probabilities must sum to 1, we have:

$$\sum_{j=0}^s \pi_j = C \sum_{j=0}^s \frac{\rho^j}{j!} = 1$$

所以 / Therefore:
$$C = \frac{1}{\sum_{i=0}^s \rho^i / i!}$$

**Step 2: 验证πQ = 0 / Verify πQ = 0**

**中文解释：** 对于M/M/s/s队列，全局平衡方程（πQ = 0）有两种形式：

**English explanation:** For the M/M/s/s queue, the global balance equations (πQ = 0) have two forms:

**对于内部状态i = 0, 1, ..., s-1 / For interior states i = 0, 1, ..., s-1:**

$$(i+1)\mu \pi_{i+1} - (\lambda + i\mu)\pi_i + \lambda \pi_{i-1} = 0$$

**对于边界状态i = s / For boundary state i = s:**

$$-s\mu \pi_s + \lambda \pi_{s-1} = 0$$

**中文解释：** 对于内部