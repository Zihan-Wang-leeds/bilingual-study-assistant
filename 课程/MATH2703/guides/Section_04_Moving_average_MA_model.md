# Section 4: Moving average (MA) model

> MATH2703 - 自学教材 / Self-Study Guide
> 生成时间: 2026-07-21 11:09
> 来源页: 33-40

---

# MATH2703: Time Series / 时间序列分析

## Chapter 4: Moving Average Models / 移动平均模型

---

### 📋 Section Overview / 章节概览

**中文解释：** 本章我们学习移动平均（MA）模型。在上一章中，我们学习了自回归（AR）模型，其中当前值依赖于过去的观测值。而MA模型则不同：当前值依赖于当前和过去的"误差"或"冲击"（即白噪声过程）。MA模型在经济学、金融学等领域有广泛应用，因为许多经济指标会受到随机事件（如罢工、政府决策等）的短期影响。本章将介绍MA模型的定义、性质、自相关函数（ACF）的特征，以及可逆性（invertibility）这一重要概念。

**English explanation:** In this chapter, we study Moving Average (MA) models. In the previous chapter, we learned about Autoregressive (AR) models, where the current value depends on past observations. MA models are different: the current value depends on current and past "errors" or "shocks" (i.e., the white noise process). MA models are widely used in economics, finance, and other fields because many economic indicators are affected by random events (such as strikes, government decisions, etc.) that have short-term effects. This chapter covers the definition, properties, autocorrelation function (ACF) characteristics, and the important concept of invertibility.

---

### 🎯 Learning Objectives / 学习目标

完成本章学习后，你应该能够 / After completing this chapter, you should be able to:

1. **定义**MA(q)过程并写出其数学表达式 / **Define** an MA(q) process and write its mathematical expression
2. **推导**MA(q)过程的均值和自协方差函数 / **Derive** the mean and autocovariance function of an MA(q) process
3. **解释**MA过程的ACF"截尾"（cut-off）性质 / **Explain** the "cut-off" property of the ACF for MA processes
4. **识别**时间序列数据是否适合用MA模型描述 / **Identify** whether time series data is suitable for MA modeling
5. **理解**可逆性（invertibility）的概念及其重要性 / **Understand** the concept of invertibility and its importance
6. **判断**一个MA过程是否可逆 / **Determine** whether an MA process is invertible

---

### 📚 Prerequisites / 前置知识

在学习本章之前，你需要熟悉 / Before studying this chapter, you should be familiar with:

- **白噪声过程 (White noise process):** {ε_t} ~ WN(0, σ²)，即均值为0、方差为σ²的不相关随机变量序列
- **弱平稳性 (Weak stationarity):** 均值为常数，自协方差仅依赖于时间差
- **自相关函数 (ACF):** ρ_k = γ_k / γ_0
- **后移算子 (Backshift operator):** B X_t = X_{t-1}
- **AR(p)过程的平稳性条件:** 特征方程的根都在单位圆外

---

### 📖 Core Content / 核心内容

---

#### 4.1 Introduction / 引言

##### Intuition / 直觉理解

**中文解释：** 让我们用一个直观的例子来理解MA模型。想象一艘船在水面上移动，船体对水面产生扰动（即"误差"或"冲击"）。当你现在观察水面的波动时，你不仅感受到船在当前时刻产生的扰动，还感受到1秒前产生的扰动（但已经减弱了一些），甚至可能还有2秒前产生的更微弱的回声。换句话说，当前的水面高度是最近几个扰动的加权和。这与AR模型不同——AR模型中，当前水面高度取决于过去的水面高度本身。

**English explanation:** Let's use an intuitive example to understand MA models. Imagine a boat moving through water, creating disturbances (i.e., "errors" or "shocks") on the water surface. When you observe the water waves now, you not only feel the disturbance created by the boat at the current moment, but also the disturbance from 1 second ago (though somewhat weakened), and possibly even a smaller echo from 2 seconds ago. In other words, the current water surface height is a weighted sum of several recent disturbances. This differs from AR models — in AR models, the current water surface height depends on past water surface heights themselves.

