# Section 9: Real data analysis example

> MATH2703 - 自学教材 / Self-Study Guide
> 生成时间: 2026-07-21 11:13
> 来源页: 83-87

---

# MATH2703: Time Series Analysis / 时间序列分析

## Section 8.4-9.2: Forecasting and Real Data Analysis / 预测与真实数据分析

---

### 📋 Section Overview / 章节概览

**中文解释：** 本章节分为两个主要部分。第一部分（第8.4节）继续讨论AR(1)模型的预测问题，特别是如何计算条件均值和条件方差，以及如何构建预测区间。第二部分（第9章）转向实际数据分析，以美国月度失业率数据为例，展示如何将前面学到的ARIMA模型理论应用到真实数据中。第9章的内容虽然不在期末考试范围内，但会在课程作业中考察。

**English explanation:** This section is divided into two main parts. The first part (Section 8.4) continues the discussion of forecasting for AR(1) models, specifically how to compute conditional means and conditional variances, and how to construct prediction intervals. The second part (Chapter 9) transitions to real data analysis, using US monthly unemployment rate data as an example to demonstrate how to apply the ARIMA model theory learned earlier to real data. Although Chapter 9 content is not examinable in the final exam, it will be examined in the coursework.

---

### 🎯 Learning Objectives / 学习目标

After completing this section, you should be able to / 完成本节后，你应该能够：

1. **Compute conditional expectations and variances for AR(1) forecasts** / 计算AR(1)预测的条件期望和条件方差
2. **Construct 95% prediction intervals for AR(1) forecasts** / 构建AR(1)预测的95%预测区间
3. **Understand the four main stages of time series modeling** / 理解时间序列建模的四个主要阶段
4. **Apply the Box-Jenkins methodology to real data** / 将Box-Jenkins方法应用于真实数据
5. **Interpret ACF and PACF plots for model identification** / 解读ACF和PACF图以进行模型识别
6. **Use AIC for model selection** / 使用AIC进行模型选择

---

### 📚 Prerequisites / 前置知识

**中文解释：** 在学习本节之前，你应该已经掌握了以下内容：
- AR(1)模型的定义和性质（第8章前面部分）
- 条件期望和条件方差的概念
- 正态分布和预测区间的构建
- ACF（自相关函数）和PACF（偏自相关函数）的基本概念（第7章）
- ARIMA模型的基本框架（第3-5章）

**English explanation:** Before studying this section, you should already have mastered:
- The definition and properties of AR(1) models (earlier parts of Chapter 8)
- Concepts of conditional expectation and conditional variance
- Normal distribution and construction of prediction intervals
- Basic concepts of ACF (Autocorrelation Function) and PACF (Partial Autocorrelation Function) (Chapter 7)
- Basic framework of ARIMA models (Chapters 3-5)

---

### 📖 Core Content / 核心内容

---

#### Topic 1: Forecasting with AR(1) Models / AR(1)模型的预测

##### Intuition / 直觉理解

**中文解释：** 在AR(1)模型中，我们假设当前值只依赖于前一个值和一个随机扰动。当我们进行预测时，我们需要考虑两个问题：预测的最佳估计值是什么（条件期望），以及这个预测有多不确定（条件方差）。随着预测步长的增加，预测会逐渐趋向于过程的长期均值，而预测的不确定性也会增加。

**English explanation:** In an AR(1) model, we assume that the current value depends only on the previous value and a random disturbance. When we make forecasts, we need to consider two questions: what is the best estimate of the forecast (conditional expectation), and how uncertain is this forecast (conditional variance). As the forecast horizon increases, the forecast gradually converges to the long-term mean of the process, and the forecast uncertainty increases.

##### Formal Definition / 形式化定义

**中文解释：** 考虑AR(1)模型：
$$X_{n+1} = aX_n + \varepsilon_{n+1}$$

其中 $\varepsilon_t$ 是白噪声，方差为 $\sigma^2$。我们想要基于当前信息 $X_n$ 预测未来的值 $X_{n+h}$。

