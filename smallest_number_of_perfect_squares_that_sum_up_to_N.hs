lowest_power_of_two n i | 2^(i) < n = lowest_power_of_two n (i+1)
                        | 2^(i) > n = 2^(i-1)
                        | otherwise = 2^(i)

smallest_number 0 = []
smallest_number n = lowest : smallest_number (n - lowest)
                    where lowest = lowest_power_of_two n 1