**Formal motivation / 形式化动机：**

**中文解释：** 在第2章中我们提到，许多随机过程的模型通过代数公式将t时刻的随机变量与过程的过去值以及不可观测的"误差"过程的值联系起来。白噪声过程通常用来描述这个"误差"过程。在本章中，我们考虑t时刻（比如今天）的随机变量依赖于今天和过去不可观测的"误差"过程的值。

**English explanation:** As mentioned in Chapter 2, many models for stochastic processes are expressed by means of an algebraic formula relating the random variable at time t to past values of the process, together with values of an unobservable "error" process. The white noise process is usually used to describe the "error" process. In this chapter, we consider the random variable at time t (say today) depends on today's and the past values of the unobservable "error" process.

**Example / 例子：**

**中文解释：** 考虑船在水面上移动产生尾流。水在时间t被船撞击（误差、扰动，有时称为"冲击"）。但你此刻感受到的波浪还包括1秒前的误差，以及可能更小的2秒前的回声。直观上，水面是对最近几个扰动的反应，而不是对自身过去高度的反应。这就是：
今天 = 今天的误差 + 昨天误差的一部分 + 前天误差的一部分

**English explanation:** Consider a boat moving through water and creating a wake. The water is hit by the boat (error, disturbance introduced by the boat sometimes called "shock") at time t. But the wave you feel now also includes the error from 1 second ago, and maybe a smaller echo from 2 seconds ago. Intuitively, the water surface is reacting to a few recent disturbances, not its own past height. This is:
today = today's error + a fraction of yesterday's error + a fraction of the day before yesterday's error

---

#### 4.2 Moving Average Models / 移动平均模型

##### Formal Definition / 形式化定义

**Definition 4.1 (Moving average processes / 移动平均过程)**

**中文解释：** 一个随机过程{X_t}被称为q阶移动平均过程（或MA(q)过程），如果它可以写成：

**English explanation:** A stochastic process {X_t} is called a moving average process of order q (or an MA(q) process) if:

$$X_t = \sum_{k=0}^{q} \beta_k \varepsilon_{t-k} = \beta_0 \varepsilon_t + \beta_1 \varepsilon_{t-1} + \cdots + \beta_q \varepsilon_{t-q}$$

其中 / where:
- $\beta_0, \beta_1, \ldots, \beta_q \in \mathbb{R}$ 是实系数 / are real coefficients
- $\{\varepsilon_t\}$ 是白噪声过程 / is a white noise process

**Symbol Table / 符号表：**

| Symbol | Meaning (English) | 含义（中文） |
|--------|-------------------|--------------|
| $X_t$ | The observed time series at time t | t时刻的观测时间序列 |
| $\varepsilon_t$ | White noise error/shock at time t | t时刻的白噪声误差/冲击 |
| $\beta_k$ | Coefficient for error at lag k | 滞后k的误差系数 |
| $q$ | Order of the MA process | MA过程的阶数 |
| $\mathbb{R}$ | Set of real numbers | 实数集 |

##### Remarks / 注释

**Remark 1: Why "moving average"? / 为什么叫"移动平均"？**

**中文解释：** 直观上称为"移动平均"，因为时间序列的每个值都是最近随机误差/扰动/冲击的加权平均，而这些冲击随时间"向前移动"。

**English explanation:** It's called moving average intuitively because each value of the time series is a weighted average of recent random errors/disturbances/shocks, and those shocks "move" forward through time.

**Remark 2: Normalization / 标准化**

**中文解释：** 不失一般性，我们可以假设β₀ = 1。如果β₀ ≠ 1，我们可以令 $\tilde{\varepsilon}_t = \beta_0 \varepsilon_t$ 作为新的白噪声，这样MA过程的定义就变为 $X_t = \tilde{\varepsilon}_t + \beta_1^* \varepsilon_{t-1} + \cdots + \beta_q^* \varepsilon_{t-q}$，其中 $\beta_k^* = \beta_k / \beta_0$。

