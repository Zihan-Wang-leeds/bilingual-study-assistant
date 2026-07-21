# Section 10: Summary (coursework due in this week)

> MATH2703 - 自学教材 / Self-Study Guide
> 生成时间: 2026-07-21 11:13
> 来源页: 88-92

---

# MATH2703: Time Series / 时间序列分析

## Section 9.4: Model Selection, Diagnostic Checking, and Forecasting / 模型选择、诊断检验与预测

---

### 📋 Section Overview / 章节概览

**中文解释：** 在本节中，我们将学习如何在实际中完成一个完整的时间序列建模过程。我们已经学习了ARIMA模型的理论基础，现在需要掌握如何从多个候选模型中选择最优模型（使用AIC准则），如何对选定的模型进行残差诊断检验，以及如何使用模型进行预测。本节以美国失业率数据为例，完整演示了这一过程。

**English explanation:** In this section, we will learn how to complete a full time series modeling process in practice. Having learned the theoretical foundations of ARIMA models, we now need to master how to select the optimal model from multiple candidates (using the AIC criterion), how to perform residual diagnostic checks on the selected model, and how to use the model for forecasting. This section uses US unemployment rate data as an example to demonstrate this complete process.

**Real-world importance / 实际重要性：**
- Economic forecasting / 经济预测：失业率预测对政策制定至关重要
- Model validation / 模型验证：确保模型可靠性的必要步骤
- Practical implementation / 实际应用：从理论到实践的桥梁

---

### 🎯 Learning Objectives / 学习目标

After completing this section, you should be able to / 完成本节后，你应该能够：

1. **Use AIC to select the best ARIMA model** from multiple candidates / **使用AIC准则从多个候选模型中选择最优ARIMA模型**
2. **Interpret AIC values** and identify the model with minimum AIC / **解释AIC值并识别具有最小AIC的模型**
3. **Perform residual diagnostic checks** including ACF plots and Ljung-Box test / **进行残差诊断检验**，包括ACF图和Ljung-Box检验
4. **Generate forecasts** using the fitted ARIMA model / **使用拟合的ARIMA模型生成预测**
5. **Construct forecast intervals** and evaluate forecast performance / **构建预测区间并评估预测性能**
6. **Handle seasonal components** in ARIMA modeling / **处理ARIMA建模中的季节性成分**

---

### 📚 Prerequisites / 前置知识

Before studying this section, you should be familiar with / 在学习本节之前，你应该熟悉：

- ARIMA(p,d,q) model structure / ARIMA(p,d,q)模型结构
- AIC (Akaike Information Criterion) concept / AIC（赤池信息准则）概念
- Basic R programming for time series / 时间序列的基本R编程
- ACF and PACF plots interpretation / ACF和PACF图的解读
- Hypothesis testing concepts / 假设检验概念

---

### 📖 Core Content / 核心内容

---

#### Topic 1: Model Selection Using AIC / 使用AIC进行模型选择

##### Intuition / 直觉理解

**中文解释：** 当我们拟合ARIMA模型时，需要选择自回归阶数p和移动平均阶数q。不同的(p,q)组合会产生不同的模型。我们如何选择最好的模型呢？AIC（赤池信息准则）是一个重要的模型选择工具。它平衡了模型的拟合优度和复杂度——AIC值越小，模型越好。这就像在购物时，我们既要考虑商品的质量（拟合优度），也要考虑价格（模型复杂度），AIC帮助我们找到性价比最高的模型。

**English explanation:** When fitting an ARIMA model, we need to choose the autoregressive order p and moving average order q. Different (p,q) combinations produce different models. How do we select the best model? AIC (Akaike Information Criterion) is an important model selection tool. It balances model fit and complexity — the smaller the AIC value, the better the model. This is like shopping where we consider both quality (model fit) and price (model complexity); AIC helps us find the model with the best value.

##### Formal Definition / 形式化定义

**AIC Formula / AIC公式：**
$$AIC = -2\ln(L) + 2k$$

where / 其中：
- $L$ = maximum likelihood of the model / 模型的最大似然值
- $k$ = number of estimated parameters / 估计参数的数量

**Symbol Table / 符号表：**

| Symbol | Chinese Meaning | English Meaning |
|--------|----------------|-----------------|
| AIC | 赤池信息准则 | Akaike Information Criterion |
| $L$ | 最大似然值 | Maximum likelihood |
| $k$ | 参数个数 | Number of parameters |
| $\ln$ | 自然对数 | Natural logarithm |

##### R Code Implementation / R代码实现

