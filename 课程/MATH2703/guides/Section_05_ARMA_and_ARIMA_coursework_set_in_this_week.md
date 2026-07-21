# Section 5: ARMA and ARIMA (coursework set in this week)

> MATH2703 - 自学教材 / Self-Study Guide
> 生成时间: 2026-07-21 11:10
> 来源页: 41-48

---

# MATH2703: Time Series Analysis / 时间序列分析

## Chapter 5: ARMA and ARIMA Models / ARMA与ARIMA模型

---

### 📋 Section Overview / 章节概览

**中文解释：** 本章我们将学习两种重要的时间序列模型：ARMA（自回归移动平均）模型和ARIMA（差分自回归移动平均）模型。ARMA模型结合了前面章节学习的AR（自回归）和MA（移动平均）模型的特点，能够更灵活地描述平稳时间序列。而ARIMA模型则通过差分操作，将非平稳时间序列转化为平稳序列后再进行建模，极大地扩展了我们的建模能力。

**English explanation:** In this chapter, we will study two important time series models: ARMA (Autoregressive Moving Average) models and ARIMA (Autoregressive Integrated Moving Average) models. ARMA models combine the characteristics of AR (autoregressive) and MA (moving average) models learned in previous chapters, providing more flexibility in describing stationary time series. ARIMA models, through differencing operations, transform non-stationary time series into stationary ones before modeling, greatly expanding our modeling capabilities.

---

### 🎯 Learning Objectives / 学习目标

完成本章学习后，你应该能够 / After completing this chapter, you should be able to:

1. **理解ARMA模型的定义和结构** / Understand the definition and structure of ARMA models
2. **判断ARMA模型的平稳性和可逆性条件** / Determine stationarity and invertibility conditions for ARMA models
3. **推导ARMA模型的自相关函数（ACF）** / Derive the autocorrelation function (ACF) for ARMA models
4. **理解差分操作和ARIMA模型** / Understand differencing operations and ARIMA models
5. **使用R语言模拟和可视化ARMA/ARIMA过程** / Simulate and visualize ARMA/ARIMA processes using R
6. **识别实际数据中的非平稳性并应用差分** / Identify non-stationarity in real data and apply differencing

---

### 📚 Prerequisites / 前置知识

在学习本章之前，你需要掌握 / Before studying this chapter, you need to master:

- **Chapter 3: AR模型** - 自回归模型的定义、平稳性条件、ACF性质
- **Chapter 4: MA模型** - 移动平均模型的定义、可逆性条件、ACF性质
- **白噪声过程（White noise process）** - 均值为0、方差为常数、无自相关的随机过程
- **后移算子（Backshift operator）B** - BX_t = X_{t-1}
- **基本R编程技能** - 模拟、绘图函数

---

### 📖 Core Content / 核心内容

---

#### 5.1 Introduction / 引言

##### Intuition / 直觉理解

**中文解释：** 在第二章中我们提到，许多随机过程的模型都可以通过一个代数公式来表达，这个公式将当前时刻t的随机变量与过去的值以及一个不可观测的"误差"过程联系起来。白噪声过程通常用来描述这个"误差"过程。在第三章和第四章中，我们分别考虑了当前时刻的值依赖于过去的值（AR模型）和依赖于当前及过去的误差（MA模型）。现在，我们将这两者结合起来，得到ARMA模型。

让我们用一个直观的例子来理解ARMA过程：想象一个房间，里面有一个恒温器试图将温度保持在20°C附近。如果昨天很暖和，今天仍然会有些暖和；如果昨天很冷，今天仍然会有些冷。随机误差可能来自开窗、阳光照射等。今天可能受到今天开窗的影响，但也可能受到昨天开窗的影响。这种关系可以表示为：

**今天 = 昨天的一部分 + 今天的随机误差 + 昨天随机误差的一部分**

