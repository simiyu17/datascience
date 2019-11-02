
//Simple Linear Regression
//Response Variable = price
//Predictor Variable = sqft_living

clear all
set more off

use "H:\training\data\projects\datascience\simple linear regression\stata\kc_house_data.dta"

//Validate response and predictor variable to see if they can be used in simple linear regression


   // Linearity: The relationship between X and the mean of Y is linear.
    //Homoscedasticity: The variance of residual is the same for any value of X.
    //Independence: Observations are independent of each other.
    //Normality: For any fixed value of X, Y is normally distributed.
	
	/*Note: We present the output from the linear regression analysis above. 
	 However, since you should have tested your data for the assumptions we explained earlier in the Assumptions section, you will also need to interpret the Stata output that was produced when you tested for these assumptions.
	 This includes: (a) the scatterplots you used to check if there was a linear relationship between your two variables (i.e., Assumption #3);
	 (b) casewise diagnostics to check there were no significant outliers (i.e., Assumption #4); 
	 (c) the output from the Durbin-Watson statistic to check for independence of observations (i.e., Assumption #5);
	 (d) a scatterplot of the regression standardized residuals against the regression standardized predicted value to determine whether your data showed homoscedasticity (i.e., Assumption #6);
	 and a histogram (with superimposed normal curve) and Normal P-P Plot to check whether the residuals (errors) were approximately normally distributed (i.e., Assumption #7).
	 Also, remember that if your data failed any of these assumptions, the output that you get from the linear regression procedure (i.e., the output we discuss above) will no longer be relevant,
	 and you may have to carry out an different statistical test to analyse your data.
*/

//Assumption #1: Your dependent variable should be measured at the continuous level
//Assumption #2: Your independent variable should be measured at the continuous or categorical level
//Assumption #3: There needs to be a linear relationship between the dependent and independent variables (We use scatterplot as below)
//Assumption #4: Your data needs to show homoscedasticity, which is where the variances along the line of best fit remain similar as you move along the line (We use scatterplot as below)
//Assumption #5: There should be no significant outliers. Using the below scatterplot, identify and remove any signifant outliers.

twoway (scatter price sqft_living)


//Assumption #6: You should have independence of observations, which you can easily check using the Durbin-Watson statistic, which is a simple test to run using Stata
    //generate time variable
	
	gen t = _n
	tsset t
	
	//run regression first before getting Durbin-Watson statistic as shown below
	regress price sqft_living
	dwstat
	
/*Assumption #7: Finally, you check for normality. you need to check that the residuals (errors) of the regression line are approximately normally distributed. 
Two common methods to check this assumption include using either a histogram (with a superimposed normal curve) or a Normal P-P Plot.	*/

	* to predict the residuals from the regression model, use the below command
	
	predict resid, residuals
	sktest resid
	
    //Null hypothesis: The data follows a normal distribution.
    //Alternative hypothesis: The data does not follow a normal distribution.
	// p-value > 0.05 then we fail to reject null hypothesis
	
	// We can also check normality by histogram as below
	
	histogram resid, normal
	
	// With no assumption violated, run regression
	
	regress price sqft_living
	
	/*
	A linear regression established that sqft_living could statistically significantly predict price, F(1, 21611) = 21002.93, p < .0001 and sqft_living accounted for 49.29% of the explained variability in prices.
	The regression equation was: predicted price = 280.8067 x (sqft_living)-43867.6 
	*/

	