**中文解释：** 下面的R代码演示了如何为美国失业率数据（已进行一阶差分，即d=1）选择最优的ARIMA模型。我们尝试p从0到5，q从0到6的所有组合，计算每个模型的AIC值。

**English explanation:** The following R code demonstrates how to select the optimal ARIMA model for US unemployment rate data (already first-differenced, i.e., d=1). We try all combinations of p from 0 to 5 and q from 0 to 6, calculating the AIC value for each model.

```r
# Create a matrix to store AIC values / 创建存储AIC值的矩阵
unem.train.aic <- matrix(0, 6, 7)

# Loop through all combinations of p and q / 遍历所有p和q的组合
for (i in 0:5) for (j in 0:6) {
  fit.arima <- arima(unem.train, order = c(i, 1, j))
  unem.train.aic[i+1, j+1] <- fit.arima$aic
}
```

**Warning messages / 警告信息：**
```
## Warning in log(s2): NaNs produced
## Warning in log(s2): NaNs produced
## Warning in log(s2): NaNs produced
## Warning in log(s2): NaNs produced
```

**中文解释：** 这些警告信息表示某些模型在估计过程中产生了数值问题（对数似然函数中出现NaN）。我们应当谨慎对待这些模型，通常不选择它们。

**English explanation:** These warning messages indicate that some models encountered numerical issues during estimation (NaN appeared in the log-likelihood function). We should treat these models with caution and typically not select them.

##### AIC Matrix Output / AIC矩阵输出

```
##            [,1]       [,2]       [,3]       [,4]       [,5]       [,6]       [,7]
## [1,] -245.9986 -251.3208 -300.1219 -312.0950 -326.4262 -348.9262 -349.0166
## [2,] -255.2527 -321.4111 -357.0407 -355.6134 -358.3576 -360.2471 -358.3074
## [3,] -320.7388 -353.6962 -365.9417 -360.9504 -380.9507 -365.0962 -364.8159
## [4,] -344.6434 -353.1440 -367.4118 -367.5215 -389.3217 -387.3275 -386.5400
## [5,] -349.7287 -351.9108 -357.6460 -370.7646 -380.2165 -393.3509 -383.3520
## [6,] -356.8014 -354.8213 -355.7019 -353.6922 -360.2156 -392.1157 -390.5397
```

**中文解释：** 这个矩阵的行对应p值（从0到5），列对应q值（从0到6）。每个单元格的值是相应ARIMA(p,1,q)模型的AIC值。AIC值越小越好。最小的AIC值是-393.3509，对应ARIMA(4,1,5)模型（第5行第6列）。

**English explanation:** This matrix has rows corresponding to p values (0 to 5) and columns corresponding to q values (0 to 6). Each cell value is the AIC for the corresponding ARIMA(p,1,q) model. Smaller AIC values are better. The minimum AIC value is -393.3509, corresponding to the ARIMA(4,1,5) model (row 5, column 6).

**Key observation / 关键观察：**
- Minimum AIC: -393.3509
- Selected model: ARIMA(4,1,5)
- Note: ARIMA(3,1,1) produced warnings, so we do not trust this model / 注意：ARIMA(3,1,1)产生了警告，我们不信任这个模型

##### Fitting the Selected Model / 拟合选定的模型

```r
fit.arima415 <- arima(unem.train, order = c(4, 1, 5))
fit.arima415
```

**Output / 输出：**
```
## Call:
## arima(x = unem.train, order = c(4, 1, 5))
##
## Coefficients:
##          ar1     ar2     ar3     ar4     ma1     ma2     ma3     ma4     ma5
##       1.3143  0.2603 -1.2820  0.5590 -1.3363 -0.0618  1.2589 -0.7557  0.2095
## s.e.  0.1017  0.0778  0.0844  0.0844  0.1056  0.0897  0.0818  0.1063  0.0396
##
## sigma^2 estimated as 0.03592: log likelihood = 206.68, aic = -393.35
```

##### Model Equation / 模型方程

**中文解释：** 拟合的ARIMA(4,1,5)模型可以写成以下形式。令$X_t$表示原始失业率序列，$Y_t = X_t - X_{t-1}$表示一阶差分后的序列。模型为：

**English explanation:** The fitted ARIMA(4,1,5) model can be written as follows. Let $X_t$ denote the original unemployment rate series, and $Y_t = X_t - X_{t-1}$ denote the first-differenced series. The model is:

$$Y_t = \phi_1 Y_{t-1} + \phi_2 Y_{t-2} + \phi_3 Y_{t-3} + \phi_4 Y_{t-4} + \varepsilon_t + \theta_1 \varepsilon_{t-1} + \theta_2 \varepsilon_{t-2} + \theta_3 \varepsilon_{t-3} + \theta_4 \varepsilon_{t-4} + \theta_5 \varepsilon_{t-5}$$

