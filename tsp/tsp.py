def tsp(cities, paths, dist):
    all_permutations = permutations(cities)
    
    for permutation in all_permutations:
        i = 0
        total_path_dist = 0
        while i < len(permutation):
            step_distance = paths[i][i + 1]
            total_path_dist += step_distance
            i += 1
        if total_path_dist < dist:
            return True
    return False


# don't touch below this line


def permutations(arr):
    res = []
    res = helper(res, arr, len(arr))
    return res


def helper(res, arr, n):
    if n == 1:
        tmp = arr.copy()
        res.append(tmp)
    else:
        for i in range(n):
            res = helper(res, arr, n - 1)
            if n % 2 == 1:
                arr[n - 1], arr[i] = arr[i], arr[n - 1]
            else:
                arr[0], arr[n - 1] = arr[n - 1], arr[0]
    return res
