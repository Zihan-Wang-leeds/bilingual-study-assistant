# Problem Sheet 7 - 详细解答 / Detailed Solutions

> MATH2702 Stochastic Processes
> 生成时间 / Generated: 2026-07-17 15:14
> 来源页 / Source Pages: 75-75

---

好的，作为大学数学导师，我将为MATH2702: 随机过程 的习题第7套提供详细、逐步的解答。

---

### Question 1 / 第1题

**Problem / 题目原文:**
Let (𝑋(𝑡)) be a Poisson process with rate 𝜆 = 5. Calculate:
(a) ℙ(𝑋(0.6) ≤ 2);
(b) 𝔼𝑋(3.2);
(c) ℙ(𝑋(0.5) = 0 and 𝑋(1) = 1).
Let 𝑇𝑛 be the 𝑛th holding time, and let 𝐽𝑛 = 𝑇₁+⋯+𝑇𝑛 be the 𝑛th arrival time. Calculate:
(d) ℙ(0.1 ≤ 𝑇₂ < 0.3);
(e) 𝔼𝐽₅₀;
(f) Var(𝐽₅₀).
(g) Using a normal approximation, approximate ℙ(8 ≤ 𝐽₅₀ ≤ 12).

**中文翻译:**
设 (𝑋(𝑡)) 是速率为 𝜆 = 5 的泊松过程。计算：
(a) ℙ(𝑋(0.6) ≤ 2)；
(b) 𝔼𝑋(3.2)；
(c) ℙ(𝑋(0.5) = 0 且 𝑋(1) = 1)。
设 𝑇𝑛 为第 𝑛 个逗留时间，𝐽𝑛 = 𝑇₁+⋯+𝑇𝑛 为第 𝑛 个到达时间。计算：
(d) ℙ(0.1 ≤ 𝑇₂ < 0.3)；
(e) 𝔼𝐽₅₀；
(f) Var(𝐽₅₀)。
(g) 使用正态近似，近似计算 ℙ(8 ≤ 𝐽₅₀ ≤ 12)。

**Knowledge Points / 考查知识点:**
- 泊松过程的定义和性质 (Definition and properties of Poisson process)
- 泊松分布 (Poisson distribution)
- 指数分布 (Exponential distribution)
- 伽马分布 (Gamma distribution)
- 期望和方差的性质 (Properties of expectation and variance)
- 中心极限定理 (Central Limit Theorem)

**Step-by-Step Solution / 逐步解答:**

**(a) ℙ(𝑋(0.6) ≤ 2)**

**Step 1: 确定随机变量的分布**
在泊松过程中，对于任意时间间隔 $t$，计数 $X(t)$ 服从参数为 $\lambda t$ 的泊松分布。
这里 $\lambda = 5$, $t = 0.6$，所以 $X(0.6) \sim \text{Poisson}(\lambda t = 5 \times 0.6 = 3)$。

**Step 2: 写出概率表达式**
我们需要计算 $P(X(0.6) \le 2) = P(X=0) + P(X=1) + P(X=2)$。
泊松分布的概率质量函数为 $P(X=k) = \frac{e^{-\mu} \mu^k}{k!}$，其中 $\mu = 3$。

**Step 3: 逐项计算并求和**
- $P(X=0) = \frac{e^{-3} \cdot 3^0}{0!} = e^{-3}$
- $P(X=1) = \frac{e^{-3} \cdot 3^1}{1!} = 3e^{-3}$
- $P(X=2) = \frac{e^{-3} \cdot 3^2}{2!} = \frac{9}{2}e^{-3} = 4.5e^{-3}$

求和：
$P(X(0.6) \le 2) = e^{-3} + 3e^{-3} + 4.5e^{-3} = 8.5e^{-3}$

**Step 4: 数值计算**
$e^{-3} \approx 0.049787$
$P(X(0.6) \le 2) = 8.5 \times 0.049787 \approx 0.42319$

**(b) 𝔼𝑋(3.2)**

