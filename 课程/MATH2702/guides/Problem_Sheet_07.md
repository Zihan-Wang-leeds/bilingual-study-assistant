# Problem Sheet 7 - 详细解答 / Detailed Solutions

> MATH2702 Stochastic Processes
> 生成时间 / Generated: 2026-07-20 16:05
> 来源页 / Source Pages: 75-75

---

好的，作为您的大学随机过程课程导师，我将为您提供这份习题集的完整双语解答。

---

### Question 1 / 第1题

**Problem / 题目原文:**
Let (𝑋(𝑡)) be a Poisson process with rate 𝜆= 5. Calculate:
(a) ℙ(𝑋(0.6) ≤2);
(b) 𝔼𝑋(3.2);
(c) ℙ(𝑋(0.5) = 0 and 𝑋(1) = 1).
Let 𝑇𝑛be the 𝑛th holding time, and let 𝐽𝑛= 𝑇1 + ⋯+ 𝑇𝑛be the 𝑛th arrival time. Calculate:
(d) ℙ(0.1 ≤𝑇2 < 0.3);
(e) 𝔼𝐽50;
(f) Var(𝐽50).
(g) Using a normal approximation, approximate ℙ(8 ≤𝐽50 ≤12).

**中文翻译 / Chinese Translation:**
设 (𝑋(𝑡)) 是一个速率为 𝜆= 5 的泊松过程。计算：
(a) ℙ(𝑋(0.6) ≤2)；
(b) 𝔼𝑋(3.2)；
(c) ℙ(𝑋(0.5) = 0 且 𝑋(1) = 1)。
设 𝑇𝑛 为第 𝑛 个逗留时间，并设 𝐽𝑛 = 𝑇1 + ⋯ + 𝑇𝑛 为第 𝑛 个到达时间。计算：
(d) ℙ(0.1 ≤𝑇2 < 0.3)；
(e) 𝔼𝐽50；
(f) Var(𝐽50)。
(g) 使用正态近似，近似计算 ℙ(8 ≤𝐽50 ≤12)。

**Knowledge Points / 考查知识点:**
- 泊松过程的定义和性质 (Definition and properties of Poisson process)
- 泊松分布的概率质量函数 (PMF of Poisson distribution)
- 泊松过程的期望和方差 (Expectation and variance of Poisson process)
- 逗留时间 (Holding times) 的指数分布性质
- 到达时间 (Arrival times) 的伽马分布性质
- 中心极限定理和正态近似 (Central Limit Theorem and normal approximation)

**Step-by-Step Solution / 逐步解答:**

**(a) ℙ(𝑋(0.6) ≤2)**

1.  **中文思路 / Chinese reasoning:**
    我们需要计算在时间区间 [0, 0.6] 内，事件发生次数不超过 2 次的概率。根据泊松过程的定义，在长度为 t 的时间区间内，事件发生次数服从参数为 λt 的泊松分布。这里 λ=5，t=0.6，所以 λt = 5 * 0.6 = 3。因此，X(0.6) ~ Poisson(3)。我们需要计算 P(X ≤ 2) = P(X=0) + P(X=1) + P(X=2)。

    **English reasoning:**
    We need to calculate the probability that the number of events occurring in the time interval [0, 0.6] is at most 2. By the definition of a Poisson process, the number of events in an interval of length t follows a Poisson distribution with parameter λt. Here λ=5, t=0.6, so λt = 5 * 0.6 = 3. Therefore, X(0.6) ~ Poisson(3). We need to compute P(X ≤ 2) = P(X=0) + P(X=1) + P(X=2).

2.  **计算过程 / Working:**
    X = X(0.6) ~ Poisson(3)
    ℙ(X = k) = e^{-3} * (3^k) / k!
    ℙ(X ≤ 2) = ℙ(X=0) + ℙ(X=1) + ℙ(X=2)
    ℙ(X=0) = e^{-3} * (3^0) / 0! = e^{-3}
    ℙ(X=1) = e^{-3} * (3^1) / 1! = 3e^{-3}
    ℙ(X=2) = e^{-3} * (3^2) / 2! = 9e^{-3} / 2 = 4.5e^{-3}
    ℙ(X ≤ 2) = e^{-3} + 3e^{-3} + 4.5e^{-3} = 8.5e^{-3}

