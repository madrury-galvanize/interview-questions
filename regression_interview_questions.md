1.  What are the common assumptions made for linear regression?  How would you rank them in order if importance?  For which applications of linear regression are the assumptions more or less important?

2.  What are the common assumptions of logistic regression?

3. Suppose you have data with two predictors `x_1` and `x_2`, and you would like to use linear regression to predict a response variable `y`.  Is it possible that when `y` is regressed against only `x_`1 the parameter associated with `x_1` is positive, yet when `y` is regressed against `x_1` and `x_2` the parameter associated with `x_1` is estimated as negative?

4. What assumptions does linear regression make about the distribution of the predictor variables?  How would you make sure these assumptions are met?

5. What issues arise when predictors in a linear regression are either collinear, or strongly correlated?  What techniques can be used to combat these issues?

6. What techniques are available to reduce the number of predictors in a regression?  Why are these techniques important?

7. In what situations is it appropriate to standardize the predictors in a regression?

8. In what situations is it appropriate to not include an intercept term in a regression?

9. A colleague fits a regression using a quadratic transformation of a variable `x`, but only includes the `x^2` term, not the `x` term.  Are there potential issues with this?  What assumptions are they implicitly making about the model?  How would you advise your colleague?

10. A scientist would like to test whether the presence of a feature has an effect on a response.  The data they have a available to fit a regression model contains a large number of features, so they propose the following procedure:

  - Fit a LASSO model using cross validation and a grid search to select the important features.
  - Fit a regular linear regression using only the features selected by the LASSO model.
  - Use the -p-value reported from the regression to test the null hypothesis that the feature has no effect.

Please critique this procedure.