**Step 1: 应用期望公式**
对于泊松过程，$X(t) \sim \text{Poisson}(\lambda t)$。泊松分布的期望等于其参数。
$\mathbb{E}[X(t)] = \lambda t$

**Step 2: 代入数值**
$\mathbb{E}[X(3.2)] = 5 \times 3.2 = 16$

**(c) ℙ(𝑋(0.5) = 0 and 𝑋(1) = 1)**

**Step 1: 利用独立增量性**
泊松过程具有独立增量性。事件 $\{X(0.5)=0\}$ 和 $\{X(1)=1\}$ 不是独立的，因为后者包含了前者的信息。我们需要将事件转化为独立增量上的事件。
$X(1) = X(0.5) + (X(1) - X(0.5))$。
事件 $\{X(0.5)=0\}$ 且 $\{X(1)=1\}$ 等价于 $\{X(0.5)=0\}$ 且 $\{X(1)-X(0.5)=1\}$。

**Step 2: 利用独立增量性分解概率**
由于增量 $X(0.5)$ 和 $X(1)-X(0.5)$ 是独立的，我们有：
$P(X(0.5)=0, X(1)=1) = P(X(0.5)=0, X(1)-X(0.5)=1)$
$= P(X(0.5)=0) \cdot P(X(1)-X(0.5)=1)$

**Step 3: 确定各增量的分布**
- $X(0.5) \sim \text{Poisson}(5 \times 0.5 = 2.5)$
- $X(1)-X(0.5) \sim \text{Poisson}(5 \times (1-0.5) = 2.5)$

**Step 4: 计算概率**
$P(X(0.5)=0) = \frac{e^{-2.5} \cdot 2.5^0}{0!} = e^{-2.5}$
$P(X(1)-X(0.5)=1) = \frac{e^{-2.5} \cdot 2.5^1}{1!} = 2.5 e^{-2.5}$

**Step 5: 相乘得到最终结果**
$P = (e^{-2.5}) \times (2.5 e^{-2.5}) = 2.5 e^{-5}$

**(d) ℙ(0.1 ≤ 𝑇₂ < 0.3)**

**Step 1: 识别逗留时间的分布**
在泊松过程中，逗留时间 $T_n$ 是独立同分布的，服从参数为 $\lambda$ 的指数分布。
$T_n \sim \text{Exp}(\lambda = 5)$。

**Step 2: 写出指数分布的概率**
指数分布的概率密度函数为 $f(t) = \lambda e^{-\lambda t}$，累积分布函数为 $F(t) = 1 - e^{-\lambda t}$。
我们需要计算 $P(0.1 \le T_2 < 0.3) = F(0.3) - F(0.1)$。

**Step 3: 代入计算**
$F(0.3) = 1 - e^{-5 \times 0.3} = 1 - e^{-1.5}$
$F(0.1) = 1 - e^{-5 \times 0.1} = 1 - e^{-0.5}$
$P(0.1 \le T_2 < 0.3) = (1 - e^{-1.5}) - (1 - e^{-0.5}) = e^{-0.5} - e^{-1.5}$

**(e) 𝔼𝐽₅₀**

**Step 1: 识别到达时间的分布**
第 $n$ 个到达时间 $J_n = T_1 + T_2 + \dots + T_n$ 是 $n$ 个独立同分布的指数随机变量之和。这服从形状参数为 $n$，速率参数为 $\lambda$ 的伽马分布（或厄兰分布）。
$J_n \sim \text{Gamma}(n, \lambda)$。

**Step 2: 应用伽马分布的期望公式**
伽马分布 $\text{Gamma}(n, \lambda)$ 的期望为 $\mathbb{E}[J_n] = \frac{n}{\lambda}$。

**Step 3: 代入数值**
$\mathbb{E}[J_{50}] = \frac{50}{5} = 10$

**(f) Var(𝐽₅₀)**

**Step 1: 应用伽马分布的方差公式**
伽马分布 $\text{Gamma}(n, \lambda)$ 的方差为 $\text{Var}(J_n) = \frac{n}{\lambda^2}$。

