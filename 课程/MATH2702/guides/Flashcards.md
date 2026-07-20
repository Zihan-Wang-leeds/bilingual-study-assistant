# MATH2702 - Flashcards / 闪卡

> 生成时间 / Generated: 2026-07-20 14:44
> 共 18 张卡片 / Total cards

---

## Card 1: What is a stochastic process?

**Front / 正面**: What is a stochastic process?

**Back / 反面**: A stochastic process is a collection of random variables $\{X_t : t \in T\}$ indexed by time $T$, used to model random systems that evolve over time.

**中文**: 随机过程是一组按时间索引的随机变量，用于建模随时间演变的随机系统。

*Type: definition | Source: Section 1.2*

---

## Card 2: What is the Markov property?

**Front / 正面**: What is the Markov property?

**Back / 反面**: The Markov property states that the future evolution of the process depends only on the present state, not on the past: $P(X_{n+1}=j \mid X_n=i, X_{n-1}=i_{n-1}, \dots, X_0=i_0) = P(X_{n+1}=j \mid X_n=i)$.

**中文**: 马尔可夫性质：未来状态只依赖于当前状态，与过去无关。

*Type: definition | Source: Section 1.3*

---

## Card 3: Definition of a time-homogeneous discrete-time Markov chain (DTMC)

**Front / 正面**: Definition of a time-homogeneous discrete-time Markov chain (DTMC)

**Back / 反面**: A DTMC $\{X_n\}$ with state space $S$ satisfies $P(X_{n+1}=j \mid X_n=i) = p_{ij}$ for all $n$, where $p_{ij}$ are transition probabilities independent of time $n$.

**中文**: 时间齐次离散时间马尔可夫链：转移概率 $p_{ij}$ 与时间 $n$ 无关。

*Type: definition | Source: Section 3.1*

---

## Card 4: What is a martingale?

**Front / 正面**: What is a martingale?

**Back / 反面**: A stochastic process $\{M_n\}$ is a martingale if $E[|M_n|] < \infty$ and $E[M_{n+1} \mid M_0, \dots, M_n] = M_n$ for all $n$.

**中文**: 鞅：给定过去信息，未来期望等于当前值。

*Type: definition | Source: Section 4.1*

---

## Card 5: Gambler's Ruin: probability of ruin starting from $i$ with total capital $N$ and win probability $p$

**Front / 正面**: Gambler's Ruin: probability of ruin starting from $i$ with total capital $N$ and win probability $p$

**Back / 反面**: For $p \neq 1/2$, $P(\text{ruin}) = \frac{(q/p)^i - (q/p)^N}{1 - (q/p)^N}$; for $p=1/2$, $P(\text{ruin}) = 1 - i/N$.

**中文**: 赌徒破产概率公式（$p$ 为赢的概率，$q=1-p$）。

*Type: formula | Source: Section 4.3*

---

## Card 6: What is a communicating class?

**Front / 正面**: What is a communicating class?

**Back / 反面**: A set of states $C$ is a communicating class if for every $i,j \in C$, $i$ leads to $j$ and $j$ leads to $i$ (i.e., $i \leftrightarrow j$). A class is closed if no transitions leave it.

**中文**: 通信类：状态之间相互可达；封闭类：无法离开该类。

*Type: definition | Source: Section 6.1*

---

## Card 7: Definition of recurrence and transience

**Front / 正面**: Definition of recurrence and transience

**Back / 反面**: A state $i$ is recurrent if $P_i(\text{return to } i \text{ eventually}) = 1$; transient if this probability is $<1$. Equivalently, $\sum_{n=0}^\infty p_{ii}^{(n)} = \infty$ for recurrent, $<\infty$ for transient.

**中文**: 常返态：几乎必然返回；暂态：可能不返回。判别：$\sum p_{ii}^{(n)}$ 发散或收敛。

*Type: definition | Source: Section 8.1*

---

## Card 8: What is a stationary distribution for a DTMC?

**Front / 正面**: What is a stationary distribution for a DTMC?

**Back / 反面**: A probability distribution $\pi$ on the state space is stationary if $\pi = \pi P$, i.e., $\pi_j = \sum_i \pi_i p_{ij}$ for all $j$.

**中文**: 平稳分布：满足 $\pi = \pi P$ 的概率分布，即一步后分布不变。

*Type: definition | Source: Section 9.1*

---

## Card 9: Detailed balance equations for reversibility

**Front / 正面**: Detailed balance equations for reversibility

**Back / 反面**: A DTMC is reversible with respect to $\pi$ if $\pi_i p_{ij} = \pi_j p_{ji}$ for all $i,j$. If these hold and $\pi$ is a stationary distribution, the chain is reversible.

**中文**: 细致平衡方程：$\pi_i p_{ij} = \pi_j p_{ji}$，是判断可逆性的条件。

*Type: theorem | Source: Section 10.2*

---

## Card 10: Ergodic theorem for DTMCs

**Front / 正面**: Ergodic theorem for DTMCs