3.  **Explanation of working / 过程解释:**
    我们首先确定了随机变量 X(0.6) 服从参数为 3 的泊松分布。然后，我们使用泊松分布的概率质量函数 (PMF) 公式 P(X=k) = e^{-λt} (λt)^k / k! 来计算 k=0, 1, 2 的概率。最后，将这些概率相加得到最终结果。注意，0! = 1。

    We first determined that the random variable X(0.6) follows a Poisson distribution with parameter 3. Then, we used the Poisson probability mass function (PMF) formula P(X=k) = e^{-λt} (λt)^k / k! to calculate the probabilities for k=0, 1, 2. Finally, we summed these probabilities to get the final result. Note that 0! = 1.

**Final Answer / 最终答案:**
ℙ(𝑋(0.6) ≤2) = 8.5e^{-3}

**(b) 𝔼𝑋(3.2)**

1.  **中文思路 / Chinese reasoning:**
    泊松过程 X(t) 的期望值等于其速率 λ 乘以时间 t。这是一个基本性质：E[X(t)] = λt。这里 λ=5，t=3.2，所以直接计算即可。

    **English reasoning:**
    The expected value of a Poisson process X(t) is equal to its rate λ multiplied by the time t. This is a fundamental property: E[X(t)] = λt. Here λ=5, t=3.2, so we can calculate directly.

2.  **计算过程 / Working:**
    𝔼𝑋(3.2) = λ * t = 5 * 3.2 = 16

3.  **Explanation of working / 过程解释:**
    这个结果直接来自于泊松过程的定义。因为 X(t) ~ Poisson(λt)，而泊松分布的期望就是其参数 λt。

    This result comes directly from the definition of a Poisson process. Since X(t) ~ Poisson(λt), the expectation of a Poisson distribution is its parameter λt.

**Final Answer / 最终答案:**
𝔼𝑋(3.2) = 16

**(c) ℙ(𝑋(0.5) = 0 and 𝑋(1) = 1)**

1.  **中文思路 / Chinese reasoning:**
    我们需要计算两个事件同时发生的概率：在时间 0.5 之前没有事件发生，并且在时间 1 时恰好有 1 个事件发生。这等价于在 [0, 0.5] 内没有事件发生，并且在 (0.5, 1] 内恰好有 1 个事件发生。由于泊松过程具有独立增量性，这两个区间内的事件数是独立的。因此，联合概率等于两个独立泊松概率的乘积。

    **English reasoning:**
    We need to calculate the probability of two events occurring simultaneously: no events before time 0.5, and exactly 1 event by time 1. This is equivalent to having 0 events in [0, 0.5] and exactly 1 event in (0.5, 1]. Due to the independent increments property of the Poisson process, the number of events in these two disjoint intervals are independent. Therefore, the joint probability is the product of two independent Poisson probabilities.

2.  **计算过程 / Working:**
    Let A = {X(0.5) = 0}, B = {X(1) = 1}.
    The event {X(0.5)=0 and X(1)=1} is equivalent to {X(0.5)=0 and X(1)-X(0.5)=1}.
    X(0.5) ~ Poisson(5 * 0.5) = Poisson(2.5)
    X(1)-X(0.5) ~ Poisson(5 * (1-0.5)) = Poisson(2.5)
    ℙ(X(0.5)=0) = e^{-2.5} * (2.5^0) / 0! = e^{-2.5}
    ℙ(X(1)-X(0.5)=1) = e^{-2.5} * (2.5^1) / 1! = 2.5e^{-2.5}
    ℙ(𝑋(0.5) = 0 and 𝑋(1) = 1) = e^{-2.5} * 2.5e^{-2.5} = 2.5e^{-5}