**English explanation:** Consider the AR(1) model:
$$X_{n+1} = aX_n + \varepsilon_{n+1}$$

where $\varepsilon_t$ is white noise with variance $\sigma^2$. We want to forecast future values $X_{n+h}$ based on current information $X_n$.

**Symbol Table / 符号表：**

| Symbol | Chinese | English |
|--------|---------|---------|
| $X_n$ | 当前观测值 | Current observation |
| $a$ | AR系数 | AR coefficient |
| $\varepsilon_t$ | 白噪声误差 | White noise error |
| $\sigma^2$ | 误差方差 | Error variance |
| $h$ | 预测步长 | Forecast horizon |

##### Key Properties / 关键性质

**1. One-step-ahead forecast / 一步预测**

**中文解释：** 对于一步预测（h=1），条件期望为：
$$E[X_{n+1}|X_n] = E[aX_n + \varepsilon_{n+1}|X_n] = aX_n$$

条件方差为：
$$var(X_{n+1}|X_n) = var(aX_n + \varepsilon_{n+1}|X_n) = \sigma^2$$

**English explanation:** For one-step-ahead forecast (h=1), the conditional expectation is:
$$E[X_{n+1}|X_n] = E[aX_n + \varepsilon_{n+1}|X_n] = aX_n$$

The conditional variance is:
$$var(X_{n+1}|X_n) = var(aX_n + \varepsilon_{n+1}|X_n) = \sigma^2$$

**2. Two-step-ahead forecast / 两步预测**

**中文解释：** 对于两步预测（h=2），我们需要先写出 $X_{n+2}$ 的表达式：
$$X_{n+2} = aX_{n+1} + \varepsilon_{n+2} = a(aX_n + \varepsilon_{n+1}) + \varepsilon_{n+2} = a^2X_n + a\varepsilon_{n+1} + \varepsilon_{n+2}$$

条件期望为：
$$E[X_{n+2}|X_n] = a^2X_n$$

条件方差为：
$$var(X_{n+2}|X_n) = a^2\sigma^2 + \sigma^2 = (1 + a^2)\sigma^2$$

**English explanation:** For two-step-ahead forecast (h=2), we first write $X_{n+2}$ in terms of $X_n$:
$$X_{n+2} = aX_{n+1} + \varepsilon_{n+2} = a(aX_n + \varepsilon_{n+1}) + \varepsilon_{n+2} = a^2X_n + a\varepsilon_{n+1} + \varepsilon_{n+2}$$

The conditional expectation is:
$$E[X_{n+2}|X_n] = a^2X_n$$

The conditional variance is:
$$var(X_{n+2}|X_n) = a^2\sigma^2 + \sigma^2 = (1 + a^2)\sigma^2$$

**3. General h-step-ahead forecast / 一般h步预测**

**中文解释：** 对于一般的h步预测，条件期望为：
$$E[X_{n+h}|X_n] = a^h X_n$$

条件方差为：
$$var(X_{n+h}|X_n) = (1 + a^2 + a^4 + \cdots + a^{2(h-1)})\sigma^2$$

注意：当 $|a| < 1$ 时，随着 $h \to \infty$，条件期望 $a^h X_n \to 0$（假设均值为0），条件方差趋近于无条件方差 $\frac{\sigma^2}{1-a^2}$。

**English explanation:** For general h-step-ahead forecast, the conditional expectation is:
$$E[X_{n+h}|X_n] = a^h X_n$$

The conditional variance is:
$$var(X_{n+h}|X_n) = (1 + a^2 + a^4 + \cdots + a^{2(h-1)})\sigma^2$$

Note: When $|a| < 1$, as $h \to \infty$, the conditional expectation $a^h X_n \to 0$ (assuming zero mean), and the conditional variance approaches the unconditional variance $\frac{\sigma^2}{1-a^2}$.

##### Prediction Interval / 预测区间