**English explanation:** In Chapter 2, we mentioned that many models for stochastic processes are expressed by means of an algebraic formula relating the random variable at time t to past values of the process, together with values of an unobservable "error" process. The white noise process is usually used to describe the "error" process. In Chapter 3 and Chapter 4, we considered the random variable at t (say today) depends on its past values (AR) and today's and the past values of the unobservable "error" process (MA). In this chapter, we consider a mixed version of these two, that is Autoregressive Moving Average (ARMA) model.

An intuitive example for ARMA process might be the room temperature example. Imagine a room with a thermostat that tries to keep the temperature near 20°C. If yesterday was warm, today will still be somewhat warm. If yesterday was cold, today will still be somewhat cold. Random error might come from opening a window, sunlight, etc. Today might be influenced by opening a window today, but might also be influenced by opening a window yesterday. This follows the relation that:

**today = a fraction of yesterday + a random error today + a fraction of a random error yesterday**

---

#### 5.2 ARMA Models / ARMA模型

##### Formal Definition / 形式化定义

**Definition 5.1 (ARMA processes / ARMA过程)** The ARMA(p, q) model satisfies:

$$X_t = \sum_{i=1}^{p} a_i X_{t-i} + \varepsilon_t + \sum_{j=1}^{q} \beta_j \varepsilon_{t-j}$$

with $\varepsilon_t$ to be white noise and independent of $X_{t-1}, X_{t-2}, \ldots$.

**中文解释：** 这个公式表示当前时刻t的观测值X_t由三部分组成：
1. **自回归部分（AR部分）**：$\sum_{i=1}^{p} a_i X_{t-i}$ - 过去p个观测值的线性组合
2. **当前误差**：$\varepsilon_t$ - 当前时刻的白噪声
3. **移动平均部分（MA部分）**：$\sum_{j=1}^{q} \beta_j \varepsilon_{t-j}$ - 过去q个误差的线性组合

其中p是自回归的阶数，q是移动平均的阶数。

**English explanation:** This formula shows that the current observation X_t consists of three parts:
1. **Autoregressive part (AR part)**: $\sum_{i=1}^{p} a_i X_{t-i}$ - linear combination of past p observations
2. **Current error**: $\varepsilon_t$ - white noise at current time
3. **Moving average part (MA part)**: $\sum_{j=1}^{q} \beta_j \varepsilon_{t-j}$ - linear combination of past q errors

where p is the order of autoregression and q is the order of moving average.

**Symbol Table / 符号表：**

| Symbol | Meaning / 含义 |
|--------|----------------|
| $X_t$ | Observation at time t / 时刻t的观测值 |
| $a_i$ | AR coefficients / 自回归系数 |
| $\beta_j$ | MA coefficients / 移动平均系数 |
| $\varepsilon_t$ | White noise at time t / 时刻t的白噪声 |
| $p$ | Order of AR part / 自回归阶数 |
| $q$ | Order of MA part / 移动平均阶数 |

##### Backshift Operator Representation / 后移算子表示

**中文解释：** 使用后移算子B，ARMA模型可以写成更简洁的形式。后移算子B的作用是：$BX_t = X_{t-1}$。

**English explanation:** Using the backshift operator B, the ARMA model can be written in a more compact form. The backshift operator B works as: $BX_t = X_{t-1}$.

**Remarks / 注释：**

1. **Using the backshift operator / 使用后移算子：** The equation in the above definition can be written as:

$$a(B)X_t = \beta(B)\varepsilon_t$$

where

$$a(y) = 1 - \sum_{i=1}^{p} a_i y^i, \quad \beta(y) = 1 + \sum_{j=1}^{q} \beta_j y^j$$

are the **AR polynomial (AR多项式)** and **MA polynomial (MA多项式)** respectively.

**中文解释：** 这里$a(B)$和$\beta(B)$是算子多项式。注意AR多项式的形式是$1 - \sum a_i B^i$，而MA多项式的形式是$1 + \sum \beta_j B^j$。这种符号约定在时间序列分析中是标准的。

**English explanation:** Here $a(B)$ and $\beta(B)$ are operator polynomials. Note that the AR polynomial takes the form $1 - \sum a_i B^i$, while the MA polynomial takes the form $1 + \sum \beta_j B^j$. This sign convention is standard in time series analysis.

