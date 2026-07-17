# Section 22: End of Part II: Continuous Time Markov Jump Processes

> MATH2702 Stochastic Processes - 自学教材
> 生成时间: 2026-07-17 14:57
> 来源页: 103-105

---

好的，同学，你好。我是你的教授。欢迎来到我们《随机过程》课程的第二部分总结与复习章节。这份自学材料将引导你完成对“连续时间马尔可夫跳跃过程”这一核心主题的全面回顾，并为你提供应对期末考试的关键指导和练习。

请务必认真阅读每一个部分，并尝试独立完成所有例题和练习。这份材料设计为“自包含”的，这意味着你不需要再查阅其他资料，所有你需要知道的内容都在这里。

让我们开始吧。

---

### 📋 Section Overview / 章节概览

This section, "End of Part II: Continuous time Markov jump processes (第二部分结束：连续时间马尔可夫跳跃过程)", serves as the comprehensive summary and review for the second major part of the course. It covers everything from the foundational **Poisson process (泊松过程)** to complex **queueing models (排队模型)**. The raw material provides a checklist of examinable topics, answers to frequently asked questions about the exam, and a problem sheet with fully worked solutions.

**Why this matters (为什么这很重要):** This is your final preparation before the exam. Mastering the concepts and techniques summarized here is crucial for success. The problem sheet demonstrates the exact level of detail and problem-solving approach expected in the exam. This section is your roadmap to a high score.

### 🎯 Learning Objectives / 学习目标

By the end of this study guide, you will be able to:

1.  **Define and calculate** with the **Poisson process (泊松过程)** and its variants (summed, marked, time-inhomogeneous).
2.  **Define and analyze** **birth processes (生灭过程)**, including the simple birth process.
3.  **Define and work with** **Markov jump processes (马尔可夫跳跃过程)** using both holding times/jump chains and infinitesimal transitions.
4.  **Derive and apply** the **forward and backward equations (向前和向后方程)**.
5.  **Analyze** the long-term behavior of a Markov jump process by finding its **stationary distribution (平稳分布)** and applying **limit and ergodic theorems (极限与遍历定理)**.
6.  **Model and solve** simple queueing systems, specifically the **M/M/1** and **M/M/s/s** queues.

### 📚 Prerequisites / 前置知识

Before you begin, you should be comfortable with the following concepts from Part I and earlier in Part II:

*   **Probability Theory (概率论):** Random variables, expectation, variance, exponential distribution (指数分布), Poisson distribution (泊松分布).
*   **Discrete-time Markov Chains (离散时间马尔可夫链):** Transition matrices, communicating classes (通信类), recurrence/transience (常返/瞬时), stationary distributions, hitting probabilities.
*   **Basic Calculus (基础微积分):** Differentiation, solving simple differential equations.
*   **Part I Summary (第一部分总结):** The concepts from the first part of the course are assumed knowledge.

### 📖 Core Content / 核心内容

#### Topic 1: Summary of Part II & Exam FAQs (第二部分总结与考试常见问题)

**Intuition / 直觉理解**: This is your final checklist. Think of it as a "survival guide" for the exam. The professor has explicitly told you what you need to know. The FAQ section answers the most common administrative questions about the exam format.

**Formal Definition / 形式化定义**: The summary is a list of skills. Let's break down each point.

1.  **Define the Poisson process (定义泊松过程)** in terms of:
    *   **(a) independent Poisson increments (独立泊松增量):** The number of events in any time interval `(s, t]` is a Poisson random variable with mean `λ(t-s)`, and the numbers of events in disjoint time intervals are independent.
    *   **(b) independent exponential holding times (独立指数停留时间):** The time between consecutive events (inter-arrival times) are independent and identically distributed (i.i.d.) exponential random variables with rate `λ`.
    *   **(c) transitions in an infinitesimal time period (无穷小时间段内的转移):** In a very small time `h`, the probability of one event is `λh + o(h)`, the probability of more than one event is `o(h)`, and the probability of no event is `1 - λh + o(h)`.

2.  **Perform basic calculations (进行基本计算)** with a Poisson process, including:
    *   **Summed Poisson processes (求和泊松过程):** If you have two independent Poisson processes with rates `λ₁` and `λ₂`, the process of all events from either is a Poisson process with rate `λ₁ + λ₂`.
    *   **Marked Poisson processes (标记泊松过程):** Each event in a Poisson process is assigned a "mark" (e.g., type 1 or type 2) with a certain probability. The processes for each mark are independent Poisson processes.

