
capture log close
log using ttests.log, replace

clear all
set more off


//Import data
import excel "student_t_test\data\t-test2.xls", sheet("One-sample t-test") firstrow


//Browse the imported dataset
browse

//Descriptive statistics
summarize Scores

/* Important Variables
So, we have performance scores of kids in a maths test.

# Question
Is there a statistically significant difference between the sample mean from 79?

# hypothesis 
H0: There's no difference between the sample mean from 79  
Ha: There's a statistically significant difference between the sample mean from 79 


# The alpha level will be 0.05.
alpha = 0.05


# Assumptions
Determine if data meets requirements to perform an one samples t-test.


Assumption #1: Your Test variable should be measured on a continuous scale.      
Assumption #2: You should have independence of observations.    
Assumption #3: There should be no significant outliers.    
Assumption #4: Your dependent variables should be approximately normally distributed.*/


//CHECK FOR OUTLIERS

//Check outliers by plotting a boxplot
graph box Scores  // or graph hbox Scores


//NORMALITY TEST

//Normality Law test using Skewness Kurtosis test for normality
    //Null hypothesis: The data follows a normal distribution.
    //Alternative hypothesis: The data does not follow a normal distribution.
sktest Scores

//Normality through histogram
histogram Scores, normal

//Normality Law test using Shapiro-Wilk W test for normal data
    //Null hypothesis: The data follows a normal distribution.
    //Alternative hypothesis: The data does not follow a normal distribution.
swilk Scores

//Normality Law test using Shapiro-Francia W' test for normal data
    //Null hypothesis: The data follows a normal distribution.
    //Alternative hypothesis: The data does not follow a normal distribution.
sfrancia Scores


//One Sample T-test
ttest Scores ==79

//log close 