2. **Stationarity condition / 平稳性条件：** For the stationarity, as for the AR(p) processes, we can write:

$$X_t = a(B)^{-1}\beta(B)\varepsilon_t$$

The model is stationary if:

$$X_t = \sum_{k=0}^{\infty} c_k \varepsilon_{t-k}$$

with $\sum_{k=0}^{\infty} |c_k| < \infty$. This is equivalent to the roots of $a(y)$ lying outside the complex unit circle.

**中文解释：** 平稳性条件要求AR多项式的所有根的模都大于1（即根在单位圆外）。这是因为如果AR多项式有单位根（模等于1）或爆炸根（模小于1），那么$X_t$的方差会随时间增长或爆炸。

**English explanation:** The stationarity condition requires that all roots of the AR polynomial have modulus greater than 1 (i.e., roots lie outside the unit circle). This is because if the AR polynomial has a unit root (modulus = 1) or explosive root (modulus < 1), then the variance of $X_t$ would grow or explode over time.

3. **Invertibility condition / 可逆性条件：** For the invertibility, as for the MA(q) processes, we can reconstruct the noise as:

$$\varepsilon_t = \beta(B)^{-1}a(B)X_t = \sum_{k=0}^{\infty} d_k X_{t-k}$$

We need $\sum_{k=0}^{\infty} |d_k| < \infty$ for invertibility, and this is again equivalent to the roots of $\beta(y)$ lying outside the complex unit circle.

**中文解释：** 可逆性条件要求MA多项式的所有根的模都大于1。可逆性意味着我们可以从观测值$X_t$唯一地重建出误差序列$\varepsilon_t$。这对于模型识别和参数估计非常重要。

**English explanation:** The invertibility condition requires that all roots of the MA polynomial have modulus greater than 1. Invertibility means we can uniquely reconstruct the error sequence $\varepsilon_t$ from the observations $X_t$. This is important for model identification and parameter estimation.

---

##### Worked Example 5.1 / 例题5.1

**Problem / 问题：** Consider the ARMA(1,1) process:

$$X_t = aX_{t-1} + \varepsilon_t + \beta\varepsilon_{t-1}$$

Write down the AR polynomial and MA polynomial. Under what conditions is it stationary? Under what conditions is it invertible?

**Solution / 解答：**

**Step 1: Identify the polynomials / 步骤1：识别多项式**

**中文解释：** 首先，我们需要将模型写成标准形式。注意ARMA(1,1)意味着p=1, q=1。比较定义式$X_t = a_1 X_{t-1} + \varepsilon_t + \beta_1 \varepsilon_{t-1}$，我们有$a_1 = a$和$\beta_1 = \beta$。

**English explanation:** First, we need to write the model in standard form. Note that ARMA(1,1) means p=1, q=1. Comparing with the definition $X_t = a_1 X_{t-1} + \varepsilon_t + \beta_1 \varepsilon_{t-1}$, we have $a_1 = a$ and $\beta_1 = \beta$.

AR polynomial is / AR多项式为：

$$a(y) = 1 - a_1 y = 1 - ay$$

MA polynomial is / MA多项式为：

$$\beta(y) = 1 + \beta_1 y = 1 + \beta y$$

**Step 2: Stationarity condition / 步骤2：平稳性条件**

**中文解释：** 平稳性条件要求AR多项式$a(y)=0$的根在单位圆外。解方程$1 - ay = 0$，得到根为$y = 1/a$。要求$|1/a| > 1$，即$|a| < 1$。

**English explanation:** The stationarity condition requires that the root of $a(y)=0$ lies outside the unit circle. Solving $1 - ay = 0$, we get the root $y = 1/a$. We require $|1/a| > 1$, which means $|a| < 1$.

**The condition for stationarity is / 平稳性条件为：** $|a| < 1$

**Step 3: Invertibility condition / 步骤3：可逆性条件**