3.  **Define and perform basic calculations with birth processes (定义并计算生灭过程)**, including the **simple birth process (简单生灭过程)**. A birth process is a Markov jump process where the state can only increase by 1. In a simple birth process, the birth rate is proportional to the current population size (e.g., `λₙ = nβ`).

4.  **State the Markov property in continuous time (陈述连续时间下的马尔可夫性)**. The future of the process, given its present state, is independent of its past. Formally: `P(X(t+s) = j | X(u) for all u ≤ s, X(s) = i) = P(X(t+s) = j | X(s) = i)`.

5.  **Define and perform basic calculations with time inhomogeneous Poisson processes (定义并计算时间非齐次泊松过程)**. The rate `λ(t)` is a function of time, not a constant.

6.  **Define Markov jump processes (定义马尔可夫跳跃过程)** in terms of:
    *   **(a) holding times and the jump chain (停留时间和跳跃链):** The process stays in a state `i` for an exponentially distributed time with rate `qᵢ`, then jumps to a new state `j` with probability `Pᵢⱼ` (the jump chain).
    *   **(b) transitions in an infinitesimal time period (无穷小时间段内的转移):** In a small time `h`, the probability of jumping from `i` to `j` is `qᵢⱼh + o(h)`, and the probability of leaving state `i` is `qᵢh + o(h)`.

7.  **State and derive the forward and backward equations (陈述并推导向前和向后方程)**. These are differential equations for the transition probabilities `Pᵢⱼ(t)`.
    *   **Backward Equation (向后方程):** `d/dt Pᵢⱼ(t) = Σₖ qᵢₖ Pₖⱼ(t) - qᵢ Pᵢⱼ(t)`
    *   **Forward Equation (向前方程):** `d/dt Pᵢⱼ(t) = Σₖ Pᵢₖ(t) qₖⱼ - qⱼ Pᵢⱼ(t)`

8.  **Draw a transition rate diagram (画出转移速率图)**. A diagram where nodes are states, and arrows between them are labeled with the transition rates `qᵢⱼ`.

9.  **Partition the state space into communicating classes (将状态空间划分为通信类)**, and identify if they are **recurrent (常返)** or **transient (瞬时)**. This is the same concept as for discrete-time chains, but applied to the jump chain.

10. **Calculate hitting probabilities and expected hitting times (计算击中概率和期望击中时间)**. The probability of reaching a set of states before another, and the expected time to do so.

11. **Find a stationary distribution by solving πQ = 0 (通过求解 πQ = 0 找到平稳分布)**. `π` is a row vector of probabilities, and `Q` is the generator matrix. The equation `πQ = 0` is the continuous-time equivalent of `πP = π`.

12. **Apply the limit and ergodic theorems (应用极限与遍历定理)** on the long term behaviour of Markov jump chains. If the process is irreducible and positive recurrent, then `lim_{t→∞} Pᵢⱼ(t) = πⱼ`, and time averages converge to ensemble averages.

13. **Use techniques from the course to analyse simple models of queues (使用课程中的技术分析简单的排队模型)**. This includes M/M/1, M/M/∞, and M/M/s/s queues.

**Exam F AQs (考试常见问题)**:
*   **How long is the exam? (考试多长时间？)** Two hours.
*   **How many questions? (多少道题？)** Four long-ish multi-part questions, each worth 20 marks.
*   **Is there R work on the exam? (考试有R语言内容吗？)** No.
*   **Are there marks for showing my working? (展示解题过程有分数吗？)** Yes!

---

#### Topic 2: Problem Sheet 11 - Worked Solutions (习题11 - 详细解答)

**Intuition / 直觉理解**: This problem sheet tests your ability to apply the concepts from the course to real-world queueing problems. The solutions are provided, but we will go through them step-by-step to ensure you understand the *logic* behind each calculation.

**Worked Examples / 例题**:

**Question 1: M/M/1 Queue (M/M/1 队列)**

**(a) Average waiting time in an M/M/1 queue (M/M/1 队列中的平均等待时间)**

