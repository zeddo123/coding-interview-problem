lowest_power_of_two n i | 2^(i) < n = lowest_power_of_two n (i+1)
                        | 2^(i) > n = 2^(i-1)
                        | otherwise = 2^(i)
