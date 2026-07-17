# Problem Sheet 11 - 详细解答 / Detailed Solutions

> MATH2702 Stochastic Processes
> 生成时间 / Generated: 2026-07-17 15:16
> 来源页 / Source Pages: 104-105

---

好的，作为您的大学随机过程课程导师，我将为您提供这份习题集的完整、详细的逐步解答。

---

### Question 1 / 第1题

**Problem / 题目原文:**
1.
(a) Consider an M/M/1 queue with arrival rate 𝜆 and service rate 𝜇 < 𝜆. Justify the statement that the average time an individual spends waiting in the queue is
𝜆 / [𝜇(𝜇−𝜆)].
Solution. We saw in lectures that there are on average 𝜆/(𝜇−𝜆) individuals in the queue. Each one will take an Exp(𝜇) time to be serviced, which has mean 1/𝜇. Multiplying these gives the result.
(b) Consider the queue for the single cash register in a shop. Customers arrive at a rate of 28 per hour, and that the average time at the till is 2 minutes. What is the average time, in minutes, that a customer waits in the queue?
Solution. If we work in time units of hours, we have 𝜆 = 28 and 𝜇 = 30, and the average waiting time is 28/[30(30−28)] = 28/60 = 28 minutes.
(c) The shop decides to open a second cash register. Each customer chooses one of the registers to queue for 50:50 at random. What is the average wait time now? (Remember to justify your answer carefully.)
Solution. The arrival process at each till is now a marked Poisson process, so has rate 𝜆/2 = 14. This means the waiting time is 14/[30(30−14)] = 7/4 × 60 = 7/4 minutes = 1 minute 45 seconds.
(d) How might you improve the model of a shop with two cash registers to more accurately reflect true queueing behaviour? What effect would this have on the average wait time?
Solution. We might assume that customers join the shortest queue, rather than picking one at random. We might assume a customer will move to the other till if it becomes empty. We might even assume that customers will change queues if the other queue gets shorter than the one they are currently in. In all cases, the average waiting time will go down.

**中文翻译:**
1.
(a) 考虑一个到达率为 𝜆，服务率为 𝜇 < 𝜆 的 M/M/1 队列。证明个体在队列中等待的平均时间为 𝜆 / [𝜇(𝜇−𝜆)]。
(b) 考虑一家商店中单个收银台的队列。顾客到达率为每小时28人，在收银台的平均时间为2分钟。求顾客在队列中等待的平均时间（以分钟为单位）。
(c) 商店决定开设第二个收银台。每个顾客以50:50的概率随机选择一个收银台排队。现在的平均等待时间是多少？（请仔细证明你的答案。）
(d) 你如何改进这个拥有两个收银台的商店模型，以更准确地反映真实的排队行为？这对平均等待时间会有什么影响？