where $\varepsilon_t \sim N(0, 0.037)$

**Parameter Values / 参数值：**

| Parameter | Estimate | Std.Error | Chinese Name | English Name |
|-----------|----------|-----------|--------------|--------------|
| $\phi_1$ | 1.3143 | 0.1017 | 自回归系数1 | AR coefficient 1 |
| $\phi_2$ | 0.2603 | 0.0778 | 自回归系数2 | AR coefficient 2 |
| $\phi_3$ | -1.2820 | 0.0844 | 自回归系数3 | AR coefficient 3 |
| $\phi_4$ | 0.5590 | 0.0844 | 自回归系数4 | AR coefficient 4 |
| $\theta_1$ | -1.3363 | 0.1056 | 移动平均系数1 | MA coefficient 1 |
| $\theta_2$ | -0.0618 | 0.0897 | 移动平均系数2 | MA coefficient 2 |
| $\theta_3$ | 1.2589 | 0.0818 | 移动平均系数3 | MA coefficient 3 |
| $\theta_4$ | -0.7557 | 0.1063 | 移动平均系数4 | MA coefficient 4 |
| $\theta_5$ | 0.2095 | 0.0396 | 移动平均系数5 | MA coefficient 5 |
| $\sigma^2$ | 0.03592 | - | 误差方差 | Error variance |

---

#### Topic 2: Residual Diagnostic Checking / 残差诊断检验

##### Intuition / 直觉理解

**中文解释：** 选择模型后，我们需要检查模型是否合适。残差是观测值与模型拟合值之间的差异。如果模型正确，残差应该表现为白噪声——即没有自相关结构。我们通过检查残差的ACF图和进行Ljung-Box检验来验证这一点。这就像医生在手术后检查病人的恢复情况——我们需要确保模型"健康"。

**English explanation:** After selecting a model, we need to check if the model is appropriate. Residuals are the differences between observed values and model-fitted values. If the model is correct, residuals should behave like white noise — meaning no autocorrelation structure. We verify this by examining the residual ACF plot and performing the Ljung-Box test. This is like a doctor checking a patient's recovery after surgery — we need to ensure the model is "healthy."

##### R Code for Diagnostic Plots / 诊断图的R代码

```r
par(mfrow = c(3, 1), mar = c(2, 4, 1, 1))
plot(residuals(fit.arima415), type = "l", xlab = "Month", ylab = "residuals", xaxt = "n")
axis(1, x.pos, x.label)
acf(residuals(fit.arima415), 25, xlab = "Lag", ylab = "ACF", main = "")
acf(residuals(fit.arima415), 25, type = "partial", xlab = "Lag", ylab = "Partial ACF", main = "")
```

**中文解释：** 这段代码生成三个图：
1. 残差的时间序列图（顶部）
2. 残差的ACF图（中间）
3. 残差的偏ACF图（底部）

**English explanation:** This code generates three plots:
1. Time series plot of residuals (top)
2. ACF plot of residuals (middle)
3. Partial ACF plot of residuals (bottom)

##### Figure 9.4 Description / 图9.4描述

**中文解释：** 图9.4显示了三个图。顶部图显示残差随时间的变化，理想情况下应该在零附近随机波动。中间和底部的ACF和PACF图显示残差的自相关结构——如果模型合适，这些相关应该在置信区间内（蓝色虚线之间）。

**English explanation:** Figure 9.4 shows three plots. The top plot shows residuals over time, which should ideally fluctuate randomly around zero. The middle and bottom ACF and PACF plots show the autocorrelation structure of residuals — if the model is appropriate, these correlations should fall within the confidence intervals (between blue dashed lines).

##### Ljung-Box Test / Ljung-Box检验

**中文解释：** Ljung-Box检验是一种正式的统计检验，用于检验残差是否为白噪声。原假设$H_0$：残差是独立同分布的白噪声。如果p值大于显著性水平（通常0.05），则不能拒绝原假设，说明模型是合适的。

**English explanation:** The Ljung-Box test is a formal statistical test for checking whether residuals are white noise. The null hypothesis $H_0$: residuals are independently and identically distributed white noise. If the p-value is greater than the significance level (typically 0.05), we cannot reject the null hypothesis, indicating the model is appropriate.

```r
Box.test(residuals(fit.arima415), lag = 20, type = "Ljung-Box")
```

**Output / 输出：**
```
##  Box-Ljung test
##
## data:  residuals(fit.arima415)
## X-squared = 30.281, df = 20, p-value = 0.06542
```

