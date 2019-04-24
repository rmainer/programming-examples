using System;

namespace Levenshtein
{
    class Levenshtein
    {
        private static int LevenshteinDistance(String w1, String w2)
        {
            w1 = w1.ToLower();
            w2 = w2.ToLower();
            int n1 = w1.Length + 1;
            int n2 = w2.Length + 1;
            int[,] d = new int[n1, n2];
            Array.Clear(d, 0, n1 * n2);

            for (int y = 1; y < n1; y++) d[y, 0] = y;
            for (int x = 1; x < n1; x++) d[0, x] = x;

            for (int y = 1; y < n1; y++)
            {
                for (int x = 1; x < n2; x++)
                {
                    if (w1[y - 1] == w2[x - 1])
                    {
                        d[y, x] = d[y - 1, x - 1];
                    }
                    else
                    {
                        d[y, x] = Math.Min(d[y - 1, x - 1], Math.Min(d[y - 1, x], d[y, x - 1])) + 1;
                    }
                }
            }

            return d[n1 - 1, n2 - 1];
        }

        public static void Main(string[] args)
        {
            Console.WriteLine(LevenshteinDistance("Roman", "Ramon"));
        }
    }
}
