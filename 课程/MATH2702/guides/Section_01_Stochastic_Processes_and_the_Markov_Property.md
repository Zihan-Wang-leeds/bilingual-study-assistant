# Section 1: Stochastic Processes and the Markov Property

> MATH2702 Stochastic Processes - 自学教材
> 生成时间: 2026-07-17 14:44
> 来源页: 10-13

---

# MATH2702 Study Guide / 学习指南
## Part I: Discrete Time Markov Chains / 第一部分：离散时间马尔可夫链
### Section 1: Stochastic Processes and the Markov Property / 随机过程与马尔可夫性质

---

## 📋 Section Overview / 章节概览

This section introduces the fundamental concepts of **stochastic processes (随机过程)** and the **Markov property (马尔可夫性质)**. We begin by distinguishing between deterministic and random models, then explore the four types of stochastic processes based on time and state space. The core of this section is understanding the Markov property - the "memoryless" property that makes certain stochastic processes tractable and widely applicable.

本章介绍随机过程和马尔可夫性质的基本概念。我们从区分确定性模型和随机模型开始，然后探讨基于时间和状态空间的四种随机过程类型。本章的核心是理解马尔可夫性质——这种"无记忆性"使得某些随机过程易于处理且应用广泛。

**Why this matters (为什么这很重要)**: Markov chains are the foundation of modern probability theory and have applications in:
- Finance (金融): Stock price modeling, option pricing
- Engineering (工程): Queueing systems, network traffic
- Biology (生物学): Population dynamics, genetic sequences
- Computer Science (计算机科学): Google's PageRank algorithm, machine learning
- Physics (物理学): Particle movement, thermodynamics

---

## 🎯 Learning Objectives / 学习目标

By the end of this section, you will be able to / 完成本章学习后，你将能够：

1. **Distinguish** between deterministic and stochastic models, and identify appropriate applications for each / 区分确定性模型和随机模型，并识别各自适用的应用场景

2. **Classify** stochastic processes according to their time (discrete/continuous) and state space (discrete/continuous) / 根据时间（离散/连续）和状态空间（离散/连续）对随机过程进行分类

3. **Explain** the Markov property in both intuitive and formal mathematical terms / 用直观和形式化数学语言解释马尔可夫性质

4. **Compute** conditional probabilities and conditional expectations for simple random variables / 计算简单随机变量的条件概率和条件期望

5. **Apply** the Markov property to determine whether a given process is a Markov chain / 应用马尔可夫性质判断给定过程是否为马尔可夫链

6. **Interpret** the conditional independence statement "past and future are independent given the present" / 解释"给定现在，过去和未来条件独立"这一表述

---

## 📚 Prerequisites / 前置知识

Before studying this section, you should be familiar with / 学习本章前，你应该熟悉：

### Probability Basics / 概率基础
- **Sample space (样本空间)**: The set of all possible outcomes of an experiment
- **Event (事件)**: A subset of the sample space
- **Probability measure (概率测度)**: A function ℙ assigning probabilities to events
- **Conditional probability (条件概率)**: ℙ(𝐴|𝐵) = ℙ(𝐴∩𝐵)/ℙ(𝐵) for ℙ(𝐵) > 0

### Random Variables / 随机变量
- **Random variable (随机变量)**: A function from sample space to real numbers
- **Discrete random variable (离散随机变量)**: Takes values in a countable set
- **Continuous random variable (连续随机变量)**: Takes values in an uncountable set
- **Expectation (期望)**: 𝔼(𝑋) = ∑_𝑠 𝑠·ℙ(𝑋=𝑠) for discrete 𝑋

### Independence / 独立性
- **Independence (独立)**: Events 𝐴 and 𝐵 are independent if ℙ(𝐴∩𝐵) = ℙ(𝐴)·ℙ(𝐵)
- **Independent random variables (独立随机变量)**: 𝑋 and 𝑌 are independent if ℙ(𝑋=𝑥, 𝑌=𝑦) = ℙ(𝑋=𝑥)·ℙ(𝑌=𝑦) for all 𝑥,𝑦