**Interpretation / 解读：**

**中文解释：** p值为0.06542，大于0.05的显著性水平。因此，在5%的显著性水平下，我们不能拒绝原假设，即残差是白噪声。这表明模型拟合是合适的。

**English explanation:** The p-value is 0.06542, which is greater than the 0.05 significance level. Therefore, at the 5% significance level, we cannot reject the null hypothesis that residuals are white noise. This indicates the model fit is appropriate.

**Symbol Table for Ljung-Box Test / Ljung-Box检验符号表：**

| Symbol | Chinese Meaning | English Meaning |
|--------|----------------|-----------------|
| X-squared | 检验统计量 | Test statistic |
| df | 自由度 | Degrees of freedom |
| p-value | p值 | p-value |
| lag | 滞后阶数 | Lag order |

---

#### Topic 3: Forecasting with ARIMA Model / 使用ARIMA模型进行预测

##### Intuition / 直觉理解

**中文解释：** 一旦我们确认模型是合适的，就可以用它来进行预测。预测就是利用模型和已知数据来估计未来的值。对于ARIMA模型，我们计算一步向前预测（即预测下一个时间点的值）以及预测区间。预测区间给出了预测值的不确定性范围——通常使用95%的置信区间。

**English explanation:** Once we confirm the model is appropriate, we can use it for forecasting. Forecasting means using the model and known data to estimate future values. For ARIMA models, we compute one-step-ahead forecasts (predicting the value at the next time point) and forecast intervals. Forecast intervals give the range of uncertainty around the forecast — typically using 95% confidence intervals.

##### Important Note / 重要说明

**中文解释：** 注意，如果原始数据经过了变换（如对数变换）或存在趋势/季节效应，在得到预测值后需要进行逆变换，并加回趋势和/或季节效应。

**English explanation:** Note that if the original data underwent transformations (such as log transformation) or has trend/seasonal effects, after obtaining forecast values, we need to apply inverse transformations and add back trend and/or seasonal effects.

##### R Code for Forecasting / 预测的R代码

```r
# Generate 12-step-ahead forecasts / 生成12步向前预测
unem.forecast <- predict(fit.arima415, n.ahead = 12)

# Create summary table / 创建汇总表
unem.forecast.summary <- cbind(unem.test,
                               unem.forecast$pred,
                               unem.forecast$pred - 1.96 * unem.forecast$se,
                               unem.forecast$pred + 1.96 * unem.forecast$se)
colnames(unem.forecast.summary) <- c("true", "forecast", "ci.lower", "ci.upper")
```

**中文解释：** 这段代码生成12个月的预测（2019年1月到12月）。`predict()`函数返回预测值（`$pred`）和标准误差（`$se`）。95%预测区间由预测值±1.96×标准误差计算得到。

**English explanation:** This code generates 12-month forecasts (January to December 2019). The `predict()` function returns forecast values (`$pred`) and standard errors (`$se`). The 95% forecast interval is calculated as forecast ± 1.96 × standard error.

##### Plotting Forecasts / 绘制预测图

```r
plot(c(1, 12), range(unem.forecast.summary), type = "n",
     xlab = "Month", ylab = "Unemployment rates", xaxt = "n")
lines(seq(1, 12), unem.forecast.summary[,1], lty = 1)
points(seq(1, 12), unem.forecast.summary[,1], pch = 16)
lines(seq(1, 12), unem.forecast.summary[,2], lty = 2)
points(seq(1, 12), unem.forecast.summary[,2], pch = 1)
lines(seq(1, 12), unem.forecast.summary[,3], lty = 3)
points(seq(1, 12), unem.forecast.summary[,3], pch = 0)
lines(seq(1, 12), unem.forecast.summary[,4], lty = 3)
points(seq(1, 12), unem.forecast.summary[,4], pch = 0)
legend(1, 3, c("true", "forecast", "forecast int.", "forecast int."), 
       lty = c(1, 2, 3, 3), pch = c(16, 1, 0, 0))
x.pos <- c(2, 4, 6, 8, 10, 12)
x.label <- c("Feb", "Apr", "Jun", "Aug", "Oct", "Dec")
axis(1, x.pos, x.label)
```

**中文解释：** 图9.5显示了真实值（实线）和预测值（虚线）的对比，以及95%预测区间（点线）。从图中可以看出：
1. 所有真实值都落在95%预测区间内
2. 预测值接近真实值
3. 这表明模型在样本外分析中也表现良好