**English explanation:** Without loss of generality, we can assume β₀ = 1. If β₀ ≠ 1, we can let $\tilde{\varepsilon}_t = \beta_0 \varepsilon_t$ as the white noise in the definition of the MA process, so the MA process becomes $X_t = \tilde{\varepsilon}_t + \beta_1^* \varepsilon_{t-1} + \cdots + \beta_q^* \varepsilon_{t-q}$, where $\beta_k^* = \beta_k / \beta_0$.

**Remark 3: Stationarity / 平稳性**

**中文解释：** 由于{ε_t}是弱平稳的，有限阶的{X_t}也是弱平稳的（证明见下一小节）。注意：与AR过程不同，MA过程不需要对系数施加任何条件就能保证平稳性。

**English explanation:** Since {ε_t} is weakly stationary, finite-order {X_t} is also weakly stationary (proof see the next subsection). Note: Unlike AR processes, MA processes do not require any conditions on the coefficients to ensure stationarity.

**Remark 4: Applications / 应用**

**中文解释：** MA过程已在许多领域得到应用，特别是计量经济学。例如，经济指标受到各种"随机"事件的影响，如罢工、政府决策、关键材料短缺等。这些事件不仅会产生即时影响，还可能在未来几个时期以较小程度影响经济指标。因此，使用MA过程来描述这些现象是合理的。

**English explanation:** MA processes have been used in many areas, particularly econometrics. For example, economic indicators are affected by a variety of 'random' events such as strikes, government decisions, shortages of key materials and so on. Such events will not only have an immediate effect but may also affect economic indicators to a lesser extent in several subsequent periods, and so it is at least plausible that an MA process may be appropriate.

---

#### 4.3 ACF of MA Processes / MA过程的自相关函数

##### Derivation of Mean / 均值的推导

**中文解释：** 对于MA(q)过程 $X_t = \sum_{k=0}^{q} \beta_k \varepsilon_{t-k}$，我们计算其均值：

**English explanation:** For an MA(q) process $X_t = \sum_{k=0}^{q} \beta_k \varepsilon_{t-k}$, we compute its mean:

$$\mu = E[X_t] = E\left[\sum_{k=0}^{q} \beta_k \varepsilon_{t-k}\right] = \sum_{k=0}^{q} \beta_k E[\varepsilon_{t-k}] = 0$$

因为白噪声的均值为0 / because the white noise has mean 0.

##### Derivation of Variance / 方差的推导

**中文解释：** 计算方差γ₀ = Var(X_t)：

**English explanation:** Compute the variance γ₀ = Var(X_t):

$$\gamma_0 = \text{Var}(X_t) = \text{Var}\left(\sum_{k=0}^{q} \beta_k \varepsilon_{t-k}\right) = \sum_{k=0}^{q} \beta_k^2 \text{Var}(\varepsilon_{t-k})$$

因为白噪声在不同时间点是不相关的，所以协方差项都为0 / because white noise at different time points is uncorrelated, so all covariance terms are 0.

$$\gamma_0 = (\beta_0^2 + \beta_1^2 + \cdots + \beta_q^2)\sigma^2$$

其中σ² = Var(ε_t) / where σ² = Var(ε_t).

##### Derivation of Autocovariance / 自协方差的推导

**中文解释：** 计算滞后k的自协方差γ_k = Cov(X_t, X_{t+k})：

**English explanation:** Compute the autocovariance at lag k, γ_k = Cov(X_t, X_{t+k}):

$$\gamma_k = \text{Cov}(X_t, X_{t+k}) = \text{Cov}\left(\sum_{i=0}^{q} \beta_i \varepsilon_{t-i}, \sum_{j=0}^{q} \beta_j \varepsilon_{t+k-j}\right)$$

$$= \sum_{i=0}^{q} \sum_{j=0}^{q} \beta_i \beta_j \text{Cov}(\varepsilon_{t-i}, \varepsilon_{t+k-j})$$

