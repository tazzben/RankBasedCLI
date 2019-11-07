# RankBasedCLI
 
A command line tool to generate the null hypothesis distributions for four different rank-based tests: Mann-Whitney (MW), Kruskal-Wallis (KW), Kolmogorov-Smirnov (KS) and Kuiper (K).  The user can specify the number of observations per group, the test to run, the observed value (optional),  and critical values (optional).  For instance, the following will produce critical values for both the KW and MW test where the two groups sizes are 25 and 6:

~~~

./RankBasedMC 25 6 --KruskalWallis --MannWhitney

~~~

If the user specifies an observed value, a p-value will be generated:

~~~

./RankBasedMC 45 67 --Kuiper --observedValue 0.27

~~~

This tool is built using [RankBasedMonteCarlo package](https://github.com/tazzben/RankBasedMonteCarlo).  However, it does not require the installation of python.  Pre-packaged builds of the software for Windows and macOS are available in the releases section.