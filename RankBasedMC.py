import sys
import argparse
from RankBasedMonteCarlo import MonteCarloKolmogorovSmirnov, MonteCarloKruskalWallis, MonteCarloKuiper, MonteCarloMannWhitney

def main():
    parser = argparse.ArgumentParser(description='Create null hypothesis distribution based on Monte Carlo simulations')
    parser.add_argument('samples', metavar='N', type=int, nargs='+', help='Group/sample sizes separated by spaces.  You must supply at least two sample sizes.')
    parser.add_argument('--observedValue', type=float, default=None, help='Specify an observed value such that a p-value can be calculated.')
    parser.add_argument('--criticalValues', nargs='*', type=float, help='Specify a list of critical values')
    parser.add_argument('--KolmogorovSmirnov', action='store_true', help='Run the Kolmogorov-Smirnov routine')
    parser.add_argument('--KruskalWallis', action='store_true', help='Run the Kruskal-Wallis routine')
    parser.add_argument('--Kuiper', action='store_true', help='Run the Kuiper routine')
    parser.add_argument('--MannWhitney', action='store_true', help='Run the Mann-Whitney routine')
    args = parser.parse_args()

    if len(args.samples) >= 2:
        samples = args.samples
        observedValue = args.observedValue
        criticalValues = args.criticalValues
    else:
        sys.exit()

    if args.KolmogorovSmirnov:
        ks = MonteCarloKolmogorovSmirnov()
        print("Generating Kolmogorov-Smirnov null distribution")
        ks.PrintCriticalValueTable(samples, observedValue=observedValue, cvs=criticalValues) if criticalValues != None else ks.PrintCriticalValueTable(samples, observedValue=observedValue)

    if args.KruskalWallis:
        kw = MonteCarloKruskalWallis()
        print("Generating Kruskal-Wallis null distribution")
        kw.PrintCriticalValueTable(samples, observedValue=observedValue, cvs=criticalValues) if criticalValues != None else kw.PrintCriticalValueTable(samples, observedValue=observedValue)

    if args.Kuiper:
        k = MonteCarloKuiper()
        print("Generating Kuiper null distribution")
        k.PrintCriticalValueTable(samples, observedValue=observedValue, cvs=criticalValues) if criticalValues != None else k.PrintCriticalValueTable(samples, observedValue=observedValue)

    if args.MannWhitney:
        mw = MonteCarloMannWhitney()
        print("Generating Mann-Whitney null distribution")
        mw.PrintCriticalValueTable(samples, observedValue=observedValue, cvs=criticalValues) if criticalValues != None else mw.PrintCriticalValueTable(samples, observedValue=observedValue)

    if args.MannWhitney != True and args.Kuiper != True and args.KruskalWallis != True and args.KolmogorovSmirnov != True:
        print("You didn't select an estimation routine so the program doesn't have any output.")

if __name__ == "__main__":
    main()
