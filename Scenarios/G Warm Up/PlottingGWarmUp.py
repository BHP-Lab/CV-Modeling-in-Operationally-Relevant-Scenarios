import pandas as pd
import os
import matplotlib.pyplot as plt

file_path = 'GWarmUp.xls'

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

'''
# Create a method to hold plotting code for the vertical lines and shaded regions
def plot_vertical_lines_and_regions(ax):
    # Add a vertical lines
    plt.axvline(x=2, color='black')
    plt.axvline(x=4, color='black')
    plt.axvline(x=13, color='black')
    plt.axvline(x=15, color='black')
    plt.axvline(x=19, color='black')
    plt.axvline(x=21, color='black')
    plt.axvline(x=30, color='black')
    # Add a region to the plot
    plt.axvspan(4, 13, facecolor='#ded1fa', alpha=0.5)
    plt.axvspan(15, 19, facecolor='#d1faea', alpha=0.5)
    plt.axvspan(21, 30, facecolor='#ded1fa', alpha=0.5)
'''
# Define the function to plot vertical lines and regions
def plot_vertical_lines_and_regions(ax):
    # Add vertical lines
    ax.axvline(x=2, color='grey', linewidth = 2)
    ax.axvline(x=4, color='grey', linewidth = 2)
    ax.axvline(x=13, color='grey', linewidth = 2)
    ax.axvline(x=15, color='grey', linewidth = 2)
    ax.axvline(x=19, color='grey', linewidth = 2)
    ax.axvline(x=21, color='grey', linewidth = 2)
    ax.axvline(x=30, color='grey', linewidth = 2)
    # Add regions to the plot
    ax.axvspan(0, 2, facecolor= '#F6E8A4', alpha=0.5)
    ax.axvspan(4, 13, facecolor='#CEECAE', alpha=0.5)
    ax.axvspan(15, 19, facecolor='#F6E8A4', alpha=0.5)
    ax.axvspan(21, 30, facecolor='#CEECAE', alpha=0.5)
    ax.axvspan(30, 31, facecolor='#F6E8A4', alpha=0.5)

# Importing data from another Excel file
data5M_Parabolic = pd.read_excel(r"C:\Users\hruda\OneDrive\Desktop\Subject Database\Subject Database\Scenarios\Parabolic Flight\ParabolicFlight.xls", sheet_name='5M')
g_level_Parabolic = data5M_Parabolic.iloc[:, 1].tolist()
time_Parabolic = data5M_Parabolic.iloc[:, 0].tolist()

print(g_level)
print(g_level_Parabolic)

g_level = [1.0, 1.0, 2.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 2.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 1.0]
g_level_Parabolic = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.4, 1.8, 1.8, 1.8, 1.8, 1.8, 1.8, 1.8, 1.8, 1.8, 1.8, 1.8, 1.8, 1.8, 1.8, 1.8, 1.8, 1.8, 1.8, 1.8, 1.8, 0.9, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.9, 1.8, 1.8, 1.8, 1.8, 1.8, 1.8, 1.8, 1.8, 1.8, 1.8, 1.8, 1.8, 1.8, 1.8, 1.8, 1.8, 1.8, 1.8, 1.8, 1.8, 1.4, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
# Create a plot with two subplots
fig, axs = plt.subplots(1, 2)
fig.suptitle('Gravitational Profiles of G Warm Up and Parabolic Flight')

# Plot the G Warm Up data
plot_vertical_lines_and_regions(axs[0])
axs[0].plot(time, g_level, label='G Warm Up', color='black', linewidth = 3)
axs[0].set_xlabel('Time [sec]')
axs[0].set_ylabel('G Level [g]')
axs[0].set_title('Gravitational Profile of G Warm Up')
axs[0].set_xlim(time[0], time[-1])

# Plot the Parabolic Flight data
axs[1].axvline(x=20, color='grey', linewidth = 2)
axs[1].axvline(x=21, color='grey', linewidth = 2)
axs[1].axvline(x=41, color='grey', linewidth = 2)
axs[1].axvline(x=42, color='grey', linewidth = 2)
axs[1].axvline(x=62, color='grey', linewidth = 2)
axs[1].axvline(x=63, color='grey', linewidth = 2)
axs[1].axvline(x=83, color='grey', linewidth = 2)
axs[1].axvline(x=84, color='grey', linewidth = 2)
# Add shaded regions
axs[1].axvspan(0, 20, facecolor='#F6E8A4', alpha=0.5)
axs[1].axvspan(21, 41, facecolor='#CEE8FE', alpha=0.5)
axs[1].axvspan(42, 62, facecolor='#FECEFE', alpha=0.5)
axs[1].axvspan(63, 83, facecolor='#CEE8FE', alpha=0.5)
axs[1].axvspan(84, 104, facecolor='#F6E8A4', alpha=0.5)
axs[1].plot(time_Parabolic, g_level_Parabolic, label='Parabolic Flight', color='black', linewidth = 3)
axs[1].set_xlabel('Time [sec]')
axs[1].set_ylabel('G Level [g]')
axs[1].set_title('Gravitational Profile of Parabolic Flight')
axs[1].set_xlim(time_Parabolic[0], time_Parabolic[-1])

ax = plt.gca()

# Plot the plot
plt.show()