**Step 2: 代入数值**
$\text{Var}(J_{50}) = \frac{50}{5^2} = \frac{50}{25} = 2$

**(g) 使用正态近似，近似计算 ℙ(8 ≤ 𝐽₅₀ ≤ 12)**

**Step 1: 应用中心极限定理**
由于 $J_{50}$ 是 50 个独立同分布随机变量之和，根据中心极限定理，其分布近似于正态分布。
$J_{50} \approx N(\mu, \sigma^2)$，其中 $\mu = \mathbb{E}[J_{50}] = 10$，$\sigma^2 = \text{Var}(J_{50}) = 2$。
因此，标准差 $\sigma = \sqrt{2}$。

**Step 2: 标准化**
我们需要计算 $P(8 \le J_{50} \le 12)$。标准化为 $Z = \frac{J_{50} - \mu}{\sigma} = \frac{J_{50} - 10}{\sqrt{2}}$。
$P(8 \le J_{50} \le 12) = P\left(\frac{8-10}{\sqrt{2}} \le Z \le \frac{12-10}{\sqrt{2}}\right)$
$= P\left(\frac{-2}{\sqrt{2}} \le Z \le \frac{2}{\sqrt{2}}\right)$
$= P(-\sqrt{2} \le Z \le \sqrt{2})$
$\sqrt{2} \approx 1.414$

**Step 3: 使用标准正态分布表**
$P(-1.414 \le Z \le 1.414) = \Phi(1.414) - \Phi(-1.414)$
由于 $\Phi(-x) = 1 - \Phi(x)$，我们有：
$= \Phi(1.414) - (1 - \Phi(1.414)) = 2\Phi(1.414) - 1$
查标准正态分布表，$\Phi(1.41) \approx 0.9207$，$\Phi(1.42) \approx 0.9222$。插值得 $\Phi(1.414) \approx 0.9215$。

**Step 4: 计算最终近似概率**
$P(8 \le J_{50} \le 12) \approx 2 \times 0.9215 - 1 = 1.843 - 1 = 0.843$

**Final Answer / 最终答案:**
(a) $8.5e^{-3} \approx 0.423$
(b) $16$
(c) $2.5e^{-5}$
(d) $e^{-0.5} - e^{-1.5}$
(e) $10$
(f) $2$
(g) $\approx 0.843$

**Key Insight / 解题要点:**
泊松过程的核心是计数过程 $X(t)$ 服从泊松分布，而到达间隔 $T_n$ 服从指数分布，到达时间 $J_n$ 服从伽马分布，利用这些分布的性质和中心极限定理可以解决大部分问题。

---

### Question 2 / 第2题

**Problem / 题目原文:**
Suppose that telephone calls arrive at a call centre according to a Poisson process with rate $\lambda = 100$ per hour, and are answered with probability 0.6.
(a) What is the probability that there are no answered calls in the next minute?
(b) Use a suitable normal approximation, with a continuity correction, to find the probability that there will be at least 25 answered calls in the next 30 minutes.

**中文翻译:**
假设电话按速率为每小时 $\lambda = 100$ 的泊松过程到达呼叫中心，并且有 0.6 的概率被接听。
(a) 下一分钟内没有接听电话的概率是多少？
(b) 使用合适的正态近似，并加上连续性校正，求接下来 30 分钟内至少有 25 个接听电话的概率。

**Knowledge Points / 考查知识点:**
- 泊松过程的分解 (Thinning of Poisson process)
- 泊松分布
- 正态近似与连续性校正 (Normal approximation with continuity correction)

**Step-by-Step Solution / 逐步解答:**

**(a) 下一分钟内没有接听电话的概率**

**Step 1: 确定接听电话的过程**
这是一个泊松过程的分解问题。每个到达的电话以概率 $p=0.6$ 被接听，以概率 $1-p=0.4$ 未被接听。被接听电话的过程是一个速率为 $\lambda p$ 的泊松过程。
接听电话的速率 $\lambda_a = \lambda \times p = 100 \times 0.6 = 60$ 每小时。