3.  **Explanation of working / 过程解释:**
    我们利用了泊松过程的独立增量性，将联合概率分解为两个独立区间上概率的乘积。第一个区间 [0, 0.5] 的长度为 0.5，第二个区间 (0.5, 1] 的长度也为 0.5。两个区间的事件数都服从参数为 2.5 的泊松分布。然后我们分别计算了 P(X=0) 和 P(X=1)，并将它们相乘。

    We used the independent increments property of the Poisson process to decompose the joint probability into a product of probabilities over two independent intervals. The length of the first interval [0, 0.5] is 0.5, and the length of the second interval (0.5, 1] is also 0.5. The number of events in both intervals follows a Poisson distribution with parameter 2.5. We then calculated P(X=0) and P(X=1) separately and multiplied them.

**Final Answer / 最终答案:**
ℙ(𝑋(0.5) = 0 and 𝑋(1) = 1) = 2.5e^{-5}

**(d) ℙ(0.1 ≤𝑇2 < 0.3)**

1.  **中文思路 / Chinese reasoning:**
    T2 是第二个逗留时间，即第一个事件发生后到第二个事件发生前的时间间隔。在泊松过程中，逗留时间 T1, T2, ... 是独立同分布的指数随机变量，参数为 λ=5。因此，T2 ~ Exp(5)。我们需要计算 T2 落在区间 [0.1, 0.3) 内的概率。对于指数分布，P(a ≤ X < b) = F(b) - F(a)，其中 F(x) = 1 - e^{-λx} 是累积分布函数 (CDF)。

    **English reasoning:**
    T2 is the second holding time, which is the time interval between the first and second events. In a Poisson process, the holding times T1, T2, ... are independent and identically distributed exponential random variables with parameter λ=5. Therefore, T2 ~ Exp(5). We need to calculate the probability that T2 falls in the interval [0.1, 0.3). For an exponential distribution, P(a ≤ X < b) = F(b) - F(a), where F(x) = 1 - e^{-λx} is the cumulative distribution function (CDF).

2.  **计算过程 / Working:**
    T2 ~ Exp(5), λ=5.
    CDF: F(t) = 1 - e^{-5t} for t ≥ 0.
    ℙ(0.1 ≤ T2 < 0.3) = F(0.3) - F(0.1)
    F(0.3) = 1 - e^{-5 * 0.3} = 1 - e^{-1.5}
    F(0.1) = 1 - e^{-5 * 0.1} = 1 - e^{-0.5}
    ℙ(0.1 ≤ T2 < 0.3) = (1 - e^{-1.5}) - (1 - e^{-0.5}) = e^{-0.5} - e^{-1.5}

3.  **Explanation of working / 过程解释:**
    我们首先识别出 T2 服从指数分布。然后，我们应用指数分布的累积分布函数公式来计算区间概率。注意，对于连续随机变量，区间端点的开闭不影响概率值，但为了严谨，我们使用了 CDF 的差值。

    We first identified that T2 follows an exponential distribution. Then, we applied the formula for the cumulative distribution function of the exponential distribution to calculate the interval probability. Note that for continuous random variables, the inclusion or exclusion of the interval endpoints does not affect the probability value, but for rigor, we used the difference of the CDF.

**Final Answer / 最终答案:**
ℙ(0.1 ≤𝑇2 < 0.3) = e^{-0.5} - e^{-1.5}

**(e) 𝔼𝐽50**

1.  **中文思路 / Chinese reasoning:**
    J50 是第 50 个事件的到达时间，它等于前 50 个逗留时间的和：J50 = T1 + T2 + ... + T50。由于每个 Ti ~ Exp(5) 且相互独立，J50 服从形状参数为 50，速率参数为 5 的伽马分布 (Gamma(50, 5))。伽马分布的期望是形状参数除以速率参数，即 E[Jn] = n/λ。

    **English reasoning:**
    J50 is the arrival time of the 50th event, which is the sum of the first 50 holding times: J50 = T1 + T2 + ... + T50. Since each Ti ~ Exp(5) and they are independent, J50 follows a Gamma distribution with shape parameter 50 and rate parameter 5 (Gamma(50, 5)). The expectation of a Gamma distribution is the shape parameter divided by the rate parameter, i.e., E[Jn] = n/λ.