'''
# Plot all the HR data
plt.plot(time, HR_5M, label='5TH PCTL M', color='#47ab3c')
plt.plot(time, HR_5F, label='5TH PCTL F', color='#f5910f')
plt.plot(time, HR_50M, label='50TH PCTL M', color='blue')
plt.plot(time, HR_50F, label='50TH PCTL F', color='red')
plt.plot(time, HR_95M, label='95TH PCTL M', color='#0a5702')
plt.plot(time, HR_95F, label='95TH PCTL F', color='#8c4103')

# Add a vertical lines and regions
plot_vertical_lines_and_regions()

# Add labels and title
plt.xlabel('Time [sec]')
plt.ylabel('HR [bpm]')
plt.title('Heart Rate in G Warm Up')
plt.legend()
# Save this plot
# plt.savefig('HR_GWarmUp.png')
plt.show()

plt.plot(time, HR_50M_Dehydrated, label='50th PCTL M Dehydrated', color = '#729DF9')
plt.plot(time, HR_50F_Dehydrated, label='50th PCTL F Dehydrated', color = '#FE968A')
plt.plot(time, HR_50M, label='50TH PCTL M', color='blue')
plt.plot(time, HR_50F, label='50TH PCTL F', color='red')
# Add vertical lines and regions
plot_vertical_lines_and_regions()

# Add legend
plt.legend()
# Add labels and title
plt.xlabel('Time [sec]')
plt.ylabel('HR [bpm]')
plt.title('Heart Rate in G Warm Up')
plt.show()

plt.plot(time, HR_50M_Athlete, label='50th PCTL M Athletic', color = '#021466')
plt.plot(time, HR_50F_Athlete, label='50th PCTL F Athletic', color = '#971102')
plt.plot(time, HR_50M, label='50TH PCTL M', color='blue')
plt.plot(time, HR_50F, label='50TH PCTL F', color='red')
# Add vertical lines and regions
plot_vertical_lines_and_regions()
# Add legend
plt.legend()
# Add labels and title
plt.xlabel('Time [sec]')
plt.ylabel('HR [bpm]')
plt.title('Heart Rate in G Warm Up')
plt.show()
    
############################################################################################################

# Plot all the CO data
plt.plot(time, CO_5M, label='5TH PCTL M', color='#47ab3c')
plt.plot(time, CO_5F, label='5TH PCTL F', color='#f5910f')
plt.plot(time, CO_50M, label='50TH PCTL M', color='blue')
plt.plot(time, CO_50F, label='50TH PCTL F', color='red')
plt.plot(time, CO_95M, label='95TH PCTL M', color='#0a5702')
plt.plot(time, CO_95F, label='95TH PCTL F', color='#8c4103')

# Add a vertical lines and regions
plot_vertical_lines_and_regions()

# Add legend
plt.legend()
# Add labels and title
plt.xlabel('Time [sec]')
plt.ylabel('CO [L/min]')
plt.title('Cardiac Output in G Warm Up')

# Save this plot
# plt.savefig('HR_GWarmUp.png')
plt.show()

# Plot dehydrated CO data
plt.plot(time, CO_50M_Dehydrated, label='50th PCTL M Dehydrated', color = '#729DF9')
plt.plot(time, CO_50F_Dehydrated, label='50th PCTL F Dehydrated', color = '#FE968A')
plt.plot(time, CO_50M, label='50TH PCTL M', color='blue')
plt.plot(time, CO_50F, label='50TH PCTL F', color='red')
# Add vertical lines and regions
plot_vertical_lines_and_regions()

# Add legend
plt.legend()
# Add labels and title
plt.xlabel('Time [sec]')
plt.ylabel('CO [L/min]')
plt.title('Cardiac Output in G Warm Up')
plt.show()

# Plot athlete CO data
plt.plot(time, CO_50M_Athlete, label='50th PCTL M Athletic', color = '#021466')
plt.plot(time, CO_50F_Athlete, label='50th PCTL F Athletic', color = '#971102')
plt.plot(time, CO_50M, label='50TH PCTL M', color='blue')
plt.plot(time, CO_50F, label='50TH PCTL F', color='red')
# Add vertical lines and regions
plot_vertical_lines_and_regions()
# Add legend
plt.legend()
# Add labels and title
plt.xlabel('Time [sec]')
plt.ylabel('CO [L/min]')
plt.title('Cardiac Output in G Warm Up')
plt.show()

############################################################################################################

# Plot all the CI data
plt.plot(time, CI_5M, label='5TH PCTL M', color='#47ab3c')
plt.plot(time, CI_5F, label='5TH PCTL F', color='#f5910f')
plt.plot(time, CI_50M, label='50TH PCTL M', color='blue')
plt.plot(time, CI_50F, label='50TH PCTL F', color='red')
plt.plot(time, CI_95M, label='95TH PCTL M', color='#0a5702')
plt.plot(time, CI_95F, label='95TH PCTL F', color='#8c4103')

# Add a vertical lines and regions
plot_vertical_lines_and_regions()

# Add legend
plt.legend()
# Add labels and title
plt.xlabel('Time [sec]')
plt.ylabel('CI [L/min/m^2]')
plt.title('Cardiac Index in G Warm Up')
plt.show()

# Plot dehydrated CI data
plt.plot(time, CI_50M_Dehydrated, label='50th PCTL M Dehydrated', color = '#729DF9')
plt.plot(time, CI_50F_Dehydrated, label='50th PCTL F Dehydrated', color = '#FE968A')
plt.plot(time, CI_50M, label='50TH PCTL M', color='blue')
plt.plot(time, CI_50F, label='50TH PCTL F', color='red')
# Add vertical lines and regions
plot_vertical_lines_and_regions()

# Add legend
plt.legend()
# Add labels and title
plt.xlabel('Time [sec]')
plt.ylabel('CI [L/min/m^2]')
plt.title('Cardiac Index in G Warm Up')
plt.show()

# Plot athlete CI data
plt.plot(time, CI_50M_Athlete, label='50th PCTL M Athletic', color = '#021466')
plt.plot(time, CI_50F_Athlete, label='50th PCTL F Athletic', color = '#971102')
plt.plot(time, CI_50M, label='50TH PCTL M', color='blue')
plt.plot(time, CI_50F, label='50TH PCTL F', color='red')
# Add vertical lines and regions
plot_vertical_lines_and_regions()

# Add legend
plt.legend()
# Add labels and title
plt.xlabel('Time [sec]')
plt.ylabel('CI [L/min/m^2]')
plt.title('Cardiac Index in G Warm Up')
plt.show()

############################################################################################################

# Plot all the SBP data
plt.plot(time, SBP_5M, label='5TH PCTL M', color='#47ab3c')
plt.plot(time, SBP_5F, label='5TH PCTL F', color='#f5910f')
plt.plot(time, SBP_50M, label='50TH PCTL M', color='blue')
plt.plot(time, SBP_50F, label='50TH PCTL F', color='red')
plt.plot(time, SBP_95M, label='95TH PCTL M', color='#0a5702')
plt.plot(time, SBP_95F, label='95TH PCTL F', color='#8c4103')

# Add a vertical lines and regions
plot_vertical_lines_and_regions()

# Add legend
plt.legend()
# Add labels and title
plt.xlabel('Time [sec]')
plt.ylabel('SBP [mmHg]')
plt.title('Systolic Blood Pressure in G Warm Up')
plt.show()

# Plot dehydrated SBP data
plt.plot(time, SBP_50M_Dehydrated, label='50th PCTL M Dehydrated', color = '#729DF9')
plt.plot(time, SBP_50F_Dehydrated, label='50th PCTL F Dehydrated', color = '#FE968A')
plt.plot(time, SBP_50M, label='50TH PCTL M', color='blue')
plt.plot(time, SBP_50F, label='50TH PCTL F', color='red')
# Add vertical lines and regions
plot_vertical_lines_and_regions()

# Add legend
plt.legend()
# Add labels and title
plt.xlabel('Time [sec]')
plt.ylabel('SBP [mmHg]')
plt.title('Systolic Blood Pressure in G Warm Up')
plt.show()

# Plot athlete SBP data
plt.plot(time, SBP_50M_Athlete, label='50th PCTL M Athletic', color = '#021466')
plt.plot(time, SBP_50F_Athlete, label='50th PCTL F Athletic', color = '#971102')
plt.plot(time, SBP_50M, label='50TH PCTL M', color='blue')
plt.plot(time, SBP_50F, label='50TH PCTL F', color='red')
# Add vertical lines and regions
plot_vertical_lines_and_regions()

# Add legend
plt.legend()
# Add labels and title
plt.xlabel('Time [sec]')
plt.ylabel('SBP [mmHg]')
plt.title('Systolic Blood Pressure in G Warm Up')
plt.show()

############################################################################################################

# Plot all the DBP data
plt.plot(time, DBP_5M, label='5TH PCTL M', color='#47ab3c')
plt.plot(time, DBP_5F, label='5TH PCTL F', color='#f5910f')
plt.plot(time, DBP_50M, label='50TH PCTL M', color='blue')
plt.plot(time, DBP_50F, label='50TH PCTL F', color='red')
plt.plot(time, DBP_95M, label='95TH PCTL M', color='#0a5702')
plt.plot(time, DBP_95F, label='95TH PCTL F', color='#8c4103')

# Add a vertical lines and regions
plot_vertical_lines_and_regions()

# Add legend
plt.legend()
# Add labels and title
plt.xlabel('Time [sec]')
plt.ylabel('DBP [mmHg]')
plt.title('Diastolic Blood Pressure in G Warm Up')
plt.show()

# Plot dehydrated DBP data
plt.plot(time, DBP_50M_Dehydrated, label='50th PCTL M Dehydrated', color = '#729DF9')
plt.plot(time, DBP_50F_Dehydrated, label='50th PCTL F Dehydrated', color = '#FE968A')
plt.plot(time, DBP_50M, label='50TH PCTL M', color='blue')
plt.plot(time, DBP_50F, label='50TH PCTL F', color='red')
# Add vertical lines and regions
plot_vertical_lines_and_regions()

# Add legend
plt.legend()
# Add labels and title
plt.xlabel('Time [sec]')
plt.ylabel('DBP [mmHg]')
plt.title('Diastolic Blood Pressure in G Warm Up')
plt.show()

# Plot athlete DBP data
plt.plot(time, DBP_50M_Athlete, label='50th PCTL M Athletic', color = '#021466')
plt.plot(time, DBP_50F_Athlete, label='50th PCTL F Athletic', color = '#971102')
plt.plot(time, DBP_50M, label='50TH PCTL M', color='blue')
plt.plot(time, DBP_50F, label='50TH PCTL F', color='red')
# Add vertical lines and regions
plot_vertical_lines_and_regions()

# Add legend
plt.legend()
# Add labels and title
plt.xlabel('Time [sec]')
plt.ylabel('DBP [mmHg]')
plt.title('Diastolic Blood Pressure in G Warm Up')
plt.show()

############################################################################################################

# Plot all the MAP data
plt.plot(time, MAP_5M, label='5TH PCTL M', color='#47ab3c')
plt.plot(time, MAP_5F, label='5TH PCTL F', color='#f5910f')
plt.plot(time, MAP_50M, label='50TH PCTL M', color='blue')
plt.plot(time, MAP_50F, label='50TH PCTL F', color='red')
plt.plot(time, MAP_95M, label='95TH PCTL M', color='#0a5702')
plt.plot(time, MAP_95F, label='95TH PCTL F', color='#8c4103')

# Add a vertical lines and regions
plot_vertical_lines_and_regions()

# Add legend
plt.legend()
# Add labels and title
plt.xlabel('Time [sec]')
plt.ylabel('MAP [mmHg]')
plt.title('Mean Arterial Pressure in G Warm Up')
plt.show()

# Plot dehydrated MAP data
plt.plot(time, MAP_50M_Dehydrated, label='50th PCTL M Dehydrated', color = '#729DF9')
plt.plot(time, MAP_50F_Dehydrated, label='50th PCTL F Dehydrated', color = '#FE968A')
plt.plot(time, MAP_50M, label='50TH PCTL M', color='blue')
plt.plot(time, MAP_50F, label='50TH PCTL F', color='red')
# Add vertical lines and regions
plot_vertical_lines_and_regions()

# Add legend
plt.legend()
# Add labels and title
plt.xlabel('Time [sec]')
plt.ylabel('MAP [mmHg]')
plt.title('Mean Arterial Pressure in G Warm Up')
plt.show()

# Plot athlete MAP data
plt.plot(time, MAP_50M_Athlete, label='50th PCTL M Athletic', color = '#021466')
plt.plot(time, MAP_50F_Athlete, label='50th PCTL F Athletic', color = '#971102')
plt.plot(time, MAP_50M, label='50TH PCTL M', color='blue')
plt.plot(time, MAP_50F, label='50TH PCTL F', color='red')
# Add vertical lines and regions
plot_vertical_lines_and_regions()

# Add legend
plt.legend()
# Add labels and title
plt.xlabel('Time [sec]')
plt.ylabel('MAP [mmHg]')
plt.title('Mean Arterial Pressure in G Warm Up')
plt.show()

############################################################################################################

# Plot all the SV data
plt.plot(time, SV_5M, label='5TH PCTL M', color='#47ab3c')
plt.plot(time, SV_5F, label='5TH PCTL F', color='#f5910f')
plt.plot(time, SV_50M, label='50TH PCTL M', color='blue')
plt.plot(time, SV_50F, label='50TH PCTL F', color='red')
plt.plot(time, SV_95M, label='95TH PCTL M', color='#0a5702')
plt.plot(time, SV_95F, label='95TH PCTL F', color='#8c4103')

# Add a vertical lines and regions
plot_vertical_lines_and_regions()

# Add legend
plt.legend()
# Add labels and title
plt.xlabel('Time [sec]')
plt.ylabel('SV [mL/beat]')
plt.title('Stroke Volume in G Warm Up')
plt.show()

# Plot dehydrated SV data
plt.plot(time, SV_50M_Dehydrated, label='50th PCTL M Dehydrated', color = '#729DF9')
plt.plot(time, SV_50F_Dehydrated, label='50th PCTL F Dehydrated', color = '#FE968A')
plt.plot(time, SV_50M, label='50TH PCTL M', color='blue')
plt.plot(time, SV_50F, label='50TH PCTL F', color='red')
# Add vertical lines and regions
plot_vertical_lines_and_regions()

# Add legend
plt.legend()
# Add labels and title
plt.xlabel('Time [sec]')
plt.ylabel('SV [mL/beat]')
plt.title('Stroke Volume in G Warm Up')
plt.show()

# Plot athlete SV data
plt.plot(time, SV_50M_Athlete, label='50th PCTL M Athletic', color = '#021466')
plt.plot(time, SV_50F_Athlete, label='50th PCTL F Athletic', color = '#971102')
plt.plot(time, SV_50M, label='50TH PCTL M', color='blue')
plt.plot(time, SV_50F, label='50TH PCTL F', color='red')
# Add vertical lines and regions
plot_vertical_lines_and_regions()

# Add legend
plt.legend()
# Add labels and title
plt.xlabel('Time [sec]')
plt.ylabel('SV [mL/beat]')
plt.title('Stroke Volume in G Warm Up')
# plt.show()
'''
############################################################################################################