*   **Problem (问题):** Consider an M/M/1 queue with arrival rate `λ` and service rate `μ < λ`. Justify the statement that the average time an individual spends waiting in the queue is `λ / (μ(μ-λ))`.
*   **Solution (解答):**
    1.  **Step 1: Recall the average number in the queue (回忆队列中的平均人数).** From lectures, we know that for an M/M/1 queue, the average number of individuals *in the queue* (not being served) is `L_q = λ² / (μ(μ-λ))`. Wait, the solution says `λ/(μ-λ)`. Let's check. The average number *in the system* is `L = λ/(μ-λ)`. The average number *in the queue* is `L_q = L - ρ = λ/(μ-λ) - λ/μ = (λμ - λ(μ-λ)) / (μ(μ-λ)) = (λμ - λμ + λ²) / (μ(μ-λ)) = λ² / (μ(μ-λ))`. The solution in the raw material says "there are on average `λ/(μ-λ)` individuals in the queue." This is a slight inaccuracy in the raw material; it should be "in the system". We will proceed with the logic as presented, but be aware of this nuance.
    2.  **Step 2: Apply Little's Law (应用利特尔法则).** Little's Law states: `L = λW`, where `L` is the average number in the system, `λ` is the arrival rate, and `W` is the average time spent in the system. For the queue, we have `L_q = λ W_q`, where `W_q` is the average time spent waiting in the queue.
    3.  **Step 3: Calculate `W_q` (计算 `W_q`).** The solution's logic is: "Each one will take an Exp(μ) time to be serviced, which has mean `1/μ`. Multiplying these gives the result." This is a heuristic. A more rigorous way is:
        *   Average number in the queue (from the solution's statement): `L_q = λ/(μ-λ)`.
        *   Using Little's Law for the queue: `W_q = L_q / λ = (λ/(μ-λ)) / λ = 1/(μ-λ)`.
        *   This is the average waiting time in the queue. The solution's formula `λ / (μ(μ-λ))` is the average waiting time in the *system* (queue + service). Let's verify: `W = W_q + 1/μ = 1/(μ-λ) + 1/μ = (μ + μ - λ) / (μ(μ-λ)) = (2μ - λ) / (μ(μ-λ))`. This is not the same as `λ / (μ(μ-λ))`.
        *   **Correction (更正):** The formula `λ / (μ(μ-λ))` is actually the average time spent *in the queue* for an M/D/1 queue (deterministic service), not M/M/1. For M/M/1, the average waiting time in the queue is `W_q = λ / (μ(μ-λ))`? Let's re-derive.
        *   `L_q = λ² / (μ(μ-λ))`.
        *   `W_q = L_q / λ = λ / (μ(μ-λ))`.
        *   Yes! The formula `λ / (μ(μ-λ))` is correct for the average waiting time in the queue for an M/M/1 queue. The solution's justification is a bit loose, but the final formula is correct. The average number in the queue is `λ²/(μ(μ-λ))`, and the average service time is `1/μ`. Multiplying them gives `λ²/(μ²(μ-λ))`, which is not `W_q`. The correct logic is to use Little's Law.

    **Final Answer (最终答案):** The average time an individual spends waiting in the queue is `W_q = λ / (μ(μ-λ))`.

**(b) Numerical example (数值例子)**

*   **Problem (问题):** Consider the queue for a single cash register. Customers arrive at a rate of 28 per hour, and the average time at the till is 2 minutes. What is the average time, in minutes, that a customer waits in the queue?
*   **Solution (解答):**
    1.  **Step 1: Define parameters (定义参数).** We need to work in consistent time units. Let's use hours.
        *   Arrival rate: `λ = 28` customers per hour.
        *   Service rate: Average service time is 2 minutes = `2/60 = 1/30` hours. So, service rate `μ = 1 / (1/30) = 30` customers per hour.
    2.  **Step 2: Apply the formula (应用公式).** The average waiting time in the queue is:
        `W_q = λ / (μ(μ-λ)) = 28 / (30 * (30 - 28)) = 28 / (30 * 2) = 28 / 60` hours.
    3.  **Step 3: Convert to minutes (转换为分钟).** `W_q = (28/60) * 60 = 28` minutes.
    **Final Answer (最终答案):** 28 minutes.

**(c) Two cash registers with random choice (两个收银台，随机选择)**

*   **Problem (问题):** The shop opens a second cash register. Each customer chooses one of the registers to queue for 50:50 at random. What is the average wait time now?
*   **Solution (解答):**
    1.  **Step 1: Model the new system (建模新系统).** Each customer independently chooses a register with probability 1/2. This is a **marked Poisson process (标记泊松过程)**. The arrival process to each register is a Poisson process with rate `λ/2 = 28/2 = 14` customers per hour.
    2.  **Step 2: Apply the M/M/1 formula (应用M/M/1公式).** Each register is now an independent M/M/1 queue with `λ' = 14` and `μ = 30`.
    3.  **Step 3: Calculate the new waiting time (计算新的等待时间).**
        `W_q' = λ' / (μ(μ-λ')) = 14 / (30 * (30 - 14)) = 14 / (30 * 16) = 14 / 480` hours.
    4.  **Step 4: Convert to minutes (转换为分钟).**
        `W_q' = (14/480) * 60 = (14 * 60) / 480 = 840 / 480 = 7/4 = 1.75` minutes.
        This is 1 minute and 45 seconds (since 0.75 minutes = 45 seconds).
    **Final Answer (最终答案):** 1 minute 45 seconds.

**(d) Improving the model (改进模型)**

*   **Problem (问题):** How might you improve the model of a shop with two cash registers to more accurately reflect true queueing behaviour? What effect would this have on the average wait time?
*   **Solution (解答):**
    *   **Improvement 1 (改进1):** Assume customers join the **shortest queue (最短队列)**, rather than picking one at random. This is more realistic.
    *   **Improvement 2 (改进2):** Assume a customer will **move to the other till (换到另一个收银台)** if it becomes empty.
    *   **Improvement 3 (改进3):** Assume that customers will **change queues (换队)** if the other queue gets shorter than the one they are currently in.
    *   **Effect on average wait time (对平均等待时间的影响):** In all cases, the average waiting time will **go down (下降)**. This is because the system becomes more efficient at utilizing the available service capacity.

---

**Question 2: M/M/s/s Queue (Erlang's Formula) (M/M/s/s 队列 - 埃尔朗公式)**

*   **Problem (问题):** Telephone calls to a call centre are modelled as an M/M/s/s queue. Call arrivals are a Poisson process with rate `λ`, call lengths are exponential with rate `μ`, and there are `s` workers. The second `s` denotes that there is only enough phone lines for `s` callers at a time – if all workers are answering calls, any new calls are immediately dropped (no queue).

**(a) Transition rates (转移速率)**

*   **Problem (问题):** Let `X(t)` be the number of calls being answered at time `t`. Write down the transition rates `qᵢⱼ` for `i, j ∈ {0, 1, ..., s}`, `i ≠ j`.
*   **Solution (解答):**
    *   **Arrivals (到达):** When there are `i` calls being answered, and `i < s`, a new call can arrive. The arrival rate is `λ`. So, for `i = 0, 1, ..., s-1`, the transition rate from `i` to `i+1` is `q_{i, i+1} = λ`.
    *   **Departures (离开):** When there are `i` calls being answered, and `i > 0`, a call can end. Each of the `i` calls ends at rate `μ`. So, the total departure rate is `iμ`. Thus, for `i = 1, 2, ..., s`, the transition rate from `i` to `i-1` is `q_{i, i-1} = iμ`.
    *   **All other transitions (所有其他转移):** For any other `i ≠ j`, `qᵢⱼ = 0`.
    **Final Answer (最终答案):**
    `q_{i, i+1} = λ` for `i = 0, 1, ..., s-1`
    `q_{i, i-1} = iμ` for `i = 1, 2, ..., s`
    All other `qᵢⱼ = 0`.

**(b) Proving Erlang's Formula (证明埃尔朗公式)**

*   **Problem (问题):** Erlang's formula states that the long-run proportion of time that all `s` workers are answering calls is `(ρˢ/s!) / (Σᵢ₌₀ˢ ρⁱ/i!)`, where `ρ = λ/μ`. Prove Erlang's formula.
*   **Solution (解答):**
    1.  **Step 1: Claim a stationary distribution (假设一个平稳分布).** We claim that a stationary distribution `π` is given by:
        `πⱼ = C * (ρʲ / j!)` for `j = 0, 1, ..., s`, where `C` is a normalizing constant.
    2.  **Step 2: Find the normalizing constant (找到归一化常数).** Since `π` is a probability distribution, the sum of all probabilities must be 1:
        `Σⱼ₌₀ˢ πⱼ = 1`
        `Σⱼ₌₀ˢ C * (ρʲ / j!) = 1`
        `C * Σⱼ₌₀ˢ (ρʲ / j!) = 1`
        Therefore, `C = 1 / (Σⱼ₌₀ˢ (ρʲ / j!))`.
    3.  **Step 3: State the goal (陈述目标).** The long-run proportion of time all `s` workers are busy is `πₛ`. So, we need to show that `πₛ = (ρˢ/s!) / (Σᵢ₌₀ˢ ρⁱ/i!)`. This is exactly `C * (ρˢ/s!)`, which matches our claim. So, we just need to prove that our claimed `π` satisfies the global balance equations `πQ = 0`.
    4.  **Step 4: Write the global balance equations (写出全局平衡方程).** The global balance equations for this birth-death process are:
        *   For state `i = 0`:
            `(rate out of 0) * π₀ = (rate into 0)`
            `(q₀₁) * π₀ = (q₁₀) * π₁`
            `λ * π₀ = μ * π₁`  (Equation 0)
        *   For state `i = 1, 2, ..., s-1`:
            `(rate out of i) * πᵢ = (rate into i)`
            `(q_{i, i+1} + q_{i, i-1}) * πᵢ = (q_{i-1, i}) * π_{i-1} + (q_{i+1, i}) * π_{i+1}`
            `(λ + iμ) * πᵢ = λ * π_{i-1} + (i+1)μ * π_{i+1}`  (Equation i)
        *   For state `i = s`:
            `(rate out of s) * πₛ = (rate into s)`
            `(q_{s, s-1}) * πₛ = (q_{s-1, s}) * π_{s-1}`
            `(sμ) * πₛ = λ * π_{s-1}`  (Equation s)
    5.  **Step 5: Verify the claim for `i = 0` (验证状态0的方程).**
        *   Left-hand side of Equation 0: `λ * π₀ = λ * C * (ρ⁰/0!) = λ * C * 1 = λC`.
        *   Right-hand side of Equation 0: `μ * π₁ = μ * C * (ρ¹/1!) = μ * C * (λ/μ) = λC`.
        *   Both sides are equal. Equation 0 holds.
    6.  **Step 6: Verify the claim for `i = 1, ..., s-1` (验证状态1到s-1的方程).** The solution says this is "exactly the same as for the M/M/∞ process in lectures". Let's verify for a general `i` in this range.
        *   Left-hand side of Equation i: `(λ + iμ) * πᵢ = (λ + iμ) * C * (ρⁱ/i!)`.
        *   Right-hand side of Equation i: `λ * π_{i-1} + (i+1)μ * π_{i+1} = λ * C * (ρ^{i-1}/(i-1)!) + (i+1)μ * C * (ρ^{i+1}/(i+1)!)`.
        *   Simplify the right-hand side:
            `= λC * (ρ^{i-1}/(i-1)!) + (i+1)μC * (ρ^{i+1}/(i+1)!)`
            `= λC * (ρ^{i-1}/(i-1)!) + μC * (ρ^{i+1}/i!)` (since `(i+1)! = (i+1)*i!`, so `(i+1)/(i+1)! = 1/i!`)
            `= λC * (ρ^{i-1}/(i-1)!) + μC * (ρ^{i} * ρ / i!)`
            `= λC * (ρ^{i-1}/(i-1)!) + μC * (ρ^{i} * (λ/μ) / i!)`
            `= λC * (ρ^{i-1}/(i-1)!) + λC * (ρ^{i} / i!)`
        *   Now, let's rewrite the left-hand side:
            `(λ + iμ) * πᵢ = λC * (ρⁱ/i!) + iμC * (ρⁱ/i!)`
            `= λC * (ρⁱ/i!) + iμC * (ρ^{i-1} * ρ / i!)`
            `= λC * (ρⁱ/i!) + iμC * (ρ^{i-1} * (λ/μ) / i!)`
            `= λC * (ρⁱ/i!) + λC * (ρ^{i-1} / (i-1)!)` (since `i/i! = 1/(i-1)!`)
        *   The left-hand side and right-hand side are now identical. Equation i holds.
    7.  **Step 7: Verify the claim for `i = s` (验证状态s的方程).**
        *   Left-hand side of Equation s: `sμ * πₛ = sμ * C * (ρˢ/s!) = sμ * C * (ρˢ / (s * (s-1)!)) = μ * C * (ρˢ / (s-1)!)`.
        *   Right-hand side of Equation s: `λ * π_{s-1} = λ * C * (ρ^{s-1}/(s-1)!)`.
        *   Now, substitute