**中文解释：** 可逆性条件要求MA多项式$\beta(y)=0$的根在单位圆外。解方程$1 + \beta y = 0$，得到根为$y = -1/\beta$。要求$|-1/\beta| > 1$，即$|\beta| < 1$。

**English explanation:** The invertibility condition requires that the root of $\beta(y)=0$ lies outside the unit circle. Solving $1 + \beta y = 0$, we get the root $y = -1/\beta$. We require $|-1/\beta| > 1$, which means $|\beta| < 1$.

**The condition for invertibility is / 可逆性条件为：** $|\beta| < 1$

**Summary / 总结：**

| Condition / 条件 | Mathematical Expression / 数学表达 | Interpretation / 解释 |
|------------------|-----------------------------------|----------------------|
| Stationarity / 平稳性 | $|a| < 1$ | AR coefficient must be less than 1 in absolute value / AR系数的绝对值小于1 |
| Invertibility / 可逆性 | $|\beta| < 1$ | MA coefficient must be less than 1 in absolute value / MA系数的绝对值小于1 |

---

#### 5.3 ACF of ARMA Processes / ARMA过程的自相关函数

##### Derivation / 推导

**中文解释：** 对于ARMA(p,q)过程，我们可以推导出自协方差函数（ACVF）和自相关函数（ACF）的表达式。自协方差函数定义为$\gamma_k = \text{cov}(X_t, X_{t+k})$。

**English explanation:** For an ARMA(p,q) process, we can derive expressions for the autocovariance function (ACVF) and autocorrelation function (ACF). The autocovariance function is defined as $\gamma_k = \text{cov}(X_t, X_{t+k})$.

**Derivation / 推导过程：**

For an ARMA(p,q) process, we have:

$$\gamma_k = \text{cov}(X_t, X_{t+k})$$

$$= \text{cov}\left(X_t, \sum_{i=1}^{p} a_i X_{t+k-i} + \varepsilon_{t+k} + \sum_{j=1}^{q} \beta_j \varepsilon_{t+k-j}\right)$$

$$= \sum_{i=1}^{p} a_i \text{cov}(X_t, X_{t+k-i}) + \text{cov}(X_t, \varepsilon_{t+k}) + \sum_{j=1}^{q} \beta_j \text{cov}(X_t, \varepsilon_{t+k-j})$$

**中文解释：** 这里的关键观察是：
- $\text{cov}(X_t, \varepsilon_{t+k}) = 0$ 对于 $k > 0$，因为$\varepsilon_{t+k}$与$X_t$独立（$\varepsilon$是未来的噪声，与过去的观测独立）
- $\text{cov}(X_t, \varepsilon_{t+k-j}) = 0$ 对于 $k > q$，因为当滞后足够大时，误差项与当前观测不相关

**English explanation:** The key observations here are:
- $\text{cov}(X_t, \varepsilon_{t+k}) = 0$ for $k > 0$, because $\varepsilon_{t+k}$ is independent of $X_t$ (future noise is independent of past observations)
- $\text{cov}(X_t, \varepsilon_{t+k-j}) = 0$ for $k > q$, because when the lag is large enough, the error term is uncorrelated with the current observation

Therefore, for $k > q$:

$$\gamma_k = \sum_{i=1}^{p} a_i \gamma_{k-i}$$

And dividing by $\gamma_0$ (the variance), we get:

$$\rho_k = \sum_{i=1}^{p} a_i \rho_{k-i} \quad \text{for } k > q$$

**中文解释：** 这个结果非常重要！它表明对于ARMA(p,q)过程，当滞后k大于q时，ACF满足与AR(p)过程相同的差分方程。这意味着ARMA过程的ACF在尾部（k>q）表现出与AR过程类似的行为——指数衰减或阻尼正弦波。

**English explanation:** This result is very important! It shows that for an ARMA(p,q) process, when the lag k is greater than q, the ACF satisfies the same difference equation as the AR(p) process. This means that the ACF of an ARMA process exhibits similar behavior to the AR process in the tail (k>q) - exponential decay or damped sine waves.