### Notation Review / 符号复习
| Symbol | Meaning | 中文含义 |
|--------|---------|----------|
| ℙ(𝐴) | Probability of event A | 事件A的概率 |
| ℙ(𝐴\|𝐵) | Conditional probability of A given B | 给定B时A的条件概率 |
| 𝔼(𝑋) | Expectation of X | X的期望 |
| 𝔼(𝑋\|𝑌) | Conditional expectation of X given Y | 给定Y时X的条件期望 |
| ∑ | Summation | 求和 |
| ∈ | Element of / belongs to | 属于 |
| ℝ | Real numbers | 实数集 |
| ℤ⁺ | Non-negative integers {0,1,2,...} | 非负整数集 |
| ℝ⁺ | Non-negative real numbers [0,∞) | 非负实数集 |

---

## 📖 Core Content / 核心内容

### Topic 1: Deterministic and Random Models / 确定性模型与随机模型

#### Intuition / 直觉理解

**What is a model? (什么是模型？)**

A **model (模型)** is an imitation of a real-world system. Think of it as a simplified representation that helps us understand, predict, and make decisions about complex systems.

**Example analogy (类比)**: 
- A model airplane in a wind tunnel helps engineers understand how a real airplane will fly
- A computer simulation of weather helps meteorologists predict tomorrow's forecast
- A mathematical model of stock prices helps investors make decisions

**Deterministic vs. Stochastic Models (确定性模型 vs. 随机模型)**

| Aspect | Deterministic Model (确定性模型) | Stochastic Model (随机模型) |
|--------|--------------------------------|---------------------------|
| **Output** | Completely determined by inputs | Variable outcomes |
| **Randomness** | No random components | Includes randomness |
| **Reproducibility** | Same inputs → same output | Same inputs → different outputs each run |
| **Use case** | Simple, predictable systems | Complex, uncertain systems |
| **Example** | Moon's orbit around Earth | Apple stock prices |

**Key insight (关键洞察)**: The choice between deterministic and stochastic models depends on:
1. How significant are the random components? (随机成分有多重要？)
2. How much uncertainty exists? (存在多少不确定性？)
3. What level of precision is needed? (需要什么精度水平？)

**The Moon vs. Apple Shares Example (月球 vs. 苹果股票例子)**:

