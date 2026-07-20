# Problem Sheet 2 - 详细解答 / Detailed Solutions

> MATH2702 Stochastic Processes
> 生成时间 / Generated: 2026-07-20 16:01
> 来源页 / Source Pages: 27-29

---

好的，作为您的大学随机过程数学导师，我将为您提供这份习题集的完整、详细的双语解答。

### Question 1 / 第1题

**Problem / 题目原文:**
Consider the gambler’s ruin problem with draws: at each step, Alice wins £1 with probability $p$, loses £1 with probability $q$, and neither wins nor loses any money with probability $s$, where $p+q+s=1$, and $0 < p, q, s < 1$. We assume that $p \neq q$. Alice starts with £$a$ and Bob with £$(m-a)$.
(a) .
(i) For the case $p \neq q$, show that $M_n = (q/p)^{X_n}$ is a martingale with respect to the increments of the random walk (so adding draws does not affect $M_n$ from lectures).
(ii) Use the optional stopping theorem to conclude that $r_a$ does not depend on $s$ in this case.
(b) Let $d_i$ be the expected duration of the game from the point that Alice has £$i$. We want to use the martingale method to prove our expression for $d_i$ (in fact we have draws, so are even more general).
(i) Find a constant $c$ so that $M_n = X_n + nc$ is a martingale.
(ii) Suppose that $p \neq q$. Using the optional stopping theorem with the martingale you found in part (i) and stopping time $T$, the first time the walk hits level $0$ or $m$ (so $\mathbb{E}(T)$ is the expected duration of the game), show that
$$\mathbb{E}(d_a) = \frac{1}{q-p}\left(a - m\frac{1-\rho^a}{1-\rho^m}\right)$$
where $\rho = q/p$.
(iii) Show that $M_n = X_n^2 - n$ is a martingale with respect to the increments of the random walk when $p = q$.
(iv) Suppose that $p = q$. Using the optional stopping theorem with the martingale you found in part (iii) and stopping time $T$, the first time the walk hits level $0$ or $m$ (so $\mathbb{E}(T)$ is the expected duration of the game), show that
$$\mathbb{E}(d_a) = a(m-a).$$
(c) Alice starts playing against Bob in a standard gambler’s ruin game with probabilities $p \neq q$ and $s=0$. A draw probability $s>0$ is then introduced in such a way that the ratio $\rho = q/p$ remains constant. Comment on how this changes Alice’s ruin probability and the expected duration of the game.

**中文翻译 / Chinese Translation:**
考虑带有平局的赌徒破产问题：在每一步，Alice 以概率 $p$ 赢得 £1，以概率 $q$ 输掉 £1，以概率 $s$ 不赢不输，其中 $p+q+s=1$，且 $0 < p, q, s < 1$。我们假设 $p \neq q$。Alice 初始有 £$a$，Bob 有 £$(m-a)$。
(a) .
(i) 对于 $p \neq q$ 的情况，证明 $M_n = (q/p)^{X_n}$ 是关于随机游走增量（increments）的一个鞅（因此平局的加入不影响课堂上学到的 $M_n$）。
(ii) 使用可选停止定理（optional stopping theorem）得出结论：在这种情况下，$r_a$（Alice的破产概率）不依赖于 $s$。
(b) 令 $d_i$ 为从 Alice 拥有 £$i$ 的时刻开始，游戏的期望持续时间。我们想用鞅方法来证明 $d_i$ 的表达式（实际上我们这里有平局，所以情况更一般）。
(i) 找到一个常数 $c$，使得 $M_n = X_n + nc$ 是一个鞅。
(ii) 假设 $p \neq q$。使用你在 (i) 部分找到的鞅和停时 $T$（即游走首次触及 0 或 $m$ 的时刻，所以 $\mathbb{E}(T)$ 是游戏的期望持续时间），结合可选停止定理，证明：
$$\mathbb{E}(d_a) = \frac{1}{q-p}\left(a - m\frac{1-\rho^a}{1-\rho^m}\right)$$
其中 $\rho = q/p$。
(iii) 证明当 $p = q$ 时，$M_n = X_n^2 - n$ 是关于随机游走增量的一个鞅。
(iv) 假设 $p = q$。使用你在 (iii) 部分找到的鞅和停时 $T$，结合可选停止定理，证明：
$$\mathbb{E}(d_a) = a(m-a).$$
(c) Alice 在一个标准的赌徒破产问题中（概率 $p \neq q$ 且 $s=0$）开始与 Bob 对弈。然后引入一个平局概率 $s>0$，使得比值 $\rho = q/p$ 保持不变。评论这如何改变 Alice 的破产概率和游戏的期望持续时间。

