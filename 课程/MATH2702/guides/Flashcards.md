# MATH2702 - Flashcards / 闪卡

> 生成时间 / Generated: 2026-07-24 10:58
> 共 20 张卡片 / Total cards

---

## Card 1: What is a stochastic process?

**Front / 正面**: What is a stochastic process?

**Back / 反面**: A stochastic process is a collection of random variables $\{X_t : t \in T\}$ indexed by time $T$, describing the evolution of a system over time.

**中文**: 随机过程是按时间索引的随机变量集合，描述系统随时间演化的过程。

*Type: definition | Source: Section 1.2*

---

## Card 2: Markov property (discrete time)

**Front / 正面**: Markov property (discrete time)

**Back / 反面**: A discrete-time stochastic process $\{X_n\}$ satisfies the Markov property if the future depends only on the present, not the past: $P(X_{n+1}=j \mid X_n=i, X_{n-1}=i_{n-1}, \dots, X_0=i_0) = P(X_{n+1}=j \mid X_n=i)$.

**中文**: 离散时间马尔可夫性：未来只依赖于当前状态，与过去无关。

*Type: definition | Source: Section 1.3*

---

## Card 3: Definition of a time-homogeneous discrete-time Markov chain (DTMC)

**Front / 正面**: Definition of a time-homogeneous discrete-time Markov chain (DTMC)

**Back / 反面**: A sequence of random variables $\{X_n\}$ with state space $S$ such that $P(X_{n+1}=j \mid X_n=i)=p_{ij}$ for all $n$, where $p_{ij}$ are transition probabilities independent of $n$, and $\sum_{j \in S} p_{ij}=1$.

**中文**: 时间齐次离散时间马尔可夫链：转移概率 $p_{ij}$ 与时间 $n$ 无关，且每行和为1。

*Type: definition | Source: Section 3.1*

---

## Card 4: n-step transition probabilities and the Chapman-Kolmogorov equations

**Front / 正面**: n-step transition probabilities and the Chapman-Kolmogorov equations

**Back / 反面**: The n-step transition probability $p_{ij}^{(n)} = P(X_{m+n}=j \mid X_m=i)$ satisfies $p_{ij}^{(m+n)} = \sum_{k \in S} p_{ik}^{(m)} p_{kj}^{(n)}$.

**中文**: n步转移概率满足 Chapman-Kolmogorov 方程：$p_{ij}^{(m+n)} = \sum_k p_{ik}^{(m)} p_{kj}^{(n)}$。

*Type: formula | Source: Section 3.3*

---

## Card 5: Definition of a martingale

**Front / 正面**: Definition of a martingale

**Back / 反面**: A stochastic process $\{M_n\}$ is a martingale if $E[|M_n|] < \infty$ and $E[M_{n+1} \mid M_0, \dots, M_n] = M_n$ for all $n$.

**中文**: 鞅：条件期望等于当前值，即 $E[M_{n+1} \mid \text{过去}] = M_n$。

*Type: definition | Source: Section 4.1*

---

## Card 6: Gambler's ruin probability (fair game)

**Front / 正面**: Gambler's ruin probability (fair game)

**Back / 反面**: For a gambler starting with $a$ units, playing against a bank with $b$ units, in a fair game ($p=1/2$), the probability of ruin is $P(\text{ruin}) = 1 - a/(a+b) = b/(a+b)$.

**中文**: 公平赌博中，初始资金 $a$ 的赌徒破产概率为 $b/(a+b)$。

*Type: formula | Source: Section 4.3*

---

## Card 7: Optional Stopping Theorem (OST)

**Front / 正面**: Optional Stopping Theorem (OST)

**Back / 反面**: If $\{M_n\}$ is a martingale and $T$ is a stopping time with $P(T<\infty)=1$, $E[|M_T|]<\infty$, and $E[M_n \mathbf{1}_{\{T>n\}}] \to 0$, then $E[M_T] = E[M_0]$.

**中文**: 可选停止定理：在适当条件下，鞅在停止时刻的期望等于初始期望。

*Type: theorem | Source: Section 4.5*

---

## Card 8: Communicating classes and irreducibility

**Front / 正面**: Communicating classes and irreducibility

**Back / 反面**: States $i$ and $j$ communicate ($i \leftrightarrow j$) if each is reachable from the other. A Markov chain is irreducible if all states belong to one communicating class.

**中文**: 互通类：状态 $i$ 和 $j$ 互相可达。不可约链：所有状态属于同一个互通类。

*Type: concept | Source: Section 6.1*

---

## Card 9: Period of a state

**Front / 正面**: Period of a state

**Back / 反面**: The period $d(i)$ of state $i$ is the greatest common divisor of $\{n \geq 1 : p_{ii}^{(n)} > 0\}$. If $d(i)=1$, the state is aperiodic.

**中文**: 状态 $i$ 的周期是 $\{n: p_{ii}^{(n)}>0\}$ 的最大公约数。周期为1称为非周期。

*Type: definition | Source: Section 6.2*

---

## Card 10: Recurrence and transience

**Front / 正面**: Recurrence and transience

**Back / 反面**: A state $i$ is recurrent if $P(\text{return to } i \mid X_0=i)=1$; otherwise it is transient. In an irreducible finite chain, all states are recurrent.

**中文**: 常返：以概率1返回；瞬过：有正概率不返回。有限不可约链所有状态常返。

*Type: concept | Source: Section 8.1*