# Create a method to hold plotting code for the vertical lines and shaded regions
def plot_vertical_lines_and_regions(ax):
    # Add vertical lines
    ax.axvline(x=2, color='grey', linewidth = 1)
    ax.axvline(x=4, color='grey', linewidth = 1)
    ax.axvline(x=13, color='grey', linewidth = 1)
    ax.axvline(x=15, color='grey', linewidth = 1)
    ax.axvline(x=19, color='grey', linewidth = 1)
    ax.axvline(x=21, color='grey', linewidth = 1)
    ax.axvline(x=30, color='grey', linewidth = 1)
    # Add regions to the plot
    ax.axvspan(0, 2, facecolor= '#F6E8A4', alpha=0.5)
    ax.axvspan(4, 13, facecolor='#CEECAE', alpha=0.5)
    ax.axvspan(15, 19, facecolor='#F6E8A4', alpha=0.5)
    ax.axvspan(21, 30, facecolor='#CEECAE', alpha=0.5)
    ax.axvspan(30, 31, facecolor='#F6E8A4', alpha=0.5) ############################ DOUBLE CHECK ########################################3
    

############################################################################################################

# Create Dehydration Plots

# Create subplots
fig, axs = plt.subplots(2, 4)
fig.suptitle('Response of Dehydration in G Warm Up')

