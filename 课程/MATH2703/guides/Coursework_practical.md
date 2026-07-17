# MATH2703 Coursework Plan / 课程作业计划

> **来源 / Source**: practical.pdf
> **生成时间 / Generated**: 2026-07-17 15:22

---

## Quick Analysis / 快速分析

```json
{
  "COURSEWORK_TYPE": "Data Analysis + Report",
  "WEIGHT": "20% of final module mark",
  "DEADLINE": "Monday 27 April 2026 at 14:00",
  "PAGE_LIMIT": "No more than five sides of A4 paper",
  "REQUIRED_TOOLS": ["R", "Turnitin", "Minerva", "Word or LaTeX (for fixed-width font if including R output)"],
  "DATA_PROVIDED": "Yes, a file named 'slavery.txt' containing yearly estimated number of slaves embarked on British-flagged ships across the Atlantic. The variable 'num' (denoted X) has been square-root transformed.",
  "CORE_TASKS": [
    "1. Plot the data (variable 'num', denoted X) and examine prominent features. Comment on findings.",
    "2. Use linear regression to remove any linear trend and/or seasonal effects. Denote residuals as Y.",
    "3. Inspect process Y and comment on whether an MA or AR process might be suitable.",
    "4. For p = 1, 2, 3, fit AR(p) models to Y using Yule-Walker equations (either via R function 'ar' or manually).",
    "5. For each p = 1, 2, 3, plot correlogram of residuals, run Ljung-Box test, and comment on model fit.",
    "6. For each p = 1, 2, 3, re-fit AR parameters using 'arima' command. Choose best model based on AIC. Provide summary of final model (all fitted parameters and standard errors).",
    "7. Using 'predict' on the best arima fit, obtain forecast for next 5 years (1808–1812). Interpret and discuss."
  ],
  "METHODS_REQUIRED": [
    "Linear regression (for detrending/deseasonalizing)",
    "Yule-Walker equations (for AR parameter estimation)",
    "Correlogram (ACF plot) of residuals",
    "Ljung-Box test (for residual autocorrelation)",
    "AIC (for model selection)",
    "ARIMA modeling (using 'arima' function)",
    "Forecasting (using 'predict' function)"
  ],
  "GRADING_EMPHASIS": [
    "Clear structure and layout",
    "Careful explanation of results and how they were obtained",
    "Meaningful plots with appropriate labels",
    "Short (1 paragraph) summary of findings written for a non-statistician",
    "Use R output sparingly or not at all; if used, must be in fixed-width font",
    "Do not repeat large sections of theory from notes",
    "Use limited page count to describe analysis and conclusions"
  ],
  "PITFALLS": [
    "Not including a signed Declaration of Academic Integrity Form (download from Minerva).",
    "Naming the report file incorrectly (must be StudentID-Name-MATH2703).",
    "Submitting via wrong platform (must be Turnitin via Minerva→Assessment and Feedback→Submit My Work).",
    "Late submission penalty: 5% per calendar day.",
    "Laying out report as 'answer 1', 'answer 2', etc. (must be structured in own way).",
    "Including large amounts of R output (discouraged).",
    "Attaching R script (not needed).",
    "Forgetting to apply square-root transformation (already done in data).",
    "Not using fixed-width font for any included R output.",
    "Overlooking the requirement to comment on whether MA or AR is suitable for Y."
  ]
}
```

---

# Coursework Analysis & Work Plan / 课程作业分析与工作计划

## 1. Overview / 概览

| Item / 项目 | Details / 详情 |
|-------------|----------------|
| **Course / 课程** | MATH2703 |
| **Coursework type / 作业类型** | Practical data analysis report / 实践数据分析报告 |
| **Weight / 权重** | 20% of final module mark / 占总成绩20% |
| **Deadline / 截止日期** | Monday 27 April 2026, 14:00 |
| **Page limit / 页数限制** | Maximum 5 sides of A4 / 最多5页A4纸 |
| **Late penalty / 迟交扣分** | 5% per calendar day / 每天扣5% |
| **Tools needed / 所需工具** | R statistical software, RStudio recommended |
| **Data provided / 提供数据** | `slavery.txt` - yearly estimated number of slaves embarked on British ships (square root transformed) |

**Key dates / 关键日期:**
- Practical set: Week 5 (23 Feb 2026)
- Q&A sessions: Week 8 workshop, Week 9 lecture
- Submission: 27 April 2026