**中文解释：** 现在，Cov(ε_{t-i}, ε_{t+k-j})只有在t-i = t+k-j时才非零（且等于σ²），即j = k+i。这意味着非零项出现在：

**English explanation:** Now, Cov(ε_{t-i}, ε_{t+k-j}) is only non-zero (and equals σ²) if t-i = t+k-j, i.e., j = k+i. This means there are non-zero terms for:

$$(i,j) = (0,k), (1,k+1), \ldots, (q-k, q)$$

因此 / Therefore:

$$\gamma_k = \begin{cases}
\sigma^2 \sum_{i=0}^{q-k} \beta_i \beta_{i+k} & \text{if } k \leq q \\
0 & \text{if } k > q
\end{cases}$$

**Key Result / 关键结果：**

**中文解释：** 显然，ACF不依赖于t，因此X_t是弱平稳的。此外，MA(q)过程的ACF在滞后q处"截尾"（cut off）——即当k > q时，γ_k = 0。这是MA过程的特殊性质，可以用来识别适合用MA模型描述的数据集。

**English explanation:** Obviously, the ACF does not depend on t, therefore X_t is weakly stationary. Moreover, the ACF of an MA(q) process "cuts off" at lag q — that is, when k > q, γ_k = 0. This is a special feature of MA processes and can be used to recognise data sets for which an MA process is suitable.

**Summary Table / 总结表：**

| Quantity | Formula | Notes |
|----------|---------|-------|
| Mean μ | 0 | Always zero for MA processes |
| Variance γ₀ | $(\beta_0^2 + \beta_1^2 + \cdots + \beta_q^2)\sigma^2$ | Sum of squared coefficients times noise variance |
| Autocovariance γ_k | $\sigma^2 \sum_{i=0}^{q-k} \beta_i \beta_{i+k}$ for k ≤ q; 0 for k > q | Cuts off after lag q |
| Autocorrelation ρ_k | γ_k / γ₀ | Also cuts off after lag q |

---

##### Example 4.1: Simulating MA Processes in R / 在R中模拟MA过程

**中文解释：** 考虑由以下R命令定义的过程X.series和Y.series。写出它们的数学表达式，绘制时间序列图和ACF图，并加以评论。

**English explanation:** Consider the processes X.series and Y.series defined by the following R commands. Write down their mathematical expressions, plot their time plot and acf plot, and comment.

```r
set.seed(123)
n <- 500
epsilon <- rnorm(n)
X.series <- epsilon[2:n] - 0.8*epsilon[1:(n-1)]
Y.series <- epsilon[3:n] + 0.4*epsilon[2:(n-1)] - 0.3*epsilon[1:(n-2)]
```

**Solution / 解答：**

**中文解释：** X.series是MA(1)过程，其数学表达式为：
$$X_t = \varepsilon_t - 0.8\varepsilon_{t-1}$$
其中ε_t ~ iid N(0, 1)。

Y.series是MA(2)过程，其数学表达式为：
$$Y_t = \varepsilon_t + 0.4\varepsilon_{t-1} - 0.3\varepsilon_{t-2}$$
其中ε_t ~ iid N(0, 1)。

**English explanation:** X.series is an MA(1) process with mathematical expression:
$$X_t = \varepsilon_t - 0.8\varepsilon_{t-1}$$
where ε_t ~ iid N(0, 1).

Y.series is an MA(2) process with mathematical expression:
$$Y_t = \varepsilon_t + 0.4\varepsilon_{t-1} - 0.3\varepsilon_{t-2}$$
where ε_t ~ iid N(0, 1).

**R code for plotting / 绘图R代码：**

```r
par(mfrow=c(2,2), mar=c(1,4,1,1))
plot(X.series, type="l", xlab="Time", ylab="X.series")
acf(X.series, xlab="Lag", ylab="ACF", main="acf of X.series")
plot(Y.series, type="l", xlab="Time", ylab="Y.series")
acf(Y.series, xlab="Lag", ylab="ACF", main="acf of Y.series")
```