**中文解释：** 假设误差项 $\varepsilon_t$ 服从正态分布，那么 $X_{n+h}$ 的条件分布也是正态的。因此，95%的预测区间为：
$$a^h X_n \pm 1.96 \times \sqrt{var(X_{n+h}|X_n)}$$

对于一步预测（h=1）：
$$aX_n \pm 1.96\sigma$$

**English explanation:** Assuming the error terms $\varepsilon_t$ are normally distributed, the conditional distribution of $X_{n+h}$ is also normal. Therefore, the 95% prediction interval is:
$$a^h X_n \pm 1.96 \times \sqrt{var(X_{n+h}|X_n)}$$

For one-step-ahead forecast (h=1):
$$aX_n \pm 1.96\sigma$$

**重要说明 / Important Note：**

**中文解释：** 对于长期预测（h很大时），预测的均值和方差会趋近于平稳过程的无条件均值和方差。这意味着数据不再提供额外的信息，预测区间会变得很宽。对于正态分布的误差项，基于模型的预测和最小均方误差（MMSE）预测会得到相同的结果。

**English explanation:** For long-term forecasts (large h), the forecast mean and variance converge to the unconditional mean and variance of the stationary process. This means the data no longer provide additional information, and the prediction intervals become wide. For normally distributed errors, model-based forecasts and MMSE (Minimum Mean Square Error) forecasts yield the same results.

---

#### Topic 2: Real Life Data Analysis / 真实数据分析

##### Intuition / 直觉理解

**中文解释：** 在实际应用中，我们很少知道数据的真实生成过程。因此，我们需要通过数据来识别合适的模型。Box-Jenkins方法提供了一套系统的步骤：模型识别、参数估计、诊断检验和预测。这个过程是迭代的——如果诊断检验发现模型不合适，我们需要回到第一步重新选择模型。

**English explanation:** In practical applications, we rarely know the true data generating process. Therefore, we need to identify an appropriate model from the data. The Box-Jenkins methodology provides a systematic procedure: model identification, parameter estimation, diagnostic checking, and forecasting. This process is iterative — if diagnostic checking reveals that the model is inadequate, we need to return to the first step and reselect the model.

##### The Four Stages of Time Series Modeling / 时间序列建模的四个阶段

**中文解释：** 建立最小均方误差预测模型的主要步骤如下：

**Stage 1: Model Identification / 阶段1：模型识别**

1. **去除趋势和季节效应**：如果数据中存在趋势或季节效应，首先使用线性回归（R命令：`lm()`）去除它们。
2. **识别ARIMA模型**：检查去除趋势和/或季节效应后的数据，通过ACF和PACF图（R命令：`acf()`, `pacf()`）判断最适合的ARIMA过程类型。

**Stage 2: Estimation / 阶段2：参数估计**

估计所选模型的参数（R命令：`ar()`, `arima()`）。

**Stage 3: Diagnostic Checking / 阶段3：诊断检验**

检查拟合模型的残差，判断所选模型是否充分。例如，使用Ljung-Box检验（R命令：`Box.test()`）。如果模型不合适，通常基于信息准则（如AIC）确定模型。

**Stage 4: Forecasting / 阶段4：预测**

基于所选模型预测未来值（R命令：`predict()`）。

**English explanation:** The main stages in setting up a minimum mean square error forecasting model are as follows:

**Stage 1: Model Identification**
1. **Remove trend and seasonal effects**: If trend or seasonal effects are present in the data, first remove them using linear regression (R command: `lm()`).
2. **Identify ARIMA model**: Examine the data (after removing trend and/or seasonal effects) to see which member of the class of ARIMA processes appears most appropriate, using ACF and PACF plots (R command: `acf()`, `pacf()`).

**Stage 2: Estimation**
Estimate the parameters of the chosen model (R command: `ar()`, `arima()`).

**Stage 3: Diagnostic Checking**
Examine the residuals from the fitted model to see if the suggested model is adequate. For example, use the Ljung-Box test (R command: `Box.test()`). If the model is inadequate, usually determine a model based on information criteria (like AIC).