**Key insight / 关键洞察：**
- AR(p) ACF: satisfies $\rho_k = \sum a_i \rho_{k-i}$ for ALL $k > 0$
- ARMA(p,q) ACF: satisfies $\rho_k = \sum a_i \rho_{k-i}$ for $k > q$
- The first q lags of ACF are "contaminated" by the MA part

---

##### Worked Example 5.2 / 例题5.2

**Problem / 问题：** Derive the autocorrelation function for ARMA(1,1) process i.e.

$$X_t = aX_{t-1} + \varepsilon_t + \beta\varepsilon_{t-1}$$

where $\varepsilon_t$ are i.i.d. with $E[\varepsilon_t] = 0$ and $\text{var}(\varepsilon_t) = \sigma^2$, and $\varepsilon_t$ independent of $X_{t-1}, X_{t-2}, \ldots$

**Solution / 解答：**

**中文解释：** 我们需要推导ARMA(1,1)过程的ACF。这需要计算自协方差$\gamma_k = \text{cov}(X_t, X_{t+k})$，然后标准化得到$\rho_k = \gamma_k/\gamma_0$。

**English explanation:** We need to derive the ACF of the ARMA(1,1) process. This requires computing the autocovariance $\gamma_k = \text{cov}(X_t, X_{t+k})$, then standardizing to get $\rho_k = \gamma_k/\gamma_0$.

**Step 1: Find the variance $\gamma_0$ / 步骤1：求方差$\gamma_0$**

**中文解释：** 首先，将模型写成无穷MA形式。对于ARMA(1,1)，我们可以展开为：

$$X_t = \sum_{k=0}^{\infty} c_k \varepsilon_{t-k}$$

其中$c_k$是待定系数。通过比较系数法可以求得$c_k$。

**English explanation:** First, write the model in infinite MA form. For ARMA(1,1), we can expand as:

$$X_t = \sum_{k=0}^{\infty} c_k \varepsilon_{t-k}$$

where $c_k$ are coefficients to be determined. We can find $c_k$ by comparing coefficients.

From the ARMA(1,1) equation:
$$X_t = aX_{t-1} + \varepsilon_t + \beta\varepsilon_{t-1}$$

Substituting the MA representation:
$$\sum_{k=0}^{\infty} c_k \varepsilon_{t-k} = a\sum_{k=0}^{\infty} c_k \varepsilon_{t-1-k} + \varepsilon_t + \beta\varepsilon_{t-1}$$

Comparing coefficients of $\varepsilon_t$: $c_0 = 1$
Comparing coefficients of $\varepsilon_{t-1}$: $c_1 = ac_0 + \beta = a + \beta$
Comparing coefficients of $\varepsilon_{t-k}$ for $k \geq 2$: $c_k = ac_{k-1}$

Therefore:
$$c_k = a^{k-1}(a + \beta) \quad \text{for } k \geq 1$$

**Step 2: Compute $\gamma_0$ / 步骤2：计算$\gamma_0$**

$$\gamma_0 = \text{var}(X_t) = \sum_{k=0}^{\infty} c_k^2 \sigma^2 = \sigma^2\left(1 + \sum_{k=1}^{\infty} a^{2(k-1)}(a+\beta)^2\right)$$

$$= \sigma^2\left(1 + \frac{(a+\beta)^2}{1-a^2}\right) = \sigma^2\frac{1 + 2a\beta + \beta^2}{1-a^2}$$

**Step 3: Compute $\gamma_1$ / 步骤3：计算$\gamma_1$**

$$\gamma_1 = \text{cov}(X_t, X_{t+1}) = E[X_t X_{t+1}]$$

Using the MA representation:
$$\gamma_1 = \text{cov}\left(\sum_{k=0}^{\infty} c_k \varepsilon_{t-k}, \sum_{l=0}^{\infty} c_l \varepsilon_{t+1-l}\right)$$

$$= \sigma^2\sum_{k=0}^{\infty} c_k c_{k+1} = \sigma^2\left(c_0 c_1 + \sum_{k=1}^{\infty} c_k c_{k+1}\right)$$

