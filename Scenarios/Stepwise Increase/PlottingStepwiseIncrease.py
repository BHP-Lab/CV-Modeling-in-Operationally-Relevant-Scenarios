import pandas as pd
import matplotlib.pyplot as plt
from statistics import stdev
file_path = 'StepwiseIncreaseTotal.xls'

# Load the Excel file
data5M = pd.read_excel(file_path, sheet_name='5M')
data5F = pd.read_excel(file_path, sheet_name='5F')
data50M = pd.read_excel(file_path, sheet_name='50M')
data50F = pd.read_excel(file_path, sheet_name='50F')
data95M = pd.read_excel(file_path, sheet_name='95M')
data95F = pd.read_excel(file_path, sheet_name='95F')
data50M_Athlete = pd.read_excel(file_path, sheet_name='50M_Athlete')
data50F_Athlete = pd.read_excel(file_path, sheet_name='50F_Athlete')
data50M_Dehydrated = pd.read_excel(file_path, sheet_name='50M_Dehydrated')
data50F_Dehydrated = pd.read_excel(file_path, sheet_name='50F_Dehydrated')


# Save the data to lists for 5M
time = data5M.iloc[:, 0].tolist()
g_level = data5M.iloc[:, 1].tolist()
Pext_5M = data5M.iloc[:, 2].tolist()
HR_5M = data5M.iloc[:, 3].tolist()
CO_5M = data5M.iloc[:, 4].tolist()
CI_5M = data5M.iloc[:, 5].tolist()
SBP_5M = data5M.iloc[:, 6].tolist()
DBP_5M = data5M.iloc[:, 7].tolist()
MAP_5M = data5M.iloc[:, 8].tolist()
SV_5M = data5M.iloc[:, 9].tolist()

# Save the data to lists for 5F
Pext_5F = data5F.iloc[:, 2].tolist()
HR_5F = data5F.iloc[:, 3].tolist()
CO_5F = data5F.iloc[:, 4].tolist()
CI_5F = data5F.iloc[:, 5].tolist()
SBP_5F = data5F.iloc[:, 6].tolist()
DBP_5F = data5F.iloc[:, 7].tolist()
MAP_5F = data5F.iloc[:, 8].tolist()
SV_5F = data5F.iloc[:, 9].tolist()

# Save the data to lists for 50M
Pext_50M = data50M.iloc[:, 2].tolist()
HR_50M = data50M.iloc[:, 3].tolist()
CO_50M = data50M.iloc[:, 4].tolist()
CI_50M = data50M.iloc[:, 5].tolist()
SBP_50M = data50M.iloc[:, 6].tolist()
DBP_50M = data50M.iloc[:, 7].tolist()
MAP_50M = data50M.iloc[:, 8].tolist()
SV_50M = data50M.iloc[:, 9].tolist()

# Save the data to lists for 50F
Pext_50F = data50F.iloc[:, 2].tolist()
HR_50F = data50F.iloc[:, 3].tolist()
CO_50F = data50F.iloc[:, 4].tolist()
CI_50F = data50F.iloc[:, 5].tolist()
SBP_50F = data50F.iloc[:, 6].tolist()
DBP_50F = data50F.iloc[:, 7].tolist()
MAP_50F = data50F.iloc[:, 8].tolist()
SV_50F = data50F.iloc[:, 9].tolist()

# Save the data to lists for 95M
Pext_95M = data95M.iloc[:, 2].tolist()
HR_95M = data95M.iloc[:, 3].tolist()
CO_95M = data95M.iloc[:, 4].tolist()
CI_95M = data95M.iloc[:, 5].tolist()
SBP_95M = data95M.iloc[:, 6].tolist()
DBP_95M = data95M.iloc[:, 7].tolist()
MAP_95M = data95M.iloc[:, 8].tolist()
SV_95M = data95M.iloc[:, 9].tolist()

