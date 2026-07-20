# Problem Sheet 11 - 详细解答 / Detailed Solutions

> MATH2702 Stochastic Processes
> 生成时间 / Generated: 2026-07-20 16:08
> 来源页 / Source Pages: 104-105

---

好的，作为您的大学随机过程数学导师，我将为您提供MATH2702课程问题集11的完整、双语、逐步解答。

---

### Question 1 / 第1题

**Problem / 题目原文:**
(a) Consider an M/M/1 queue with arrival rate λ and service rate μ < λ. Justify the statement that the average time an individual spends waiting in the queue is λ/(μ(μ−λ)).
(b) Consider the queue for the single cash register in a shop. Customers arrive at a rate of 28 per hour, and that the average time at the till is 2 minutes. What is the average time, in minutes, that a customer waits in the queue?
(c) The shop decides to open a second cash register. Each customer chooses one of the registers to queue for 50∶50 at random. What is the average wait time now? (Remember to justify your answer carefully.)
(d) How might you improve the model of a shop with two cash registers to more accurately reflect true queueing behaviour? What effect would this have on the average wait time?

**中文翻译 / Chinese Translation:**
(a) 考虑一个M/M/1队列，其到达率为λ，服务率为μ，且μ < λ。论证个体在队列中等待的平均时间为 λ/(μ(μ−λ))。
(b) 考虑一家商店中单个收银台的队列。顾客以每小时28人的速率到达，在收银台的平均时间为2分钟。顾客在队列中等待的平均时间（以分钟计）是多少？
(c) 商店决定开设第二个收银台。每位顾客以50∶50的随机概率选择其中一个收银台排队。现在的平均等待时间是多少？（记住要仔细论证你的答案。）
(d) 你如何改进拥有两个收银台的商店模型，以更准确地反映真实的排队行为？这会对平均等待时间产生什么影响？