**Submission format / 提交格式:**
- File name: `StudentID-Name-MATH2703`
- Via Turnitin on Minerva → Assessment and Feedback → Submit My Work
- Include signed Declaration of Academic Integrity Form

---

## 2. Requirements Breakdown / 需求拆解

### Task 1: Data Loading and Initial Plot / 数据加载与初始绘图
**What to do / 做什么:**
- Load `slavery.txt` into R using `read.table()`
- Create a time series plot of `num` (denoted as X) against `year`
- Examine prominent features (trend, seasonality, outliers, variance changes)

**Relevant knowledge / 相关知识:**
- Week 1-2: Basic R data handling, plotting
- Week 3-4: Time series visualization, trend identification

**Difficulty / 难度:** Easy / 简单

---

### Task 2: Linear Regression for Trend/Seasonality Removal / 线性回归去除趋势/季节性
**What to do / 做什么:**
- Fit linear regression model(s) to remove linear trend
- If seasonal effects are present, include seasonal terms (e.g., sine/cosine or dummy variables)
- Denote residuals as Y

**Relevant knowledge / 相关知识:**
- Week 5-6: Linear regression for time series, detrending methods
- Understanding of seasonal patterns in historical data

**Difficulty / 难度:** Medium / 中等

---

### Task 3: Inspect Residuals Y for AR/MA Structure / 检查残差Y的AR/MA结构
**What to do / 做什么:**
- Plot Y (residuals after detrending)
- Examine ACF and PACF plots
- Comment on whether AR or MA model is appropriate

**Relevant knowledge / 相关知识:**
- Week 7-8: ACF, PACF interpretation, AR vs MA identification
- Stationarity concepts

**Difficulty / 难度:** Medium / 中等

---

### Task 4: Fit AR(p) Models Using Yule-Walker (p=1,2,3) / 使用Yule-Walker拟合AR(p)模型
**What to do / 做什么:**
- For p=1,2,3, fit AR(p) models to Y
- Use either `ar()` function in R or solve Yule-Walker equations manually
- Obtain parameter estimates

**Relevant knowledge / 相关知识:**
- Week 8-9: Yule-Walker equations, AR model estimation
- Understanding of AR(p) model structure

**Difficulty / 难度:** Medium-Hard / 中高

---

### Task 5: Residual Diagnostics for AR(p) Models / AR(p)模型残差诊断
**What to do / 做什么:**
- For each p=1,2,3:
  - Plot correlogram of residuals
  - Run Ljung-Box test
  - Comment on model fit quality

**Relevant knowledge / 相关知识:**
- Week 9-10: Residual analysis, Ljung-Box test, model diagnostics
- Interpreting correlograms for white noise

**Difficulty / 难度:** Medium / 中等

---

### Task 6: Re-fit Using arima() and AIC Selection / 使用arima()重新拟合与AIC选择
**What to do / 做什么:**
- For p=1,2,3, re-fit AR parameters using `arima()` function
- Compare models using AIC criterion
- Select best model
- Provide summary with fitted parameters and standard errors

**Relevant knowledge / 相关知识:**
- Week 10-11: ARIMA modeling, AIC for model selection
- Understanding of maximum likelihood estimation vs Yule-Walker

**Difficulty / 难度:** Medium / 中等

---

### Task 7: Forecasting and Interpretation / 预测与解释
**What to do / 做什么:**
- Use `predict()` on the best arima model
- Obtain forecast for next 5 years (1808-1812)
- Interpret and discuss results in context

**Relevant knowledge / 相关知识:**
- Week 11-12: Time series forecasting, prediction intervals
- Contextual interpretation of slave trade data

**Difficulty / 难度:** Medium / 中等

---

### Task 8: Report Writing / 报告撰写
**What to do / 做什么:**
- Write 1-paragraph executive summary for non-statisticians
- Structure report clearly (not as "answer 1, answer 2...")
- Include meaningful plots with proper labels
- Use R output sparingly
- Include signed Declaration of Academic Integrity

**Relevant knowledge / 相关知识:**
- Academic writing skills
- Data presentation best practices

**Difficulty / 难度:** Medium / 中等

---

## 3. Step-by-Step Analysis Plan / 分步分析计划

### Task 1: Data Loading and Initial Plot / 数据加载与初始绘图

**Goal / 目标:** Load data and create initial visualization to understand the time series.

**Relevant Theory / 相关理论:**
- Course sections: Week 1-2 (R basics), Week 3-4 (time series plots)
- Key concepts: Time series components (trend, seasonality, cycle, irregular)

