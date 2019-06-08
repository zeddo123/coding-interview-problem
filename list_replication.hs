replicate_list n (x:xs) = replicate n x : replicate_list n xs
replicate_list n [] = []

rep n l = mapM_ print (replicate_list n l)