$$= \sigma^2\left((a+\beta) + \sum_{k=1}^{\infty} a^{2k-1}(a+\beta)^2\right)$$

$$= \sigma^2\left((a+\beta) + \frac{a(a+\beta)^2}{1-a^2}\right)$$

$$= \sigma^2\frac{(a+\beta)(1+a\beta)}{1-a^2}$$

**Step 4: Compute $\rho_1$ / 步骤4：计算$\rho_1$**

$$\rho_1 = \frac{\gamma_1}{\gamma_0} = \frac{(a+\beta)(1+a\beta)}{1+2a\beta+\beta^2}$$

**Step 5: Compute $\rho_k$ for $k > 1$ / 步骤5：计算$k>1$时的$\rho_k$**

**中文解释：** 对于k>1，我们可以使用之前推导的性质：对于ARMA(1,1)，当k>q=1时，ACF满足AR(1)的差分方程$\rho_k = a\rho_{k-1}$。

**English explanation:** For k>1, we can use the property derived earlier: for ARMA(1,1), when k>q=1, the ACF satisfies the AR(1) difference equation $\rho_k = a\rho_{k-1}$.

Therefore:

$$\rho_k = a^{k-1}\rho_1 = \frac{(a+\beta)(1+a\beta)}{1+2a\beta+\beta^2} a^{k-1} \quad \text{for } k \geq 1$$

**Final result / 最终结果：**

$$\rho_1 = \frac{(a+\beta)(1+a\beta)}{1+2a\beta+\beta^2}$$

$$\rho_k = \frac{(a+\beta)(1+a\beta)}{1+2a\beta+\beta^2} a^{k-1} \quad \text{for } k \geq 1$$

**中文解释：** 注意这个结果告诉我们ARMA(1,1)的ACF从滞后1开始就呈指数衰减（如果|a|<1），衰减速度由AR系数a决定。这与AR(1)过程不同，AR(1)的ACF从滞后0开始就呈指数衰减。

**English explanation:** Note that this result tells us that the ACF of ARMA(1,1) decays exponentially from lag 1 (if |a|<1), with the decay rate determined by the AR coefficient a. This differs from the AR(1) process, whose ACF decays exponentially from lag 0.

---

##### Worked Example 5.3 / 例题5.3

**Problem / 问题：** Consider the processes X.series and Y.series defined by the following R commands. Write down their mathematical expressions. Plot their time plot and acf plot and comment.

```r
set.seed(123)
n <- 100
X.series <- arima.sim(n=n, list(order = c(1,0,1), ar = 0.6, ma=0.8))
Y.series <- arima.sim(n=n, list(order = c(1,0,1), ar = -0.6, ma=-0.8))
```

**Solution / 解答：**

**Step 1: Mathematical expressions / 步骤1：数学表达式**

**中文解释：** `arima.sim`函数中的`order = c(1,0,1)`表示ARIMA(1,0,1)，即ARMA(1,1)。`ar = 0.6`是AR系数，`ma = 0.8`是MA系数。

**English explanation:** The `order = c(1,0,1)` in the `arima.sim` function means ARIMA(1,0,1), which is ARMA(1,1). `ar = 0.6` is the AR coefficient, `ma = 0.8` is the MA coefficient.

**X.series:** $X_t = 0.6X_{t-1} + \varepsilon_t + 0.8\varepsilon_{t-1}$ where $\varepsilon_t \sim \text{i.i.d. } N(0, 1)$

**Y.series:** $Y_t = -0.6Y_{t-1} + \varepsilon_t - 0.8\varepsilon_{t-1}$ where $\varepsilon_t \sim \text{i.i.d. } N(0, 1)$

**Step 2: R code for plotting / 步骤2：绘图R代码**

```r
par(mfrow=c(2,2), mar=c(4,4,4,4))
plot(X.series, type="l", xlab="Time", ylab="Series X.series")
acf(X.series, xlab="Lag", ylab="ACF", main="acf of X.series")
plot(Y.series, type="l", xlab="Time", ylab="Series Y.series")
acf(Y.series, xlab="Lag", ylab