# Plot HR data
axs[0, 0].plot(time, HR_50M_Dehydrated, label='50th PCTL M Dehydrated', color='#729DF9')
axs[0, 0].plot(time, HR_50F_Dehydrated, label='50th PCTL F Dehydrated', color='#FE968A')
axs[0, 0].plot(time, HR_50M, label='50th PCTL M', color='blue')
axs[0, 0].plot(time, HR_50F, label='50th PCTL F', color='red')
axs[0, 0].set_xlabel('Time [sec]')
axs[0, 0].set_ylabel('HR [bpm]')
axs[0, 0].set_title('Heart Rate')
axs[0, 0].set_xlim(time[0], time[-1])
axs[0, 0].annotate('A', (0.02, 1.02), xycoords='axes fraction', fontsize=10, fontweight='bold', color='black')
plot_vertical_lines_and_regions(axs[0, 0])

# Plot SV data
axs[0, 1].plot(time, SV_50M_Dehydrated, label='50th PCTL M Dehydrated', color='#729DF9')
axs[0, 1].plot(time, SV_50F_Dehydrated, label='50th PCTL F Dehydrated', color='#FE968A')
axs[0, 1].plot(time, SV_50M, label='50th PCTL M', color='blue')
axs[0, 1].plot(time, SV_50F, label='50th PCTL F', color='red')
axs[0, 1].set_xlabel('Time [sec]')
axs[0, 1].set_ylabel('SV [mL/beat]')
axs[0, 1].set_title('Stroke Volume')
axs[0, 1].set_xlim(time[0], time[-1])
axs[0, 1].annotate('B', (0.02, 1.02), xycoords='axes fraction', fontsize=10, fontweight='bold', color='black')
plot_vertical_lines_and_regions(axs[0, 1])