---

## Card 11: Stationary distribution definition

**Front / 正面**: Stationary distribution definition

**Back / 反面**: A probability distribution $\pi$ on state space $S$ is stationary for a DTMC with transition matrix $P$ if $\pi = \pi P$, i.e., $\pi_j = \sum_i \pi_i p_{ij}$ for all $j$.

**中文**: 平稳分布 $\pi$ 满足 $\pi = \pi P$，即分布经一步转移后不变。

*Type: definition | Source: Section 9.1*

---

## Card 12: Detailed balance equations (reversibility)

**Front / 正面**: Detailed balance equations (reversibility)

**Back / 反面**: A Markov chain is reversible with respect to $\pi$ if $\pi_i p_{ij} = \pi_j p_{ji}$ for all $i,j$. If these hold, $\pi$ is a stationary distribution.

**中文**: 细致平衡方程：$\pi_i p_{ij} = \pi_j p_{ji}$，满足则 $\pi$ 是平稳分布且链可逆。

*Type: formula | Source: Section 10.2*

---

## Card 13: Ergodic theorem for DTMCs

**Front / 正面**: Ergodic theorem for DTMCs

**Back / 反面**: For an irreducible, aperiodic, positive recurrent Markov chain, for any bounded function $f$, $\frac{1}{n} \sum_{k=1}^n f(X_k) \to \sum_i \pi_i f(i)$ almost surely as $n \to \infty$.

**中文**: 遍历定理：时间平均收敛于平稳分布下的空间平均。

*Type: theorem | Source: Section 11.3*

---

## Card 14: Poisson process definition (independent Poisson increments)

**Front / 正面**: Poisson process definition (independent Poisson increments)

**Back / 反面**: A counting process $\{N(t)\}$ with $N(0)=0$, independent increments, and $N(t)-N(s) \sim \text{Poisson}(\lambda(t-s))$ for $0 \leq s < t$.

**中文**: 泊松过程：增量独立且服从泊松分布，参数 $\lambda(t-s)$。

*Type: definition | Source: Section 13.2*

---

## Card 15: Poisson process definition (exponential holding times)

**Front / 正面**: Poisson process definition (exponential holding times)

**Back / 反面**: A Poisson process has i.i.d. interarrival times $T_1, T_2, \dots$ with $T_i \sim \text{Exp}(\lambda)$.

**中文**: 泊松过程：到达间隔时间独立同分布，服从指数分布 $\text{Exp}(\lambda)$。

*Type: definition | Source: Section 14.2*

---

## Card 16: Forward equations for continuous-time Markov jump processes

**Front / 正面**: Forward equations for continuous-time Markov jump processes

**Back / 反面**: The transition probabilities $p_{ij}(t)$ satisfy $\frac{d}{dt} p_{ij}(t) = \sum_{k \neq j} p_{ik}(t) q_{kj} - p_{ij}(t) \sum_{k \neq j} q_{jk}$, or in matrix form $P'(t) = P(t) Q$.

**中文**: 向前方程：$\frac{d}{dt} P(t) = P(t) Q$，其中 $Q$ 是速率矩阵。

*Type: formula | Source: Section 18.2*

---

## Card 17: Stationary distribution for continuous-time Markov chain

**Front / 正面**: Stationary distribution for continuous-time Markov chain

**Back / 反面**: A distribution $\pi$ is stationary if $\pi Q = 0$, i.e., $\sum_i \pi_i q_{ij} = 0$ for all $j$, and $\sum_i \pi_i = 1$.

**中文**: 连续时间马尔可夫链的平稳分布满足 $\pi Q = 0$ 且概率和为1。

*Type: definition | Source: Section 19.3*

---

## Card 18: M/M/1 queue stationary distribution

**Front / 正面**: M/M/1 queue stationary distribution

**Back / 反面**: For an M/M/1 queue with arrival rate $\lambda$ and service rate $\mu > \lambda$, the stationary distribution is $\pi_i = (1-\rho)\rho^i$ for $i=0,1,2,\dots$, where $\rho = \lambda/\mu < 1$.

**中文**: M/M/1 队列平稳分布：$\pi_i = (1-\rho)\rho^i$，$\rho = \lambda/\mu$，几何分布。

*Type: theorem | Source: Section 21.2*

---

## Card 19: Long-run average number in M/M/1 queue

**Front / 正面**: Long-run average number in M/M/1 queue

**Back / 反面**: The long-run average number of customers in an M/M/1 queue with $\rho = \lambda/\mu < 1$ is $\frac{\rho}{1-\rho} = \frac{\lambda}{\mu-\lambda}$.

**中文**: M/M/1 队列长期平均顾客数：$\frac{\lambda}{\mu-\lambda}$。

*Type: formula | Source: Section 21.2*

---

## Card 20: Erlang's formula for M/M/s/s queue

**Front / 正面**: Erlang's formula for M/M/s/s queue

**Back / 反面**: The long-run proportion of time all $s$ servers are busy in an M/M/s/s queue is $\frac{\rho^s / s!}{\sum_{i=0}^s \rho^i / i!}$, where $\rho = \lambda/\mu$.

**中文**: Erlang 公式：所有 $s$ 个服务员都忙的长期比例为 $\frac{\rho^s / s!}{\sum_{i=0}^s \rho^i / i!}$。

*Type: formula | Source: Section 22.2 (Problem Sheet 11)*

---