**English explanation:** Figure 9.5 shows the comparison between true values (solid line) and forecast values (dashed line), along with 95% forecast intervals (dotted lines). From the figure we can see:
1. All true values fall within the 95% forecast intervals
2. Forecast values are close to true values
3. This indicates the model performs well in out-of-sample analysis

##### Forecast Summary Table Structure / 预测汇总表结构

| Column | Chinese Name | English Name | Description |
|--------|--------------|--------------|-------------|
| true | 真实值 | True values | Actual observed values |
| forecast | 预测值 | Forecast values | Model predictions |
| ci.lower | 置信区间下限 | CI lower bound | Lower bound of 95% forecast interval |
| ci.upper | 置信区间上限 | CI upper bound | Upper bound of 95% forecast interval |

---

#### Topic 4: Seasonal ARIMA Models / 季节性ARIMA模型

##### Intuition / 直觉理解

**中文解释：** 在检查图6.3（原始数据的ACF图）时，我们注意到在滞后12和24处仍有明显的季节性模式。这表明我们可能需要考虑季节性ARIMA模型。季节性ARIMA模型在普通ARIMA模型的基础上增加了季节性成分，用SARIMA(p,d,q)(P,D,Q)_s表示，其中s是季节周期长度。

**English explanation:** When examining Figure 6.3 (the ACF plot of the original data), we noticed that there are still apparent seasonal patterns at lags 12 and 24. This suggests we may need to consider seasonal ARIMA models. Seasonal ARIMA models add seasonal components to the regular ARIMA model, denoted as SARIMA(p,d,q)(P,D,Q)_s, where s is the seasonal period length.

##### R Code for Seasonal Model Selection / 季节性模型选择的R代码

```r
# Convert to time series object with monthly frequency / 转换为月度频率的时间序列对象
unem.train.ts <- ts(unem.train, start = c(1948, 1), end = c(2018, 12), frequency = 12)

# Create matrix for seasonal AIC values / 创建季节性AIC值矩阵
unem.train.s.aic <- matrix(0, 5, 4)
for (i in 0:4) for (j in 0:3) {
  fit.arima <- arima(unem.train.ts, order = c(i, 1, j), 
                     seasonal = list(order = c(1, 0, 1), period = 12))
  unem.train.s.aic[i+1, j+1] <- fit.arima$aic
}
```

##### Seasonal AIC Matrix / 季节性AIC矩阵

```
##            [,1]       [,2]       [,3]       [,4]
## [1,] -313.0674 -316.7961 -361.1789 -376.0731
## [2,] -319.7503 -393.3150 -428.6676 -427.6147
## [3,] -380.1802 -424.6584 -429.1652 -426.3944
## [4,] -409.8237 -424.9333 -430.9179 -426.2522
## [5,] -417.7931 -423.7385 -420.9409 -428.6469
```

**中文解释：** 这个矩阵的行对应p值（0到4），列对应q值（0到3），季节性部分固定为SAR(1)和SMA(1)。最小的AIC是-430.9179，对应ARIMA(3,1,2) with seasonal(1,0,1)。但注意ARIMA(3,1,2)产生了警告，所以我们可能选择ARIMA(2,1,2)或ARIMA(1,1,2)。

**English explanation:** This matrix has rows for p (0 to 4) and columns for q (0 to 3), with seasonal part fixed as SAR(1) and SMA(1). The minimum AIC is -430.9179, corresponding to ARIMA(3,1,2) with seasonal(1,0,1). But note ARIMA(3,1,2) produced warnings, so we might choose ARIMA(2,1,2) or ARIMA(1,1,2).

##### Fitting Seasonal Model / 拟合季节性模型

```r
arima(unem.train.ts, order = c(1, 1, 2), 
      seasonal = list(order = c(1, 0, 1), period = 12))
```

**Output / 输出：**
```
## Call:
## arima(x = unem.train.ts, order = c(1, 1, 2), seasonal = list(order = c(1, 0, 1), period = 12))
##
## Coefficients:
##          ar1      ma1     ma2    sar1     sma1
##       0.8546  -0.8743  0.2253  0.5367  -0.8109
## s.e.  0.0324   0.0457  0.0349  0.0660   0.0479
##
## sigma^2 estimated as 0.03474: log likelihood = 220.33, aic = -428.67
```

**中文解释：** 这个季节性ARIMA(1,1,2)(1,0,1)_12模型的AIC为-428.67，比非季节性模型（-393.35）更小，说明季节性模型更好。模型包含：
- 非季节性部分：AR(1)和MA(2)
- 季节性部分：SAR(1)和SMA(1)，周期为12个月

**English explanation:** This seasonal ARIMA(1,1,2)(1,0,1)_12 model has A