# Save the data to lists for 95F
Pext_95F = data95F.iloc[:, 2].tolist()
HR_95F = data95F.iloc[:, 3].tolist()
CO_95F = data95F.iloc[:, 4].tolist()
CI_95F = data95F.iloc[:, 5].tolist()
SBP_95F = data95F.iloc[:, 6].tolist()
DBP_95F = data95F.iloc[:, 7].tolist()
MAP_95F = data95F.iloc[:, 8].tolist()
SV_95F = data95F.iloc[:, 9].tolist()

# Save the data to lists for 50M_Athlete
Pext_50M_Athlete = data50M_Athlete.iloc[:, 2].tolist()
HR_50M_Athlete = data50M_Athlete.iloc[:, 3].tolist()
CO_50M_Athlete = data50M_Athlete.iloc[:, 4].tolist()
CI_50M_Athlete = data50M_Athlete.iloc[:, 5].tolist()
SBP_50M_Athlete = data50M_Athlete.iloc[:, 6].tolist()
DBP_50M_Athlete = data50M_Athlete.iloc[:, 7].tolist()
MAP_50M_Athlete = data50M_Athlete.iloc[:, 8].tolist()
SV_50M_Athlete = data50M_Athlete.iloc[:, 9].tolist()

# Save the data to lists for 50F_Athlete
Pext_50F_Athlete = data50F_Athlete.iloc[:, 2].tolist()
HR_50F_Athlete = data50F_Athlete.iloc[:, 3].tolist()
CO_50F_Athlete = data50F_Athlete.iloc[:, 4].tolist()
CI_50F_Athlete = data50F_Athlete.iloc[:, 5].tolist()
SBP_50F_Athlete = data50F_Athlete.iloc[:, 6].tolist()
DBP_50F_Athlete = data50F_Athlete.iloc[:, 7].tolist()
MAP_50F_Athlete = data50F_Athlete.iloc[:, 8].tolist()
SV_50F_Athlete = data50F_Athlete.iloc[:, 9].tolist()

# Save the data to lists for 50M_Dehydrated
Pext_50M_Dehydrated = data50M_Dehydrated.iloc[:, 2].tolist()
HR_50M_Dehydrated = data50M_Dehydrated.iloc[:, 3].tolist()
CO_50M_Dehydrated = data50M_Dehydrated.iloc[:, 4].tolist()
CI_50M_Dehydrated = data50M_Dehydrated.iloc[:, 5].tolist()
SBP_50M_Dehydrated = data50M_Dehydrated.iloc[:, 6].tolist()
DBP_50M_Dehydrated = data50M_Dehydrated.iloc[:, 7].tolist()
MAP_50M_Dehydrated = data50M_Dehydrated.iloc[:, 8].tolist()
SV_50M_Dehydrated = data50M_Dehydrated.iloc[:, 9].tolist()

# Save the data to lists for 50F_Dehydrated
Pext_50F_Dehydrated = data50F_Dehydrated.iloc[:, 2].tolist()
HR_50F_Dehydrated = data50F_Dehydrated.iloc[:, 3].tolist()
CO_50F_Dehydrated = data50F_Dehydrated.iloc[:, 4].tolist()
CI_50F_Dehydrated = data50F_Dehydrated.iloc[:, 5].tolist()
SBP_50F_Dehydrated = data50F_Dehydrated.iloc[:, 6].tolist()
DBP_50F_Dehydrated = data50F_Dehydrated.iloc[:, 7].tolist()
MAP_50F_Dehydrated = data50F_Dehydrated.iloc[:, 8].tolist()
SV_50F_Dehydrated = data50F_Dehydrated.iloc[:, 9].tolist()

# Create a method to hold plotting code for the vertical lines and shaded regions
def plot_vertical_lines_and_regions(ax):
    # Add vertical lines
    ax.axvline(x=3011, color='black')
    ax.axvline(x=3310, color='black')
    ax.axvline(x=300, color='black')
    # Add shaded regions
    ax.axvspan(301, 3010, facecolor='#fcf9d9', alpha=0.5)
    ax.axvspan(3011, 3310, facecolor='#FAF2AC', alpha=0.5)
    ax.axvspan(3311, 6321, facecolor='#fcee72', alpha=0.5)
    
