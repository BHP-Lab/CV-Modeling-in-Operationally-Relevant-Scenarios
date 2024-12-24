clear; close all;
load input_reflex_filters.mat
%load_system('cv_model_CMORPH_5OM.slx');
%set_param('cv_model_CMORPH_50M','AccelVerboseBuild','on')
sim cv_model_CMORPH_50F_Dehydrated_new.slx
process_output
calculate_trends
plot_graphs

mdlWks = get_param('cv_model_CMORPH_50F_Dehydrated_new','ModelWorkspace');
BSA =1.747;
SpreadsheetName = 'StepwiseTotal.csv';
SheetName = '50F_Dehydrated';

save('50F_Dehydrated_StepwiseTotal.mat');

% StepwiseTotal
% ParabolicFlight
% GWarmUp
% StepwiseDecrease
% StepwiseIncrease

%{
tout_1400 = tout(320480:end);
HR_1400 = HR(320480:end);
Vint_1400 = Vint(320480:end);
Vtot_1400 = Vtot(320480:end);

writematrix(tout, 'IEEE data again final maybe.xlsx','Sheet',3, 'Range','A1')
writematrix(HR, 'IEEE data again final maybe.xlsx','Sheet',3, 'Range','B1')
%writematrix(Vint, '2012 Army Personnel data.xlsx','Sheet',8, 'Range','C1')
%writematrix(Vtot, '2012 Army Personnel data.xlsx','Sheet',8, 'Range','D1')
%}
%{
times_1400 = times(1307:end);
MAP_1400 = MAP(1307:end);
DBP_1400 = DBP(1307:end);
SBP_1400 = SBP(1307:end);   
DBP_1400 = DBP(1307:end);
CO_1400 = CO(1307:end);
PP_1400 = PP(1307:end);
SV_1400 = SV(1307:end);


writematrix(times, 'IEEE data again final maybe.xlsx','Sheet',4, 'Range','A1')
writematrix(MAP, 'IEEE data again final maybe.xlsx','Sheet',4, 'Range','A2')
writematrix(DBP, 'IEEE data again final maybe.xlsx','Sheet',4, 'Range','A3')
writematrix(SBP, 'IEEE data again final maybe.xlsx','Sheet',4, 'Range','A4')
writematrix(CO, 'IEEE data again final maybe.xlsx','Sheet',4, 'Range','A5')
writematrix(PP, 'IEEE data again final maybe.xlsx','Sheet',4, 'Range','A6')
writematrix(SV, 'IEEE data again final maybe.xlsx','Sheet',4, 'Range','A7')
%}