**Knowledge Points / 考查知识点:**
- **M/M/1队列 (M/M/1 Queue):** 泊松到达、指数服务时间、单服务器、无限缓冲区。涉及利特尔法则 (Little's Law) 和平均队列长度的推导。
- **泊松过程的分裂 (Splitting of Poisson Processes):** 当每个到达独立地以固定概率被分配到不同流时，每个子流仍然是泊松过程。
- **排队论中的利特尔法则 (Little's Law in Queueing Theory):** 平均队列长度 (L) 等于平均到达率 (λ) 乘以平均等待时间 (W)，即 L = λW。
- **模型假设与局限性 (Model Assumptions and Limitations):** 识别现实世界排队行为与简单模型假设之间的差异，如随机选择队列与最短队列选择。

**Step-by-Step Solution / 逐步解答:**

#### Part (a) / 第(a)部分

**Step 1: 回顾已知结论并理解问题 / Review known results and understand the problem**

*   **中文思路:** 题目要求我们论证一个关于M/M/1队列平均等待时间的公式。我们已经从课程中知道，M/M/1队列中的平均队列长度（即正在等待的顾客数，不包括正在接受服务的顾客）是 Lq = λ²/(μ(μ-λ))。题目中给出的公式是平均等待时间 Wq = λ/(μ(μ-λ))。我们需要将这两个公式联系起来。关键工具是利特尔法则，它适用于队列中的等待部分。
*   **English reasoning:** The problem asks us to justify a formula for the average waiting time in an M/M/1 queue. We know from lectures that the average queue length (number of customers waiting, excluding the one in service) is Lq = λ²/(μ(μ-λ)). The formula given is for the average waiting time Wq = λ/(μ(μ-λ)). We need to connect these two. The key tool is Little's Law, which can be applied specifically to the waiting portion of the queue.

**Step 2: 应用利特尔法则到队列 / Apply Little's Law to the queue**

*   **中文思路:** 利特尔法则指出，对于一个稳定的系统，长期平均顾客数 (L) 等于长期平均到达率 (λ) 乘以每个顾客在系统中花费的平均时间 (W)。这个法则非常通用，可以应用于整个系统，也可以应用于系统的任何部分，比如队列本身。对于队列部分，平均队列长度 Lq 等于到达率 λ 乘以平均等待时间 Wq。因此，我们有 Lq = λ * Wq。
*   **English reasoning:** Little's Law states that for a stable system, the long-term average number of customers (L) is equal to the long-term average arrival rate (λ) multiplied by the average time a customer spends in the system (W). This law is very general and can be applied to the entire system or any part of it, such as the queue itself. For the queue portion, the average queue length Lq equals the arrival rate λ multiplied by the average waiting time Wq. Therefore, we have Lq = λ * Wq.

**Step 3: 代入已知的平均队列长度公式并求解 / Substitute the known formula for average queue length and solve**

*   **中文思路:** 我们从课程中知道，对于M/M/1队列，平均队列长度 Lq = λ²/(μ(μ-λ))。将此代入利特尔法则 Lq = λ * Wq，我们得到 λ²/(μ(μ-λ)) = λ * Wq。然后，两边同时除以 λ（假设 λ > 0），即可解出 Wq = λ/(μ(μ-λ))。
*   **English reasoning:** We know from the course that for an M/M/1 queue, the average queue length is Lq = λ²/(μ(μ-λ)). Substituting this into Little's Law Lq = λ * Wq, we get λ²/(μ(μ-λ)) = λ * Wq. Then, dividing both sides by λ (assuming λ > 0), we solve for Wq = λ/(μ(μ-λ)).

*   **计算过程 / Working:**
    $$L_q = \frac{\lambda^2}{\mu(\mu - \lambda)}$$
    $$L_q = \lambda W_q$$
    $$\frac{\lambda^2}{\mu(\mu - \lambda)} = \lambda W_q$$
    $$W_q = \frac{\lambda^2}{\mu(\mu - \lambda)} \cdot \frac{1}{\lambda} = \frac{\lambda}{\mu(\mu - \lambda)}$$

*   **Explanation of working / 过程解释:**
    *   第一行是课程中给出的M/M/1队列的平均队列长度公式。
    *   第二行是利特尔法则应用于队列部分。
    *   第三行将第一行的公式代入第二行。
    *   第四行通过两边同时除以 λ 来解出 Wq。这完成了论证。

#### Part (b) / 第(b)部分

**Step 1: 统一时间单位并确定参数 / Unify time units and identify parameters**

*   **中文思路:** 题目给出的到达率是每小时28人，而平均服务时间是2分钟。为了使用公式，我们需要统一时间单位。我们选择以小时为单位。到达率 λ = 28 人/小时。平均服务时间是2分钟，即 2/60 = 1/30 小时。服务率 μ 是平均服务时间的倒数，所以 μ = 1 / (1/30) = 30 人/小时。
*   **English reasoning:** The arrival rate is given as 28 per hour, and the average service time is 2 minutes. To use the formula, we need consistent time units. We choose hours. The arrival rate λ = 28 customers/hour. The average service time is 2 minutes, which is 2/60 = 1/30 hour. The service rate μ is the reciprocal of the average service time, so μ = 1 / (1/30) = 30 customers/hour.

**Step 2: 应用第(a)部分的公式 / Apply the formula from part (a)**

*   **中文思路:** 现在我们将 λ = 28 和 μ = 30 代入平均等待时间公式 Wq = λ/(μ(μ-λ))。注意，条件 μ < λ 不成立，因为 30 > 28。实际上，系统稳定的条件是 λ < μ。这里 λ=28, μ=30，所以系统是稳定的。我们进行计算。
*   **English reasoning:** Now we substitute λ = 28 and μ = 30 into the average waiting time formula Wq = λ/(μ(μ-λ)). Note that the condition for stability is λ < μ, which holds here (28 < 30). Let's perform the calculation.

*   **计算过程 / Working:**
    $$W_q = \frac{\lambda}{\mu(\mu - \lambda)} = \frac{28}{30 \times (30 - 28)} = \frac{28}{30 \times 2} = \frac{28}{60} \text{ 小时}$$

**Step 3: 将结果转换为分钟 / Convert the result to minutes**

*   **中文思路:** 题目要求以分钟为单位给出答案。我们将小时数乘以60得到分钟数。Wq = (28/60) * 60 = 28 分钟。
*   **English reasoning:** The problem asks for the answer in minutes. We multiply the hours by 60 to get minutes. Wq = (28/60) * 60 = 28 minutes.

*   **计算过程 / Working:**
    $$W_q = \frac{28}{60} \times 60 \text{ 分钟} = 28 \text{ 分钟}$$

*   **Explanation of working / 过程解释:**
    *   我们首先计算了以小时为单位的等待时间，结果是28/60小时。
    *   然后乘以60将其转换为分钟，得到28分钟。

#### Part (c) / 第(c)部分

**Step 1: 分析两个队列的到达过程 / Analyze the arrival process for the two queues**

*   **中文思路:** 现在有两个收银台。每个顾客独立地、以相等的概率（50:50）随机选择一个收银台排队。这意味着原始的到达过程（速率为 λ=28 人/小时）被分裂成两个独立的泊松过程。根据泊松过程的分裂性质，每个子过程（即每个收银台的到达过程）仍然是一个泊松过程，其速率是原始速率乘以选择该收银台的概率。因此，每个收银台的到达率是 λ/2 = 28/2 = 14 人/小时。
*   **English reasoning:** Now there are two tills. Each customer independently and randomly chooses one of the tills to queue for with equal probability (50:50). This means the original arrival process (rate λ=28 per hour) is split into two independent Poisson processes. By the splitting property of Poisson processes, each resulting process (the arrival process at each till) is still a Poisson process, with a rate equal to the original rate multiplied by the probability of choosing that till. Therefore, the arrival rate at each till is λ/2 = 28/2 = 14 customers per hour.

**Step 2: 将每个队列视为独立的M/M/1队列 / Treat each queue as an independent M/M/1 queue**

*   **中文思路:** 每个收银台都有自己的队列，服务率仍然是 μ=30 人/小时。每个队列现在可以看作是一个独立的M/M/1队列，其到达率为 λ_sub = 14，服务率为 μ = 30。注意，条件 λ_sub < μ 成立 (14 < 30)，所以每个队列都是稳定的。
*   **English reasoning:** Each till has its own queue, and the service rate remains μ=30 customers per hour. Each queue can now be considered an independent M/M/1 queue with arrival rate λ_sub = 14 and service rate μ = 30. Note that the stability condition λ_sub < μ holds (14 < 30), so each queue is stable.

**Step 3: 计算每个队列的平均等待时间 / Calculate the average waiting time for each queue**

*   **中文思路:** 我们再次使用第(a)部分的公式，但这次使用新的到达率 λ_sub = 14。平均等待时间 Wq_new = λ_sub / (μ(μ - λ_sub)) = 14 / (30 * (30 - 14))。
*   **English reasoning:** We use the formula from part (a) again, but this time with the new arrival rate λ_sub = 14. The average waiting time Wq_new = λ_sub / (μ(μ - λ_sub)) = 14 / (30 * (30 - 14)).

*   **计算过程 / Working:**
    $$W_q^{\text{new}} = \frac{\lambda_{\text{sub}}}{\mu(\mu - \lambda_{\text{sub}})} = \frac{14}{30 \times (30 - 14)} = \frac{14}{30 \times 16} = \frac{14}{480} \text{ 小时}$$

**Step 4: 将结果转换为分钟 / Convert the result to minutes**

*   **中文思路:** 将小时转换为分钟：Wq_new = (14/480) * 60 分钟。简化这个分数。
*   **English reasoning:** Convert hours to minutes: Wq_new = (14/480) * 60 minutes. Simplify this fraction.

*   **计算过程 / Working:**
    $$W_q^{\text{new}} = \frac{14}{480} \times 60 = \frac{14 \times 60}{480} = \frac{14}{8} = \frac{7}{4} = 1.75 \text{ 分钟}$$
    $$1.75 \text{ 分钟} = 1 \text{ 分钟} + 0.75 \times 60 \text{ 秒} = 1 \text{ 分钟} 45 \text{ 秒}$$

*   **Explanation of working / 过程解释:**
    *   我们计算了新的等待时间，得到14/480小时。
    *   乘以60得到分钟数，即 (14*60)/480 = 840/480 = 7/4 = 1.75分钟。
    *   将0.75分钟乘以60秒，得到45秒。所以最终答案是1分钟45秒。

#### Part (d) / 第(d)部分

**Step 1: 识别模型的局限性 / Identify the limitations of the model**

*   **中文思路:** 当前模型假设顾客随机选择一个队列，并且一旦选择就绝不更换。这在现实中并不总是准确的。顾客通常会观察两个队列的长度，并选择较短的队列（最短队列规则）。此外，如果另一个队列变空，顾客可能会更换队列（排跳槽）。
*   **English reasoning:** The current model assumes customers choose a queue at random and never switch once they have chosen. This is not always accurate in reality. Customers often observe the lengths of both queues and join the shorter one (shortest queue discipline). Furthermore, customers might switch queues if the other one becomes empty (jockeying).

**Step 2: 提出改进模型的方法 / Propose ways to improve the model**

*   **中文思路:** 为了更准确地反映现实，我们可以对模型进行以下改进：
    1.  **最短队列规则:** 假设新到达的顾客总是加入当前长度最短的队列。
    2.  **排跳槽:** 允许顾客在等待过程中，如果发现另一个队列变得更短，可以更换队列。
    3.  **单队列双服务器:** 更现实的模型是只有一个队列，但有两个服务器（收银台）。顾客到达后排成一个队，哪个服务器空闲了，队首的顾客就过去接受服务。这实际上是一个M/M/2队列（在多服务器系统中，通常假设一个队列）。
*   **English reasoning:** To more accurately reflect reality, we can improve the model by:
    1.  **Shortest Queue Discipline:** Assume arriving customers always join the queue that is currently shortest.
    2.  **Jockeying:** Allow customers to switch queues if the other queue becomes shorter while they are waiting.
    3.  **Single Queue, Two Servers:** A more realistic model is to have a single queue feeding both servers. Customers arrive, form a single line, and when a server becomes free, the customer at the head of the line goes to that server. This is effectively an M/M/2 queue (in multi-server systems, a single queue is often assumed).

**Step 3: 分析对平均等待时间的影响 / Analyze the effect on average waiting time**

*   **中文思路:** 所有这些改进措施（最短队列、排跳槽、单队列多服务器）都旨在更有效地利用服务器资源，减少服务器空闲而队列非空的情况。它们通过更智能地分配顾客，减少了系统内的不平衡。因此，与随机分配队列的模型相比，这些改进通常会**降低**平均等待时间。特别是，单队列多服务器（M/M/2）模型在相同负载下，其性能总是优于或等于多个独立的M/M/1队列。
*   **English reasoning:** All these improvements (shortest queue, jockeying, single queue with multiple servers) aim to utilize the server resources more efficiently, reducing the chance of one server being idle while the other queue is long. They reduce imbalance in the system by distributing customers more intelligently. Therefore, these improvements will generally **decrease** the average waiting time compared to the random assignment model. In particular, a single queue with multiple servers (M/M/2) model always performs better than or equal to multiple independent M/M/1 queues under the same load.

**Final Answer / 最终答案:**
(a) 论证完成。平均等待时间为 $\frac{\lambda}{\mu(\mu-\lambda)}$。
    Justification complete. The average waiting time is $\frac{\lambda}{\mu(\mu-\lambda)}$.
(b) 平均等待时间为 **28 分钟**。
    The average waiting time is **28 minutes**.
(c) 平均等待时间为 **1 分钟 45 秒** (或 1.75 分钟)。
    The average waiting time is **1 minute 45 seconds** (or 1.75 minutes).
(d) 可以通过采用最短队列规则、允许排跳槽或使用单队列双服务器模型来改进模型。这些改进通常会**降低**平均等待时间。
    The model can be improved by using the shortest queue discipline, allowing jockeying, or using a single queue with two servers model. These improvements would generally **decrease** the average waiting time.

**Key Insight / 解题要点:**
- **利特尔法则 (Little's Law)** 是连接平均队列长度和平均等待时间的关键桥梁。
- **泊松过程的分裂 (Splitting of Poisson processes)** 允许我们将一个复杂的排队网络分解为多个独立的、更简单的M/M/1队列进行分析。
- 模型假设（如随机选择队列 vs. 最短队列）对结果有显著影响，理解这些假设对于建立准确的现实世界模型至关重要。

---

### Question 2 / 第2题

**Problem / 题目原文:**
Telephone calls to a call centre are modelled as an M/M/s/s queue: call arrivals are a Poisson process with rate λ, call lengths are exponential with rate μ, and there are s workers available to answer the phone. The second s denotes that there is only enough phone lines for s callers at a time – if all workers are answering calls, any new calls are immediately dropped, and there is no technology for holding in a queue or waiting for a worker to become free.
(a) Let X(t) be the number of calls being answered at time t. Write down the transition rates q_{ij} for i, j ∈ {0, 1, …, s}, i ≠ j.
(b) Erlang’s formula states that the long-run proportion of time that all s workers are answering calls is (ρ^s / s!) / (∑_{i=0}^s ρ^i / i!), where ρ = λ/μ. Prove Erlang’s formula.

**中文翻译 / Chinese Translation:**
电话呼叫中心的电话被建模为一个M/M/s/s队列：呼叫到达是一个速率为λ的泊松过程，通话时长服从速率为μ的指数分布，并且有s名工作人员可以接听电话。第二个s表示一次只有s条电话线路可用——如果所有工作人员都在接听电话，任何新呼叫都会被立即丢弃，并且没有技术可以保持排队或等待工作人员空闲。
(a) 令 X(t) 为在时刻 t 正在被接听的电话数量。写出对于 i, j ∈ {0, 1, …, s}, i ≠ j 的转移速率 q_{ij}。
(b) 埃尔朗公式指出，所有s名工作人员都在接听电话的长期时间比例为 (ρ^s / s!) / (∑_{i=0}^s ρ^i / i!)，其中 ρ = λ/μ。证明埃尔朗公式。

**Knowledge Points / 考查知识点:**
- **M/M/s/s 队列 (Erlang-B 模型 / Erlang-B Model):** 一种损失系统，其中没有等待空间。到达者如果发现所有服务器都忙，则被阻塞并离开系统。
- **生灭过程 (Birth-Death Process):** 该队列的连续时间马尔可夫链是一个有限状态空间（0到s）的生灭过程。
- **全局平衡方程 (Global Balance Equations):** 用于求解生灭过程平稳分布的标准方法。对于生灭过程，局部平衡方程（细致平衡）成立。
- **平稳分布 (Stationary Distribution):** 求解马尔可夫链的长期概率分布。
- **埃尔朗B公式 (Erlang's B Formula):** 用于计算电话网络和呼叫中心中呼叫阻塞概率的著名公式。

**Step-by-Step Solution / 逐步解答:**

#### Part (a) / 第(a)部分

**Step 1: 理解系统动态 / Understand the system dynamics**

*   **中文思路:** 系统状态 X(t) 表示在时刻 t 正在被接听的电话数量。这是一个生灭过程。当系统处于状态 i 时，可能发生两种事件：一个新呼叫到达（“生”），或者一个正在进行的通话结束（“灭”）。由于没有排队空间，新呼叫只有在 i < s 时才能被接听，否则会被丢弃。通话结束的速率取决于当前正在通话的人数。
*   **English reasoning:** The system state X(t) represents the number of calls being answered at time t. This is a birth-death process. When the system is in state i, two types of events can occur: a new call arrival (a "birth"), or a call completion (a "death"). Since there is no queue, a new call can only be answered if i < s, otherwise it is lost. The rate of call completions depends on the number of calls currently in progress.

**Step 2: 写出转移速率 / Write down the transition rates**

*   **中文思路:** 转移速率 q_{ij} 是从状态 i 到状态 j 的速率。
    *   **生 (到达):** 当 i = 0, 1, ..., s-1 时，新呼叫可以到达并被接听，使状态从 i 增加到 i+1。到达率是 λ，所以 q_{i, i+1} = λ。当 i = s 时，所有线路都忙，新呼叫被丢弃，所以没有从状态 s 到 s+1 的转移，即 q_{s, s+1} = 0。
    *   **灭 (离开):** 当 i = 1, 2, ..., s 时，一个正在进行的通话可能结束，使状态从 i 减少到 i-1。如果有 i 个通话正在进行，每个通话以速率 μ 结束，那么总结束速率是 i * μ。所以 q_{i, i-1} = iμ。当 i = 0 时，没有通话可以结束，所以 q_{0, -1} = 0。
    *   **其他转移:** 对于所有其他 i ≠ j，转移速率为 0，因为一次只能发生一个事件（到达或离开）。
*   **English reasoning:** The transition rate q_{ij} is the rate of going from state i to state j.
    *   **Birth (Arrival):** For i = 0, 1, ..., s-1, a new call can arrive and be answered, increasing the state from i to i+1. The arrival rate is λ, so q_{i, i+1} = λ. When i = s, all lines are busy, new calls are lost, so there is no transition from state s to s+1, i.e., q_{s, s+1} = 0.
    *   **Death (Departure):** For i = 1, 2, ..., s, an ongoing call can end, decreasing the state from i to i-1. If there are i calls in progress, each ending at rate μ, the total rate of endings is i * μ. So q_{i, i-1} = iμ. When i = 0, no calls can end, so q_{0, -1} = 0.
    *   **Other transitions:** For all other i ≠ j, the transition rate is 0, as only one event (arrival or departure) can happen at a time.

*   **最终答案 / Final Answer for (a):**
    $$q_{i, i+1} = \lambda \quad \text{for } i = 0, 1, \dots, s-1$$
    $$q_{i, i-1} = i\mu \quad \text{for } i = 1, 2, \dots, s$$
    $$q_{i, j} = 0 \quad \text{for all other } i \neq j$$

#### Part (b) / 第(b)部分

**Step 1: 提出平稳分布的形式 / Propose the form of the stationary distribution**

*   **中文思路:** 为了证明埃尔朗公式，我们需要找到这个生灭过程的平稳分布 π。我们猜测平稳分布具有形式 π_j = C * (ρ^j / j!)，其中 j = 0, 1, ..., s，ρ = λ/μ，C 是归一化常数。这个形式与M/M/∞队列的平稳分布相同，但状态空间被截断在 s。
*   **English reasoning:** To prove Erlang's formula, we need to find the stationary distribution π of this birth-death process. We guess that the stationary distribution has the form π_j = C * (ρ^j / j!), for j = 0, 1, ..., s, where ρ = λ/μ, and C is a normalizing constant. This form is the same as the stationary distribution for an M/M/∞ queue, but with the state space truncated at s.

**Step 2: 推导局部平衡方程 / Derive the local balance equations**

*   **中文思路:** 对于生灭过程，平稳分布满足局部平衡方程（也称为细致平衡方程）。这些方程表达了在平衡状态下，从状态 i 到 i+1 的“概率流”等于从状态 i+1 到 i 的“概率流”。具体来说，对于状态 i 和 i+1，我们有 π_i * q_{i, i+1} = π_{i+1} * q_{i+1, i}。
*   **English reasoning:** For a birth-death process, the stationary distribution satisfies the local balance equations (also known as detailed balance equations). These equations state that in equilibrium, the "probability flow" from state i to i+1 equals the "probability flow" from state i+1 to i. Specifically, for states i and i+1, we have π_i * q_{i, i+1} = π_{i+1} * q_{i+1, i}.

**Step 3: 应用局部平衡方程 / Apply the local balance equations**

*   **