# Plot CO data
axs[0, 2].plot(time, CO_50M_Dehydrated, label='50th PCTL M Dehydrated', color='#729DF9')
axs[0, 2].plot(time, CO_50F_Dehydrated, label='50th PCTL F Dehydrated', color='#FE968A')
axs[0, 2].plot(time, CO_50M, label='50th PCTL M', color='blue')
axs[0, 2].plot(time, CO_50F, label='50th PCTL F', color='red')
axs[0, 2].set_xlabel('Time [sec]')
axs[0, 2].set_ylabel('CO [L/min]')
axs[0, 2].set_title('Cardiac Output')
axs[0, 2].set_xlim(time[0], time[-1])
axs[0, 2].annotate('C', (0.02, 1.02), xycoords='axes fraction', fontsize=10, fontweight='bold', color='black')
plot_vertical_lines_and_regions(axs[0, 2])

# Plot CI data
axs[0, 3].plot(time, CI_50M_Dehydrated, label='50th PCTL M Dehydrated', color='#729DF9')
axs[0, 3].plot(time, CI_50F_Dehydrated, label='50th PCTL F Dehydrated', color='#FE968A')
axs[0, 3].plot(time, CI_50M, label='50th PCTL M', color='blue')
axs[0, 3].plot(time, CI_50F, label='50th PCTL F', color='red')
axs[0, 3].set_xlabel('Time [sec]')
axs[0, 3].set_ylabel('CI [L/min/m^2]')
axs[0, 3].set_title('Cardiac Index')
axs[0, 3].set_xlim(time[0], time[-1])
axs[0, 3].annotate('D', (0.02, 1.02), xycoords='axes fraction', fontsize=10, fontweight='bold', color='black')
plot_vertical_lines_and_regions(axs[0, 3])

# Plot SBP data
axs[1, 0].plot(time, SBP_50M_Dehydrated, label='50th PCTL M Dehydrated', color='#729DF9')
axs[1, 0].plot(time, SBP_50F_Dehydrated, label='50th PCTL F Dehydrated', color='#FE968A')
axs[1, 0].plot(time, SBP_50M, label='50th PCTL M', color='blue')
axs[1, 0].plot(time, SBP_50F, label='50th PCTL F', color='red')
axs[1, 0].set_xlabel('Time [sec]')
axs[1, 0].set_ylabel('SBP [mmHg]')
axs[1, 0].set_title('Systolic Blood Pressure')
axs[1, 0].set_xlim(time[0], time[-1])
axs[1, 0].annotate('E', (0.02, 1.02), xycoords='axes fraction', fontsize=10, fontweight='bold', color='black')
plot_vertical_lines_and_regions(axs[1, 0])

# Plot DBP data
axs[1, 1].plot(time, DBP_50M_Dehydrated, label='50th PCTL M Dehydrated', color='#729DF9')
axs[1, 1].plot(time, DBP_50F_Dehydrated, label='50th PCTL F Dehydrated', color='#FE968A')
axs[1, 1].plot(time, DBP_50M, label='50th PCTL M', color='blue')
axs[1, 1].plot(time, DBP_50F, label='50th PCTL F', color='red')
axs[1, 1].set_xlabel('Time [sec]')
axs[1, 1].set_ylabel('DBP [mmHg]')
axs[1, 1].set_title('Diastolic Blood Pressure')
axs[1, 1].set_xlim(time[0], time[-1])
axs[1, 1].annotate('F', (0.02, 1.02), xycoords='axes fraction', fontsize=10, fontweight='bold', color='black')
plot_vertical_lines_and_regions(axs[1, 1])