############################################################################################################
# Find the mean of the HR data at each time point 
HR_mean = [sum(x) / len(x) for x in zip(HR_50M, HR_50F, HR_5M, HR_5F, HR_95M, HR_95F, HR_50M_Athlete, HR_50F_Athlete, HR_50M_Dehydrated, HR_50F_Dehydrated)]
MAP_mean = [sum(x) / len(x) for x in zip(MAP_50M, MAP_50F, MAP_5M, MAP_5F, MAP_95M, MAP_95F, MAP_50M_Athlete, MAP_50F_Athlete, MAP_50M_Dehydrated, MAP_50F_Dehydrated)]

# Find the standard deviation of the HR data at each time point
HR_std = [stdev(x) for x in zip(HR_50M, HR_50F, HR_5M, HR_5F, HR_95M, HR_95F, HR_50M_Athlete, HR_50F_Athlete, HR_50M_Dehydrated, HR_50F_Dehydrated)]
MAP_std = [stdev(x) for x in zip(MAP_50M, MAP_50F, MAP_5M, MAP_5F, MAP_95M, MAP_95F, MAP_50M_Athlete, MAP_50F_Athlete, MAP_50M_Dehydrated, MAP_50F_Dehydrated)]

# Create a plot for the mean and standard deviation of HR data
fig, axs = plt.subplots(1, 3)
fig.suptitle('Mean \u00B1 Standard Deviation Heart Rate and Mean Arterial Pressure in Stepwise Increase')

# Plot gravity level data
axs[0].plot(time, g_level, label='Gravity Level', color='black',linewidth=4)
axs[0].set_xlim(time[0], time[-1])
axs[0].annotate('A', (0.05, 1.02), xycoords='axes fraction', fontsize=12, fontweight='bold', color='black')
axs[0].set_xlabel('Time [sec]')
axs[0].set_ylabel('Gravity Level [g]')
axs[0].set_title('Gravity Level')
plot_vertical_lines_and_regions(axs[0])

# Plot HR data
axs[1].plot(time, HR_mean, label='Mean HR', color='#1c6302')
axs[1].fill_between(time, [x - y for x, y in zip(HR_mean, HR_std)], [x + y for x, y in zip(HR_mean, HR_std)], color='#1c6302', alpha=0.5)
axs[1].set_xlim(time[0], time[-1])
axs[1].annotate('B', (0.05, 1.02), xycoords='axes fraction', fontsize=12, fontweight='bold', color='black')
axs[1].set_xlabel('Time [sec]')
axs[1].set_ylabel('HR [bpm]')
axs[1].set_title('Heart Rate')
plot_vertical_lines_and_regions(axs[1])

# Plot MAP data
axs[2].plot(time, MAP_mean, label='Mean MAP', color='#490263')
axs[2].fill_between(time, [x - y for x, y in zip(MAP_mean, MAP_std)], [x + y for x, y in zip(MAP_mean, MAP_std)], color='#490263', alpha=0.5)
axs[2].set_xlim(time[0], time[-1])
axs[2].annotate('C', (0.05, 1.02), xycoords='axes fraction', fontsize=12, fontweight='bold', color='black')
axs[2].set_xlabel('Time [sec]')
axs[2].set_ylabel('MAP [mmHg]')
axs[2].set_title('Mean Arterial Pressure')
plot_vertical_lines_and_regions(axs[2])

# Adjust layout
plt.tight_layout(rect=[0, 0, 1, 1])
plt.subplots_adjust(hspace=0.3, wspace=0.3)  # Adjust these values to decrease space
plt.show()