**Approach / 方法:**
1. Download `slavery.txt` from Minerva
2. Save in R working directory
3. Load data using `read.table()`
4. Explore structure with `summary()` and `str()`
5. Create time series plot of `num` vs `year`
6. Visually inspect for trends, cycles, outliers

**Code Framework / 代码框架:**
```r
# Set working directory
# setwd("path/to/your/folder")

# Load data
xf <- read.table("slavery.txt")

# Explore data structure
summary(xf)
str(xf)

# Create time series plot
plot(xf$year, xf$num, type = "l", 
     xlab = "Year", ylab = "Number of Slaves (sqrt transformed)",
     main = "Yearly Slave Embarkations on British Ships")
```

**What to Look For / 注意事项:**
- Check for missing values in the data
- Look for overall trend (increasing, decreasing, stable)
- Check for cyclical patterns or seasonality
- Note any outliers or unusual years
- The data is square root transformed - keep this in mind for interpretation

**Expected Output / 预期输出:**
- A line plot of X vs year with proper labels
- A paragraph describing prominent features observed

---

### Task 2: Linear Regression for Trend/Seasonality Removal / 线性回归去除趋势/季节性

**Goal / 目标:** Remove linear trend and/or seasonal effects to obtain stationary residuals Y.

**Relevant Theory / 相关理论:**
- Course sections: Week 5-6 (linear regression for time series)
- Key concepts: Detrending, seasonal adjustment, residuals

**Approach / 方法:**
1. Fit linear regression: `num ~ year` to remove linear trend
2. Examine residuals for remaining patterns
3. If seasonal effects are present, add seasonal terms (e.g., using sine/cosine or year^2)
4. Extract residuals as Y

**Code Framework / 代码框架:**
```r
# Option 1: Simple linear trend removal
model_trend <- lm(num ~ year, data = xf)
Y <- residuals(model_trend)

# Plot residuals
plot(xf$year, Y, type = "l", 
     xlab = "Year", ylab = "Residuals (Y)",
     main = "Detrended Series")

# Option 2: If quadratic trend needed
# model_trend2 <- lm(num ~ year + I(year^2), data = xf)
# Y2 <- residuals(model_trend2)

# Option 3: If seasonal effects suspected
# model_seasonal <- lm(num ~ year + sin(2*pi*year/period) + cos(2*pi*year/period), data = xf)
# Y3 <- residuals(model_seasonal)
```

**What to Look For / 注意事项:**
- Check if linear trend is sufficient or if quadratic/polynomial is needed
- Look at the data range - does it span multiple centuries? Seasonality may not be annual
- The data is yearly, so annual seasonality is not applicable - focus on trend
- Consider if a log transformation or differencing might be more appropriate
- Check residuals for remaining structure

**Expected Output / 预期输出:**
- Residual series Y (detrended data)
- A plot of Y vs year
- Explanation of which trend model was chosen and why

---

### Task 3: Inspect Residuals Y for AR/MA Structure / 检查残差Y的AR/MA结构

**Goal / 目标:** Determine whether AR or MA model is appropriate for Y.

**Relevant Theory / 相关理论:**
- Course sections: Week 7-8 (ACF, PACF, AR vs MA identification)
- Key concepts: ACF decays for AR, cuts off for MA; PACF cuts off for AR, decays for MA

**Approach / 方法:**
1. Plot the residual series Y
2. Compute and plot ACF (autocorrelation function)
3. Compute and plot PACF (partial autocorrelation function)
4. Interpret patterns to suggest AR or MA order

**Code Framework / 代码框架:**
```r
# Plot the residual series
plot(xf$year, Y, type = "l", 
     xlab = "Year", ylab = "Y",
     main = "Detrended Series Y")

# ACF and PACF plots
par(mfrow = c(1, 2))
acf(Y, main = "ACF of Y", lag.max = 20)
pacf(Y, main = "PACF of Y", lag.max = 20)
par(mfrow = c(1, 1))
```

**What to Look For / 注意事项:**
- ACF: If it decays gradually → AR process; if it cuts off after lag q → MA(q)
- PACF: If it cuts off after lag p → AR(p); if it decays → MA process
- Look at significance bounds (dashed blue lines)
- Check if residuals appear stationary (constant mean, variance)
- Consider if differencing might be needed

**Expected Output / 预期输出:**
- ACF and PACF plots of Y
- A paragraph explaining whether AR or MA is suggested and what order

---

