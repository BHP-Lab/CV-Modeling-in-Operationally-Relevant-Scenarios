%% Graphs
%TPR
%{
Rtot=1./(1./Rubn+1./Rrcn+1./Rscn+1./Rlcn);
figure;plot(tout,Rtot, Color=[0 0.4470 0.7410])
title('Total Peripheral Resistance')
%axis([1400 1540 0.8 1.25])
xlabel("Time [s]")
%}
%HR
figure;
plot(times,HRnew, Color=[0 0.4470 0.7410])
title('Heart Rate')
%axis([1400 1431 30 200])
%axis([1400 1504 30 200])
axis([1400 7721 30 200])
xlabel("Time [s]")
ylabel("HR [bpm]")

% Pext
figure;
plot(times,Pext, Color=[0 0.4470 0.7410])
title('External Pressure')
%axis([1400 1431 30 200])
%axis([1400 1504 -4 70])
axis([1400 7721 -4 75])
xlabel("Time [s]")
ylabel("Pext [mmHg]")

% %Venous ZPFV
% %TotVenousZPFV= ZV4+ZV9+ZV11+ZV13;
% figure;plot(tout,TotVenousZPFV)
% title('Total Venous Zero-Pressure Filling Volume')
% 
% %Total Leg Volume
% %TotalLegVol=V12+V13;
% figure;plot(tout,TotalLegVol)
% title('Total Volume in Legs')
% 
% %Total Abdominal Volume
% %TotalAbVol=V7+V8+V9+V10+V11+V14;
% figure;plot(tout,TotalAbVol)
% title('Total Volume in Abdomen')

%Blood Pressure
figure;
%hold on
plot (times, MAP, Color=[0 0.4470 0.7410]);
%plot(times,DBP);
%plot(times,SBP);
title ('Mean Arterial Pressure')
%axis([1400 1431 40 130])
%axis([1400 1504 40 130])
axis([1400 7721 40 130])
xlabel("Time [s]")
ylabel("MAP [mmHg]")

% Cardiac Output
figure;
plot(times,CO,Color=[0 0.4470 0.7410]);
title ('Cardiac Output')
%axis([1400 1431 2 9])
%axis([1400 1504 2 9])
axis([1400 7721 2 8])
xlabel("Time [s]")
ylabel("CO [L/min]")

% Pulse Pressure
%figure;
%plot(times,PP, Color=[0 0.4470 0.7410]);
%title ('Pulse Pressure')
%xlabel("Time [s]")


% Stroke Volume
figure;
plot(times,SV, Color=[0 0.4470 0.7410]);
title ('Stroke Volume')
%axis([1400 1504 0 110])
%axis([1400 1431 0 110])
axis([1400 7721 0 160])
xlabel("Time [s]")
ylabel("SV [mL]")


% Stroke Volume
figure;
plot(times,SVV, Color=[0 0.4470 0.7410]);
title ('Stroke Volume')
%axis([1400 1431 0 110])
%axis([1400 1504 0 100])
axis([1400 7721 0 160])
xlabel("Time [s]")
ylabel("SVV [mL]")

%{
% Interstitial Volume
figure;plot(tout,Vint, Color=[0 0.4470 0.7410])
title('Interstitial Volume')
%axis([1400 1540 680 800])
xlabel("Time [s]")
%}

% Total Blood Volume
figure;plot(tout,Vtot, Color=[0 0.4470 0.7410])
title('Total Blood Volume')
xlabel("Time [s]")
%{
% Tilt Angle
figure;plot(tout,TiltAngle,Color=[0 0.4470 0.7410])
title('Tilt Angle')
xlabel("Time [s]")
%}
% DOE_TiltAngle
%figure;plot(tout,DOE_TiltAngle)
%title('DOE Tilt Angle')
%{
% DOE_LBNP
figure;plot(tout,DOE_LBNP)
title('DOE LBNP Angle')
%}
% DOE_GLevel
figure;plot(tout,DOE_GLevel)
title('DOE G Level')