**Stage 4: Forecasting**
Forecast future values based on the suggested model (R command: `predict()`).

---

#### Topic 3: US Monthly Unemployment Rate Data Analysis / 美国月度失业率数据分析

##### Data Description / 数据描述

**中文解释：** 我们分析美国1948年1月至2021年9月的月度失业率数据。数据可以从美国劳工统计局网站下载，也可以在Minerva上找到（文件名：US unemployment rate_seasonal adjusted.csv）。

**English explanation:** We analyze the monthly unemployment rates in the U.S. from January 1948 to September 2021. The data can be downloaded from the U.S. Bureau of Labor Statistics website, or found on Minerva (filename: US unemployment rate_seasonal adjusted.csv).

##### Data Preprocessing / 数据预处理

**中文解释：** 从1948年到2019年，失业率在2.1%到10.4%之间变化。然而，由于疫情，2020年初失业率急剧上升。因此，我们只考虑1948年1月至2019年12月的数据，记为 $\{X_t\}, t = 1, \ldots, 864$。

**English explanation:** From 1948 to 2019, the unemployment rates vary from 2.1% to 10.4%. However, the unemployment rates increase sharply at the beginning of 2020 due to the pandemic. Therefore, we only consider the unemployment rates from January 1948 to December 2019, denoted as $\{X_t\}, t = 1, \ldots, 864$.

##### R Code for Data Loading and Plotting / 数据加载和绘图的R代码

```r
# Load data / 加载数据
data <- read.csv("US unemployment rate_seasonal adjusted.csv", header = T)
unem <- as.vector(as.numeric(unlist(t(data[-(1:11), -1]))))
unem <- unem[!is.na(unem)]

# Figure 9.1: Full series and pre-2020 series with ACF and PACF
par(mfrow = c(4, 1), mar = c(1, 4, 1, 1))

# Plot 1: Full series / 完整序列图
plot(unem, type = "l", xlab = "Month", ylab = "Rates", xaxt = "n")
x.pos <- c(1, 145, 289, 433, 577, 721, 865)
x.label <- c("1948/01", "1960/01", "1972/01", "1984/01", "1996/01", "2008/01", "2020/01")
axis(1, x.pos, x.label)

# Plot 2: Pre-2020 series / 2020年前序列
unem.19 <- unem[1:864]
plot(unem.19, type = "l", xlab = "Month", ylab = "Rates", xaxt = "n")
x.pos <- c(1, 145, 289, 433, 577, 721, 864)
x.label <- c("1948/01", "1960/01", "1972/01", "1984/01", "1996/01", "2008/01", "2019/12")
axis(1, x.pos, x.label)

# Plot 3: ACF / 自相关函数图
acf(unem.19, 25, xlab = "Lag", ylab = "ACF", main = "")

# Plot 4: PACF / 偏自相关函数图
acf(unem.19, 25, type = "partial", xlab = "Lag", ylab = "Partial ACF", main = "")
```

##### ACF and PACF Interpretation / ACF和PACF解读

**中文解释：** 从图9.1可以看出，原始序列的样本ACF随着滞后的增加缓慢衰减，这表明序列可能非平稳，需要进行差分处理。因此，ARIMA(p, d, q)模型可能适合这个序列。

**English explanation:** From Figure 9.1, we can see that the sample ACF of the original series decays slowly with the increase of lags, which suggests the series might be non-stationary and differencing is necessary. Therefore, an ARIMA(p, d, q) model might be appropriate for this series.

##### Training-Test Split / 训练-测试集划分

**中文解释：** 为了评估模型的样本外预测性能，我们将数据分为训练集和测试集：
- 训练集：1948年1月至2018年12月（852个观测值）
- 测试集：2019年1月至2019年12月（12个观测值）

记 $\{X_t^{in}\}$ 为训练期的失业率，$\{X_t^{out}\}$ 为测试期的失业率。