2.  **计算过程 / Working:**
    𝔼𝐽50 = n / λ = 50 / 5 = 10

3.  **Explanation of working / 过程解释:**
    这个结果非常直观。平均每 1/5 = 0.2 个单位时间发生一次事件。因此，发生 50 次事件的平均时间是 50 * 0.2 = 10。

    This result is very intuitive. On average, one event occurs every 1/5 = 0.2 time units. Therefore, the average time for 50 events to occur is 50 * 0.2 = 10.

**Final Answer / 最终答案:**
𝔼𝐽50 = 10

**(f) Var(𝐽50)**

1.  **中文思路 / Chinese reasoning:**
    同样，J50 ~ Gamma(50, 5)。伽马分布的方差是形状参数除以速率参数的平方，即 Var(Jn) = n/λ^2。

    **English reasoning:**
    Similarly, J50 ~ Gamma(50, 5). The variance of a Gamma distribution is the shape parameter divided by the square of the rate parameter, i.e., Var(Jn) = n/λ^2.

2.  **计算过程 / Working:**
    Var(𝐽50) = n / λ^2 = 50 / 5^2 = 50 / 25 = 2

3.  **Explanation of working / 过程解释:**
    每个指数分布的方差是 1/λ^2 = 1/25。由于它们是独立的，和的方差等于方差的和，所以 Var(J50) = 50 * (1/25) = 2。

    The variance of each exponential distribution is 1/λ^2 = 1/25. Since they are independent, the variance of the sum is the sum of the variances, so Var(J50) = 50 * (1/25) = 2.

**Final Answer / 最终答案:**
Var(𝐽50) = 2

**(g) Using a normal approximation, approximate ℙ(8 ≤𝐽50 ≤12)**

1.  **中文思路 / Chinese reasoning:**
    由于 J50 是 50 个独立同分布指数随机变量的和，根据中心极限定理 (CLT)，当 n 很大时，J50 的分布近似于正态分布。J50 的均值为 μ = 10，方差为 σ^2 = 2，标准差为 σ = √2。我们需要计算 P(8 ≤ J50 ≤ 12)。首先，我们将 J50 标准化为 Z = (J50 - μ) / σ。然后，将区间端点也标准化。最后，使用标准正态分布的累积分布函数 Φ(z) 来近似概率。

    **English reasoning:**
    Since J50 is the sum of 50 i.i.d. exponential random variables, by the Central Limit Theorem (CLT), the distribution of J50 is approximately normal when n is large. The mean of J50 is μ = 10, the variance is σ^2 = 2, and the standard deviation is σ = √2. We need to calculate P(8 ≤ J50 ≤ 12). First, we standardize J50 to Z = (J50 - μ) / σ. Then, we standardize the interval endpoints. Finally, we use the cumulative distribution function Φ(z) of the standard normal distribution to approximate the probability.

2.  **计算过程 / Working:**
    μ = 10, σ = √2 ≈ 1.4142
    ℙ(8 ≤ J50 ≤ 12) = ℙ( (8-10)/√2 ≤ (J50-10)/√2 ≤ (12-10)/√2 )
    = ℙ( -2/√2 ≤ Z ≤ 2/√2 )
    = ℙ( -√2 ≤ Z ≤ √2 )
    ≈ ℙ( -1.4142 ≤ Z ≤ 1.4142 )
    = Φ(1.4142) - Φ(-1.4142)
    = Φ(1.4142) - (1 - Φ(1.4142))
    = 2Φ(1.4142) - 1
    查标准正态分布表，Φ(1.41) ≈ 0.9207, Φ(1.42) ≈ 0.9222。我们可以取平均值或使用更精确的值。Φ(1.4142) ≈ 0.9213。
    ℙ(8 ≤ J50 ≤ 12) ≈ 2 * 0.9213 - 1 = 1.8426 - 1 = 0.8426