**中文解释：** 从ACF图中我们可以看到，X.series的ACF在滞后1处截尾，Y.series的ACF在滞后2处截尾。这正是我们从自相关函数中预期的结果。

**English explanation:** From the ACF plots we can see, the ACF plot of X.series cuts off at lag 1 and that of Y.series cuts off at lag 2. This is what we expect from the autocorrelation function.

**Alternative R method / 另一种R方法：**

**中文解释：** 我们也可以使用R函数arima.sim()来模拟MA过程：

**English explanation:** We can also use the R function arima.sim() to simulate MA processes:

```r
set.seed(1234)
n <- 500
X.series.2 <- arima.sim(n, model=list(ma=c(-0.8)))
Y.series.2 <- arima.sim(n, model=list(ma=c(0.4, -0.3)))
par(mfrow=c(2,2), mar=c(1,4,1,1))
plot(X.series.2, type="l", xlab="Time", ylab="X.series.2")
acf(X.series.2, xlab="Lag", ylab="ACF")
plot(Y.series.2, type="l", xlab="Time", ylab="Y.series.2")
acf(Y.series.2, xlab="Lag", ylab="ACF")
```

**Note on arima.sim() / 关于arima.sim()的说明：**

**中文解释：** 在arima.sim()函数中，参数`ma=c(-0.8)`表示MA(1)模型X_t = ε_t - 0.8ε_{t-1}。注意：arima.sim()默认β₀ = 1，所以ma向量给出的是β₁, β₂, ..., β_q的值。

**English explanation:** In the arima.sim() function, the parameter `ma=c(-0.8)` represents the MA(1) model X_t = ε_t - 0.8ε_{t-1}. Note: arima.sim() defaults to β₀ = 1, so the ma vector gives the values of β₁, β₂, ..., β_q.

---

##### Example 4.2: Comparing MA and AR ACFs / 比较MA和AR的ACF

**中文解释：** 评论以下两个R生成的时间序列的ACF。

**English explanation:** Comment on the ACF of the following two time series generated in R.

```r
set.seed(123)
n <- 500
X.series.2 <- arima.sim(n, model=list(ma=c(-0.8)))
X2.ar1.2 <- arima.sim(n, model=list(ar=c(-0.8)))  # See example 3.2 in Chapter 2
par(mfrow=c(2,2), mar=c(1,4,1,1))
plot(X.series.2, type="l", xlab="Time", ylab="X.series.2")
acf(X.series.2, xlab="Lag", ylab="ACF")
plot(X2.ar1.2, type="l", xlab="Time", ylab="Series X2.ar1.2")
acf(X2.ar1.2, xlab="Lag", ylab="ACF")
```

**Solution / 解答：**

**中文解释：** 第一个过程是MA(1)过程，系数为-0.8，其ACF在滞后1处截尾。第二个过程是AR(1)过程，系数为-0.8，其ACF呈指数衰减且正负交替，但没有截尾现象。

**English explanation:** The first process is an MA(1) process with coefficient -0.8, its ACF cuts off at lag 1. The second process is an AR(1) process with coefficient -0.8, its ACF decays exponentially with alternating signs, but it does not have a cut-off phenomenon.

**Key distinction / 关键区别：**

| Feature | MA(q) | AR(p) |
|---------|-------|-------|
| ACF behavior | Cuts off after lag q | Decays exponentially (or damped sine wave) |
| PACF behavior | Decays exponentially | Cuts off after lag p |

---

#### 4.4 Invertibility / 可逆性

##### Motivation / 动机

**中文解释：** 对于有限阶的MA过程，不需要对系数{β_k}施加任何限制就能保证平稳性。但是，通常需要对{β_k}施加限制，以确保过程满足一个称为"可逆性"（invertibility）的条件。

**English explanation:** No restrictions on the {β_k} are required for a (finite-order) MA process to be stationary, but it is generally desirable to impose restrictions on the {β_k} to ensure that the process satisfies a condition called invertibility.

##### The MA(1) Case / MA(1)情况

**中文解释：** 让我们从MA(1)过程开始。从上一小节我们知道，MA(1)过程的ACF为：

