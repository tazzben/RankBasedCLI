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
        ks.PrintCriticalValueTable(samples, observedValue=observedValue, cvs=criticalValues) if criticalValues != None else ks.PrintCriticalValueTable(samples, observedValue=observedValue)

    if args.KruskalWallis:
        kw = MonteCarloKruskalWallis()
        kw.PrintCriticalValueTable(samples, observedValue=observedValue, cvs=criticalValues) if criticalValues != None else kw.PrintCriticalValueTable(samples, observedValue=observedValue)

    if args.Kuiper:
        k = MonteCarloKuiper()
        k.PrintCriticalValueTable(samples, observedValue=observedValue, cvs=criticalValues) if criticalValues != None else k.PrintCriticalValueTable(samples, observedValue=observedValue)

    if args.MannWhitney:
        mw = MonteCarloMannWhitney()
        mw.PrintCriticalValueTable(samples, observedValue=observedValue, cvs=criticalValues) if criticalValues != None else mw.PrintCriticalValueTable(samples, observedValue=observedValue)

if __name__ == "__main__":
    main()