For the **Moon (月球)**:
- Physical laws (Newton's laws, gravity) are well-understood
- Random effects (meteorite impacts) are negligible
- → **Deterministic model** is sufficient

For **Apple shares (苹果股票)**:
- Price changes are highly uncertain
- Many unpredictable factors (news, market sentiment, economy)
- → **Stochastic model** is appropriate

#### Formal Definition / 形式化定义

**Definition (定义)**: A **stochastic model (随机模型)** (pronounced "sto-KASS-tik") is a mathematical model that incorporates randomness to account for uncertainty and unpredictability. The word "stochastic" comes from Greek "stokhastikos" meaning "able to guess" or "aiming at a target."

**Key terminology (关键术语)**:
- **Deterministic model (确定性模型)**: Output is completely determined by inputs and parameters
- **Stochastic model (随机模型)**: Output has variable outcomes due to random components
- **Parameter (参数)**: A constant that characterizes a model (e.g., mean of a distribution)

#### Key Properties / 关键性质

1. **Deterministic models** are appropriate when:
   - Random components are negligible
   - System follows well-understood physical laws
   - High precision is required and achievable

2. **Stochastic models** are appropriate when:
   - System is highly complex
   - Many uncertainties exist
   - We need to understand the range of possible outcomes

3. **Advantages of stochastic models (随机模型的优势)**:
   - Can be run many times to get distribution of outcomes
   - Account for variability and unpredictability
   - Provide risk assessment capabilities

---

### Topic 2: Stochastic Processes / 随机过程

#### Intuition / 直觉理解

**From Random Variables to Stochastic Processes (从随机变量到随机过程)**

Think of a **random variable (随机变量)** as a snapshot - it captures the state at one point in time.

A **stochastic process (随机过程)** is like a movie - it captures how the state evolves over time.

**Analogy (类比)**: 
- Random variable: A photograph of a busy street at noon
- Stochastic process: A video recording of the street throughout the day

**Example: Insurance Claims (保险索赔例子)**

- **Single random variable**: Total number of claims in 2023 → Model as Poisson(λ)
- **Stochastic process**: Number of claims changing over 2024 → Need (𝑋₀, 𝑋₁, 𝑋₂, ...)

**Why do we need stochastic processes? (为什么需要随机过程？)**

Because many real-world phenomena change over time, and we need to understand:
- How they evolve (它们如何演变)
- Dependencies between different time points (不同时间点之间的依赖关系)
- Long-term behavior (长期行为)

#### Formal Definition / 形式化定义

**Definition 1 (定义1)**: A **stochastic process (随机过程)**, usually written as (𝑋ₙ) or (𝑋ₙ : 𝑛 ≥ 0), is an indexed sequence of random variables that are (usually) dependent on each other.

**Components of a Stochastic Process (随机过程的组成部分)**:

1. **State Space (状态空间) 𝒮**: The set of all possible values the process can take
   - Symbol: 𝒮 (calligraphic S)
   - Example: 𝒮 = {Heads, Tails} for coin flips

2. **Index Set (指标集)**: The set that orders the random variables
   - Usually interpreted as time
   - Example: 𝑛 = 0, 1, 2, ... for discrete time

3. **Random Variables (随机变量) 𝑋ₙ**: The value of the process at time 𝑛
   - Each 𝑋ₙ takes values in 𝒮

**Notation (符号说明)**:
- (𝑋ₙ) = (𝑋₀, 𝑋₁, 𝑋₂, ...) - the entire process
- 𝑋ₙ - the value at time 𝑛
- 𝒮 - state space
- 𝑛 - time index

#### Types of Stochastic Processes / 随机过程的类型

**Four Possibilities (四种可能性)**:

| | **Discrete State Space (离散状态空间)** | **Continuous State Space (连续状态空间)** |
|---|---|---|
| **Discrete Time (离散时间)** | **Discrete time, discrete space** | **Discrete time, continuous space** |
| | Example: Number of students attending each lecture | Example: Daily maximum temperature in Leeds |
| | **Main topic of first half of module** | Briefly mentioned |
| **Continuous Time (连续时间)** | **Continuous time, discrete space** | **Continuous time, continuous space** |
| | Example: Number of visitors to a webpage over time | Example: FTSE 100 share index level |
| | **Main topic of second half of module** | Outside scope (see MATH3734) |

**Detailed Explanation of Each Type (每种类型的详细解释)**:

**1. Discrete Time, Discrete Space (离散时间，离散空间)**
- **Time**: Measured at distinct points: 𝑛 = 0, 1, 2, ...
- **State space**: Countable set (finite or countably infinite)
- **Example**: Number of students in each lecture
  - Time: Lecture number (1, 2, 3, ...)
  - State: Number of students (0, 1, 2, ..., up to room capacity)
- **Course focus**: Markov chains - the main topic of Part I

**2. Discrete Time, Continuous Space (离散时间，连续空间)**
- **Time**: Measured at distinct points: 𝑛 = 0, 1, 2, ...
- **State space**: Uncountably infinite continuum
- **Example**: Daily maximum temperature in Leeds
  - Time: Day number (1, 2, 3, ...)
  - State: Temperature in °C (any real number)
- **Course focus**: Briefly mentioned, not emphasized

**3. Continuous Time, Discrete Space (连续时间，离散空间)**
- **Time**: Monitored constantly: 𝑡 ∈ ℝ⁺ = {𝑥 ∈ ℝ : 𝑥 ≥ 0}
- **State space**: Countable set
- **Example**: Number of webpage visitors over time
  - Time: Real time (seconds, minutes, hours)
  - State: Number of visitors (0, 1, 2, ...)
- **Course focus**: Markov jump processes - main topic of Part II

**4. Continuous Time, Continuous Space (连续时间，连续空间)**
- **Time**: Monitored constantly: 𝑡 ∈ ℝ⁺
- **State space**: Uncountably infinite continuum
- **Example**: FTSE 100 share index level
  - Time: Real time throughout trading day
  - State: Index value (any positive real number)
- **Course focus**: Outside scope (see MATH3734 Stochastic Calculus for Finance)

#### Key Properties / 关键性质

1. **Dependence (依赖性)**: The random variables in a stochastic process are usually dependent on each other
   - 𝑋ₙ₊₁ typically depends on 𝑋ₙ
   - This dependence is what makes stochastic processes interesting and useful

2. **Indexing (索引)**: The index set puts the random variables in order
   - Discrete: 𝑛 = 0, 1, 2, ...
   - Continuous: 𝑡 ∈ ℝ⁺

3. **State Space Classification (状态空间分类)**:
   - **Discrete (离散)**: Distinct, separate outcomes (countable)
   - **Continuous (连续)**: Gradually varying continuum (uncountable)

---

### Topic 3: Conditional Probability and Conditional Expectation / 条件概率与条件期望

#### Intuition / 直觉理解

**Why do we need conditional probability? (为什么需要条件概率？)**

In real life, we often have partial information. Conditional probability helps us update our beliefs based on new information.

**Analogy (类比)**: 
- **Unconditional probability**: Probability of rain tomorrow without any other information
- **Conditional probability**: Probability of rain tomorrow given that it's cloudy today

**Conditional Expectation (条件期望)**:
- **Unconditional expectation**: Average value of a random variable
- **Conditional expectation**: Best guess of a random variable given some information

**Example (例子)**: 
- 𝑋 = score on a test
- 𝔼(𝑋) = average score of all students
- 𝔼(𝑋 | studied ≥ 5 hours) = average score of students who studied at least 5 hours

#### Formal Definition / 形式化定义

**Conditional Probability (条件概率)**

**Definition (定义)**: For events 𝐴 and 𝐵 with ℙ(𝐵) > 0, the conditional probability of 𝐴 given 𝐵 is:

ℙ(𝐴 | 𝐵) = ℙ(𝐴 ∩ 𝐵) / ℙ(𝐵)

**Symbol explanation (符号说明)**:
- ℙ(𝐴 | 𝐵): Probability of event A occurring given that event B has occurred
- ℙ(𝐴 ∩ 𝐵): Probability that both A and B occur
- ℙ(𝐵): Probability that B occurs
- Condition: ℙ(𝐵) > 0 (we cannot condition on an impossible event)

**Important note (重要说明)**: Whenever we write a conditional probability, we implicitly assume the conditioning event has strictly positive probability.

**Conditional Expectation (条件期望)**

**Definition (定义)**: For a random variable 𝑋 taking values in state space 𝒮 and event 𝐵 (with ℙ(𝐵) > 0), the conditional expectation of 𝑋 given 𝐵 is:

𝔼(𝑋 | 𝐵) = ∑_{𝑠∈𝒮} 𝑠 · ℙ(𝑋 = 𝑠 | 𝐵)

**Symbol explanation (符号说明)**:
- 𝔼(𝑋 | 𝐵): Expected value of X given that event B occurred
- ∑_{𝑠∈𝒮}: Sum over all possible values s in the state space
- 𝑠: A possible value of X
- ℙ(𝑋 = 𝑠 | 𝐵): Conditional probability that X equals s given B

**Conditional Expectation Given a Random Variable (给定随机变量的条件期望)**

**Definition (定义)**: For random variables X and Y, the conditional expectation 𝔼(𝑋 | 𝑌) is a random variable defined as follows:

1. First, define a function 𝑓(𝑏) = 𝔼(𝑋 | 𝑌 = 𝑏) = ∑_{𝑠∈𝒮} 𝑠 · ℙ(𝑋 = 𝑠 | 𝑌 = 𝑏)

2. Then, 𝔼(𝑋 | 𝑌) = 𝑓(𝑌) is the random variable that takes value 𝔼(𝑋 | 𝑌 = 𝑏) when 𝑌 = 𝑏

**Key insight (关键洞察)**: 
- 𝔼(𝑋 | 𝑌 = 𝑏) is a **number** (the expected value given a specific outcome)
- 𝔼(𝑋 | 𝑌) is a **random variable** (it depends on the random value of Y)

#### Worked Example / 例题

**Example 1.1 (例题1.1)**: Rolling Dice

**Problem (问题)**: Let 𝑍₁, 𝑍₂ be the outcomes of rolling independent fair dice, and define:
- 𝑌 = 𝑍₁
- 𝑋 = 𝑍₁ + 𝑍₂

Find 𝔼(𝑋 | 𝑌), the conditional expectation of X given Y.

**Solution (解答)**:

**Step 1: Understand the setup (理解设置)**
- 𝑍₁ and 𝑍₂ are independent fair dice rolls
- Each takes values in {1, 2, 3, 4, 5, 6} with probability 1/6 each
- 𝑌 = 𝑍₁ (Y equals the first die roll)
- 𝑋 = 𝑍₁ + 𝑍₂ (X equals the sum of both dice)

**Step 2: Apply linearity of conditional expectation (应用条件期望的线性性)**

𝔼(𝑋 | 𝑌) = 𝔼(𝑍₁ + 𝑍₂ | 𝑍₁)
         = 𝔼(𝑍₁ | 𝑍₁) + 𝔼(𝑍₂ | 𝑍₁)

**Why? (为什么？)** Conditional expectation is linear, just like ordinary expectation.

**Step 3: Compute 𝔼(𝑍₁ | 𝑍₁) (计算给定Z₁时Z₁的条件期望)**

If we already know the value of 𝑍₁, our "best guess" of 𝑍₁ is exactly that value.

Formally: The function 𝑓₁(𝑠) = 𝑠 satisfies 𝑓₁(𝑠) = 𝔼(𝑍₁ | 𝑍₁ = 𝑠)

Therefore: 𝔼(𝑍₁ | 𝑍₁) = 𝑍₁

**Step 4: Compute 𝔼(𝑍₂ | 𝑍₁) (计算给定Z₁时Z₂的条件期望)**

Since 𝑍₁ and 𝑍₂ are independent, knowing 𝑍₁ gives no information about 𝑍₂.

Our best guess of 𝑍₂ is simply its unconditional expectation 𝔼(𝑍₂).

𝔼(𝑍₂) = (1+2+3+4+5+6)/6 = 21/6 = 3.5

Formally: The function 𝑓₂(𝑠) = 𝔼(𝑍₂) = 3.5 for all 𝑠 ∈ {1,2,3,4,5,6}

Therefore: 𝔼(𝑍₂ | 𝑍₁) = 3.5

**Step 5: Combine results (合并结果)**

𝔼(𝑋 | 𝑌) = 𝔼(𝑍₁ | 𝑍₁) + 𝔼(𝑍₂ | 𝑍₁)
         = 𝑍₁ + 3.5
         = 𝑌 + 3.5

**Final Answer (最终答案)**: 𝔼(𝑋 | 𝑌) = 𝑌 + 3.5

**Interpretation (解释)**: Given that we know the first die roll is Y, our best guess of the sum X is Y + 3.5 (the known first roll plus the expected value of the second roll).

---

### Topic 4: The Markov Property / 马尔可夫性质

#### Intuition / 直觉理解

**The "Memoryless" Property ("无记忆性"性质)**

Think of a simple board game where you roll dice and move forward:

**Analogy (类比)**: 
- You are currently on square 𝑋ₙ
- Your next square 𝑋ₙ₊₁ depends on:
  1. Where you are now (𝑋ₙ) - you add the dice roll to your current position
  2. The dice roll (random)
- **Crucially**: Given where you are now, it doesn't matter how you got there!

**The Markov property says (马尔可夫性质说明)**:
"The past and the future are conditionally independent given the present."

**In plain language (通俗解释)**:
- To predict the future, only the present matters
- The process "forgets" its history
- We only need to remember where we are, not how we got here

**Real-world examples (现实世界例子)**:
1. **Board game (棋盘游戏)**: Your next position depends only on current position, not on previous moves
2. **Weather (天气)**: Tomorrow's weather depends on today's weather, not on last week's weather (simplified)
3. **Stock prices (股票价格)**: Future price depends on current price, not on the entire price history (in efficient markets)

#### Formal Definition / 形式化定义

**Definition 1.1 (定义1.1)**: Let (𝑋ₙ) = (𝑋₀, 𝑋₁, 𝑋₂, ...) be a stochastic process in discrete time 𝑛 = 0, 1, 2, ... and discrete space 𝒮. Then we say that (𝑋ₙ) has the **Markov property (马尔可夫性质)** if, for all times 𝑛 and all states 𝑥₀, 𝑥₁, ..., 𝑥ₙ, 𝑥ₙ₊₁ ∈ 𝒮, we have:

ℙ(𝑋ₙ₊₁ = 𝑥ₙ₊₁ | 𝑋ₙ = 𝑥ₙ, 𝑋ₙ₋₁ = 𝑥ₙ₋₁, ..., 𝑋₀ = 𝑥₀) = ℙ(𝑋ₙ₊₁ = 𝑥ₙ₊₁ | 𝑋ₙ = 𝑥ₙ)

**Symbol explanation (符号说明)**:
- ℙ(𝑋ₙ₊₁ = 𝑥ₙ₊₁ | ...): Probability that the next state is 𝑥ₙ₊₁ given the history
- 𝑋ₙ₊₁: The random variable at time n+1 (next time step)
- 𝑥ₙ₊₁: A specific value that 𝑋ₙ₊₁ could take
- 𝑋ₙ = 𝑥ₙ: The current state is 𝑥ₙ
- 𝑋ₙ₋₁ = 𝑥ₙ₋₁, ..., 𝑋₀ = 𝑥₀: The entire history of the process
- ℙ(𝑋ₙ₊₁ = 𝑥ₙ₊₁ | 𝑋ₙ = 𝑥ₙ): Probability of next state given only the current state

**What this means (这意味着什么)**:

The left-hand side: Probability of going to state 𝑥ₙ₊₁ next, conditioned on the **entire history** (all past states and current state)

The right-hand side: Probability of going to state 𝑥ₙ₊₁ next, conditioned **only on the current state**

The equality tells us: The entire history doesn't matter - only the current state matters for predicting the future.

#### Key Properties / 关键性质

1. **Memoryless (无记忆性)**: The process "forgets" how it got to the current state
   - Only the present matters for future evolution
   - Past information is irrelevant given the present

2. **Conditional Independence (条件独立)**: Past and future are conditionally independent given the present
   - ℙ(Past and Future | Present) = ℙ(Past | Present) · ℙ(Future | Present)

3. **Simplification (简化)**: Markov processes are much easier to study than general processes
   - We only need to track the current state
   - We can "forget" the entire history

4. **One-step dependence (一步依赖)**: The Markov property is often called "one-step memory"
   - 𝑋ₙ₊₁ depends on 𝑋ₙ but not on 𝑋ₙ₋₁, 𝑋ₙ₋₂, ..., 𝑋₀
   - This is the simplest form of dependence

5. **Historical Note (历史注记)**: Although particular examples of Markov processes go back further, the first general study was by the Russian mathematician **Andrey Andreyevich Markov (安德烈·安德烈耶维奇·马尔可夫)**, published in 1906.

#### Worked Example / 例题

**Example: Board Game (棋盘游戏例子)**

**Problem (问题)**: Consider a simple board game where you start at square 0 and roll a fair die to move forward. Let 𝑋ₙ be your position after n moves. Does this process have the Markov property?

**Solution (解答)**:

**Step 1: Understand the process (理解过程)**
- 𝑋₀ = 0 (start at square 0)
- Each turn: roll die (1-6), move that many squares forward
- 𝑋ₙ₊₁ = 𝑋ₙ + (die roll at turn n+1)

**Step 2: Check the Markov property (检查马尔可夫性质)**

Consider: ℙ(𝑋ₙ₊₁ = 𝑥ₙ₊₁ | 𝑋ₙ = 𝑥ₙ, 𝑋ₙ₋₁ = 𝑥ₙ₋₁, ..., 𝑋₀ = 𝑥₀)

Given the entire history, the next position is:
𝑋ₙ₊₁ = 𝑋ₙ + (die roll)

The die roll is independent of everything, so:
ℙ(𝑋ₙ₊₁ = 𝑥ₙ₊₁ | history) = ℙ(die roll = 𝑥ₙ₊₁ - 𝑥ₙ)

Now consider: ℙ(𝑋ₙ₊₁ = 𝑥ₙ₊₁ | 𝑋ₙ = 𝑥ₙ)

Given only the current position:
ℙ(𝑋ₙ₊₁ = 𝑥ₙ₊₁ | 𝑋ₙ = 𝑥ₙ) = ℙ(die roll = 𝑥ₙ₊₁ - 𝑥ₙ)

**Step 3: Compare (比较)**

Both sides equal ℙ(die roll = 𝑥ₙ₊₁ - 𝑥ₙ), so the Markov property holds.

**Answer (答案)**: Yes, this board game process has the Markov property.

**Intuition (直觉)**: To know where you'll be next turn, you only need to know where you are now. It doesn't matter whether you got there by rolling all 1's or by rolling a 6 once - the future depends only on your current position.

---

### Topic 5: Continuous Time Markov Property / 连续时间马尔可夫性质

#### Intuition / 直觉理解

The Markov property also applies to continuous time processes, though the formal definition is slightly different.

**Analogy (类比)**: 
- Discrete time: Checking the process at specific moments (like checking your position every minute)
- Continuous time: Watching