**Step 2: 统一时间单位**
问题问的是“下一分钟”，所以我们需要将速率转换为每分钟。
$\lambda_a = 60$ 每小时 $= \frac{60}{60} = 1$ 每分钟。

**Step 3: 计算概率**
在 1 分钟内，接听电话的数量 $A(1) \sim \text{Poisson}(\lambda_a \times 1 = 1)$。
“没有接听电话”即 $A(1) = 0$。
$P(A(1) = 0) = \frac{e^{-1} \cdot 1^0}{0!} = e^{-1}$

**(b) 使用正态近似求 30 分钟内至少有 25 个接听电话的概率**

**Step 1: 确定 30 分钟内接听电话的分布**
接听电话的速率是每分钟 1 个。在 30 分钟内，接听电话的数量 $A(30) \sim \text{Poisson}(\mu = 1 \times 30 = 30)$。

**Step 2: 应用正态近似**
由于 $\mu = 30$ 较大，我们可以用正态分布 $N(\mu, \sigma^2)$ 来近似泊松分布，其中 $\mu = 30$，方差 $\sigma^2 = \mu = 30$，标准差 $\sigma = \sqrt{30}$。

**Step 3: 应用连续性校正**
我们要求 $P(A(30) \ge 25)$。使用连续性校正时，我们将离散的整数点映射到连续的区间上。事件 $\{A \ge 25\}$ 对应于连续区间 $\{A \ge 24.5\}$。
所以，我们近似计算 $P(A \ge 24.5)$。

**Step 4: 标准化**
$Z = \frac{A - \mu}{\sigma} = \frac{A - 30}{\sqrt{30}}$。
$P(A \ge 24.5) = P\left(Z \ge \frac{24.5 - 30}{\sqrt{30}}\right)$
$= P\left(Z \ge \frac{-5.5}{\sqrt{30}}\right)$
$\sqrt{30} \approx 5.477$
$Z$ 值 $= \frac{-5.5}{5.477} \approx -1.004$

**Step 5: 计算概率**
$P(Z \ge -1.004) = 1 - P(Z < -1.004) = 1 - \Phi(-1.004)$
由于 $\Phi(-x) = 1 - \Phi(x)$，我们有：
$P(Z \ge -1.004) = 1 - (1 - \Phi(1.004)) = \Phi(1.004)$
查标准正态分布表，$\Phi(1.00) = 0.8413$，$\Phi(1.01) = 0.8438$。插值得 $\Phi(1.004) \approx 0.8423$。

**Final Answer / 最终答案:**
(a) $e^{-1}$
(b) $\approx 0.842$

**Key Insight / 解题要点:**
泊松过程的分解（稀疏化）产生一个新的泊松过程，其速率是原速率乘以选择概率。当用正态近似离散分布时，连续性校正（如将 $\ge 25$ 改为 $\ge 24.5$）能显著提高近似精度。

---

### Question 3 / 第3题

**Problem / 题目原文:**
(a) Let $X \sim Po(\lambda)$ and $Y \sim Po(\mu)$ be two independent Poisson distributions. Show that $X + Y \sim Po(\lambda+\mu)$. One way to start would be to write
$\mathbb{P}(X + Y = z) = \sum_{x=0}^{z} \mathbb{P}(X = x) \mathbb{P}(Y = z - x)$.
(b) Let $(X(t))$ and $(Y(t))$ be independent Poisson processes with rate $\lambda$ and $\mu$ respectively. Use part (a) to show that $(X(t)+Y(t))$ is a Poisson process with rate $\lambda+\mu$.
(c) Number 1 buses arrive at a bus stop at a rate of $\lambda_1=4$ per hour, and Number 6 buses arrive at the rate $\lambda_6=2$ per hour. I have been waiting at the bus stop for 5 minutes for either bus to arrive; how much longer do I have to wait, on average?

