
clear all
set more off

use "regression_auto.dta", clear

global ylist mpg
global xlist weight1

describe $ylist $xlist 
summarize $ylist $xlist
summarize $ylist, detail

/*
Question
Can the weight of a car statistically significantly predict a car's miles per gallon?

Hypothesis
H0: Car weight can not  statistically significantly predict a car's miles per gallon
Ha: Car weight can statistically significantly predict a car's miles per gallon

The level of significance
alpha = 0.05

ASSUMPTIONS
Determine if data meets requirements to perform a linear regression.

Assumption #1: Your response variable should be measured on a continuous scale.     
Assumption #2: Your independent variable should be measured at the continuous or categorical level. 
Assumption #3: There needs to be a linear relationship between the dependent and independent variables. Let’s plot a scatter plot and check
Assumption #4: You should have independence of observations.    
Assumption #5: There should be no significant outliers.    
Assumption #6: Your data needs to show homoscedasticity, which is where the variances along the line of best fit remain similar as you move along the line.
Assumption #7: Finally, you need to check that the residuals (errors) of the regression line are approximately normally distributed. 

*/

*Assumption #3: There needs to be a linear relationship between the dependent and independent variables. Let’s plot a scatter plot and check
* Correlation
correlate $ylist $xlist

* Plotting the data
graph twoway (scatter $ylist $xlist)

*Assumption #4: You should have independence of observations. We can easily check using the Durbin-Watson statistic
//generate time variable
gen t = _n
tsset t

*Run regression first before getting Durbin-Watson statistic as shown below
* Simple regression 
reg $ylist $xlist

dwstat

*Assumption #5: There should be no significant outliers.  
graph hbox mpg weight1

*Assumption #6: Your data needs to show homoscedasticity, which is where the variances along the line of best fit remain similar as you move along the line.
rvfplot, yline(0)
estat imtest
estat hettest

*Assumption #7: Finally, you need to check that the residuals (errors) of the regression line are approximately normally distributed.
* Simple regression 
reg $ylist $xlist
* Regression residuals
predict e1hat, resid
*residual normality test
kdensity e1hat, normal
*The pnorm command graphs a standardized normal probability (P-P) plot while qnorm plots the quantiles of a variable against the quantiles of a normal distribution
pnorm e1hat
qnorm e1hat
* using Shapiro-Wilk W test for normal data
swilk e1hat
histogram e1hat, normal

summarize e1hat
graph twoway (scatter e1hat $xlist)


* Plotting a regression line
graph twoway (scatter $ylist $xlist)(lfit $ylist $xlist) 

* Predicted values for the dependent variable
predict y1hat, xb
summarize $ylist y1hat
graph twoway (scatter $ylist $xlist)(scatter y1hat $xlist)



* Hypothesis testing (coefficient significantly different from zero)
test $xlist

* Marginal effects (at the mean and average marginal effect)
quietly reg $ylist $xlist
margins, dydx(*) atmeans
margins, dydx(*)