**English explanation:** To evaluate the out-of-sample forecasting performance, we split the data into training and test sets:
- Training set: January 1948 to December 2018 (852 observations)
- Test set: January 2019 to December 2019 (12 observations)

Denote $\{X_t^{in}\}$ as the unemployment rates in the training period, and $\{X_t^{out}\}$ as the rates in the test period.

##### R Code for Training-Test Split / 划分训练-测试集的R代码

```r
# Partition the series into training and testing data
unem.train <- unem[1:852]
unem.test <- unem[(852+1):864]

# Figure 9.2: Training series with ACF and PACF
par(mfrow = c(3, 1), mar = c(1, 4, 1, 1))

plot(unem.train, type = "l", xlab = "Month", ylab = "Rates", xaxt = "n")
x.pos <- c(1, 145, 289, 433, 577, 721, 852)
x.label <- c("1948/01", "1960/01", "1972/01", "1984/01", "1996/01", "2008/01", "2018/12")
axis(1, x.pos, x.label)

acf(unem.train, 25, xlab = "Lag", ylab = "ACF", main = "")
acf(unem.train, 25, type = "partial", xlab = "Lag", ylab = "Partial ACF", main = "")
```

##### Differencing / 差分处理

**中文解释：** 训练集序列 $\{X_t^{in}\}$ 的样本ACF（图9.2中间图）衰减非常缓慢，这表明可能需要进行差分。因此，ARIMA(p, d, q)模型可能适合这个序列。一阶差分后的序列及其ACF和PACF如图9.3所示。差分后的ACF不再缓慢衰减，所以我们决定使用ARIMA(p, 1, q)模型。

**English explanation:** The sample ACF of the training series $\{X_t^{in}\}$ in Figure 9.2 (middle) decays very slowly, suggesting that differencing might be necessary. Therefore, an ARIMA(p, d, q) model might be appropriate for the series. The first-order differenced series and its sample ACF and PACF are plotted in Figure 9.3. The corresponding ACF does not decay very slowly, so we decide to use ARIMA(p, 1, q) model.

##### R Code for Differencing / 差分处理的R代码

```r
# Figure 9.3: First-order differenced series with ACF and PACF
par(mfrow = c(3, 1), mar = c(1, 4, 1, 1))

plot(diff(unem.train), type = "l", xlab = "Month", ylab = "Rates", xaxt = "n")
axis(1, x.pos, x.label)

acf(diff(unem.train), 25, xlab = "Lag", ylab = "ACF", main = "")
acf(diff(unem.train), 25, type = "partial", xlab = "Lag", ylab = "Partial ACF", main = "")
```

##### Model Selection Using AIC / 使用AIC进行模型选择

**中文解释：** 由于p和q的阶数未知，且从图9.3的ACF和PACF图中不容易猜测它们的值，我们拟合一组ARIMA(p, 1, q)模型到训练集 $\{X_t^{in}\}$，并计算拟合模型的AIC值。AIC值越小，模型拟合越好。

**English explanation:** Since the orders p and q are unknown and it's not easy to guess their values from the ACF and PACF plots shown in Figure 9.3, we fit a set of ARIMA(p, 1, q) models to the training series $\{X_t^{in}\}$ and compute the AICs of the fitted models. The smaller the AIC value, the better the fit.

**AIC (Akaike Information Criterion) / 赤池信息准则：**

**中文解释：** AIC是一种模型选择准则，它在模型拟合优度和模型复杂度之间取得平衡。AIC的计算公式为：
$$AIC = -2\ln(L) + 2k$$

其中 $L$ 是模型的最大似然值，$k$ 是模型中参数的个数。较小的AIC值表示更好的模型。

**English explanation:** AIC is a model selection criterion that balances model fit and model complexity. The AIC formula is:
$$AIC = -2\ln(L) + 2k$$

where $L$ is the maximum likelihood value of the model, and $k$ is the number of parameters in the model. Smaller AIC values indicate better models.

---

### 🔗 Connections / 知识关联

