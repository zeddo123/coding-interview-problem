flip_180 [] = []
flip_180 (x:xs) | x == '9' = '6':flip_180 xs
                | x == '6' = '9':flip_180 xs
                | otherwise = x:flip_180 xs 

is_strogrammatic string = string == flip_180 (reverse string) 