3.  **Explanation of working / 过程解释:**
    我们应用了中心极限定理。首先计算了均值和标准差。然后，我们将原始概率问题转化为标准正态分布的概率问题。通过标准化，我们得到了 Z 的上下限为 ±√2。然后，我们使用标准正态分布表或计算器来查找 Φ(1.4142) 的值。注意，Φ(-z) = 1 - Φ(z)。最终概率是 Φ(上界) - Φ(下界)。

    We applied the Central Limit Theorem. First, we calculated the mean and standard deviation. Then, we transformed the original probability problem into a standard normal probability problem. Through standardization, we obtained the upper and lower bounds for Z as ±√2. Then, we used a standard normal distribution table or calculator to find the value of Φ(1.4142). Note that Φ(-z) = 1 - Φ(z). The final probability is Φ(upper bound) - Φ(lower bound).

**Final Answer / 最终答案:**
ℙ(8 ≤𝐽50 ≤12) ≈ 0.8426

**Key Insight / 解题要点:**
- 泊松过程的核心是事件计数服从泊松分布，而事件间隔时间服从指数分布。
- 到达时间 Jn 是 n 个独立指数分布的和，服从伽马分布，其均值和方差有简洁公式。
- 中心极限定理允许我们用正态分布来近似伽马分布，从而计算复杂区间概率。
- The core of a Poisson process is that event counts follow a Poisson distribution, and inter-event times follow an exponential distribution.
- The arrival time Jn is the sum of n independent exponential distributions, follows a Gamma distribution, and has simple formulas for its mean and variance.
- The Central Limit Theorem allows us to approximate the Gamma distribution with a normal distribution to calculate complex interval probabilities.

---

### Question 2 / 第2题

**Problem / 题目原文:**
Suppose that telephone calls arrive at a call centre according to a Poisson process with rate 𝜆= 100 per hour, and are answered with probability 0.6.
(a) What is the probability that there are no answered calls in the next minute?
(b) Use a suitable normal approximation, with a continuity correction, to find the probability that there will be at least 25 answered calls in the next 30 minutes.

**中文翻译 / Chinese Translation:**
假设电话呼叫按照速率为每小时 100 次的泊松过程到达一个呼叫中心，并且每次呼叫被接听的概率为 0.6。
(a) 在接下来的一分钟内没有接听电话的概率是多少？
(b) 使用合适的正态近似，并应用连续性校正，求在接下来的 30 分钟内至少有 25 个接听电话的概率。

**Knowledge Points / 考查知识点:**
- 泊松过程 (Poisson process)
- 随机稀释/稀疏 (Random thinning/ splitting of Poisson process)
- 二项分布 (Binomial distribution)
- 泊松分布 (Poisson distribution)
- 正态近似 (Normal approximation to Poisson)
- 连续性校正 (Continuity correction)

**Step-by-Step Solution / 逐步解答:**

**(a) What is the probability that there are no answered calls in the next minute?**