# Plot MAP data
axs[1, 2].plot(time, MAP_50M_Dehydrated, label='50th PCTL M Dehydrated', color='#729DF9')
axs[1, 2].plot(time, MAP_50F_Dehydrated, label='50th PCTL F Dehydrated', color='#FE968A')
axs[1, 2].plot(time, MAP_50M, label='50th PCTL M', color='blue')
axs[1, 2].plot(time, MAP_50F, label='50th PCTL F', color='red')
axs[1, 2].set_xlabel('Time [sec]')
axs[1, 2].set_ylabel('MAP [mmHg]')
axs[1, 2].set_title('Mean Arterial Pressure')
axs[1, 2].set_xlim(time[0], time[-1])
axs[1, 2].annotate('G', (0.02, 1.02), xycoords='axes fraction', fontsize=10, fontweight='bold', color='black')
plot_vertical_lines_and_regions(axs[1, 2])

#  Plot legend in the last subplot
axs[1, 3].axis('off')
handles, labels = axs[1, 2].get_legend_handles_labels()
axs[1, 3].legend(handles, labels, loc='center', bbox_to_anchor=(0.5, 0.5), fontsize='large', frameon=False)

# Adjust layout
plt.tight_layout(rect=[-0.05, -0.05, 1.05, 1.05])
plt.subplots_adjust(hspace=0.4, wspace=0.4)  # Adjust these values to decrease space
plt.show()

############################################################################################################

# Create Athlete Plots

# Create subplots
fig, axs = plt.subplots(2, 4)
fig.suptitle('Response of Athleticism in G Warm Up')

# Plot HR data
axs[0, 0].plot(time, HR_50M_Athlete, label='50th PCTL M Athletic', color='#021466')
axs[0, 0].plot(time, HR_50F_Athlete, label='50th PCTL F Athletic', color='#971102')
axs[0, 0].plot(time, HR_50M, label='50th PCTL M', color='blue')
axs[0, 0].plot(time, HR_50F, label='50th PCTL F', color='red')
axs[0, 0].set_xlabel('Time [sec]')
axs[0, 0].set_ylabel('HR [bpm]')
axs[0, 0].set_title('Heart Rate')
axs[0, 0].set_xlim(time[0], time[-1])
axs[0, 0].annotate('A', (0.02, 1.02), xycoords='axes fraction', fontsize=10, fontweight='bold', color='black')
plot_vertical_lines_and_regions(axs[0, 0])

# Plot SV data
axs[0, 1].plot(time, SV_50M_Athlete, label='50th PCTL M Athletic', color='#021466')
axs[0, 1].plot(time, SV_50F_Athlete, label='50th PCTL F Athletic', color='#971102')
axs[0, 1].plot(time, SV_50M, label='50th PCTL M', color='blue')
axs[0, 1].plot(time, SV_50F, label='50th PCTL F', color='red')
axs[0, 1].set_xlabel('Time [sec]')
axs[0, 1].set_ylabel('SV [mL/beat]')
axs[0, 1].set_title('Stroke Volume')
axs[0, 1].set_xlim(time[0], time[-1])
axs[0, 1].annotate('B', (0.02, 1.02), xycoords='axes fraction', fontsize=10, fontweight='bold', color='black')
plot_vertical_lines_and_regions(axs[0, 1])

# Plot CO data
axs[0, 2].plot(time, CO_50M_Athlete, label='50th PCTL M Athletic', color='#021466')
axs[0, 2].plot(time, CO_50F_Athlete, label='50th PCTL F Athletic', color='#971102')
axs[0, 2].plot(time, CO_50M, label='50th PCTL M', color='blue')
axs[0, 2].plot(time, CO_50F, label='50th PCTL F', color='red')
axs[0, 2].set_xlabel('Time [sec]')
axs[0, 2].set_ylabel('CO [L/min]')
axs[0, 2].set_title('Cardiac Output')
axs[0, 2].set_xlim(time[0], time[-1])
axs[0, 2].annotate('C', (0.02, 1.02), xycoords='axes fraction', fontsize=10, fontweight='bold', color='black')
plot_vertical_lines_and_regions(axs[0, 2])

# Plot CI data
axs[0, 3].plot(time, CI_50M_Athlete, label='50th PCTL M Athletic', color='#021466')
axs[0, 3].plot(time, CI_50F_Athlete, label='50th PCTL F Athletic', color='#971102')
axs[0, 3].plot(time, CI_50M, label='50th PCTL M', color='blue')
axs[0, 3].plot(time, CI_50F, label='50th PCTL F', color='red')
axs[0, 3].set_xlabel('Time [sec]')
axs[0, 3].set_ylabel('CI [L/min/m^2]')
axs[0, 3].set_title('Cardiac Index')
axs[0, 3].set_xlim(time[0], time[-1])
axs[0, 3].annotate('D', (0.02, 1.02), xycoords='axes fraction', fontsize=10, fontweight='bold', color='black')
plot_vertical_lines_and_regions(axs[0, 3])

