
clear all
set more off

//Import data
import excel "student_t_test\data\t-test2.xls", sheet("Independent-sample t-test") firstrow

//Browse the imported dataset
browse

//some statistics
summarize Wear_Amount if Sole_Material_Type=="A"
summarize Wear_Amount if Sole_Material_Type=="B"
tabulate Sole_Material_Type, summarize(Wear_Amount)

/*
Question
Is there a statistically significant difference between A and B on their Wear_Amount?

Hypothesis
H0: There's no difference in Wear_Amount between A and B  
Ha: There's a statistically significant difference in Wear_Amount between A and B

The level of significance
alpha = 0.05


Assumptions
Determine if data meets requirements to perform an independent samples t-test.

Assumption #1: Your dependent variable should be measured on a continuous scale.   
Assumption #2: Your independent variable should consist of two categorical, independent groups.   
Assumption #3: You should have independence of observations.    
Assumption #4: There should be no significant outliers.    
Assumption #5: Your dependent variable should be approximately normally distributed for each group of the independent variables.    
Assumption #6: There needs to be homogeneity of variances.
*/

//CHECK FOR OUTLIERS

//Check outliers by plotting a boxplot
graph box Wear_Amount, over(Sole_Material_Type)  // or graph hbox Wear_Amount, over(Sole_Material_Type)

//NORMALITY TEST

//Normality Law test using Skewness Kurtosis test for normality
    //Null hypothesis: The data follows a normal distribution.
    //Alternative hypothesis: The data does not follow a normal distribution.
sktest Wear_Amount if Sole_Material_Type=="A"
sktest Wear_Amount if Sole_Material_Type=="B"

//Normality through histogram
histogram Wear_Amount if Sole_Material_Type=="A", normal
histogram Wear_Amount if Sole_Material_Type=="B", normal

//Normality Law test using Shapiro-Wilk W test for normal data
    //Null hypothesis: The data follows a normal distribution.
    //Alternative hypothesis: The data does not follow a normal distribution.
swilk Wear_Amount if Sole_Material_Type=="A"
swilk Wear_Amount if Sole_Material_Type=="B"

//Normality Law test using Shapiro-Francia W' test for normal data
    //Null hypothesis: The data follows a normal distribution.
    //Alternative hypothesis: The data does not follow a normal distribution.
sfrancia Wear_Amount if Sole_Material_Type=="A"
sfrancia Wear_Amount if Sole_Material_Type=="B"


//Check Homogeneity of variances
robvar Wear_Amount , by( Sole_Material_Type )

/*LEVENE and BROWN-FORSYTHE tests are obtained using the command robvar. These are good choices especially  when assumption of normality is in question.. 
 W_0 = Levene test.
 W_50 = Forsythe-Browne modification of Levene test (mean is replaced by median). 
 W_10 = Fosythe-Browne modification of Levene test (mean is replaced by 10% trim). 
*/

//Unpaired Sample T-test
ttest Wear_Amount, by(Sole_Material_Type)