**Back / 反面**: For an irreducible, positive recurrent DTMC with stationary distribution $\pi$, for any bounded function $f$, $\frac{1}{n} \sum_{k=0}^{n-1} f(X_k) \to \sum_i \pi_i f(i)$ almost surely as $n \to \infty$.

**中文**: 遍历定理：时间平均收敛于平稳分布下的空间平均。

*Type: theorem | Source: Section 11.3*

---

## Card 11: Three equivalent definitions of a Poisson process

**Front / 正面**: Three equivalent definitions of a Poisson process

**Back / 反面**: (1) Independent Poisson increments: $N(t) \sim \text{Poisson}(\lambda t)$ with independent increments. (2) Independent exponential holding times: interarrival times i.i.d. $\text{Exp}(\lambda)$. (3) Infinitesimal: $P(N(t+h)-N(t)=1) = \lambda h + o(h)$, $P(\ge 2)=o(h)$.

**中文**: 泊松过程的三种等价定义：泊松增量、指数间隔、无穷小时间增量。

*Type: definition | Source: Sections 13.2, 14.2, 15.1*

---

## Card 12: What is a continuous-time Markov jump process (CTMJP)?

**Front / 正面**: What is a continuous-time Markov jump process (CTMJP)?

**Back / 反面**: A CTMJP $\{X(t)\}$ has holding times that are exponential with rate $q_i$ (depending on current state $i$), and then jumps to state $j$ with probability $p_{ij}$, where $\sum_j p_{ij}=1$ and $p_{ii}=0$.

**中文**: 连续时间马尔可夫跳跃过程：指数停留时间后按转移概率跳转。

*Type: definition | Source: Section 17.1*

---

## Card 13: Forward and backward equations for CTMC

**Front / 正面**: Forward and backward equations for CTMC

**Back / 反面**: Forward: $P'(t) = P(t) Q$; Backward: $P'(t) = Q P(t)$, where $P(t)$ is the transition matrix and $Q$ is the generator matrix with $q_{ij}$ for $i\neq j$ and $q_{ii} = -\sum_{j\neq i} q_{ij}$.

**中文**: 向前方程 $P'(t)=P(t)Q$，向后方程 $P'(t)=QP(t)$，$Q$ 为生成矩阵。

*Type: formula | Source: Section 18.2*

---

## Card 14: Stationary distribution for a CTMC satisfies $\pi Q = 0$

**Front / 正面**: Stationary distribution for a CTMC satisfies $\pi Q = 0$

**Back / 反面**: For an irreducible, positive recurrent CTMC, the stationary distribution $\pi$ satisfies $\pi Q = 0$ and $\sum_i \pi_i = 1$.

**中文**: 连续时间马尔可夫链的平稳分布满足 $\pi Q = 0$。

*Type: theorem | Source: Section 19.2*

---

## Card 15: M/M/1 queue stationary distribution

**Front / 正面**: M/M/1 queue stationary distribution

**Back / 反面**: For an M/M/1 queue with arrival rate $\lambda$ and service rate $\mu > \lambda$, the stationary distribution is $\pi_i = (1-\rho)\rho^i$ for $i=0,1,2,\dots$, where $\rho = \lambda/\mu < 1$ (geometric distribution).

**中文**: M/M/1 队列的平稳分布为几何分布 $\pi_i = (1-\rho)\rho^i$，$\rho=\lambda/\mu$。

*Type: theorem | Source: Section 21.2*

---

## Card 16: Long-run average number in M/M/1 queue

**Front / 正面**: Long-run average number in M/M/1 queue

**Back / 反面**: The long-run average number of individuals in the M/M/1 queue is $\frac{\rho}{1-\rho} = \frac{\lambda}{\mu-\lambda}$.

**中文**: M/M/1 队列中长期平均人数为 $\frac{\lambda}{\mu-\lambda}$。

*Type: formula | Source: Section 21.2*

---

## Card 17: Erlang's formula for M/M/s/s queue (loss system)

**Front / 正面**: Erlang's formula for M/M/s/s queue (loss system)

**Back / 反面**: The long-run proportion of time all $s$ servers are busy is $\pi_s = \frac{\rho^s / s!}{\sum_{i=0}^s \rho^i / i!}$, where $\rho = \lambda/\mu$.

**中文**: Erlang 公式：$s$ 个服务器全忙的比例为 $\frac{\rho^s/s!}{\sum_{i=0}^s \rho^i/i!}$。

*Type: formula | Source: Section 21.2 (Problem Sheet 11)*

---

## Card 18: Limit theorem for CTMCs

**Front / 正面**: Limit theorem for CTMCs

**Back / 反面**: For an irreducible, positive recurrent CTMC with stationary distribution $\pi$, $\lim_{t\to\infty} P(X(t)=j) = \pi_j$ for all $j$, regardless of initial distribution.

**中文**: 连续时间马尔可夫链的极限定理：长时间后分布收敛于平稳分布。

*Type: theorem | Source: Section 19.3*

---