# Plot SBP data
axs[1, 0].plot(time, SBP_50M_Athlete, label='50th PCTL M Athletic', color='#021466')
axs[1, 0].plot(time, SBP_50F_Athlete, label='50th PCTL F Athletic', color='#971102')
axs[1, 0].plot(time, SBP_50M, label='50th PCTL M', color='blue')
axs[1, 0].plot(time, SBP_50F, label='50th PCTL F', color='red')
axs[1, 0].set_xlabel('Time [sec]')
axs[1, 0].set_ylabel('SBP [mmHg]')
axs[1, 0].set_title('Systolic Blood Pressure')
axs[1, 0].set_xlim(time[0], time[-1])
axs[1, 0].annotate('E', (0.02, 1.02), xycoords='axes fraction', fontsize=10, fontweight='bold', color='black')
plot_vertical_lines_and_regions(axs[1, 0])

# Plot DBP data
axs[1, 1].plot(time, DBP_50M_Athlete, label='50th PCTL M Athletic', color='#021466')
axs[1, 1].plot(time, DBP_50F_Athlete, label='50th PCTL F Athletic', color='#971102')
axs[1, 1].plot(time, DBP_50M, label='50th PCTL M', color='blue')
axs[1, 1].plot(time, DBP_50F, label='50th PCTL F', color='red')
axs[1, 1].set_xlabel('Time [sec]')
axs[1, 1].set_ylabel('DBP [mmHg]')
axs[1, 1].set_title('Diastolic Blood Pressure')
axs[1, 1].set_xlim(time[0], time[-1])
axs[1, 1].annotate('F', (0.02, 1.02), xycoords='axes fraction', fontsize=10, fontweight='bold', color='black')
plot_vertical_lines_and_regions(axs[1, 1])

# Plot MAP data
axs[1, 2].plot(time, MAP_50M_Athlete, label='50th PCTL M Athletic', color='#021466')
axs[1, 2].plot(time, MAP_50F_Athlete, label='50th PCTL F Athletic', color='#971102')
axs[1, 2].plot(time, MAP_50M, label='50th PCTL M', color='blue')
axs[1, 2].plot(time, MAP_50F, label='50th PCTL F', color='red')
axs[1, 2].set_xlabel('Time [sec]')
axs[1, 2].set_ylabel('MAP [mmHg]')
axs[1, 2].set_title('Mean Arterial Pressure')
axs[1, 2].set_xlim(time[0], time[-1])
axs[1, 2].annotate('G', (0.02, 1.02), xycoords='axes fraction', fontsize=10, fontweight='bold', color='black')
plot_vertical_lines_and_regions(axs[1, 2])

#  Plot legend in the last subplot
axs[1, 3].axis('off')
handles, labels = axs[1, 2].get_legend_handles_labels()
axs[1, 3].legend(handles, labels, loc='center', bbox_to_anchor=(0.5, 0.5), fontsize='large', frameon=False)

# Adjust layout
plt.tight_layout(rect=[-0.05, -0.05, 1.05, 1.05])
plt.subplots_adjust(hspace=0.4, wspace=0.4)  # Adjust these values to decrease space
plt.show()

############################################################################################################

# Create Anthropometric Plots

# Create subplots
fig, axs = plt.subplots(2, 4)
fig.suptitle('Response of Anthropometrics in G Warm Up')

# Plot HR data
axs[0, 0].plot(time, HR_50M, label='50th PCTL M', color='blue')
axs[0, 0].plot(time, HR_50F, label='50th PCTL F', color='red')
axs[0, 0].plot(time, HR_5F, label='5th PCTL F', color='#f5910f')
axs[0, 0].plot(time, HR_5M, label='5th PCTL M', color='#47ab3c')
axs[0, 0].plot(time, HR_95F, label='95th PCTL F', color='#8c4103')
axs[0, 0].plot(time, HR_95M, label='95th PCTL M', color='#0a5702')
axs[0, 0].set_xlabel('Time [sec]')
axs[0, 0].set_ylabel('HR [bpm]')
axs[0, 0].set_title('Heart Rate')
axs[0, 0].set_xlim(time[0], time[-1])
axs[0, 0].annotate('A', (0.02, 1.02), xycoords='axes fraction', fontsize=10, fontweight='bold', color='black')
plot_vertical_lines_and_regions(axs[0, 0])

# Plot SV data
axs[0, 1].plot(time, SV_50M, label='50th PCTL M', color='blue')
axs[0, 1].plot(time, SV_50F, label='50th PCTL F', color='red')
axs[0, 1].plot(time, SV_5F, label='5th PCTL F', color='#f5910f')
axs[0, 1].plot(time, SV_5M, label='5th PCTL M', color='#47ab3c')
axs[0, 1].plot(time, SV_95F, label='95th PCTL F', color='#8c4103')
axs[0, 1].plot(time, SV_95M, label='95th PCTL M', color='#0a5702')
axs[0, 1].set_xlabel('Time [sec]')
axs[0, 1].set_ylabel('SV [mL/beat]')
axs[0, 1].set_title('Stroke Volume')
axs[0, 1].set_xlim(time[0], time[-1])
axs[0, 1].annotate('B', (0.02, 1.02), xycoords='axes fraction', fontsize=10, fontweight='bold', color='black')
plot_vertical_lines_and_regions(axs[0, 1])

