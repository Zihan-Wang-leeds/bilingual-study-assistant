# Problem Sheet 8 - 详细解答 / Detailed Solutions

> MATH2702 Stochastic Processes
> 生成时间 / Generated: 2026-07-20 16:06
> 来源页 / Source Pages: 82-82

---

好的，作为大学数学导师，我将为您提供MATH2702: 随机过程习题集8的完整双语解答。

---

### Question 1 / 第1题

**Problem / 题目原文:**
1. Let (𝑋(𝑡)) be a Poisson process with rate 𝜆.
(a) Fix 𝑛. What is the expected time between the 𝑛th arrival and the (𝑛+ 1)th arrival?
(b) Fix 𝑡. What is the expected time between the previous arrival before 𝑡 and the next arrival after 𝑡?
(c) Your answers to the previous two questions should be different. Explain why one should expect the second answer to be bigger than the first.

**中文翻译 / Chinese Translation:**
1. 设 (𝑋(𝑡)) 是一个速率为 𝜆 的泊松过程。
(a) 固定 𝑛。求第 𝑛 次到达与第 (𝑛+1) 次到达之间的期望时间。
(b) 固定 𝑡。求在时间 𝑡 之前最后一次到达与在时间 𝑡 之后第一次到达之间的期望时间。
(c) 你对前两个问题的答案应该是不同的。解释为什么预期第二个答案比第一个大。

**Knowledge Points / 考查知识点:**
- 泊松过程的到达间隔时间分布 (Exponential distribution of interarrival times in a Poisson process)
- 泊松过程的无记忆性 (Memoryless property of the Poisson process)
- 检查悖论 (Inspection Paradox)

**Step-by-Step Solution / 逐步解答:**

#### (a) 固定 n 的期望间隔时间

**1. 中文思路 / Chinese reasoning:**
对于泊松过程，到达间隔时间（即连续两次到达之间的时间）是独立同分布的指数随机变量，其参数为速率 λ。第 n 次和第 n+1 次到达之间的时间正是第 (n+1) 个到达间隔时间。因此，我们只需要计算一个指数分布随机变量的期望值。

**English reasoning:**
For a Poisson process, the interarrival times (the times between successive arrivals) are independent and identically distributed exponential random variables with rate λ. The time between the nth and (n+1)th arrival is precisely the (n+1)th interarrival time. Therefore, we just need to compute the expectation of an exponential random variable.

**2. 计算过程 / Working:**
设 $T_{n+1}$ 为第 $n+1$ 个到达间隔时间。我们知道 $T_{n+1} \sim \text{Exp}(\lambda)$。
一个指数随机变量的期望是 $\mathbb{E}[T_{n+1}] = \frac{1}{\lambda}$。

**Explanation of working / 过程解释:**
我们定义 $T_{n+1}$ 为第 $n$ 次和第 $n+1$ 次到达之间的时间。根据泊松过程的定义，所有到达间隔时间 $T_1, T_2, \ldots$ 是独立同分布的，且都服从参数为 $\lambda$ 的指数分布。指数分布 $\text{Exp}(\lambda)$ 的概率密度函数为 $f(t) = \lambda e^{-\lambda t}$，其期望值 $\mathbb{E}[T] = \int_0^\infty t \lambda e^{-\lambda t} dt = 1/\lambda$。

**Final Answer / 最终答案:**
$$\boxed{\frac{1}{\lambda}}$$
期望时间为 $\frac{1}{\lambda}$。 / The expected time is $\frac{1}{\lambda}$.

#### (b) 固定 t 的期望间隔时间

**1. 中文思路 / Chinese reasoning:**
这个问题涉及到“检查悖论”。我们固定一个时间点 t，然后考虑包含这个时间点的那个“完整”的到达间隔。这个间隔由两部分组成：从 t 之前最后一次到达到 t 的时间（记为 $S_t$），以及从 t 到 t 之后第一次到达的时间（记为 $X_t$）。由于泊松过程具有无记忆性，$X_t$ 仍然服从参数为 $\lambda$ 的指数分布，其期望为 $1/\lambda$。然而，$S_t$ 的分布与 $X_t$ 相同，也是指数分布，期望为 $1/\lambda$。因此，整个间隔的期望是 $1/\lambda + 1/\lambda = 2/\lambda$。

