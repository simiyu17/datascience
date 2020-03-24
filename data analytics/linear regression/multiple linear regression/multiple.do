
clear all
set more off

use "regression_auto.dta", clear

global ylist mpg
global xlist weight1 price foreign

describe $ylist $xlist 
summarize $ylist $xlist
summarize $ylist, detail

/*
Question
Can the weight, its price and whether it’s foreign or not statistically significantly predict a car's miles per gallon?

Hypothesis
H0: Car weight, its price and whether it’s foreign or not can not  statistically significantly predict a car's miles per gallon
Ha: Car weight, its price and whether it’s foreign or not can statistically significantly predict a car's miles per gallon

The level of significance
alpha = 0.05

ASSUMPTIONS
Determine if data meets requirements to perform a linear regression.

Assumption #1: Your response variable should be measured on a continuous scale.     
Assumption #2: You have two or more independent variables, which should be measured at the continuous or categorical level. 
Assumption #3: You should have independence of observations (i.e., independence of residuals), which you can check in Stata using the Durbin-Watson statistic.
Assumption #4: There needs to be a linear relationship between (a) the dependent variable and each of your independent variables, and (b) the dependent variable and the independent variables collectively. 
Assumption #5: Your data needs to show homoscedasticity, which is where the variances along the line of best fit remain similar as you move along the line.
Assumption #6: Your data must not show multicollinearity, which occurs when you have two or more independent variables that are highly correlated with each other.
Assumption #7: There should be no significant outliers, high leverage points or highly influential points, which represent observations in your data set that are in some way unusual.
Assumption #8: The residuals (errors) should be approximately normally distributed.
*/


*Assumption #8: The residuals (errors) should be approximately normally distributed.
* Multiple regression
reg $ylist $xlist

* Predicted values for the dependent variable
predict yhat, xb
summarize $ylist yhat

* Regression residuals
predict ehat, resid
summarize ehat

*kdensity command to produce a kernel density plot
kdensity ehat, normal
*The pnorm command graphs a standardized normal probability (P-P) plot while qnorm plots the quantiles of a variable against the quantiles of a normal distribution
pnorm ehat
qnorm ehat
*iqr stands for inter-quartile range
swilk ehat

*Assumption #5: Your data needs to show homoscedasticity, which is where the variances along the line of best fit remain similar as you move along the line.
*Checking Homoscedasticity of Residuals
rvfplot, yline(0)
*Now let’s look at a couple of commands that test for heteroscedasticity.
estat imtest
estat hettest

*Assumption #6: Your data must not show multicollinearity, which occurs when you have two or more independent variables that are highly correlated with each other.
*Checking for Multicollinearity
vif

*Assumption #4: There needs to be a linear relationship between (a) the dependent variable and each of your independent variables, and (b) the dependent variable and the independent variables collectively. 
*plot the standardized residuals against each of the predictor variables
scatter ehat weight1
scatter ehat price
scatter ehat foreign

/*

    Detecting Unusual and Influential Data
        predict — used to create predicted values, residuals, and measures of influence.
        rvpplot — graphs a residual-versus-predictor plot.
        rvfplot — graphs residual-versus-fitted plot.
        lvr2plot — graphs a leverage-versus-squared-residual plot.
        dfbeta — calculates DFBETAs for all the independent variables in the linear model.
        avplot — graphs an added-variable plot, a.k.a. partial regression plot.
    Tests for Normality of Residuals
        kdensity — produces kernel density plot with normal distribution overlayed.
        pnorm — graphs a standardized normal probability (P-P) plot.
        qnorm — plots the quantiles of varname against the quantiles of a normal distribution.
        iqr — resistant normality check and outlier identification.
        swilk — performs the Shapiro-Wilk W test for normality.
    Tests for Heteroscedasticity
        rvfplot — graphs residual-versus-fitted plot.
        hettest — performs Cook and Weisberg test for heteroscedasticity.
        whitetst — computes the White general test for Heteroscedasticity.
    Tests for Multicollinearity
        vif — calculates the variance inflation factor for the independent variables in the linear model.
        collin — calculates the variance inflation factor and other multicollinearity diagnostics
    Tests for Non-Linearity
        acprplot — graphs an augmented component-plus-residual plot.
        cprplot — graphs component-plus-residual plot, a.k.a. residual plot.
    Tests for Model Specification
        linktest — performs a link test for model specification.
        ovtest — performs regression specification error test (RESET) for omitted variables.

*/


* Correlation
correlate $ylist $xlist