**中文翻译:**
(a) 设 $X \sim Po(\lambda)$ 和 $Y \sim Po(\mu)$ 是两个独立的泊松分布。证明 $X + Y \sim Po(\lambda+\mu)$。一个可行的出发点是写出 $\mathbb{P}(X + Y = z) = \sum_{x=0}^{z} \mathbb{P}(X = x) \mathbb{P}(Y = z - x)$。
(b) 设 $(X(t))$ 和 $(Y(t))$ 是速率分别为 $\lambda$ 和 $\mu$ 的独立泊松过程。利用 (a) 部分证明 $(X(t)+Y(t))$ 是速率为 $\lambda+\mu$ 的泊松过程。
(c) 1 路公交车以每小时 $\lambda_1=4$ 辆的速率到达公交站，6 路公交车以每小时 $\lambda_6=2$ 辆的速率到达。我已经在公交站等了 5 分钟，等待其中任意一辆车到来；平均而言，我还需要等多久？

**Knowledge Points / 考查知识点:**
- 泊松分布的可加性 (Additivity of Poisson distribution)
- 泊松过程的定义 (Definition of Poisson process)
- 指数分布的无记忆性 (Memoryless property of exponential distribution)
- 最小值的分布 (Distribution of minimum of exponentials)

**Step-by-Step Solution / 逐步解答:**

**(a) 证明 $X+Y \sim Po(\lambda+\mu)$**

**Step 1: 写出全概率公式**
由于 $X$ 和 $Y$ 独立，我们可以通过卷积公式得到 $X+Y$ 的分布。
$P(X+Y = z) = \sum_{x=0}^{z} P(X = x, Y = z-x)$
由于独立，$P(X = x, Y = z-x) = P(X=x)P(Y=z-x)$。

**Step 2: 代入泊松分布的概率质量函数**
$P(X=x) = \frac{e^{-\lambda} \lambda^x}{x!}$
$P(Y=z-x) = \frac{e^{-\mu} \mu^{z-x}}{(z-x)!}$
所以，
$P(X+Y = z) = \sum_{x=0}^{z} \frac{e^{-\lambda} \lambda^x}{x!} \cdot \frac{e^{-\mu} \mu^{z-x}}{(z-x)!}$

**Step 3: 整理求和式**
$P(X+Y = z) = e^{-(\lambda+\mu)} \sum_{x=0}^{z} \frac{1}{x!(z-x)!} \lambda^x \mu^{z-x}$

**Step 4: 引入二项式系数**
$\frac{1}{x!(z-x)!} = \frac{z!}{z!} \cdot \frac{1}{x!(z-x)!} = \frac{1}{z!} \binom{z}{x}$
所以，
$P(X+Y = z) = \frac{e^{-(\lambda+\mu)}}{z!} \sum_{x=0}^{z} \binom{z}{x} \lambda^x \mu^{z-x}$

**Step 5: 应用二项式定理**
根据二项式定理，$\sum_{x=0}^{z} \binom{z}{x} \lambda^x \mu^{z-x} = (\lambda + \mu)^z$。

**Step 6: 得到最终形式**
$P(X+Y = z) = \frac{e^{-(\lambda+\mu)} (\lambda+\mu)^z}{z!}$
这正是参数为 $\lambda+\mu$ 的泊松分布的概率质量函数。因此，$X+Y \sim Po(\lambda+\mu)$。证毕。

**(b) 证明 $(X(t)+Y(t))$ 是速率为 $\lambda+\mu$ 的泊松过程**

**Step 1: 回顾泊松过程的定义**
一个计数过程 $\{N(t), t \ge 0\}$ 是速率为 $\nu$ 的泊松过程，如果：
1. $N(0) = 0$。
2. 具有独立增量性。
3. 对于任意 $s, t \ge 0$，增量 $N(t+s) - N(s) \sim Po(\nu t)$。

