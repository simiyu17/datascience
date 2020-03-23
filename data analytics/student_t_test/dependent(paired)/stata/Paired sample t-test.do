
clear all
set more off

//Import data
import excel "student_t_test\data\t-test2.xls", sheet("Paired-sample t-test") firstrow


//Browse the imported dataset
browse

//Descriptive statistics
summarize Morning Evening


/*
# Important Variables
So, we have performance of kids in the morning and evening on a certain game.

# Question
Is there a statistically significant difference between the morning and evening performance?

# hypothesis 
H0: There's no difference between morning and evening performance  
Ha: There's a statistically significant difference between morning and evening performance

# The alpha level will be 0.05.
alpha = 0.05

# Assumptions
Determine if data meets requirements to perform an dependent samples t-test.


Assumption #1: Your dependent variables should be measured on a continuous scale.      
Assumption #2: You should have dependence of observations.    
Assumption #3: There should be no significant outliers.    
Assumption #4: Your dependent variables should be approximately normally distributed.    
Assumption #5: There needs to be homogeneity of variances.

*/


//CHECK FOR OUTLIERS

//Check outliers by plotting a boxplot
graph box Morning Evening  // or graph hbox Morning Evening


//NORMALITY TEST

//Normality Law test using Skewness Kurtosis test for normality
    //Null hypothesis: The data follows a normal distribution.
    //Alternative hypothesis: The data does not follow a normal distribution.
sktest Morning Evening

//Normality through histogram
histogram Morning Evening, normal

//Normality Law test using Shapiro-Wilk W test for normal data
    //Null hypothesis: The data follows a normal distribution.
    //Alternative hypothesis: The data does not follow a normal distribution.
swilk Morning Evening

//Normality Law test using Shapiro-Francia W' test for normal data
    //Null hypothesis: The data follows a normal distribution.
    //Alternative hypothesis: The data does not follow a normal distribution.
sfrancia Morning Evening

//Paired Sample T-test
//ttest FirstVariable == SecondVariable, level(ConfidenceIntervalPercentage)
ttest Morning==Evening