**中文解释：** 本节内容与前面章节有密切联系：
- **第3-5章**：ARIMA模型的理论基础
- **第6章**：参数估计方法
- **第7章**：ACF和PACF用于模型识别，Ljung-Box检验用于诊断
- **第8章**：预测理论和方法

这些知识共同构成了完整的时间序列建模框架。

**English explanation:** This section is closely connected to previous chapters:
- **Chapters 3-5**: Theoretical foundation of ARIMA models
- **Chapter 6**: Parameter estimation methods
- **Chapter 7**: ACF and PACF for model identification, Ljung-Box test for diagnostics
- **Chapter 8**: Forecasting theory and methods

These pieces of knowledge together form a complete time series modeling framework.

---

### ⚠️ Common Mistakes / 常见误区

1. **忽略非平稳性**：直接对非平稳数据拟合ARMA模型，而没有先进行差分。应该先检查ACF是否缓慢衰减，必要时进行差分。

2. **过度依赖ACF和PACF**：仅凭ACF和PACF图确定p和q的阶数，而不使用信息准则（如AIC）进行验证。在实际应用中，ACF和PACF可能不清晰，需要结合信息准则选择模型。

3. **忽略诊断检验**：拟合模型后不检查残差是否满足白噪声假设。应该使用Ljung-Box检验等方法检查残差。

4. **预测区间误解**：认为预测区间是固定的，而实际上随着预测步长的增加，预测区间会变宽。

5. **数据泄露**：在模型选择时使用了测试集数据。应该只使用训练集进行模型识别和参数估计，测试集只用于评估预测性能。

**English explanation:**

1. **Ignoring non-stationarity**: Fitting ARMA models directly to non-stationary data without differencing first. Should check if ACF decays slowly and difference if necessary.

2. **Over-reliance on ACF and PACF**: Determining p and q orders solely from ACF and PACF plots without using information criteria (like AIC) for verification. In practice, ACF and PACF may be unclear, so information criteria should be used together.

3. **Ignoring diagnostic checking**: Not checking whether residuals satisfy white noise assumptions after fitting the model. Should use Ljung-Box test and other methods to check residuals.

4. **Misunderstanding prediction intervals**: Thinking prediction intervals are fixed, when in fact they widen as the forecast horizon increases.

5. **Data leakage**: Using test set data during model selection. Should only use training set for model identification and parameter estimation, with test set only for evaluating forecast performance.

---

### ✍️ Practice / 练习

**Question 1 / 问题1：**

考虑AR(1)模型 $X_t = 0.7X_{t-1} + \varepsilon_t$，其中 $\varepsilon_t \sim N(0, 1)$。如果 $X_{100} = 2$，计算：
- (a) $E[X_{101}|X_{100}]$ 和 $var(X_{101}|X_{100})$
- (b) $E[X_{102}|X_{100}]$ 和 $var(X_{102}|X_{100})$
- (c) 构建 $X_{101}$ 的95%预测区间

**Hint / 提示：** 使用公式 $E[X_{n+h}|X_n] = a^h X_n$ 和 $var(X_{n+h}|X_n) = (1 + a^2 + \cdots + a^{2(h-1)})\sigma^2$。

---

**Question 2 / 问题2：**

解释为什么在时间序列建模中需要将数据分为训练集和测试集？为什么不能使用全部数据来拟合模型？

**Hint / 提示：** 考虑过拟合和模型评估的客观性。

---

**Question 3 / 问题3：**

从图9.3中，一阶差分后的序列的ACF和PACF图有什么特征？这些特征如何帮助我们选择ARIMA模型的阶数p和q？

**Hint / 提示：** 回顾ACF和PACF在AR和MA模型中的理论模式。

---

**Question 4 / 问题4：**

假设你拟合了两个ARIMA模型到同一组数据，模型1的AIC=452.3，模型2的AIC=458.1。你应该选择哪个模型？为什么？

**Hint / 提示：** 比较AIC值，较小的值表示更好的模型。

---

**Question 5 / 问题5：**

为什么对于长期预测，预测区间