**English reasoning:**
This problem involves the "inspection paradox". We fix a time point t and consider the "complete" interarrival interval that contains this time point. This interval consists of two parts: the time from the last arrival before t to t (denoted $S_t$), and the time from t to the next arrival after t (denoted $X_t$). Due to the memoryless property of the Poisson process, $X_t$ is still an exponential random variable with rate λ, so its expectation is $1/\lambda$. However, $S_t$ also has the same distribution as $X_t$, which is exponential with expectation $1/\lambda$. Therefore, the expectation of the whole interval is $1/\lambda + 1/\lambda = 2/\lambda$.

**2. 计算过程 / Working:**
设 $S_t$ 为从时间 t 回溯到上一次到达的时间，$X_t$ 为从时间 t 到下一次到达的时间。
由泊松过程的无记忆性，$X_t \sim \text{Exp}(\lambda)$，所以 $\mathbb{E}[X_t] = 1/\lambda$。
对于 $S_t$，由于泊松过程的时间可逆性，$S_t$ 也服从 $\text{Exp}(\lambda)$ 分布，所以 $\mathbb{E}[S_t] = 1/\lambda$。
因此，期望的总间隔时间为 $\mathbb{E}[S_t + X_t] = \mathbb{E}[S_t] + \mathbb{E}[X_t] = \frac{1}{\lambda} + \frac{1}{\lambda} = \frac{2}{\lambda}$。

**Explanation of working / 过程解释:**
我们定义 $S_t$ 和 $X_t$。无记忆性意味着，无论我们在什么时间点 t 观察，剩余等待时间 $X_t$ 的分布与一个全新的到达间隔时间完全相同，即指数分布。对于 $S_t$，因为泊松过程在时间上是可逆的（即如果我们反转时间轴，它仍然是一个相同速率的泊松过程），所以从 t 回溯到上一次到达的时间 $S_t$ 也具有相同的指数分布。因此，包含 t 的整个间隔的期望长度是这两个独立指数随机变量期望之和，即 $2/\lambda$。

**Final Answer / 最终答案:**
$$\boxed{\frac{2}{\lambda}}$$
期望时间为 $\frac{2}{\lambda}$。 / The expected time is $\frac{2}{\lambda}$.

#### (c) 解释为什么第二个答案更大

**1. 中文思路 / Chinese reasoning:**
在 (a) 中，我们随机选择一个特定的到达间隔（第 n 个间隔），它的期望长度是 $1/\lambda$。在 (b) 中，我们随机选择一个时间点 t，然后测量包含这个时间点的那个间隔。因为较长的间隔更有可能覆盖一个随机选择的时间点，所以这种“按时间长度加权”的采样方式会倾向于选择更长的间隔。这被称为“检查悖论”或“长度偏倚抽样”。

**English reasoning:**
In (a), we randomly select a specific interarrival interval (the nth interval), and its expected length is $1/\lambda$. In (b), we randomly select a time point t, and then measure the interval that contains this point. Because longer intervals are more likely to cover a randomly chosen time point, this "length-biased" sampling tends to select longer intervals. This is known as the "inspection paradox" or "length-biased sampling".

**2. 计算过程 / Working:**
(a) 的答案是 $1/\lambda$，而 (b) 的答案是 $2/\lambda$。显然 $2/\lambda > 1/\lambda$。
直观上，如果我们随机地“检查”一个过程，我们更有可能落在一个较长的间隔中，而不是一个较短的间隔中。因此，被检查到的间隔的期望长度会大于所有间隔的平均长度。

**Explanation of working / 过程解释:**
(a) 的答案是 $1/\lambda$，而 (b) 的答案是 $2/\lambda$。显然 $2/\lambda > 1/\lambda$。直观上，如果我们随机地“检查”一个过程，我们更有可能落在一个较长的间隔中，而不是一个较短的间隔中。因此，被检查到的间隔的期望长度会大于所有间隔的平均长度。

**Final Answer / 最终答案:**
第二个答案更大，因为随机时间点 t 更有可能落在一个较长的到达间隔内，这是一种长度偏倚抽样。 / The second answer is larger because a random time point t is more likely to fall within a longer interarrival interval, which is a length-biased sampling.