**Knowledge Points / 考查知识点:**
- **鞅 (Martingales):** 鞅的定义，如何通过条件期望验证一个过程是否为鞅。
- **可选停止定理 (Optional Stopping Theorem, OST):** 在满足特定条件（有界停时、一致可积等）下，鞅在停时的期望等于其初始值。
- **赌徒破产问题 (Gambler's Ruin Problem):** 破产概率和期望持续时间的推导。
- **随机游走 (Random Walk):** 带有平局的随机游走，其增量分布。
- **条件期望 (Conditional Expectation):** 鞅性质的核心。

**Step-by-Step Solution / 逐步解答:**

#### Part (a)(i)

**Step 1: 定义随机游走和增量 / Define the Random Walk and Increments**

**中文思路 / Chinese reasoning:**
首先，我们需要明确随机游走 $X_n$ 的定义。$X_n$ 表示 Alice 在第 $n$ 步后的资金。其增量 $\xi_n = X_n - X_{n-1}$ 是一个随机变量，取值为 $+1$（赢），$-1$（输），$0$（平局），对应的概率分别为 $p, q, s$。我们要验证 $M_n = (q/p)^{X_n}$ 是一个鞅，即验证 $\mathbb{E}[M_{n+1} | \mathcal{F}_n] = M_n$，其中 $\mathcal{F}_n$ 是到第 $n$ 步为止的信息（自然滤波）。

**English reasoning:**
First, we need to define the random walk $X_n$. $X_n$ represents Alice's fortune after $n$ steps. Its increment $\xi_n = X_n - X_{n-1}$ is a random variable taking values $+1$ (win), $-1$ (lose), $0$ (draw), with probabilities $p, q, s$ respectively. We want to verify that $M_n = (q/p)^{X_n}$ is a martingale, i.e., $\mathbb{E}[M_{n+1} | \mathcal{F}_n] = M_n$, where $\mathcal{F}_n$ is the information up to step $n$ (natural filtration).

**计算过程 / Working:**
Let $X_n$ be Alice's fortune after $n$ steps. $X_0 = a$. The increment $\xi_{n+1} = X_{n+1} - X_n$ has distribution:
$$\mathbb{P}(\xi_{n+1} = 1) = p, \quad \mathbb{P}(\xi_{n+1} = -1) = q, \quad \mathbb{P}(\xi_{n+1} = 0) = s.$$

**Step 2: 计算条件期望 / Compute the Conditional Expectation**

**中文思路 / Chinese reasoning:**
我们计算 $\mathbb{E}[M_{n+1} | \mathcal{F}_n]$。由于 $M_{n+1} = (q/p)^{X_{n+1}} = (q/p)^{X_n + \xi_{n+1}} = M_n \cdot (q/p)^{\xi_{n+1}}$。因此，$\mathbb{E}[M_{n+1} | \mathcal{F}_n] = M_n \cdot \mathbb{E}[(q/p)^{\xi_{n+1}} | \mathcal{F}_n]$。由于 $\xi_{n+1}$ 独立于 $\mathcal{F}_n$，条件期望等于无条件期望。我们只需计算 $\mathbb{E}[(q/p)^{\xi_{n+1}}]$。

**English reasoning:**
We compute $\mathbb{E}[M_{n+1} | \mathcal{F}_n]$. Since $M_{n+1} = (q/p)^{X_{n+1}} = (q/p)^{X_n + \xi_{n+1}} = M_n \cdot (q/p)^{\xi_{n+1}}$. Thus, $\mathbb{E}[M_{n+1} | \mathcal{F}_n] = M_n \cdot \mathbb{E}[(q/p)^{\xi_{n+1}} | \mathcal{F}_n]$. Since $\xi_{n+1}$ is independent of $\mathcal{F}_n$, the conditional expectation equals the unconditional expectation. We just need to compute $\mathbb{E}[(q/p)^{\xi_{n+1}}]$.

**计算过程 / Working:**
$$\mathbb{E}[M_{n+1} | \mathcal{F}_n] = \mathbb{E}[ (q/p)^{X_n + \xi_{n+1}} | \mathcal{F}_n] = (q/p)^{X_n} \mathbb{E}[ (q/p)^{\xi_{n+1}} | \mathcal{F}_n] = M_n \mathbb{E}[ (q/p)^{\xi_{n+1}}].$$

**Step 3: 计算期望值 / Compute the Expectation**

**中文思路 / Chinese reasoning:**
现在计算 $\mathbb{E}[(q/p)^{\xi_{n+1}}]$。我们需要对 $\xi_{n+1}$ 的所有可能取值进行加权求和。当 $\xi_{n+1}=1$ 时，$(q/p)^1 = q/p$；当 $\xi_{n+1}=-1$ 时，$(q/p)^{-1} = p/q$；当 $\xi_{n+1}=0$ 时，$(q/p)^0 = 1$。将这些值与对应的概率相乘并求和。

**English reasoning:**
Now compute $\mathbb{E}[(q/p)^{\xi_{n+1}}]$. We need to sum over all possible values of $\xi_{n+1}$ weighted by their probabilities. When $\xi_{n+1}=1$, $(q/p)^1 = q/p$; when $\xi_{n+1}=-1$, $(q/p)^{-1} = p/q$; when $\xi_{n+1}=0$, $(q/p)^0 = 1$. Multiply these values by their corresponding probabilities and sum.

**计算过程 / Working:**
$$\begin{aligned}
\mathbb{E}[(q/p)^{\xi_{n+1}}] &= p \cdot (q/p)^1 + q \cdot (q/p)^{-1} + s \cdot (q/p)^0 \\
&= p \cdot \frac{q}{p} + q \cdot \frac{p}{q} + s \cdot 1 \\
&= q + p + s \\
&= 1.
\end{aligned}$$

**Step 4: 得出结论 / Conclude**

**中文思路 / Chinese reasoning:**
由于 $\mathbb{E}[(q/p)^{\xi_{n+1}}] = 1$，我们得到 $\mathbb{E}[M_{n+1} | \mathcal{F}_n] = M_n \cdot 1 = M_n$。这正好是鞅的定义。注意，这个结果与 $s$ 无关，因为 $p+q+s=1$ 保证了期望值为 1。这与课堂上没有平局（$s=0$）的情况完全一致。

**English reasoning:**
Since $\mathbb{E}[(q/p)^{\xi_{n+1}}] = 1$, we get $\mathbb{E}[M_{n+1} | \mathcal{F}_n] = M_n \cdot 1 = M_n$. This is exactly the definition of a martingale. Notice that this result is independent of $s$, because $p+q+s=1$ ensures the expectation is 1. This is identical to the case without draws ($s=0$) from the lectures.

**计算过程 / Working:**
$$\mathbb{E}[M_{n+1} | \mathcal{F}_n] = M_n.$$
Thus, $M_n = (q/p)^{X_n}$ is a martingale.

#### Part (a)(ii)

**Step 1: 定义停时和破产概率 / Define Stopping Time and Ruin Probability**

**中文思路 / Chinese reasoning:**
定义停时 $T = \min\{n \ge 0: X_n = 0 \text{ or } X_n = m\}$，即游戏结束的时刻。Alice 的破产概率 $r_a = \mathbb{P}(X_T = 0 | X_0 = a)$。我们将使用可选停止定理（OST）于鞅 $M_n$ 和停时 $T$。我们需要检查 OST 的条件是否满足。由于状态空间有限（0 到 m），且 $T$ 几乎必然有限（因为 $p,q>0$，最终会破产或赢光），并且 $M_n$ 是有界的（因为 $X_n$ 在 0 和 m 之间，所以 $M_n$ 在 $(q/p)^m$ 和 $(q/p)^0=1$ 之间），因此 OST 适用。

**English reasoning:**
Define the stopping time $T = \min\{n \ge 0: X_n = 0 \text{ or } X_n = m\}$, the time the game ends. Alice's ruin probability $r_a = \mathbb{P}(X_T = 0 | X_0 = a)$. We will apply the Optional Stopping Theorem (OST) to the martingale $M_n$ and stopping time $T$. We need to check the conditions for OST. Since the state space is finite (0 to m), and $T$ is almost surely finite (because $p,q>0$, ruin or victory will eventually happen), and $M_n$ is bounded (since $X_n$ is between 0 and m, $M_n$ is between $(q/p)^m$ and $(q/p)^0=1$), OST applies.

**Step 2: 应用可选停止定理 / Apply Optional Stopping Theorem**

**中文思路 / Chinese reasoning:**
根据可选停止定理，$\mathbb{E}[M_T] = \mathbb{E}[M_0] = (q/p)^a$。另一方面，$M_T$ 是一个随机变量，取决于 $T$ 时刻的状态。如果 $X_T = 0$，则 $M_T = (q/p)^0 = 1$。如果 $X_T = m$，则 $M_T = (q/p)^m$。因此，$\mathbb{E}[M_T] = 1 \cdot \mathbb{P}(X_T=0) + (q/p)^m \cdot \mathbb{P}(X_T=m)$。注意 $\mathbb{P}(X_T=m) = 1 - r_a$。

**English reasoning:**
By the Optional Stopping Theorem, $\mathbb{E}[M_T] = \mathbb{E}[M_0] = (q/p)^a$. On the other hand, $M_T$ is a random variable depending on the state at time $T$. If $X_T = 0$, then $M_T = (q/p)^0 = 1$. If $X_T = m$, then $M_T = (q/p)^m$. Thus, $\mathbb{E}[M_T] = 1 \cdot \mathbb{P}(X_T=0) + (q/p)^m \cdot \mathbb{P}(X_T=m)$. Note $\mathbb{P}(X_T=m) = 1 - r_a$.

**计算过程 / Working:**
$$\mathbb{E}[M_T] = r_a \cdot 1 + (1 - r_a) \cdot (q/p)^m.$$
By OST, $\mathbb{E}[M_T] = M_0 = (q/p)^a$.
So,
$$r_a + (1 - r_a)(q/p)^m = (q/p)^a.$$

**Step 3: 解出破产概率 / Solve for Ruin Probability**

**中文思路 / Chinese reasoning:**
解这个关于 $r_a$ 的方程。将含有 $r_a$ 的项移到一边，然后求解。

**English reasoning:**
Solve this equation for $r_a$. Move the terms containing $r_a$ to one side and solve.

**计算过程 / Working:**
$$r_a + (q/p)^m - r_a (q/p)^m = (q/p)^a$$
$$r_a (1 - (q/p)^m) = (q/p)^a - (q/p)^m$$
$$r_a = \frac{(q/p)^a - (q/p)^m}{1 - (q/p)^m}.$$

**Step 4: 分析结果 / Analyze the Result**

**中文思路 / Chinese reasoning:**
我们得到的 $r_a$ 表达式只依赖于 $p$ 和 $q$（通过比值 $\rho = q/p$），而不依赖于平局概率 $s$。这是因为在 (a)(i) 部分中，我们证明了 $M_n$ 是一个鞅，且其鞅性质与 $s$ 无关。因此，可选停止定理给出的结果也与 $s$ 无关。这证明了 $r_a$ 不依赖于 $s$。

**English reasoning:**
The expression for $r_a$ we obtained depends only on $p$ and $q$ (through the ratio $\rho = q/p$), and not on the draw probability $s$. This is because in part (a)(i), we proved that $M_n$ is a martingale, and its martingale property is independent of $s$. Therefore, the result from the Optional Stopping Theorem is also independent of $s$. This proves that $r_a$ does not depend on $s$.

**计算过程 / Working:**
The final expression for the ruin probability is:
$$r_a = \frac{\rho^a - \rho^m}{1 - \rho^m}, \quad \text{where } \rho = q/p.$$
This expression contains no $s$, so $r_a$ does not depend on $s$.

#### Part (b)(i)

**Step 1: 寻找常数 $c$ 使得 $M_n$ 是鞅 / Find constant $c$ such that $M_n$ is a martingale**

**中文思路 / Chinese reasoning:**
我们想找到一个常数 $c$，使得 $M_n = X_n + nc$ 是一个鞅。这意味着 $\mathbb{E}[M_{n+1} | \mathcal{F}_n] = M_n$。计算条件期望 $\mathbb{E}[X_{n+1} + (n+1)c | \mathcal{F}_n]$，并令其等于 $X_n + nc$，然后解出 $c$。

**English reasoning:**
We want to find a constant $c$ such that $M_n = X_n + nc$ is a martingale. This means $\mathbb{E}[M_{n+1} | \mathcal{F}_n] = M_n$. Compute the conditional expectation $\mathbb{E}[X_{n+1} + (n+1)c | \mathcal{F}_n]$, set it equal to $X_n + nc$, and solve for $c$.

**计算过程 / Working:**
$$\begin{aligned}
\mathbb{E}[M_{n+1} | \mathcal{F}_n] &= \mathbb{E}[X_{n+1} + (n+1)c | \mathcal{F}_n] \\
&= \mathbb{E}[X_n + \xi_{n+1} + (n+1)c | \mathcal{F}_n] \\
&= X_n + \mathbb{E}[\xi_{n+1}] + (n+1)c \quad (\text{since } \xi_{n+1} \perp \mathcal{F}_n) \\
&= X_n + (p \cdot 1 + q \cdot (-1) + s \cdot 0) + (n+1)c \\
&= X_n + (p - q) + (n+1)c.
\end{aligned}$$

**Step 2: 令其等于 $M_n$ 并解出 $c$ / Set equal to $M_n$ and solve for $c$**

**中文思路 / Chinese reasoning:**
为了 $M_n$ 是鞅，我们需要 $\mathbb{E}[M_{n+1} | \mathcal{F}_n] = M_n = X_n + nc$。因此，$X_n + (p-q) + (n+1)c = X_n + nc$。化简后解出 $c$。

**English reasoning:**
For $M_n$ to be a martingale, we need $\mathbb{E}[M_{n+1} | \mathcal{F}_n] = M_n = X_n + nc$. Thus, $X_n + (p-q) + (n+1)c = X_n + nc$. Simplify and solve for $c$.

**计算过程 / Working:**
$$X_n + (p-q) + (n+1)c = X_n + nc$$
$$(p-q) + nc + c = nc$$
$$p - q + c = 0$$
$$c = q - p.$$

**Step 3: 验证 / Verification**

**中文思路 / Chinese reasoning:**
我们找到 $c = q-p$。因此，$M_n = X_n + n(q-p)$ 是一个鞅。注意，当 $p=q$ 时，$c=0$，$M_n = X_n$ 本身就是一个鞅（因为期望增量为0）。当 $p \neq q$ 时，$c$ 非零，通过减去趋势项 $n(p-q)$ 来构造鞅。

**English reasoning:**
We found $c = q-p$. Therefore, $M_n = X_n + n(q-p)$ is a martingale. Note that when $p=q$, $c=0$, and $M_n = X_n$ itself is a martingale (since the expected increment is 0). When $p \neq q$, $c$ is non-zero, and we construct a martingale by subtracting the trend term $n(p-q)$.

**计算过程 / Working:**
The constant is $c = q-p$. The martingale is $M_n = X_n + n(q-p)$.

#### Part (b)(ii)

**Step 1: 应用可选停止定理 / Apply Optional Stopping Theorem**

**中文思路 / Chinese reasoning:**
我们使用在 (b)(i) 中找到的鞅 $M_n = X_n + n(q-p)$ 和停时 $T$（首次触及 0 或 m 的时刻）。可选停止定理给出 $\mathbb{E}[M_T] = \mathbb{E}[M_0] = X_0 + 0 \cdot (q-p) = a$。注意 $M_T = X_T + T(q-p)$。$X_T$ 是 $T$ 时刻的状态，要么是 0，要么是 m。$T$ 是游戏持续时间，其期望 $\mathbb{E}[T] = \mathbb{E}[d_a]$ 正是我们想求的。

**English reasoning:**
We use the martingale $M_n = X_n + n(q-p)$ found in (b)(i) and the stopping time $T$ (first time hitting 0 or m). The Optional Stopping Theorem gives $\mathbb{E}[M_T] = \mathbb{E}[M_0] = X_0 + 0 \cdot (q-p) = a$. Note $M_T = X_T + T(q-p)$. $X_T$ is the state at time $T$, either 0 or m. $T$ is the duration of the game, and its expectation $\mathbb{E}[T] = \mathbb{E}[d_a]$ is what we want to find.

**计算过程 / Working:**
$$\mathbb{E}[M_T] = \mathbb{E}[X_T + T(q-p)] = \mathbb{E}[X_T] + (q-p)\mathbb{E}[T].$$
By OST, $\mathbb{E}[M_T] = a$.
So,
$$\mathbb{E}[X_T] + (q-p)\mathbb{E}[d_a] = a.$$

**Step 2: 计算 $\mathbb{E}[X_T]$ / Compute $\mathbb{E}[X_T]$**

**中文思路 / Chinese reasoning:**
我们需要计算 $\mathbb{E}[X_T]$。$X_T$ 是游戏结束时的资金。它以概率 $r_a$ 为 0，以概率 $1-r_a$ 为 m。因此，$\mathbb{E}[X_T] = 0 \cdot r_a + m \cdot (1-r_a) = m(1-r_a)$。我们在 (a)(ii) 中已经得到了 $r_a$ 的表达式。

**English reasoning:**
We need to compute $\mathbb{E}[X_T]$. $X_T$ is the fortune at the end of the game. It is 0 with probability $r_a$, and m with probability $1-r_a$. Thus, $\mathbb{E}[X_T] = 0 \cdot r_a + m \cdot (1-r_a) = m(1-r_a)$. We already have the expression for $r_a$ from (a)(ii).

**计算过程 / Working:**
From part (a)(ii), $r_a = \frac{\rho^a - \rho^m}{1 - \rho^m}$, where $\rho = q/p$.
So,
$$1 - r_a = 1 - \frac{\rho^a - \rho^m}{1 - \rho^m} = \frac{1 - \rho^m - \rho^a + \rho^m}{1 - \rho^m} = \frac{1 - \rho^a}{1 - \rho^m}.$$
Thus,
$$\mathbb{E}[X_T] = m \cdot \frac{1 - \rho^a}{1 - \rho^m}.$$

**Step 3: 代入并解出 $\mathbb{E}[d_a]$ / Substitute and solve for $\mathbb{E}[d_a]$**

**中文思路 / Chinese reasoning:**
将 $\mathbb{E}[X_T]$ 的表达式代入方程 $\mathbb{E}[X_T] + (q-p)\mathbb{E}[d_a] = a$，然后解出 $\mathbb{E}[d_a]$。注意 $q-p = -(p-q)$。

**English reasoning:**
Substitute the expression for $\mathbb{E}[X_T]$ into the equation $\mathbb{E}[X_T] + (q-p)\mathbb{E}[d_a] = a$, and solve for $\mathbb{E}[d_a]$. Note $q-p = -(p-q)$.

**计算过程 / Working:**
$$m\frac{1 - \rho^a}{1 - \rho^m} + (q-p)\mathbb{E}[d_a] = a$$
$$(q-p)\mathbb{E}[d_a] = a - m\frac{1 - \rho^a}{1 - \rho^m}$$
$$\mathbb{E}[d_a] = \frac{1}{q-p}\left(a - m\frac{1 - \rho^a}{1 - \rho^m}\right).$$
This is the required expression.

#### Part (b)(iii)

**Step