'''
fig, axs = plt.subplots(1, 3)
fig.suptitle('Mean and SD of HR in Stepwise Increase')

# Plot HR data
axs[0].plot(time, HR_50M, label='50M', color='blue')
'''
'''
# Create Dehydration Plots

# Create subplots
fig, axs = plt.subplots(2, 4)
fig.suptitle('Response of Dehydration in Stepwise Increase')

# Plot HR data
axs[0, 0].plot(time, HR_50M_Dehydrated, label='50M Dehydrated', color='#729DF9')
axs[0, 0].plot(time, HR_50F_Dehydrated, label='50F Dehydrated', color='#FE968A')
axs[0, 0].plot(time, HR_50M, label='50M', color='blue')
axs[0, 0].plot(time, HR_50F, label='50F', color='red')
axs[0, 0].set_xlabel('Time [sec]')
axs[0, 0].set_ylabel('HR [bpm]')
axs[0, 0].set_title('Heart Rate')
plot_vertical_lines_and_regions(axs[0, 0])

# Plot SV data
axs[0, 1].plot(time, SV_50M_Dehydrated, label='50M Dehydrated', color='#729DF9')
axs[0, 1].plot(time, SV_50F_Dehydrated, label='50F Dehydrated', color='#FE968A')
axs[0, 1].plot(time, SV_50M, label='50M', color='blue')
axs[0, 1].plot(time, SV_50F, label='50F', color='red')
axs[0, 1].set_xlabel('Time [sec]')
axs[0, 1].set_ylabel('SV [mL/beat]')
axs[0, 1].set_title('Stroke Volume')
plot_vertical_lines_and_regions(axs[0, 1])

# Plot CO data
axs[0, 2].plot(time, CO_50M_Dehydrated, label='50M Dehydrated', color='#729DF9')
axs[0, 2].plot(time, CO_50F_Dehydrated, label='50F Dehydrated', color='#FE968A')
axs[0, 2].plot(time, CO_50M, label='50M', color='blue')
axs[0, 2].plot(time, CO_50F, label='50F', color='red')
axs[0, 2].set_xlabel('Time [sec]')
axs[0, 2].set_ylabel('CO [L/min]')
axs[0, 2].set_title('Cardiac Output')
plot_vertical_lines_and_regions(axs[0, 2])

# Plot CI data
axs[0, 3].plot(time, CI_50M_Dehydrated, label='50M Dehydrated', color='#729DF9')
axs[0, 3].plot(time, CI_50F_Dehydrated, label='50F Dehydrated', color='#FE968A')
axs[0, 3].plot(time, CI_50M, label='50M', color='blue')
axs[0, 3].plot(time, CI_50F, label='50F', color='red')
axs[0, 3].set_xlabel('Time [sec]')
axs[0, 3].set_ylabel('CI [L/min/m^2]')
axs[0, 3].set_title('Cardiac Index')
plot_vertical_lines_and_regions(axs[0, 3])

# Plot SBP data
axs[1, 0].plot(time, SBP_50M_Dehydrated, label='50M Dehydrated', color='#729DF9')
axs[1, 0].plot(time, SBP_50F_Dehydrated, label='50F Dehydrated', color='#FE968A')
axs[1, 0].plot(time, SBP_50M, label='50M', color='blue')
axs[1, 0].plot(time, SBP_50F, label='50F', color='red')
axs[1, 0].set_xlabel('Time [sec]')
axs[1, 0].set_ylabel('SBP [mmHg]')
axs[1, 0].set_title('Systolic Blood Pressure')
plot_vertical_lines_and_regions(axs[1, 0])

# Plot DBP data
axs[1, 1].plot(time, DBP_50M_Dehydrated, label='50M Dehydrated', color='#729DF9')
axs[1, 1].plot(time, DBP_50F_Dehydrated, label='50F Dehydrated', color='#FE968A')
axs[1, 1].plot(time, DBP_50M, label='50M', color='blue')
axs[1, 1].plot(time, DBP_50F, label='50F', color='red')
axs[1, 1].set_xlabel('Time [sec]')
axs[1, 1].set_ylabel('DBP [mmHg]')
axs[1, 1].set_title('Diastolic Blood Pressure')
plot_vertical_lines_and_regions(axs[1, 1])

# Plot MAP data
axs[1, 2].plot(time, MAP_50M_Dehydrated, label='50M Dehydrated', color='#729DF9')
axs[1, 2].plot(time, MAP_50F_Dehydrated, label='50F Dehydrated', color='#FE968A')
axs[1, 2].plot(time, MAP_50M, label='50M', color='blue')
axs[1, 2].plot(time, MAP_50F, label='50F', color='red')
axs[1, 2].set_xlabel('Time [sec]')
axs[1, 2].set_ylabel('MAP [mmHg]')
axs[1, 2].set_title('Mean Arterial Pressure')
plot_vertical_lines_and_regions(axs[1, 2])

#  Plot legend in the last subplot
axs[1, 3].axis('off')
handles, labels = axs[1, 2].get_legend_handles_labels()
axs[1, 3].legend(handles, labels, loc='center', bbox_to_anchor=(0.5, 0.5), fontsize='large')

# Adjust layout
plt.tight_layout(rect=[-0.05, -0.05, 1.05, 1.05])
plt.subplots_adjust(hspace=0.4, wspace=0.4)  # Adjust these values to decrease space
plt.show()

############################################################################################################

# Create Athlete Plots

# Create subplots
fig, axs = plt.subplots(2, 4)
fig.suptitle('Response of Athleticism in Stepwise Increase')

# Plot HR data
axs[0, 0].plot(time, HR_50M_Athlete, label='50M Athlete', color='#021466')
axs[0, 0].plot(time, HR_50F_Athlete, label='50F Athlete', color='#971102')
axs[0, 0].plot(time, HR_50M, label='50M', color='blue')
axs[0, 0].plot(time, HR_50F, label='50F', color='red')
axs[0, 0].set_xlabel('Time [sec]')
axs[0, 0].set_ylabel('HR [bpm]')
axs[0, 0].set_title('Heart Rate')
plot_vertical_lines_and_regions(axs[0, 0])

# Plot SV data
axs[0, 1].plot(time, SV_50M_Athlete, label='50M Athlete', color='#021466')
axs[0, 1].plot(time, SV_50F_Athlete, label='50F Athlete', color='#971102')
axs[0, 1].plot(time, SV_50M, label='50M', color='blue')
axs[0, 1].plot(time, SV_50F, label='50F', color='red')
axs[0, 1].set_xlabel('Time [sec]')
axs[0, 1].set_ylabel('SV [mL/beat]')
axs[0, 1].set_title('Stroke Volume')
plot_vertical_lines_and_regions(axs[0, 1])

# Plot CO data
axs[0, 2].plot(time, CO_50M_Athlete, label='50M Athlete', color='#021466')
axs[0, 2].plot(time, CO_50F_Athlete, label='50F Athlete', color='#971102')
axs[0, 2].plot(time, CO_50M, label='50M', color='blue')
axs[0, 2].plot(time, CO_50F, label='50F', color='red')
axs[0, 2].set_xlabel('Time [sec]')
axs[0, 2].set_ylabel('CO [L/min]')
axs[0, 2].set_title('Cardiac Output')
plot_vertical_lines_and_regions(axs[0, 2])

# Plot CI data
axs[0, 3].plot(time, CI_50M_Athlete, label='50M Athlete', color='#021466')
axs[0, 3].plot(time, CI_50F_Athlete, label='50F Athlete', color='#971102')
axs[0, 3].plot(time, CI_50M, label='50M', color='blue')
axs[0, 3].plot(time, CI_50F, label='50F', color='red')
axs[0, 3].set_xlabel('Time [sec]')
axs[0, 3].set_ylabel('CI [L/min/m^2]')
axs[0, 3].set_title('Cardiac Index')
plot_vertical_lines_and_regions(axs[0, 3])

# Plot SBP data
axs[1, 0].plot(time, SBP_50M_Athlete, label='50M Athlete', color='#021466')
axs[1, 0].plot(time, SBP_50F_Athlete, label='50F Athlete', color='#971102')
axs[1, 0].plot(time, SBP_50M, label='50M', color='blue')
axs[1, 0].plot(time, SBP_50F, label='50F', color='red')
axs[1, 0].set_xlabel('Time [sec]')
axs[1, 0].set_ylabel('SBP [mmHg]')
axs[1, 0].set_title('Systolic Blood Pressure')
plot_vertical_lines_and_regions(axs[1, 0])

# Plot DBP data
axs[1, 1].plot(time, DBP_50M_Athlete, label='50M Athlete', color='#021466')
axs[1, 1].plot(time, DBP_50F_Athlete, label='50F Athlete', color='#971102')
axs[1, 1].plot(time, DBP_50M, label='50M', color='blue')
axs[1, 1].plot(time, DBP_50F, label='50F', color='red')
axs[1, 1].set_xlabel('Time [sec]')
axs[1, 1].set_ylabel('DBP [mmHg]')
axs[1, 1].set_title('Diastolic Blood Pressure')
plot_vertical_lines_and_regions(axs[1, 1])

# Plot MAP data
axs[1, 2].plot(time, MAP_50M_Athlete, label='50M Athlete', color='#021466')
axs[1, 2].plot(time, MAP_50F_Athlete, label='50F Athlete', color='#971102')
axs[1, 2].plot(time, MAP_50M, label='50M', color='blue')
axs[1, 2].plot(time, MAP_50F, label='50F', color='red')
axs[1, 2].set_xlabel('Time [sec]')
axs[1, 2].set_ylabel('MAP [mmHg]')
axs[1, 2].set_title('Mean Arterial Pressure')
plot_vertical_lines_and_regions(axs[1, 2])

#  Plot legend in the last subplot
axs[1, 3].axis('off')
handles, labels = axs[1, 2].get_legend_handles_labels()
axs[1, 3].legend(handles, labels, loc='center', bbox_to_anchor=(0.5, 0.5), fontsize='large')

# Adjust layout
plt.tight_layout(rect=[-0.05, -0.05, 1.05, 1.05])
plt.subplots_adjust(hspace=0.4, wspace=0.4)  # Adjust these values to decrease space
plt.show()

############################################################################################################

# Create Anthropometric Plots

# Create subplots
fig, axs = plt.subplots(2, 4)
fig.suptitle('Response of Anthropometrics in Stepwise Increase')

# Plot HR data
axs[0, 0].plot(time, HR_50M, label='50M', color='blue')
axs[0, 0].plot(time, HR_50F, label='50F', color='red')
axs[0, 0].plot(time, HR_5F, label='5F', color='#f5910f')
axs[0, 0].plot(time, HR_5M, label='5M', color='#47ab3c')
axs[0, 0].plot(time, HR_95F, label='95F', color='#8c4103')
axs[0, 0].plot(time, HR_95M, label='95M', color='#0a5702')
axs[0, 0].set_xlabel('Time [sec]')
axs[0, 0].set_ylabel('HR [bpm]')
axs[0, 0].set_title('Heart Rate')
plot_vertical_lines_and_regions(axs[0, 0])

# Plot SV data
axs[0, 1].plot(time, SV_50M, label='50M', color='blue')
axs[0, 1].plot(time, SV_50F, label='50F', color='red')
axs[0, 1].plot(time, SV_5F, label='5F', color='#f5910f')
axs[0, 1].plot(time, SV_5M, label='5M', color='#47ab3c')
axs[0, 1].plot(time, SV_95F, label='95F', color='#8c4103')
axs[0, 1].plot(time, SV_95M, label='95M', color='#0a5702')
axs[0, 1].set_xlabel('Time [sec]')
axs[0, 1].set_ylabel('SV [mL/beat]')
axs[0, 1].set_title('Stroke Volume')
plot_vertical_lines_and_regions(axs[0, 1])

# Plot CO data
axs[0, 2].plot(time, CO_50M, label='50M', color='blue')
axs[0, 2].plot(time, CO_50F, label='50F', color='red')
axs[0, 2].plot(time, CO_5F, label='5F', color='#f5910f')
axs[0, 2].plot(time, CO_5M, label='5M', color='#47ab3c')
axs[0, 2].plot(time, CO_95F, label='95F', color='#8c4103')
axs[0, 2].plot(time, CO_95M, label='95M', color='#0a5702')
axs[0, 2].set_xlabel('Time [sec]')
axs[0, 2].set_ylabel('CO [L/min]')
axs[0, 2].set_title('Cardiac Output')
plot_vertical_lines_and_regions(axs[0, 2])

# Plot CI data
axs[0, 3].plot(time, CI_50M, label='50M', color='blue')
axs[0, 3].plot(time, CI_50F, label='50F', color='red')
axs[0, 3].plot(time, CI_5F, label='5F', color='#f5910f')
axs[0, 3].plot(time, CI_5M, label='5M', color='#47ab3c')
axs[0, 3].plot(time, CI_95F, label='95F', color='#8c4103')
axs[0, 3].plot(time, CI_95M, label='95M', color='#0a5702')
axs[0, 3].set_xlabel('Time [sec]')
axs[0, 3].set_ylabel('CI [L/min/m^2]')
axs[0, 3].set_title('Cardiac Index')
plot_vertical_lines_and_regions(axs[0, 3])

# Plot SBP data
axs[1, 0].plot(time, SBP_50M, label='50M', color='blue')
axs[1, 0].plot(time, SBP_50F, label='50F', color='red')
axs[1, 0].plot(time, SBP_5F, label='5F', color='#f5910f')
axs[1, 0].plot(time, SBP_5M, label='5M', color='#47ab3c')
axs[1, 0].plot(time, SBP_95F, label='95F', color='#8c4103')
axs[1, 0].plot(time, SBP_95M, label='95M', color='#0a5702')
axs[1, 0].set_xlabel('Time [sec]')
axs[1, 0].set_ylabel('SBP [mmHg]')
axs[1, 0].set_title('Systolic Blood Pressure')
plot_vertical_lines_and_regions(axs[1, 0])

# Plot DBP data
axs[1, 1].plot(time, DBP_50M, label='50M', color='blue')
axs[1, 1].plot(time, DBP_50F, label='50F', color='red')
axs[1, 1].plot(time, DBP_5F, label='5F', color='#f5910f')
axs[1, 1].plot(time, DBP_5M, label='5M', color='#47ab3c')

axs[1, 1].plot(time, DBP_95F, label='95F', color='#8c4103')
axs[1, 1].plot(time, DBP_95M, label='95M', color='#0a5702')
axs[1, 1].set_xlabel('Time [sec]')
axs[1, 1].set_ylabel('DBP [mmHg]')
axs[1, 1].set_title('Diastolic Blood Pressure')
plot_vertical_lines_and_regions(axs[1, 1])

# Plot MAP data
axs[1, 2].plot(time, MAP_50M, label='50M', color='blue')
axs[1, 2].plot(time, MAP_50F, label='50F', color='red')
axs[1, 2].plot(time, MAP_5F, label='5F', color='#f5910f')
axs[1, 2].plot(time, MAP_5M, label='5M', color='#47ab3c')
axs[1, 2].plot(time, MAP_95F, label='95F', color='#8c4103')
axs[1, 2].plot(time, MAP_95M, label='95M', color='#0a5702')
axs[1, 2].set_xlabel('Time [sec]')
axs[1, 2].set_ylabel('MAP [mmHg]')
axs[1, 2].set_title('Mean Arterial Pressure')
plot_vertical_lines_and_regions(axs[1, 2])

#  Plot legend in the last subplot
axs[1, 3].axis('off')
handles, labels = axs[1, 2].get_legend_handles_labels()
axs[1, 3].legend(handles, labels, loc='center', bbox_to_anchor=(0.5, 0.5), fontsize='large')

# Adjust layout
plt.tight_layout(rect=[0, 0, 1, 1])
plt.subplots_adjust(hspace=0.3, wspace=0.3)  # Adjust these values to decrease space
plt.show()
'''