# Plot CO data
axs[0, 2].plot(time, CO_50M, label='50th PCTL M', color='blue')
axs[0, 2].plot(time, CO_50F, label='50th PCTL F', color='red')
axs[0, 2].plot(time, CO_5F, label='5th PCTL F', color='#f5910f')
axs[0, 2].plot(time, CO_5M, label='5th PCTL M', color='#47ab3c')
axs[0, 2].plot(time, CO_95F, label='95th PCTL F', color='#8c4103')
axs[0, 2].plot(time, CO_95M, label='95th PCTL M', color='#0a5702')
axs[0, 2].set_xlabel('Time [sec]')
axs[0, 2].set_ylabel('CO [L/min]')
axs[0, 2].set_title('Cardiac Output')
axs[0, 2].set_xlim(time[0], time[-1])
axs[0, 2].annotate('C', (0.02, 1.02), xycoords='axes fraction', fontsize=10, fontweight='bold', color='black')
plot_vertical_lines_and_regions(axs[0, 2])

# Plot CI data
axs[0, 3].plot(time, CI_50M, label='50th PCTL M', color='blue')
axs[0, 3].plot(time, CI_50F, label='50th PCTL F', color='red')
axs[0, 3].plot(time, CI_5F, label='5th PCTL F', color='#f5910f')
axs[0, 3].plot(time, CI_5M, label='5th PCTL M', color='#47ab3c')
axs[0, 3].plot(time, CI_95F, label='95th PCTL F', color='#8c4103')
axs[0, 3].plot(time, CI_95M, label='95th PCTL M', color='#0a5702')
axs[0, 3].set_xlabel('Time [sec]')
axs[0, 3].set_ylabel('CI [L/min/m^2]')
axs[0, 3].set_title('Cardiac Index')
axs[0, 3].set_xlim(time[0], time[-1])
axs[0, 3].annotate('D', (0.02, 1.02), xycoords='axes fraction', fontsize=10, fontweight='bold', color='black')
plot_vertical_lines_and_regions(axs[0, 3])

# Plot SBP data
axs[1, 0].plot(time, SBP_50M, label='50th PCTL M', color='blue')
axs[1, 0].plot(time, SBP_50F, label='50th PCTL F', color='red')
axs[1, 0].plot(time, SBP_5F, label='5th PCTL F', color='#f5910f')
axs[1, 0].plot(time, SBP_5M, label='5th PCTL M', color='#47ab3c')
axs[1, 0].plot(time, SBP_95F, label='95th PCTL F', color='#8c4103')
axs[1, 0].plot(time, SBP_95M, label='95th PCTL M', color='#0a5702')
axs[1, 0].set_xlabel('Time [sec]')
axs[1, 0].set_ylabel('SBP [mmHg]')
axs[1, 0].set_title('Systolic Blood Pressure')
axs[1, 0].set_xlim(time[0], time[-1])
axs[1, 0].annotate('E', (0.02, 1.02), xycoords='axes fraction', fontsize=10, fontweight='bold', color='black')
plot_vertical_lines_and_regions(axs[1, 0])

# Plot DBP data
axs[1, 1].plot(time, DBP_50M, label='50th PCTL M', color='blue')
axs[1, 1].plot(time, DBP_50F, label='50th PCTL F', color='red')
axs[1, 1].plot(time, DBP_5F, label='5th PCTL F', color='#f5910f')
axs[1, 1].plot(time, DBP_5M, label='5th PCTL M', color='#47ab3c')
axs[1, 1].plot(time, DBP_95F, label='95th PCTL F', color='#8c4103')
axs[1, 1].plot(time, DBP_95M, label='95th PCTL M', color='#0a5702')
axs[1, 1].set_xlabel('Time [sec]')
axs[1, 1].set_ylabel('DBP [mmHg]')
axs[1, 1].set_title('Diastolic Blood Pressure')
axs[1, 1].set_xlim(time[0], time[-1])
axs[1, 1].annotate('F', (0.02, 1.02), xycoords='axes fraction', fontsize=10, fontweight='bold', color='black')
plot_vertical_lines_and_regions(axs[1, 1])

# Plot MAP data
axs[1, 2].plot(time, MAP_50M, label='50th PCTL M', color='blue')
axs[1, 2].plot(time, MAP_50F, label='50th PCTL F', color='red')
axs[1, 2].plot(time, MAP_5F, label='5th PCTL F', color='#f5910f')
axs[1, 2].plot(time, MAP_5M, label='5th PCTL M', color='#47ab3c')
axs[1, 2].plot(time, MAP_95F, label='95th PCTL F', color='#8c4103')
axs[1, 2].plot(time, MAP_95M, label='95th PCTL M', color='#0a5702')
axs[1, 2].set_xlabel('Time [sec]')
axs[1, 2].set_ylabel('MAP [mmHg]')
axs[1, 2].set_title('Mean Arterial Pressure')
axs[1, 2].set_xlim(time[0], time[-1])
axs[1, 2].annotate('G', (0.02, 1.02), xycoords='axes fraction', fontsize=10, fontweight='bold', color='black')
plot_vertical_lines_and_regions(axs[1, 2])

#  Plot legend in the last subplot
axs[1, 3].axis('off')
handles, labels = axs[1, 2].get_legend_handles_labels()
axs[1, 3].legend(handles, labels, loc='center', bbox_to_anchor=(0.5, 0.5), fontsize='large', frameon=False)

# Adjust layout
plt.tight_layout(rect=[-0.05, -0.05, 1.05, 1.05])
plt.subplots_adjust(hspace=0.4, wspace=0.4)  # Adjust these values to decrease space
plt.show()