### Task 4: Fit AR(p) Models Using Yule-Walker (p=1,2,3) / 使用Yule-Walker拟合AR(p)模型

**Goal / 目标:** Fit AR(1), AR(2), and AR(3) models to Y using Yule-Walker equations.

**Relevant Theory / 相关理论:**
- Course sections: Week 8-9 (Yule-Walker equations, AR model estimation)
- Key concepts: Yule-Walker equations relate autocorrelations to AR parameters

**Approach / 方法:**
1. Use `ar()` function with `method = "yule-walker"` for p=1,2,3
2. Alternatively, solve Yule-Walker equations manually using autocorrelations
3. Extract parameter estimates for each model

**Code Framework / 代码框架:**
```r
# Method 1: Using ar() function
ar_yw1 <- ar(Y, order.max = 1, method = "yule-walker", aic = FALSE)
ar_yw2 <- ar(Y, order.max = 2, method = "yule-walker", aic = FALSE)
ar_yw3 <- ar(Y, order.max = 3, method = "yule-walker", aic = FALSE)

# Extract parameters
ar_yw1$ar  # AR(1) coefficient
ar_yw2$ar  # AR(2) coefficients
ar_yw3$ar  # AR(3) coefficients

# Method 2: Manual Yule-Walker (for AR(1) example)
# rho1 <- acf(Y, plot = FALSE)$acf[2]
# phi1 <- rho1  # For AR(1): phi1 = rho1
```

**What to Look For / 注意事项:**
- Ensure `aic = FALSE` to force specific order
- Check if estimated parameters satisfy stationarity conditions (|φ| < 1 for AR(1))
- For AR(2): check characteristic equation roots lie outside unit circle
- Compare parameter estimates across models

**Expected Output / 预期输出:**
- Parameter estimates for AR(1), AR(2), AR(3) models
- Brief comment on parameter values

---

### Task 5: Residual Diagnostics for AR(p) Models / AR(p)模型残差诊断

**Goal / 目标:** Assess model fit quality for each AR(p) model using residual analysis.

**Relevant Theory / 相关理论:**
- Course sections: Week 9-10 (residual analysis, Ljung-Box test)
- Key concepts: Good residuals should be white noise (no autocorrelation)

**Approach / 方法:**
1. For each model (p=1,2,3):
   - Extract residuals
   - Plot correlogram of residuals
   - Run Ljung-Box test
2. Compare and comment on which model fits best

**Code Framework / 代码框架:**
```r
# For AR(1) example
resid1 <- ar_yw1$resid[!is.na(ar_yw1$resid)]  # Remove NA values

# Correlogram of residuals
acf(resid1, main = "Residuals of AR(1) Model", lag.max = 20)

# Ljung-Box test
Box.test(resid1, lag = 10, type = "Ljung-Box")
Box.test(resid1, lag = 15, type = "Ljung-Box")
Box.test(resid1, lag = 20, type = "Ljung-Box")

# Repeat for AR(2) and AR(3)
```

**What to Look For / 注意事项:**
- Ljung-Box test: p-value > 0.05 indicates residuals are white noise (good fit)
- Check multiple lags (e.g., 10, 15, 20) for robustness
- Look for any remaining significant autocorrelations in correlogram
- Compare across models: which has the "whitest" residuals?

**Expected Output / 预期输出:**
- Three correlogram plots (one for each model)
- Ljung-Box test results (p-values) for each model
- A paragraph comparing model fits

---

### Task 6: Re-fit Using arima() and AIC Selection / 使用arima()重新拟合与AIC选择

**Goal / 目标:** Re-fit AR models using maximum likelihood (arima function) and select best model by AIC.

**Relevant Theory / 相关理论:**
- Course sections: Week 10-11 (ARIMA modeling, AIC)
- Key concepts: AIC balances fit and complexity; lower AIC is better

**Approach / 方法:**
1. Fit ARIMA(p,0,0) models for p=1,2,3 using `arima()`
2. Compare AIC values
3. Select the model with lowest AIC
4. Provide summary with parameters and standard errors

**Code Framework / 代码框架:**
```r
# Fit ARIMA models using arima()
arima1 <- arima(Y, order = c(1, 0, 0))
arima2 <- arima(Y, order = c(2, 0, 0))
arima3 <- arima(Y, order = c(3, 0, 0))

# Compare AIC values
AIC(arima1, arima2, arima3)

# Summary of best model (example: if AR(2) is best)
summary(arima2)

# Extract coefficients and standard errors
coef(arima2)
sqrt(diag(vcov(arima2)))
```