**Step 2: 验证定义中的条件**
设 $Z(t) = X(t) + Y(t)$。
1. $Z(0) = X(0) + Y(0) = 0 + 0 = 0$。条件满足。
2. **独立增量性**：由于 $X(t)$ 和 $Y(t)$ 都是泊松过程，它们各自具有独立增量性。对于任意不相交的时间区间，$X$ 的增量与 $Y$ 的增量都是独立的。因此，$Z$ 的增量（即 $X$ 和 $Y$ 增量之和）在不相交的时间区间上也是独立的。条件满足。
3. **增量分布**：对于任意 $s, t \ge 0$，考虑增量 $Z(t+s) - Z(s) = [X(t+s)-X(s)] + [Y(t+s)-Y(s)]$。由于 $X$ 和 $Y$ 是独立的泊松过程，它们的增量是独立的随机变量，且分别服从 $Po(\lambda t)$ 和 $Po(\mu t)$。根据 (a) 部分，两个独立泊松随机变量之和仍服从泊松分布，参数为两者参数之和。因此，$Z(t+s) - Z(s) \sim Po((\lambda+\mu)t)$。条件满足。

**Step 3: 结论**
由于 $Z(t)$ 满足泊松过程的所有定义条件，且其增量的速率为 $\lambda+\mu$，所以 $Z(t) = X(t)+Y(t)$ 是速率为 $\lambda+\mu$ 的泊松过程。证毕。

**(c) 平均还需等待多久**

**Step 1: 确定合并过程的速率**
两种公交车的到达过程是独立的泊松过程。合并后的过程（即“任一公交车到达”）也是一个泊松过程，其速率 $\lambda = \lambda_1 + \lambda_6 = 4 + 2 = 6$ 每小时。

**Step 2: 应用指数分布的无记忆性**
等待时间（即到达间隔时间）服从参数为 $\lambda$ 的指数分布。指数分布具有无记忆性。这意味着，无论我已经等了多久（5分钟），剩余等待时间的分布与初始等待时间的分布相同。

**Step 3: 计算平均剩余等待时间**
平均等待时间是指数分布的期望，即 $1/\lambda$。
$\mathbb{E}[\text{等待时间}] = \frac{1}{\lambda} = \frac{1}{6}$ 小时。
将小时转换为分钟：$\frac{1}{6} \times 60 = 10$ 分钟。

**Final Answer / 最终答案:**
(a) 证明如上。
(b) 证明如上。
(c) 10 分钟。

**Key Insight / 解题要点:**
独立泊松过程的和仍然是泊松过程，其速率是各速率之和。指数分布的无记忆性意味着“已经等待的时间”不会影响“剩余等待时间”的分布。

---

### Question 4 / 第4题

**Problem / 题目原文:**
Let $T_1 \sim Exp(\lambda_1)$, $T_2 \sim Exp(\lambda_2)$, ..., $T_n \sim Exp(\lambda_n)$ be independent exponential distributions, and let $T$ be the minimum $T = \min\{T_1, T_2, ..., T_n\}$.
(a) Show that $T \sim Exp(\lambda_1+\lambda_2+\cdots+\lambda_n)$. You may use the fact that
$\mathbb{P}(T > t) = \mathbb{P}(T_1 > t) \mathbb{P}(T_2 > t) \cdots \mathbb{P}(T_n > t)$,
provided you explain why it is true.
(b) Show that the probability that the minimum is $T_j$ is given by
$\mathbb{P}(T_j = T) = \frac{\lambda_j}{\lambda_1+\lambda_2+\cdots+\lambda_n}$.
(You could choose to begin by proving the $n=2$ case, if you want.)

**中文翻译:**
设 $T_1 \sim Exp(\lambda_1)$, $T_2 \sim Exp(\lambda_2)$, ..., $T_n \sim Exp(\lambda_n)$ 是独立的指数分布，并设 $T$ 为最小值 $T = \min\{T_1, T_2, ..., T_n\}$。
(a) 证明 $T \sim Exp(\lambda_1+\lambda_2+\cdots+\lambda_n)$。你可以使用 $\mathbb{P}(T > t) = \mathbb{P}(T_1 > t) \mathbb{P}(T_2 > t) \cdots \mathbb{P}(T_n > t)$ 这一事实，但需要解释为什么它成立。
(b) 证明最小值是 $T_j$ 的概率为 $\mathbb{P}(T_j = T) = \frac{\lambda_j}{\lambda_1+\lambda_2+\cdots+\lambda_n}$。（如果你愿意，可以从证明