**Knowledge Points / 考查知识点:**
- Section 21: Queueing Theory
- M/M/1 queue properties (Little's Law, average queue length, average waiting time)
- Poisson process splitting (thinning)
- Model assumptions and their impact on performance

**Step-by-Step Solution / 逐步解答:**

#### (a)

**Step 1: State the known result for the average number of customers in the queue.**
We know from lectures (or can derive from the M/M/1 queue's stationary distribution) that the average number of customers waiting in the queue, denoted $L_q$, is:
$$L_q = \frac{\lambda^2}{\mu(\mu - \lambda)}$$
*Explanation:* This is a standard result for an M/M/1 queue. The condition $\mu > \lambda$ is required for the queue to be stable (i.e., not grow infinitely long). The formula comes from the stationary distribution $\pi_n = (1-\rho)\rho^n$, where $\rho = \lambda/\mu$, and summing over the queue length.

**Step 2: Relate the average queue length to the average waiting time using Little's Law.**
Little's Law states that for a stable queueing system, the long-run average number of customers in a system (or a subsystem) is equal to the long-run average arrival rate multiplied by the long-run average time a customer spends in that system (or subsystem).
$$L = \lambda W$$
We apply Little's Law to the *queue* (the waiting area, not including the server). The average number of customers in the queue is $L_q$. The average arrival rate to the queue is $\lambda$. The average time a customer spends in the queue is $W_q$.
$$L_q = \lambda W_q$$

**Step 3: Solve for the average waiting time $W_q$.**
From Step 2, we have $W_q = L_q / \lambda$. Substitute the expression for $L_q$ from Step 1:
$$W_q = \frac{1}{\lambda} \cdot \frac{\lambda^2}{\mu(\mu - \lambda)} = \frac{\lambda}{\mu(\mu - \lambda)}$$
*Explanation:* We simply divide the average queue length by the arrival rate. The $\lambda$ in the numerator cancels one of the $\lambda$'s in the numerator of $L_q$, giving the final result.

**Step 4: (Alternative justification from the provided solution)**
The provided solution uses a different, more intuitive argument: "Each one will take an Exp(𝜇) time to be serviced, which has mean 1/𝜇. Multiplying these gives the result." This is a heuristic that works because of the memoryless property of the exponential distribution. The average number of people ahead of a new arrival is $L_q$. The new arrival must wait for each of these people to be served. The total waiting time is the sum of these service times. Since the service times are i.i.d. Exp(𝜇), the expected total waiting time is $L_q \times E[\text{service time}] = \frac{\lambda^2}{\mu(\mu - \lambda)} \times \frac{1}{\mu} = \frac{\lambda}{\mu(\mu - \lambda)}$. This is valid because the service times are independent of the queue length process.

#### (b)

**Step 1: Identify the parameters and ensure consistent units.**
Arrival rate: $\lambda = 28$ customers per hour.
Service rate: The average service time is 2 minutes. We need the service rate in customers per hour.
$$\mu = \frac{1}{\text{average service time}} = \frac{1}{2 \text{ minutes}} = \frac{1}{2/60 \text{ hours}} = \frac{60}{2} = 30 \text{ customers per hour}.$$
*Explanation:* Rates must be in the same time unit. We choose hours.

**Step 2: Apply the formula for average waiting time from part (a).**
The average waiting time in the queue, $W_q$, is:
$$W_q = \frac{\lambda}{\mu(\mu - \lambda)}$$
Substitute $\lambda = 28$ and $\mu = 30$:
$$W_q = \frac{28}{30 \times (30 - 28)} = \frac{28}{30 \times 2} = \frac{28}{60} \text{ hours}.$$

**Step 3: Convert the answer to minutes.**
$$W_q = \frac{28}{60} \text{ hours} \times 60 \frac{\text{minutes}}{\text{hour}} = 28 \text{ minutes}.$$
*Explanation:* The provided solution states the answer is 28 minutes. This is a very long wait, which highlights how unstable an M/M/1 queue becomes as $\lambda$ approaches $\mu$ ($\rho = 28/30 = 0.933$).

#### (c)

**Step 1: Model the new system.**
We now have two independent M/M/1 queues. Customers arrive at the shop at a rate of $\lambda = 28$ per hour. Each customer independently chooses a queue with probability $p=0.5$. This is a **thinning** (or splitting) of a Poisson process.

**Step 2: Determine the arrival rate to each queue.**
The arrival process to each cash register is a marked Poisson process. The rate for each queue is:
$$\lambda_{\text{queue}} = p \times \lambda = 0.5 \times 28 = 14 \text{ customers per hour}.$$
*Explanation:* Thinning a Poisson process with rate $\lambda$ by a probability $p$ results in two independent Poisson processes with rates $p\lambda$ and $(1-p)\lambda$.

**Step 3: Determine the service rate for each queue.**
The service rate at each till is the same as before, as the cashiers work at the same speed.
$$\mu = 30 \text{ customers per hour}.$$

**Step 4: Apply the M/M/1 waiting time formula to one of the queues.**
Since the queues are identical and independent, the average waiting time in either queue is the same.
$$W_q^{\text{(new)}} = \frac{\lambda_{\text{queue}}}{\mu(\mu - \lambda_{\text{queue}})} = \frac{14}{30 \times (30 - 14)} = \frac{14}{30 \times 16} = \frac{14}{480} \text{ hours}.$$

**Step 5: Simplify and convert to minutes.**
$$W_q^{\text{(new)}} = \frac{14}{480} = \frac{7}{240} \text{ hours}.$$
Convert to minutes:
$$W_q^{\text{(new)}} = \frac{7}{240} \text{ hours} \times 60 \frac{\text{minutes}}{\text{hour}} = \frac{7 \times 60}{240} = \frac{7}{4} = 1.75 \text{ minutes}.$$
This is 1 minute and 45 seconds (since $0.75 \times 60 = 45$ seconds).

#### (d)

**Step 1: Identify the unrealistic assumption in the current model.**
The current model assumes customers choose a queue at random and never switch. In reality, customers are rational and will try to minimize their waiting time.

**Step 2: Propose a more realistic model.**
A more accurate model would be an M/M/2 queue with a single queue feeding both servers (or a "join the shortest queue" (JSQ) policy). In this model:
- Customers arrive at a single Poisson process with rate $\lambda = 28$.
- There are two servers, each with service rate $\mu = 30$.
- When a customer arrives, they join the queue that is shorter (or if both are empty, they choose one at random).

**Step 3: Explain the effect on average waiting time.**
In an M/M/2 system (or JSQ), the servers are pooled. This is much more efficient than two separate M/M/1 queues because:
1.  **No "one queue idle, other queue busy" scenario:** A server will never be idle while there are customers waiting in the other queue.
2.  **Reduced variability:** The combined service capacity is better utilized to handle random fluctuations in arrivals.

The effect is that the average waiting time $W_q$ will be **significantly lower** than the 1.75 minutes calculated for the two independent M/M/1 queues. The provided solution correctly states that the average waiting time will go down.

**Final Answer / 最终答案:**
(a) Proven using Little's Law: $W_q = L_q / \lambda = \frac{\lambda^2}{\mu(\mu-\lambda)} / \lambda = \frac{\lambda}{\mu(\mu-\lambda)}$.
(b) $\boxed{28 \text{ minutes}}$
(c) $\boxed{1 \text{ minute } 45 \text{ seconds} \text{ (or } 1.75 \text{ minutes})}$
(d) A better model is an M/M/2 queue with a single queue or a "join the shortest queue" policy. This would **decrease** the average waiting time.

**Key Insight / 解题要点:**
The key insight is that splitting a single fast server into two slower servers (or in this case, splitting the arrival stream) is inefficient compared to pooling the service capacity into a single queue, due to the law of diminishing returns and the benefits of statistical multiplexing.

---

### Question 2 / 第2题

**Problem / 题目原文:**
2. Telephone calls to a call centre are modelled as an M/M/𝑠/𝑠 queue: call arrivals are a Poisson process with rate 𝜆, call lengths are exponential with rate 𝜇, and there are 𝑠 workers available to answer the phone. The second 𝑠 denotes that there is only enough phone lines for 𝑠 callers at a time – if all workers are answering calls, any new calls are immediately dropped, and there is no technology for holding in a queue or waiting for a worker to become free.
(a) Let 𝑋(𝑡) be the number of calls being answered at time 𝑡. Write down the transition rates 𝑞𝑖𝑗 for 𝑖,𝑗 ∈ {0,1,…,𝑠}, 𝑖 ≠ 𝑗.
Solution. The transition rate are 𝑞𝑖,𝑖+1 = 𝜆 for 𝑖 = 0,1,…,𝑠−1, representing arrivals at rate 𝜆 when there is at least one free server, and 𝑞𝑖,𝑖−1 = 𝑖𝜇 for 𝑖 = 1,2,…,𝑠 representing departures.
(b) Erlang’s formula states that the long-run proportion of time that all 𝑠 workers are answering calls is
$$\frac{\rho^s / s!}{\sum_{i=0}^s \rho^i / i!},$$
where $\rho = \lambda / \mu$. Prove Erlang’s formula.
Solution. We claim that a stationary distribution is given by $\pi_j = C \rho^j / j!$ for $j = 0,1,\dots,s$, where the normalising constant will have to be
$$C = \frac{1}{\sum_{i=0}^s \rho^i / i!}.$$
By the ergodic theorem, the long-run proportion of time all $s$ workers are answering calls is $\pi_s$.
It remains to prove the claim. The equations for $\pi Q = 0$ are
$$(i+1)\mu \pi_{i+1} - (\lambda + i\mu)\pi_i + \lambda \pi_{i-1} = 0.$$
for $i = 0,1,\dots,s-1$, and
$$-s\mu \pi_s + \lambda \pi_{s-1} = 0.$$
Proving this holds for $i = 0,1,\dots,s-1$ is exactly the same as for the M/M/∞ process in lectures, while for $i = s$ we have
$$-s\mu \pi_s + \lambda \pi_{s-1} = -s\mu C \frac{\rho^s}{s!} + \lambda C \frac{\rho^{s-1}}{(s-1)!}$$
$$= -C \mu \rho \frac{\rho^{s-1}}{(s-1)!} + C \lambda \frac{\rho^{s-1}}{(s-1)!}$$
$$= -C \lambda \frac{\rho^{s-1}}{(s-1)!} + C \lambda \frac{\rho^{s-1}}{(s-1)!} = 0,$$
thus proving the claim.

**中文翻译:**
2. 呼叫中心的电话被建模为一个 M/M/𝑠/𝑠 队列：呼叫到达是一个速率为 𝜆 的泊松过程，通话时长服从速率为 𝜇 的指数分布，有 𝑠 个工作人员可以接听电话。第二个 𝑠 表示一次只有足够的电话线路供 𝑠 个呼叫者使用——如果所有工作人员都在接听电话，任何新的呼叫都会立即被丢弃，并且没有技术可以保持排队或等待工作人员空闲。
(a) 令 𝑋(𝑡) 为在时间 𝑡 正在被接听的电话数量。写出对于 𝑖,𝑗 ∈ {0,1,…,𝑠}, 𝑖 ≠ 𝑗 的转移速率 𝑞𝑖𝑗。
(b) 埃尔朗公式指出，所有 𝑠 个工作人员都在接听电话的长期时间比例为 $\frac{\rho^s / s!}{\sum_{i=0}^s \rho^i / i!}$，其中 $\rho = \lambda / \mu$。证明埃尔朗公式。

**Knowledge Points / 考查知识点:**
- Section 21: Queueing Theory (specifically M/M/s/s or Erlang-B queue)
- Continuous-time Markov Chains (CTMCs)
- Global Balance Equations (or detailed balance)
- Stationary distribution of a CTMC
- Erlang's Loss Formula (Erlang-B)

**Step-by-Step Solution / 逐步解答:**

#### (a)

**Step 1: Define the state space and the process.**
The process $X(t)$ is the number of calls being answered at time $t$. Since there are $s$ workers and no queue, the state space is $\{0, 1, 2, \dots, s\}$.

**Step 2: Determine the transition rates for arrivals (upward jumps).**
An arrival occurs at rate $\lambda$. This will cause the state to increase by 1, from $i$ to $i+1$, **only if** there is a free worker to answer the call. This is possible when $i < s$. If $i = s$, the call is lost and the state does not change.
Therefore, for $i = 0, 1, \dots, s-1$:
$$q_{i, i+1} = \lambda$$
For $i = s$:
$$q_{s, s+1} = 0$$

**Step 3: Determine the transition rates for departures (downward jumps).**
A departure occurs when a call ends. If there are $i$ calls in progress, each call ends at rate $\mu$. Since the calls are independent, the total rate at which a call ends is $i\mu$. This will cause the state to decrease by 1, from $i$ to $i-1$. This is possible when $i > 0$.
Therefore, for $i = 1, 2, \dots, s$:
$$q_{i, i-1} = i\mu$$
For $i = 0$:
$$q_{0, -1} = 0$$

**Step 4: State the final transition rates.**
All other transition rates $q_{ij}$ for $|i-j| > 1$ are 0, as this is a birth-death process.

#### (b)

**Step 1: State the claim and the goal.**
We claim that the stationary distribution $\pi$ for this M/M/s/s queue is:
$$\pi_j = \frac{\rho^j / j!}{\sum_{i=0}^s \rho^i / i!}, \quad \text{for } j = 0, 1, \dots, s$$
where $\rho = \lambda / \mu$.
The goal is to prove that this $\pi$ satisfies the global balance equations (or the detailed balance equations, since this is a birth-death process).

**Step 2: Write down the global balance equations for a birth-death process.**
For a birth-death process, the stationary distribution satisfies the **detailed balance equations** (also known as local balance equations). The flow from state $i$ to $i+1$ must equal the flow from state $i+1$ to $i$.
$$\pi_i \times q_{i, i+1} = \pi_{i+1} \times q_{i+1, i}$$
For our process:
- Birth rate from state $i$: $q_{i, i+1} = \lambda$ for $i = 0, \dots, s-1$.
- Death rate from state $i+1$: $q_{i+1, i} = (i+1)\mu$ for $i = 0, \dots, s-1$.

**Step 3: Derive the recurrence relation from the detailed balance equations.**
For $i = 0, 1, \dots, s-1$:
$$\pi_i \lambda = \pi_{i+1} (i+1)\mu$$
Solve for $\pi_{i+1}$:
$$\pi_{i+1} = \frac{\lambda}{(i+1)\mu} \pi_i = \frac{\rho}{i+1} \pi_i$$
*Explanation:* We define $\rho = \lambda / \mu$.

**Step 4: Solve the recurrence relation to find $\pi_j$ in terms of $\pi_0$.**
We can iterate the recurrence:
- For $i=0$: $\pi_1 = \frac{\rho}{1} \pi_0$
- For $i=1$: $\pi_2 = \frac{\rho}{2} \pi_1 = \frac{\rho}{2} \cdot \frac{\rho}{1} \pi_0 = \frac{\rho^2}{2!} \pi_0$
- For $i=2$: $\pi_3 = \frac{\rho}{3} \pi_2 = \frac{\rho}{3} \cdot \frac{\rho^2}{2!} \pi_0 = \frac{\rho^3}{3!} \pi_0$
By induction, for any $j = 0, 1, \dots, s$:
$$\pi_j = \frac{\rho^j}{j!} \pi_0$$

**Step 5: Find $\pi_0$ using the normalization condition.**
The sum of all probabilities must equal 1:
$$\sum_{j=0}^s \pi_j = 1$$
Substitute the expression for $\pi_j$:
$$\sum_{j=0}^s \frac{\rho^j}{j!} \pi_0 = 1$$
Solve for $\pi_0$:
$$\pi_0 = \frac{1}{\sum_{j=0}^s \frac{\rho^j}{j!}}$$

**Step 6: Write the final expression for $\pi_j$.**
Substitute $\pi_0$ back into the formula for $\pi_j$:
$$\pi_j = \frac{\rho^j}{j!} \cdot \frac{1}{\sum_{i=0}^s \frac{\rho^i}{i!}} = \frac{\rho^j / j!}{\sum_{i=0}^s \rho^i / i!}$$

**Step 7: State the long-run proportion of time all $s$ workers are busy.**
The long-run proportion of time that all $s$ workers are answering calls is the stationary probability of being in state $s$, which is $\pi_s$.
$$\pi_s = \frac{\rho^s / s!}{\sum_{i=0}^s \rho^i / i!}$$
This is Erlang's formula (Erlang-B). The provided solution also verifies this by plugging the formula into the global balance equation for the boundary state $s$, which is a valid alternative method.

**Final Answer / 最终答案:**
(a) The transition rates are:
$$q_{i, i+1} = \lambda \quad \text{for } i = 0, 1, \dots, s-1$$
$$q_{i, i-1} = i\mu \quad \text{for } i = 1, 2, \dots, s$$
All other $q_{ij} = 0$.

(b) Proven by solving the detailed balance equations $\pi_i \lambda = \pi_{i+1} (i+1)\mu$ for a birth-death process, yielding $\pi_j = \frac{\rho^j}{j!} \pi_0$, and then normalizing to find $\pi_0$. The final result is:
$$\boxed{\pi_s = \frac{\rho^s / s!}{\sum_{i=0}^s \rho^i / i!}}$$

**Key Insight / 解题要点:**
The M/M/s/s queue is a pure loss system (no queue), and its stationary distribution is a truncated Poisson distribution, derived by applying detailed balance equations to a finite-state birth-death process.