**What to Look For / 注意事项:**
- AIC values: lower is better, but differences < 2 are not significant
- Check if arima() estimates differ from Yule-Walker estimates
- Standard errors indicate precision of estimates
- Ensure the model is causal (all roots outside unit circle)

**Expected Output / 预期输出:**
- AIC comparison table for p=1,2,3
- Selected model with fitted parameters and standard errors
- Explanation of why this model was chosen

---

### Task 7: Forecasting and Interpretation / 预测与解释

**Goal / 目标:** Generate and interpret forecasts for 1808-1812.

**Relevant Theory / 相关理论:**
- Course sections: Week 11-12 (forecasting with ARIMA models)
- Key concepts: Point forecasts, prediction intervals, forecast uncertainty

**Approach / 方法:**
1. Use `predict()` on the best arima model
2. Obtain forecasts for next 5 years
3. Plot historical data with forecasts
4. Interpret results in context of slave trade history

**Code Framework / 代码框架:**
```r
# Forecast next 5 years
forecast_result <- predict(arima2, n.ahead = 5)

# View forecast values
forecast_result$pred
forecast_result$se  # Standard errors

# Create forecast years
forecast_years <- 1808:1812

# Plot historical data with forecast
plot(xf$year, Y, type = "l", xlim = c(min(xf$year), 1812),
     xlab = "Year", ylab = "Y",
     main = "Historical Data and Forecast")
lines(forecast_years, forecast_result$pred, col = "red", lty = 2)

# Add confidence intervals (95%)
lines(forecast_years, forecast_result$pred + 1.96 * forecast_result$se, 
      col = "blue", lty = 3)
lines(forecast_years, forecast_result$pred - 1.96 * forecast_result$se, 
      col = "blue", lty = 3)
```

**What to Look For / 注意事项:**
- Forecast uncertainty increases with forecast horizon
- Consider the historical context: British slave trade abolished in 1807
- The forecast may not capture structural breaks (policy changes)
- Interpret with caution - the model assumes past patterns continue

**Expected Output / 预期输出:**
- Forecast plot with confidence intervals
- Table of forecast values
- Discussion of forecast interpretation and limitations

---

### Task 8: Report Writing / 报告撰写

**Goal / 目标:** Produce a clear, well-structured report within 5 pages.

**Approach / 方法:**
1. Write executive summary first (1 paragraph for non-statisticians)
2. Structure report logically (not as Q&A)
3. Include key plots with proper labels
4. Use R output sparingly
5. Proofread and check page limit

**What to Look For / 注意事项:**
- Do NOT repeat theory from notes
- Focus on YOUR analysis and conclusions
- Use fixed-width font for any R output
- Include signed Declaration of Academic Integrity
- File name: `StudentID-Name-MATH2703`

**Expected Output / 预期输出:**
- Complete report (max 5 pages)
- Executive summary
- Clear sections with analysis and interpretation

---

## 4. Report Structure / 报告结构

### Title / 标题
- Student ID, Name, Course code (MATH2703)
- Title: "Analysis of Slave Voyage Data: A Time Series Approach"

### Executive Summary / 执行摘要 (1 paragraph)
- Written for non-statistician
- Brief overview of data, methods, key findings
- Avoid technical jargon

### Section 1: Introduction / 引言
- Brief description of the data
- Research question: analyzing trends in slave embarkations
- Overview of approach

### Section 2: Data Exploration and Detrending / 数据探索与去趋势
- Initial plot of X vs year
- Description of prominent features
- Linear regression model for trend removal
- Plot of residuals Y

### Section 3: Model Identification / 模型识别
- ACF and PACF plots of Y
- Discussion of AR vs MA suitability
- Justification for AR model choice

### Section 4: Model Fitting and Diagnostics / 模型拟合与诊断
- Yule-Walker estimates for AR(1), AR(2), AR(3)
- Residual diagnostics (correlograms, Ljung-Box tests)
- Comparison of model fits

### Section 5: Model Selection and Final Model / 模型选择与最终模型
- AIC comparison table
- Selected model from arima() fitting
- Parameter estimates with standard errors

### Section 6: Forecasting / 预测
- Forecast plot for 1808-1812
- Table of forecast values
- Interpretation and discussion

### Section 7: Conclusion / 结论
- Summary of key findings
- Limitations of the analysis
- Suggestions for further work

### References / 参考文献 (if any)

### Declaration of Academic Integrity / 学术诚信声明
- Signed form attached