**English explanation:** Let's start with the MA(1) process. From the previous subsection, we have seen that MA(1) has:

$$\rho_0 = 1, \quad \rho_1 = \frac{\beta_1}{1 + \beta_1^2}, \quad \rho_k = 0 \text{ for } k \geq 2$$

假设我们观测到了ρ₁（或者我们可以从样本中计算出ρ₁），想要确定β₁：

**中文解释：** 假设我们观测到了ρ₁，想要确定β₁。从ρ₁ = β₁/(1+β₁²)，我们可以解出β₁：

**English explanation:** Assume we have observed ρ₁ (or we can calculate ρ₁ from a sample) and want to determine β₁. From ρ₁ = β₁/(1+β₁²), we can solve for β₁:

$$\rho_1 = \frac{\beta_1}{1 + \beta_1^2}$$

$$\beta_1^2 \rho_1 - \beta_1 + \rho_1 = 0$$

$$\beta_1 = \frac{1 \pm \sqrt{1 - 4\rho_1^2}}{2\rho_1}$$

**Key insight / 关键洞察：**

**中文解释：** 所以存在两个MA(1)过程具有相同的自相关函数！这个问题被称为"可逆性"问题。

**English explanation:** So there are two MA(1) processes with the same autocorrelation function! This problem is referred to as "invertibility".

##### Resolving the Ambiguity / 解决歧义

**中文解释：** 为了做出选择，回忆我们可以将X_t写成X_t = (1 + β₁B)ε_t，其中B是后移算子。因此：

**English explanation:** To motivate a choice, recall that we can write X_t as X_t = (1 + β₁B)ε_t where B is the backshift operator. Therefore, we have:

$$\varepsilon_t = (1 + \beta_1 B)^{-1} X_t$$

$$= (1 - \beta_1 B + \beta_1^2 B^2 - \beta_1^3 B^3 + \cdots) X_t$$

$$= X_t - \beta_1 X_{t-1} + \beta_1^2 X_{t-2} - \beta_1^3 X_{t-3} + \cdots$$

所以 / So:

$$X_t = \beta_1 X_{t-1} - \beta_1^2 X_{t-2} + \beta_1^3 X_{t-3} - \cdots + \varepsilon_t$$

**中文解释：** 因此，X_t可以看作是一个AR(∞)表示。这在什么时候有意义呢？

**English explanation:** So, X_t can be seen as an AR(∞) representation. When does this make sense?

**Case 1:** |β₁| > 1 — 遥远的过去比最近的过去有更大的影响 / distant (infinite) past has more influence than the recent past.

**Case 2:** |β₁| < 1 — 过去的影响呈指数衰减 / past influence decays exponentially.

**中文解释：** 情况1是不现实的，所以要求|β₁| < 1似乎是合理的。这个条件称为可逆性。

**English explanation:** Case 1 is unrealistic so requiring |β₁| < 1 seems sensible. This condition is called invertibility.

##### Formal Definition / 形式化定义

**中文解释：** 实际上，如果|β₁| < 1，X_{t-j}的系数级数收敛。更一般地，一个过程{X_t}被称为可逆的，如果ε_t可以写成X_t, t < s的收敛和，即：

**English explanation:** Actually, if |β₁| < 1, the series of coefficients of X_{t-j} converges. More generally, a process {X_t} is said to be invertible if ε_t can be written as a convergent sum of X_t, t < s, i.e.:

$$\varepsilon_t = \sum_{j=0}^{\infty} \pi_j X_{t-j}$$

其中 $\sum_{j=0}^{\infty} |\pi_j| < \infty$。

**中文解释：** 这意味着MA过程可以写成AR过程的形式，其系数构成一个收敛和。施加可逆性条件确保对于给定的自相关函数，存在唯一的可逆MA过程。

**English explanation:** This means that the MA processes can be written in the form of an AR process whose coefficients form a convergent sum. The imposition of the invertibility condition ensures that there is a unique invertible MA process for a given autocorrelation