1.  **中文思路 / Chinese reasoning:**
    首先，我们需要确定在接下来一分钟内到达的呼叫数量。速率是每小时 100 次，所以每分钟的速率是 λ_min = 100/60 = 5/3 次每分钟。因此，在一分钟内到达的呼叫数 N ~ Poisson(5/3)。每个呼叫被接听的概率是 p=0.6，且是否接听是独立的。因此，被接听的呼叫数 A 是在 N 次独立伯努利试验中成功的次数。给定 N=n，A 的条件分布是 Binomial(n, 0.6)。我们需要 P(A=0)。我们可以通过对 N 的所有可能值求和来求这个概率，或者利用泊松过程的一个性质：对泊松过程进行独立稀释后，结果仍然是一个泊松过程，其速率变为 λ * p。因此，被接听的呼叫过程是一个速率为 λ_min * p = (5/3) * 0.6 = 1 的泊松过程。所以，在一分钟内被接听的呼叫数 A ~ Poisson(1)。那么 P(A=0) 就很容易计算了。

    **English reasoning:**
    First, we need to determine the number of calls arriving in the next minute. The rate is 100 per hour, so the rate per minute is λ_min = 100/60 = 5/3 calls per minute. Therefore, the number of calls arriving in one minute, N, follows a Poisson distribution with mean 5/3. Each call is answered with probability p=0.6, and whether it is answered is independent. Thus, the number of answered calls, A, is the number of successes in N independent Bernoulli trials. Given N=n, the conditional distribution of A is Binomial(n, 0.6). We need P(A=0). We could sum over all possible values of N, or use a property of Poisson processes: if you independently thin a Poisson process, the result is still a Poisson process with rate λ * p. Therefore, the process of answered calls is a Poisson process with rate λ_min * p = (5/3) * 0.6 = 1. So, the number of answered calls in one minute, A, follows a Poisson distribution with mean 1. Then P(A=0) is easy to calculate.

2.  **计算过程 / Working:**
    λ_per_minute = 100 / 60 = 5/3
    p = 0.6
    λ_answered_per_minute = λ_per_minute * p = (5/3) * 0.6 = (5/3) * (3/5) = 1
    A ~ Poisson(1)
    ℙ(A = 0) = e^{-1} * (1^0) / 0! = e^{-1}

3.  **Explanation of working / 过程解释:**
    我们利用了泊松过程的稀释性质。原始呼叫过程速率为 5/3，每个呼叫以概率 0.6 被接听。稀释后的过程（即被接听的呼叫）的速率是原始速率乘以接听概率，结果为 1。因此，一分钟内接听电话数服从均值为 1 的泊松分布。P(A=0) 就是 e^{-1}。

    We used the thinning property of Poisson processes. The original call process has a rate of 5/3, and each call is answered with probability 0.6. The rate of the thinned process (i.e., answered calls) is the original rate multiplied by the answering probability, resulting in 1. Therefore, the number of answered calls in one minute follows a Poisson distribution with mean 1. P(A=0) is e^{-1}.

**Final Answer / 最终答案:**
The probability is e^{-1}.

**(b) Use a suitable normal approximation, with a continuity correction, to find the probability that there will be at least 25 answered calls in the next 30 minutes.**

1.  **中文思路 / Chinese reasoning:**
    首先，我们需要确定 30 分钟内被接听电话数的分布。30 分钟内到达的呼叫数 N_30 ~ Poisson(100/小时 * 0.5 小时) = Poisson(50)。经过稀释后，30 分钟内被接听的呼叫数 A_30 ~ Poisson(50 * 0.6) = Poisson(30)。我们需要 P(A_30 ≥ 25)。由于泊松分布的均值 30 足够大，我们可以用正态分布来近似。正态近似的均值为 μ = 30，方差为 σ^2 = 30，标准差为 σ = √30。因为我们要用连续分布（正态）来近似离散分布（泊松），所以需要应用连续性校正。对于事件 {A ≥ 25}，在离散情况下，它包含 25, 26, 27, ...。在连续近似中，我们使用区间 [24.5, ∞) 来代表这个事件。所以，我们计算 P(A_30 ≥ 24.5) 的正态近似。

    **English reasoning:**
    First, we need to determine the distribution of the number of answered calls in 30 minutes. The number of calls arriving in 30 minutes, N_30, follows a Poisson distribution with mean 100/hour * 0.5 hour = 50. After thinning, the number of answered calls in 30 minutes, A_30, follows a Poisson distribution with mean 50 * 0.6 = 30. We need P(A_30 ≥ 25). Since the mean of the Poisson distribution is 30, which is large enough, we can approximate it with a normal distribution. The mean of the normal approximation is μ = 30, the variance is