**Figure/Table Placement / 图表放置建议:**
- Figure 1: Time series plot of X (Section 2)
- Figure 2: Residuals Y after detrending (Section 2)
- Figure 3: ACF and PACF of Y (Section 3)
- Figure 4: Residual correlograms (Section 4) - consider combining into one figure
- Table 1: AIC comparison (Section 5)
- Figure 5: Forecast plot (Section 6)
- Table 2: Forecast values (Section 6)

---

## 5. Code Organization / 代码组织

### Suggested Script Structure / 建议脚本结构

```r
# ============================================
# MATH2703 Practical - Slave Voyage Analysis
# Student ID: [Your ID]
# ============================================

# --- 1. Setup and Data Loading ---
# Set working directory
# Load libraries
library(forecast)  # Optional, for additional functions

# Load data
xf <- read.table("slavery.txt")
summary(xf)

# --- 2. Initial Plot ---
# Create time series plot

# --- 3. Detrending ---
# Fit linear regression
# Extract residuals Y

# --- 4. ACF/PACF Analysis ---
# Plot ACF and PACF of Y

# --- 5. Yule-Walker AR Fitting ---
# Fit AR(1), AR(2), AR(3)

# --- 6. Residual Diagnostics ---
# For each model: correlogram, Ljung-Box test

# --- 7. arima() Fitting and AIC ---
# Fit ARIMA(p,0,0) for p=1,2,3
# Compare AIC

# --- 8. Forecasting ---
# Predict next 5 years
# Plot with confidence intervals

# --- 9. Save Outputs ---
# Save plots if needed
```

### Key Libraries Needed / 关键库
```r
# Base R (no additional packages required)
# stats package (built-in) for:
#   - lm(), ar(), arima(), predict()
#   - acf(), pacf()
#   - Box.test()
```

### Tips for Reproducible Analysis / 可重复分析提示
1. Use `set.seed()` for reproducibility (though not critical here)
2. Comment your code thoroughly
3. Save all plots as high-resolution PNG or PDF
4. Keep data file in same directory as script
5. Use relative paths, not absolute paths

---

## 6. Submission Checklist / 提交检查清单

### Before Submission / 提交前检查

- [ ] **Data analysis complete** / 数据分析完成
  - [ ] Data loaded and plotted
  - [ ] Trend removed, residuals Y obtained
  - [ ] ACF/PACF analyzed
  - [ ] AR(1), AR(2), AR(3) fitted via Yule-Walker
  - [ ] Residual diagnostics performed
  - [ ] arima() models fitted and AIC compared
  - [ ] Best model selected
  - [ ] Forecast generated

- [ ] **Report complete** / 报告完成
  - [ ] Executive summary written (1 paragraph)
  - [ ] Report structured logically (not Q&A format)
  - [ ] All required analyses described
  - [ ] Plots included with proper labels
  - [ ] R output used sparingly
  - [ ] No large theory sections copied from notes
  - [ ] Report ≤ 5 pages A4

- [ ] **Formatting checks** / 格式检查
  - [ ] R output in fixed-width font (Courier or verbatim)
  - [ ] Clear structure and layout
  - [ ] Figures have titles and axis labels
  - [ ] Tables are clearly formatted

- [ ] **Academic integrity** / 学术诚信
  - [ ] Declaration of Academic Integrity Form signed
  - [ ] Work is your own (ideas can be shared, but not text)

- [ ] **File naming** / 文件命名
  - [ ] File name: `StudentID-Name-MATH2703`
  - [ ] Correct format (e.g., `12345678-Smith-MATH2703.pdf`)

- [ ] **Submission process** / 提交流程
  - [ ] Submitted via Turnitin on Minerva
  - [ ] Submitted before deadline: Monday 27 April 2026, 14:00
  - [ ] Electronic version only (no paper copy needed)

---

## 7. Time Management / 时间规划

### Week-by-Week Plan / 每周计划

| Week | Dates | Tasks | Estimated Hours |
|------|-------|-------|-----------------|
| **Week 5** | 23 Feb - 1 Mar | Read practical brief, download data, explore data structure | 2 hours |
| **Week 6** | 2 Mar - 8 Mar | Task 1: Initial plot and analysis; Task 2: Detrending | 3 hours |
| **Week 7** | 9 Mar - 15 Mar | Task 3: ACF/PACF analysis; Task 4: Yule-Walker fitting | 4 hours |
| **Week 8** | 16 Mar - 22 Mar | **Workshop Q&A session**; Task 