**Key Insight / 解题要点:**
- 泊松过程的到达间隔是独立同分布的指数分布。
- 检查悖论：随机时间点所在的间隔的期望长度是平均间隔长度的两倍。
- 无记忆性使得 $X_t$ 和 $S_t$ 都服从指数分布。

---

### Question 2 / 第2题

**Problem / 题目原文:**
2. Let 𝑋(𝑡) be a Poisson process with rate 𝜆, and mark each arrival independently with probability 𝑝.
Use the infinitesimals definition to show that the marked process is a Poisson process with rate 𝑝𝜆.

**中文翻译 / Chinese Translation:**
2. 设 𝑋(𝑡) 是一个速率为 𝜆 的泊松过程，并以概率 𝑝 独立地对每次到达进行标记。使用无穷小量定义来证明这个标记过程是一个速率为 𝑝𝜆 的泊松过程。

**Knowledge Points / 考查知识点:**
- 泊松过程的无穷小量定义 (Infinitesimal definition of a Poisson process)
- 随机稀疏化 (Random thinning of a Poisson process)
- 独立增量性 (Independent increments)

**Step-by-Step Solution / 逐步解答:**

**1. 中文思路 / Chinese reasoning:**
为了证明标记过程 $Y(t)$ 是一个泊松过程，我们需要验证它满足泊松过程的无穷小量定义。这包括三个条件：(i) $Y(0)=0$；(ii) $Y(t)$ 具有独立增量；(iii) 在任意小的时间区间 $(t, t+h]$ 内，发生一次事件的概率约为 $\lambda p h$，发生多于一次事件的概率是 $o(h)$。我们需要从原始过程 $X(t)$ 的性质出发来推导这些条件。

**English reasoning:**
To prove that the marked process $Y(t)$ is a Poisson process, we need to verify that it satisfies the infinitesimal definition of a Poisson process. This involves three conditions: (i) $Y(0)=0$; (ii) $Y(t)$ has independent increments; (iii) in any small time interval $(t, t+h]$, the probability of one event is approximately $\lambda p h$, and the probability of more than one event is $o(h)$. We need to derive these conditions from the properties of the original process $X(t)$.

**2. 计算过程 / Working:**

**步骤 1: 验证 $Y(0)=0$**
由于 $X(0)=0$，在时间 0 之前没有到达，因此也没有标记事件。所以 $Y(0)=0$。

**步骤 2: 验证独立增量性**
考虑任意不相交的时间区间 $(t_1, t_2]$ 和 $(t_3, t_4]$。原始过程 $X(t)$ 在这些区间上的增量 $X(t_2)-X(t_1)$ 和 $X(t_4)-X(t_3)$ 是独立的。标记过程 $Y(t)$ 的增量 $Y(t_2)-Y(t_1)$ 和 $Y(t_4)-Y(t_3)$ 分别只依赖于 $X(t_2)-X(t_1)$ 和 $X(t_4)-X(t_3)$ 以及独立的标记。由于这些原始增量是独立的，且标记是独立进行的，因此 $Y(t)$ 的增量也是独立的。

