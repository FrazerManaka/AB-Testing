import numpy as np
from scipy import stats
import statsmodels.api as sm

# Sample data (replace with actual data)
control_group = [100, 120, 115, 98, 105, 112]  # Conversion rates for old design
experiment_group = [125, 130, 118, 122, 135, 120]  # Conversion rates for new design

# Calculate means and standard deviations
mean_control = np.mean(control_group)
std_control = np.std(control_group, ddof=1)
mean_experiment = np.mean(experiment_group)
std_experiment = np.std(experiment_group, ddof=1)

# Perform t-test
t_stat, p_value = stats.ttest_ind(control_group, experiment_group, equal_var=False)

# Set significance level
alpha = 0.05

# Print results
print("Mean of control group:", mean_control)
print("Mean of experiment group:", mean_experiment)
print("t-statistic:", t_stat)
print("p-value:", p_value)

# Make decision
if p_value < alpha:
    print("Reject null hypothesis: There is a significant difference between the two groups.")
else:
    print("Fail to reject null hypothesis: There is no significant difference between the two groups.")