**步骤 3: 验证无穷小增量概率**
考虑一个小区间 $(t, t+h]$。原始过程 $X(t)$ 在该区间内发生一次事件的概率为 $\mathbb{P}(X(t+h)-X(t)=1) = \lambda h + o(h)$。发生多于一次事件的概率为 $\mathbb{P}(X(t+h)-X(t) \ge 2) = o(h)$。
对于标记过程 $Y(t)$，在 $(t, t+h]$ 内发生一次事件，意味着原始过程发生了一次事件，并且这次事件被标记了。因此：
$$\mathbb{P}(Y(t+h)-Y(t)=1) = \mathbb{P}(X(t+h)-X(t)=1 \text{ and the arrival is marked})$$
由于标记是独立进行的，这个概率等于：
$$\mathbb{P}(X(t+h)-X(t)=1) \times p = (\lambda h + o(h)) \times p = \lambda p h + o(h)$$
接下来，考虑在 $(t, t+h]$ 内发生多于一次标记事件。这有两种可能：要么原始过程发生了多于一次事件（无论是否标记），要么原始过程恰好发生了一次事件，但这次事件被标记了，同时还有另一次事件（概率为 $o(h)$）。更严格地说：
$$\mathbb{P}(Y(t+h)-Y(t) \ge 2) \le \mathbb{P}(X(t+h)-X(t) \ge 2) + \mathbb{P}(X(t+h)-X(t)=1 \text{ and it's marked and something else})$$
但更简单的说法是，如果 $Y(t)$ 有两次或更多次事件，那么 $X(t)$ 也必须有两次或更多次事件（因为每次标记事件都对应一次原始事件）。因此：
$$\mathbb{P}(Y(t+h)-Y(t) \ge 2) \le \mathbb{P}(X(t+h)-X(t) \ge 2) = o(h)$$
所以 $\mathbb{P}(Y(t+h)-Y(t) \ge 2) = o(h)$。

**Explanation of working / 过程解释:**
我们逐步验证了泊松过程的无穷小量定义的三个条件。
- 条件 (i) 是显然的。
- 条件 (ii) 利用了原始过程的独立增量性和标记的独立性。因为不相交区间上的原始事件数是独立的，而每个事件是否被标记也是独立于其他事件的，所以这些区间上的标记事件数也是独立的。
- 条件 (iii) 是核心。在小区间内，原始过程发生一次事件的概率是 $\lambda h + o(h)$。为了得到一个标记事件，我们需要这次原始事件被标记，其概率为 $p$。由于 $h$ 很小，我们可以忽略高阶项，得到 $\lambda p h$。同时，在小区间内发生多于一次标记事件的概率，不会超过原始过程发生多于一次事件的概率，而后者是 $o(h)$。因此，标记过程满足速率为 $\lambda p$ 的泊松过程的定义。

**Final Answer / 最终答案:**
标记过程 $Y(t)$ 是一个速率为 $\lambda p$ 的泊松过程。 / The marked process $Y(t)$ is a Poisson process with rate $\lambda p$.

**Key Insight / 解题要点:**
- 随机稀疏化（独立地以概率 p 保留事件）将一个速率为 λ 的泊松过程转化为一个速率为 λp 的泊松过程。
- 证明的关键是利用原始泊松过程的无穷小量性质，并结合标记的独立性。

---

### Question 3 / 第3题

**Problem / 题目原文:**
3. Let (𝑋(𝑡)) be a simple birth process with rates 𝜆𝑗= 𝜆𝑗 starting from 𝑋(0) = 1. Let 𝑝𝑗(𝑡) = ℙ(𝑋(𝑡) = 𝑗).
(a) Write down the Kolmogorov forward equations for 𝑝𝑗(𝑡). You should have separate equations for 𝑗= 1 and 𝑗≥2. Remember to include the initial conditions 𝑝𝑗(0).
(b) Show that 𝑋(𝑡) follows a geometric distribution 𝑋(𝑡) ∼Geom(𝑒−𝜆𝑡). That is, show that
𝑝𝑗(𝑡) = (1 −𝑒−𝜆𝑡)𝑗−1𝑒−𝜆𝑡
satisfies the forward equation.
(c) Hence, calculate 𝔼𝑋(𝑡), the expected population size at time 𝑡.

**中文翻译 / Chinese Translation:**
3. 设 (𝑋(𝑡)) 是一个简单生灭过程，其出生率为 𝜆𝑗= 𝜆𝑗，从 𝑋(0) = 1 开始。令 𝑝𝑗(𝑡) = ℙ(𝑋(𝑡) = 𝑗)。
(a) 写出 𝑝𝑗(𝑡) 的 Kolmogorov 向前方程。你应该为 𝑗=1 和 𝑗≥2 分别写出方程。记得包括初始条件 𝑝𝑗(0)。
(b) 证明 𝑋(𝑡) 服从几何分布 𝑋(𝑡) ∼Geom(𝑒−𝜆𝑡)。即证明
𝑝𝑗(𝑡) = (1 −𝑒−𝜆𝑡)𝑗−1𝑒−𝜆𝑡
满足向前方程。
(c) 由此，计算 𝔼𝑋(𝑡)，即时间 𝑡 时的期望种群大小。

**Knowledge Points / 考查知识点:**
- 简单生灭过程 (Simple birth process / Yule process)
- Kolmogorov 向前方程 (Kolmogorov forward equations)
- 几何分布 (Geometric distribution)
- 期望值计算 (Expectation calculation)

**Step-by-Step Solution / 逐步解答:**

#### (a) Kolmogorov 向前方程

**1. 中文思路 / Chinese reasoning:**
Kolmogorov 向前方程描述了在时间 t 时处于状态 j 的概率 $p_j(t)$ 随时间的变化率。对于简单生灭过程，状态只能通过出生事件增加。从状态 j 出发，出生事件以速率 $\lambda_j = \lambda j$ 发生，使系统进入状态 j+1。因此，$p_j(t)$ 的变化率由两部分组成：从状态 j-1 进入状态 j 的速率，以及从状态 j 离开到状态 j+1 的速率。我们需要为 j=1 和 j≥2 分别写出方程，因为当 j=1 时，没有状态 0 可以进入。

**English reasoning:**
The Kolmogorov forward equations describe the rate of change of the probability $p_j(t)$ of being in state j at time t. For a simple birth process, the state can only increase through birth events. From state j, a birth event occurs at rate $\lambda_j = \lambda j$, moving the system to state j+1. Therefore, the rate of change of $p_j(t)$ consists of two parts: the rate of entering state j from state j-1, and the rate of leaving state j to state j+1. We need separate equations for j=1 and j≥2 because when j=1, there is no state 0 to enter from.

**2. 计算过程 / Working:**
对于 $j \ge 2$，向前方程为：
$$\frac{d}{dt} p_j(t) = -\lambda_j p_j(t) + \lambda_{j-1} p_{j-1}(t) = -\lambda j p_j(t) + \lambda (j-1) p_{j-1}(t)$$
对于 $j=1$，由于没有状态 0，所以没有从状态 0 进入的项：
$$\frac{d}{dt} p_1(t) = -\lambda_1 p_1(t) = -\lambda \cdot 1 \cdot p_1(t) = -\lambda p_1(t)$$
初始条件为 $X(0)=1$，所以：
$$p_1(0) = 1, \quad p_j(0) = 0 \text{ for } j \ge 2$$

**Explanation of working / 过程解释:**
方程 $\frac{d}{dt} p_j(t) = -\lambda_j p_j(t) + \lambda_{j-1} p_{j-1}(t)$ 是标准的 Kolmogorov 向前方程形式。第一项 $-\lambda_j p_j(t)$ 表示从状态 j 离开的速率（乘以处于状态 j 的概率），第二项 $\lambda_{j-1} p_{j-1}(t)$ 表示从状态 j-1 进入状态 j 的速率。对于 j=1，没有状态 0，所以第二项不存在。初始条件直接来自问题陈述：在时间 0 时，种群大小为 1，所以 $p_1(0)=1$，其他状态的概率为 0。

**Final Answer / 最终答案:**
对于 $j=1$: $\frac{d}{dt} p_1(t) = -\lambda p_1(t)$，初始条件 $p_1(0)=1$。
对于 $j \ge 2$: $\frac{d}{dt} p_j(t) = -\lambda j p_j(t) + \lambda (j-1) p_{j-1}(t)$，初始条件 $p_j(0)=0$。

#### (b) 证明几何分布

**1. 中文思路 / Chinese reasoning:**
我们需要验证给定的 $p_j(t) = (1 - e^{-\lambda t})^{j-1} e^{-\lambda t}$ 满足 (a) 部分中的向前方程。这需要计算 $p_j(t)$ 对时间 t 的导数，并将其代入方程，同时也要验证 $p_{j-1}(t)$ 的表达式。我们分别对 j=1 和 j≥2 进行验证。

**English reasoning:**
We need to verify that the given $p_j(t) = (1 - e^{-\lambda t})^{j-1} e^{-\lambda t}$ satisfies the forward equations from part (a). This involves calculating the derivative of $p_j(t)$ with respect to time t, substituting it into the equation, and also using the expression for $p_{j-1}(t)$. We will verify for j=1 and j≥2 separately.

**2. 计算过程 / Working:**

**验证 j=1:**
给定 $p_1(t) = (1 - e^{-\lambda t})^{0} e^{-\lambda t} = e^{-\lambda t}$。
计算导数：$\frac{d}{dt} p_1(t) = \frac{d}{dt} e^{-\lambda t} = -\lambda e^{-\lambda t} = -\lambda p_1(t)$。
这正好是 (a) 中对于 j=1 的方程。所以成立。

**验证 j≥2:**
给定 $p_j(t) = (1 - e^{-\lambda t})^{j-1} e^{-\lambda t}$。
我们需要计算 $\frac{d}{dt} p_j(t)$。
令 $u = 1 - e^{-\lambda t}$，则 $p_j(t) = u^{j-1} e^{-\lambda t}$。
首先，$\frac{du}{dt} = \lambda e^{-\lambda t}$。
然后，使用乘积法则和链式法则：
$$\frac{d}{dt} p_j(t) = \frac{d}{dt} \left( u^{j-1} e^{-\lambda t} \right) = (j-1) u^{j-2} \frac{du}{dt} e^{-\lambda t} + u^{j-1} (-\lambda e^{-\lambda t})$$
代入 $\frac{du}{dt} = \lambda e^{-\lambda t}$：
$$\frac{d}{dt} p_j(t) = (j-1) u^{j-2} (\lambda e^{-\lambda t}) e^{-\lambda t} - \lambda u^{j-1} e^{-\lambda t}$$
$$= \lambda e^{-\lambda t} \left[ (j-1) u^{j-2} e^{-\lambda t} - u^{j-1} \right]$$
现在，将 $u = 1 - e^{-\lambda t}$ 代回，并尝试将表达式写成 $-\lambda j p_j(t) + \lambda (j-1) p_{j-1}(t)$ 的形式。
首先，$p_j(t) = u^{j-1} e^{-\lambda t}$。
其次，$p_{j-1}(t) = (1 - e^{-\lambda t})^{(j-1)-1} e^{-\lambda t} = u^{j-2} e^{-\lambda t}$。
现在计算 $-\lambda j p_j(t) + \lambda (j-1) p_{j-1}(t)$：
$$-\lambda j u^{j-1} e^{-\lambda t} + \lambda (j-1) u^{j-2} e^{-\lambda t}$$
$$= \lambda e^{-\lambda t} \left[ -j u^{j-1} + (j-1) u^{j-2} \right]$$
$$= \lambda e^{-\lambda t} \left[ (j-1) u^{j-2} - j u^{j-1} \right]$$
我们需要证明这个表达式等于我们之前计算的导数 $\frac{d}{dt} p_j(t)$。
我们之前计算的导数是：
$$\frac{d}{dt} p_j(t) = \lambda e^{-\lambda t} \left[ (j-1) u^{j-2} e^{-\lambda t} - u^{j-1} \right]$$
注意 $e^{-\lambda t} = 1 - u$。所以：
$$\frac{d}{dt} p_j(t) = \lambda e^{-\lambda t} \left[ (j-1) u^{j-2} (1-u) - u^{j-1} \right]$$
$$= \lambda e^{-\lambda t} \left[ (j-1) u^{j-2} - (j-1) u^{j-1} - u^{j-1} \right]$$
$$= \lambda e^{-\lambda t} \left[ (j-1) u^{j-2} - j u^{j-1} \right]$$
这正好等于 $-\lambda j p_j(t) + \lambda (j-1) p_{j-1}(t)$。因此，给定的 $p_j(t)$ 满足向前方程。

**Explanation of working / 过程解释:**
我们通过直接求导和代数运算验证了 $p_j(t)$ 满足微分方程。关键步骤是使用链式法则求导，然后将 $e^{-\lambda t}$ 用 $1-u$ 替换，最终将导数表达式化简为与向前方程右侧完全相同的形式。这证明了 $p_j(t) = (1 - e^{-\lambda t})^{j-1} e^{-\lambda t}$ 确实是向前方程的解。这个概率质量函数正是参数为 $p = e^{-\lambda t}$ 的几何分布（定义在 $\{1, 2, 3, \ldots\}$ 上，即首次成功所需的试验次数）。

**Final Answer / 最终答案:**
已证明 $p_j(t) = (1 - e^{-\lambda t})^{j-1} e^{-\lambda t}$ 满足 Kolmogorov 向前方程。 / It has been shown that $p_j(t) = (1 - e^{-\lambda t})^{j-1} e^{-\lambda t}$ satisfies the Kolmogorov forward equations.

#### (c) 计算期望种群大小

**1. 中文思路 / Chinese reasoning:**
既然我们已经知道 $X(t)$ 服从参数为 $p = e^{-\lambda t}$ 的几何分布